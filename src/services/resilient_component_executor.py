#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Resilient Component Executor
Executor resiliente que isola falhas e continua processamento
"""

import time
import random
import logging
from typing import Dict, Any, Optional, Callable, List
from datetime import datetime
from services.auto_save_manager import auto_save_manager, salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class ResilientComponentExecutor:
    """Executor resiliente que nunca para por falhas individuais"""
    
    def __init__(self):
        """Inicializa executor resiliente"""
        self.components_registry = {}
        self.fallback_registry = {}
        self.execution_results = {}
        self.session_id = None
        
        logger.info("🛡️ Resilient Component Executor inicializado")
    
    def registrar_componente(
        self, 
        nome: str, 
        executor: Callable,
        fallback: Optional[Callable] = None,
        obrigatorio: bool = False,
        timeout: int = 300
    ):
        """Registra componente com fallback opcional"""
        
        self.components_registry[nome] = {
            'executor': executor,
            'fallback': fallback,
            'obrigatorio': obrigatorio,
            'timeout': timeout,
            'tentativas': 0,
            'ultimo_erro': None
        }
        
        logger.info(f"📝 Componente registrado: {nome} (obrigatório: {obrigatorio})")
    
    def executar_pipeline_resiliente(
        self, 
        dados_entrada: Dict[str, Any],
        session_id: str = None,
        progress_callback: Optional[Callable] = None
    ) -> Dict[str, Any]:
        """Executa pipeline completo com isolamento de falhas"""
        
        self.session_id = session_id or auto_save_manager.iniciar_sessao()
        start_time = time.time()
        
        logger.info(f"🚀 Iniciando pipeline resiliente - Sessão: {self.session_id}")
        
        # Salva dados de entrada imediatamente
        salvar_etapa("dados_entrada", dados_entrada, categoria="logs")
        
        # Pipeline de componentes em ordem
        pipeline_order = [
            'pesquisa_web_massiva',
            'avatar_ultra_detalhado', 
            'drivers_mentais_customizados',
            'provas_visuais_sugeridas',
            'sistema_anti_objecao',
            'pre_pitch_invisivel',
            'predicoes_futuro_completas',
            'consolidacao_final'
        ]
        
        resultados_acumulados = dados_entrada.copy()
        componentes_executados = []
        componentes_falharam = []
        
        for i, componente_nome in enumerate(pipeline_order):
            if progress_callback:
                progress_callback(i + 1, f"Executando {componente_nome}...")
            
            try:
                logger.info(f"🔄 Executando componente: {componente_nome}")
                
                # Executa componente com isolamento
                resultado = self._executar_componente_isolado(
                    componente_nome, 
                    resultados_acumulados
                )
                
                if resultado['sucesso']:
                    # Salva resultado imediatamente
                    salvar_etapa(
                        componente_nome, 
                        resultado['dados'], 
                        status="sucesso",
                        categoria=self._get_categoria_componente(componente_nome)
                    )
                    
                    # Adiciona aos resultados acumulados
                    resultados_acumulados[componente_nome] = resultado['dados']
                    componentes_executados.append(componente_nome)
                    
                    logger.info(f"✅ Componente {componente_nome} executado com sucesso")
                    
                else:
                    # Salva erro mas continua
                    salvar_erro(
                        componente_nome, 
                        Exception(resultado['erro']),
                        contexto={'dados_entrada': dados_entrada}
                    )
                    
                    componentes_falharam.append({
                        'nome': componente_nome,
                        'erro': resultado['erro'],
                        'fallback_usado': resultado.get('fallback_usado', False)
                    })
                    
                    # Se tem fallback, adiciona resultado do fallback
                    if resultado.get('dados_fallback'):
                        resultados_acumulados[componente_nome] = resultado['dados_fallback']
                        salvar_etapa(
                            f"{componente_nome}_fallback", 
                            resultado['dados_fallback'],
                            status="fallback",
                            categoria=self._get_categoria_componente(componente_nome)
                        )
                    
                    logger.warning(f"⚠️ Componente {componente_nome} falhou mas pipeline continua")
                
                # Salva progresso
                progresso = ((i + 1) / len(pipeline_order)) * 100
                auto_save_manager.salvar_progresso(componente_nome, progresso)
                
                # Delay entre componentes
                time.sleep(random.uniform(0.5, 1.5))
                
            except Exception as e:
                # Erro crítico no componente
                logger.error(f"❌ Erro crítico em {componente_nome}: {e}")
                
                salvar_erro(componente_nome, e, contexto={'dados_entrada': dados_entrada})
                componentes_falharam.append({
                    'nome': componente_nome,
                    'erro': str(e),
                    'critico': True
                })
                
                # Continua mesmo com erro crítico
                continue
        
        # Consolida resultados finais
        resultado_final = self._consolidar_resultados_finais(
            resultados_acumulados,
            componentes_executados,
            componentes_falharam,
            start_time
        )
        
        # Salva resultado final
        salvar_etapa("resultado_final", resultado_final, categoria="analise_completa")
        
        # Consolida sessão
        relatorio_consolidado = auto_save_manager.consolidar_sessao(self.session_id)
        
        logger.info(f"🏁 Pipeline concluído: {len(componentes_executados)} sucessos, {len(componentes_falharam)} falhas")
        
        return resultado_final
    
    def _executar_componente_isolado(self, nome: str, dados: Dict[str, Any]) -> Dict[str, Any]:
        """Executa componente com isolamento total de falhas"""
        
        if nome not in self.components_registry:
            return {
                'sucesso': False,
                'erro': f'Componente {nome} não registrado',
                'dados': None
            }
        
        config = self.components_registry[nome]
        
        try:
            # Executa componente principal
            start_time = time.time()
            
            resultado = config['executor'](dados)
            
            execution_time = time.time() - start_time
            
            # Valida resultado
            if self._validar_resultado_componente(nome, resultado):
                return {
                    'sucesso': True,
                    'dados': resultado,
                    'tempo_execucao': execution_time
                }
            else:
                raise ValueError(f"Resultado inválido para {nome}")
                
        except Exception as e:
            logger.error(f"❌ Falha no componente {nome}: {e}")
            
            # Tenta fallback se disponível
            if config['fallback']:
                try:
                    logger.info(f"🔄 Tentando fallback para {nome}...")
                    
                    resultado_fallback = config['fallback'](dados)
                    
                    if resultado_fallback:
                        return {
                            'sucesso': False,
                            'erro': str(e),
                            'dados_fallback': resultado_fallback,
                            'fallback_usado': True
                        }
                        
                except Exception as fallback_error:
                    logger.error(f"❌ Fallback também falhou para {nome}: {fallback_error}")
            
            return {
                'sucesso': False,
                'erro': str(e),
                'dados': None,
                'fallback_usado': False
            }
    
    def _validar_resultado_componente(self, nome: str, resultado: Any) -> bool:
        """Valida se resultado do componente é válido"""
        
        if resultado is None:
            return False
        
        # Validações específicas por componente
        if nome == 'drivers_mentais_customizados':
            return (isinstance(resultado, dict) and 
                   'drivers_customizados' in resultado and
                   len(resultado['drivers_customizados']) > 0)
        
        elif nome == 'sistema_anti_objecao':
            return (isinstance(resultado, dict) and 
                   ('objecoes_universais' in resultado or 'scripts_personalizados' in resultado))
        
        elif nome == 'avatar_ultra_detalhado':
            return (isinstance(resultado, dict) and 
                   'perfil_demografico' in resultado)
        
        # Validação genérica
        return len(str(resultado)) > 50  # Pelo menos 50 caracteres
    
    def _get_categoria_componente(self, nome: str) -> str:
        """Determina categoria do componente para salvamento"""
        
        categorias = {
            'pesquisa_web_massiva': 'pesquisa_web',
            'avatar_ultra_detalhado': 'avatar',
            'drivers_mentais_customizados': 'drivers_mentais',
            'provas_visuais_sugeridas': 'provas_visuais',
            'sistema_anti_objecao': 'anti_objecao',
            'pre_pitch_invisivel': 'pre_pitch',
            'predicoes_futuro_completas': 'analise_completa',
            'consolidacao_final': 'analise_completa'
        }
        
        return categorias.get(nome, 'geral')
    
    def _consolidar_resultados_finais(
        self,
        resultados: Dict[str, Any],
        sucessos: List[str],
        falhas: List[Dict[str, Any]],
        start_time: float
    ) -> Dict[str, Any]:
        """Consolida resultados finais do pipeline"""
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        return {
            'session_id': self.session_id,
            'analysis_id': auto_save_manager.analysis_id,
            'processamento': {
                'inicio': datetime.fromtimestamp(start_time).isoformat(),
                'fim': datetime.fromtimestamp(end_time).isoformat(),
                'duracao_segundos': processing_time,
                'duracao_formatada': f"{int(processing_time // 60)}m {int(processing_time % 60)}s"
            },
            'estatisticas': {
                'componentes_executados': len(sucessos),
                'componentes_falharam': len(falhas),
                'taxa_sucesso': (len(sucessos) / (len(sucessos) + len(falhas))) * 100 if (sucessos or falhas) else 0,
                'pipeline_completo': len(sucessos) >= 5  # Pelo menos 5 componentes
            },
            'componentes_sucesso': sucessos,
            'componentes_falha': falhas,
            'dados_gerados': {k: v for k, v in resultados.items() if k not in ['session_id', 'analysis_id']},
            'metadata': {
                'versao': '2.0.0',
                'modo': 'resiliente',
                'salvamento_automatico': True,
                'isolamento_falhas': True,
                'garantia_dados': 'Todos os dados intermediários foram salvos'
            }
        }

# Instância global
resilient_executor = ResilientComponentExecutor()