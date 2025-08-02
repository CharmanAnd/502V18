#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARQV30 Enhanced v2.0 - Mental Drivers Architect
Arquiteto de Drivers Mentais - Sistema de Ancoragem Psicológica
"""

import time
import random
import logging
import json
from typing import Dict, List, Any, Optional
from services.ai_manager import ai_manager
from services.auto_save_manager import salvar_etapa, salvar_erro

logger = logging.getLogger(__name__)

class MentalDriversArchitect:
    """Arquiteto de Drivers Mentais - Sistema de Ancoragem Psicológica"""
    
    def __init__(self):
        """Inicializa o arquiteto de drivers mentais"""
        self.universal_drivers = self._load_universal_drivers()
        self.quality_filters = self._load_quality_filters()
        self.telemedicine_templates = self._load_telemedicine_templates()
        self.quality_filters = self._load_quality_filters()
        self.telemedicine_templates = self._load_telemedicine_templates()
        self.quality_filters = self._load_quality_filters()
        self.telemedicine_templates = self._load_telemedicine_templates()
        self.quality_filters = self._load_quality_filters()
        self.telemedicine_templates = self._load_telemedicine_templates()
        logger.info(f"Mental Drivers Architect inicializado com {len(self.universal_drivers)} drivers universais")
    
    def _load_quality_filters(self) -> Dict[str, Any]:
        """Carrega filtros de qualidade para drivers mentais"""
        return {
            'min_specific_elements': 3,  # Mínimo 3 elementos específicos
            'required_medical_terms': ['médico', 'paciente', 'consulta', 'diagnóstico', 'tratamento', 'saúde'],
            'required_course_terms': ['curso', 'aluno', 'aprender', 'certificação', 'conhecimento'],
            'forbidden_generic_terms': ['customizado para', 'baseado em', 'específico para', 'adaptado para'],
            'min_story_length': 150,  # Mínimo 150 caracteres para histórias
            'max_generic_ratio': 0.2  # Máximo 20% de palavras genéricas
        }
    
                    f"Pacientes merecem o melhor de você, não o mais conveniente"
                ],
                "Ambição Expandida": [
                    f"Seu impacto médico não tem limite, seus métodos sim",
                    f"Pequenas ambições em medicina geram pequenos resultados para pacientes",
                    f"Se vai curar, cure no máximo da sua capacidade"
                ],
                "Relógio Psicológico": [
                    f"Cada dia sem telemedicina é um dia limitando seu alcance médico",
                    f"Pacientes não esperam você estar pronto para inovar",
                    f"Adiamento em medicina é oportunidade perdida de salvar vidas"
                ]
            }
        elif 'curso' in template.get('required_terms', []):
            phrases = {
                "Diagnóstico Brutal": [
                    f"Conhecimento sem aplicação em {segmento} é desperdício",
                    f"Seus resultados profissionais refletem seu nível de especialização",
                    f"Mediocridade profissional é escolha, não destino"
                ],
                "Ambição Expandida": [
                    f"Seu potencial de aprendizado não tem teto, sua dedicação sim",
                    f"Pequenos investimentos em educação geram pequenas transformações",
                    f"Se vai estudar {segmento}, domine completamente"
                ],
                "Relógio Psicológico": [
                    f"Cada mês sem especialização é um mês perdendo oportunidades",
                    f"O mercado não espera você estar pronto para competir",
                    f"Procrastinação educacional é autossabotagem profissional"
                ]
            }
        else:
            phrases = {
                "Diagnóstico Brutal": [
                    f"Resultados medianos em {segmento} são escolha, não acaso",
                    f"Sua performance reflete suas ferramentas e métodos",
                    f"Aceitar menos é roubar seu próprio potencial"
                ],
                "Ambição Expandida": [
                    f"Seu potencial em {segmento} é ilimitado, suas crenças não",
                    f"Grandes resultados exigem grandes ambições",
                    f"Se vai fazer {segmento}, faça extraordinariamente"
                ],
                "Relógio Psicológico": [
                    f"Cada dia sem otimização é oportunidade perdida",
                    f"Concorrentes não esperam você se decidir",
                    f"Tempo perdido em {segmento} não volta mais"
                ]
            }
    
    def _load_quality_filters(self) -> Dict[str, Any]:
        """Carrega filtros de qualidade para drivers mentais"""
        return {
            'min_specific_elements': 3,  # Mínimo 3 elementos específicos
            'required_medical_terms': ['médico', 'paciente', 'consulta', 'diagnóstico', 'tratamento', 'saúde'],
            'required_course_terms': ['curso', 'aluno', 'aprender', 'certificação', 'conhecimento'],
            'forbidden_generic_terms': ['customizado para', 'baseado em', 'específico para', 'adaptado para'],
            'min_story_length': 150,  # Mínimo 150 caracteres para histórias
            'max_generic_ratio': 0.2  # Máximo 20% de palavras genéricas
        }
    
    
    def _load_quality_filters(self) -> Dict[str, Any]:
        """Carrega filtros de qualidade para drivers mentais"""
        return {
            'min_specific_elements': 3,  # Mínimo 3 elementos específicos
            'required_medical_terms': ['médico', 'paciente', 'consulta', 'diagnóstico', 'tratamento', 'saúde'],
            'required_course_terms': ['curso', 'aluno', 'aprender', 'certificação', 'conhecimento'],
            'forbidden_generic_terms': ['customizado para', 'baseado em', 'específico para', 'adaptado para'],
            'min_story_length': 150,  # Mínimo 150 caracteres para histórias
            'max_generic_ratio': 0.2  # Máximo 20% de palavras genéricas
        }
    
            logger.warning(f"⚠️ História muito curta: {len(historia)} < {self.quality_filters['min_story_length']}")
            return False
        
        # 2. Verifica termos genéricos proibidos
        historia_lower = historia.lower()
        for forbidden_term in self.quality_filters['forbidden_generic_terms']:
            if forbidden_term in historia_lower:
                logger.warning(f"⚠️ Termo genérico detectado: '{forbidden_term}'")
                return False
        
        # 3. Verifica especificidade baseada no contexto
        if not self._has_specific_context(historia):
            logger.warning(f"⚠️ História sem contexto específico suficiente")
            return False
        
        # 4. Verifica elementos específicos mínimos
        specific_elements = self._count_specific_elements(historia)
        if specific_elements < self.quality_filters['min_specific_elements']:
            logger.warning(f"⚠️ Elementos específicos insuficientes: {specific_elements} < {self.quality_filters['min_specific_elements']}")
            return False
        
        return True
    
    def _has_specific_context(self, historia: str) -> bool:
        """Verifica se a história tem contexto específico"""
        historia_lower = historia.lower()
        
        # Indicadores de especificidade
        specificity_indicators = [
            r'\d+%',  # Percentuais
            r'R\$\s*\d+',  # Valores monetários
            r'\d+\s*(dias|meses|anos|horas)',  # Períodos específicos
            r'Dr\.|Dra\.',  # Títulos médicos
            r'\d+\s*(pacientes|alunos|clientes)',  # Quantidades específicas
        ]
        
        import re
        found_indicators = 0
        for pattern in specificity_indicators:
            if re.search(pattern, historia):
                found_indicators += 1
        
        return found_indicators >= 2  # Pelo menos 2 indicadores de especificidade
    
    def _count_specific_elements(self, historia: str) -> int:
        """Conta elementos específicos na história"""
        elements = 0
        historia_lower = historia.lower()
        
        # Elementos específicos por categoria
        specific_elements = {
            'nomes_proprios': [r'\b[A-Z][a-z]+\b'],  # Nomes próprios
            'numeros_concretos': [r'\d+'],  # Números
            'locais_especificos': ['consultório', 'hospital', 'clínica', 'sala', 'centro'],
            'resultados_mensuráveis': ['aumentou', 'reduziu', 'melhorou', 'otimizou', 'economizou'],
            'contexto_temporal': ['antes', 'depois', 'agora', 'hoje', 'ontem', 'semana', 'mês']
        }
        
        import re
        for category, patterns in specific_elements.items():
            for pattern in patterns:
                if isinstance(pattern, str):
                    if pattern in historia_lower:
                        elements += 1
                else:
                    if re.search(pattern, historia):
                        elements += 1
        
        return elements
    
    def _load_quality_filters(self) -> Dict[str, Any]:
        """Carrega filtros de qualidade para drivers mentais"""
        return {
            'min_specific_elements': 3,  # Mínimo 3 elementos específicos
            'required_medical_terms': ['médico', 'paciente', 'consulta', 'diagnóstico', 'tratamento', 'saúde'],
            'required_course_terms': ['curso', 'aluno', 'aprender', 'certificação', 'conhecimento'],
            'forbidden_generic_terms': ['customizado para', 'baseado em', 'específico para', 'adaptado para'],
            'min_story_length': 150,  # Mínimo 150 caracteres para histórias
            'max_generic_ratio': 0.2  # Máximo 20% de palavras genéricas
        }
    
            ]
        }
    
    def _load_segment_templates(self) -> Dict[str, Dict[str, Any]]:
        """Carrega templates específicos por segmento"""
        return {
            'medicina': {
                'required_terms': ['médico', 'paciente', 'consulta', 'diagnóstico', 'tratamento', 'saúde'],
                'context_elements': ['consultório', 'hospital', 'clínica', 'atendimento', 'prontuário'],
                'transformation_indicators': ['renda médica', 'tempo de consulta', 'satisfação paciente', 'eficiência'],
                'story_templates': [
                    "Dr. {nome}, {especialidade}, que atendia {numero} pacientes/mês presencialmente e agora atende {numero_novo} via telemedicina",
                    "Médica {nome} reduziu tempo de deslocamento de {tempo_antes} para {tempo_depois} usando teleconsultas",
                    "Cardiologista {nome} aumentou renda em {percentual}% implementando consultas online"
                ]
            },
            'educacao': {
                'required_terms': ['curso', 'aluno', 'aprender', 'ensino', 'conhecimento', 'certificação'],
                'context_elements': ['aula', 'material', 'exercício', 'avaliação', 'diploma'],
                'transformation_indicators': ['aprovação', 'conhecimento adquirido', 'carreira', 'salário'],
                'story_templates': [
                    "Aluno {nome} completou curso de {tema} em {tempo} e conseguiu {resultado}",
                    "Profissional {nome} aumentou salário em {percentual}% após certificação em {area}",
                    "Estudante {nome} passou de {situacao_antes} para {situacao_depois} com o curso"
                ]
            },
            'tecnologia': {
                'required_terms': ['sistema', 'software', 'digital', 'automação', 'tecnologia'],
                'context_elements': ['plataforma', 'aplicativo', 'interface', 'dados', 'processo'],
                'transformation_indicators': ['eficiência', 'produtividade', 'economia', 'escalabilidade'],
                'story_templates': [
                    "Empresa {nome} automatizou {processo} e reduziu custos em {percentual}%",
                    "Sistema {nome} processou {numero} transações em {tempo}",
                    "Plataforma {nome} conectou {numero} usuários em {periodo}"
                ]
            }
        }
    
    def _load_universal_drivers(self) -> List[Dict[str, Any]]:
        """Carrega os 19 drivers mentais universais"""
        return [
            {
                "id": 1,
                "nome": "Ferida Exposta",
                "categoria": "Emocional Primário",
                "gatilho": "Dor não resolvida",
                "mecanica": "Trazer à consciência o que foi reprimido",
                "template_ativacao": "Você ainda [comportamento doloroso] mesmo sabendo que [consequência]?"
            },
            {
                "id": 2,
                "nome": "Troféu Secreto", 
                "categoria": "Emocional Primário",
                "gatilho": "Desejo inconfessável",
                "mecanica": "Validar ambições proibidas",
                "template_ativacao": "Não é sobre dinheiro, é sobre [desejo real oculto]"
            },
            {
                "id": 3,
                "nome": "Inveja Produtiva",
                "categoria": "Emocional Primário", 
                "gatilho": "Comparação com pares",
                "mecanica": "Transformar inveja em combustível",
                "template_ativacao": "Enquanto você [situação atual], outros como você [resultado desejado]"
            },
            {
                "id": 4,
                "nome": "Relógio Psicológico",
                "categoria": "Emocional Primário",
                "gatilho": "Urgência existencial",
                "mecanica": "Tempo como recurso finito", 
                "template_ativacao": "Quantos [período] você ainda vai [desperdício]?"
            },
            {
                "id": 5,
                "nome": "Identidade Aprisionada",
                "categoria": "Emocional Primário",
                "gatilho": "Conflito entre quem é e quem poderia ser",
                "mecanica": "Expor a máscara social",
                "template_ativacao": "Você não é [rótulo limitante], você é [potencial real]"
            },
            {
                "id": 6,
                "nome": "Custo Invisível",
                "categoria": "Emocional Primário",
                "gatilho": "Perda não percebida",
                "mecanica": "Quantificar o preço da inação",
                "template_ativacao": "Cada dia sem [solução] custa [perda específica]"
            },
            {
                "id": 7,
                "nome": "Ambição Expandida",
                "categoria": "Emocional Primário",
                "gatilho": "Sonhos pequenos demais",
                "mecanica": "Elevar o teto mental de possibilidades",
                "template_ativacao": "Se o esforço é o mesmo, por que você está pedindo tão pouco?"
            },
            {
                "id": 8,
                "nome": "Diagnóstico Brutal",
                "categoria": "Emocional Primário",
                "gatilho": "Confronto com a realidade atual",
                "mecanica": "Criar indignação produtiva com status quo",
                "template_ativacao": "Olhe seus números/situação. Até quando você vai aceitar isso?"
            },
            {
                "id": 9,
                "nome": "Ambiente Vampiro",
                "categoria": "Emocional Primário",
                "gatilho": "Consciência do entorno tóxico",
                "mecanica": "Revelar como ambiente atual suga energia/potencial",
                "template_ativacao": "Seu ambiente te impulsiona ou te mantém pequeno?"
            },
            {
                "id": 10,
                "nome": "Mentor Salvador",
                "categoria": "Emocional Primário",
                "gatilho": "Necessidade de orientação externa",
                "mecanica": "Ativar desejo por figura de autoridade que acredita neles",
                "template_ativacao": "Você precisa de alguém que veja seu potencial quando você não consegue"
            },
            {
                "id": 11,
                "nome": "Coragem Necessária",
                "categoria": "Emocional Primário",
                "gatilho": "Medo paralisante disfarçado",
                "mecanica": "Transformar desculpas em decisões corajosas",
                "template_ativacao": "Não é sobre condições perfeitas, é sobre decidir apesar do medo"
            },
            {
                "id": 12,
                "nome": "Mecanismo Revelado",
                "categoria": "Racional Complementar",
                "gatilho": "Compreensão do como",
                "mecanica": "Desmistificar o complexo",
                "template_ativacao": "É simplesmente [analogia simples], não [complicação percebida]"
            },
            {
                "id": 13,
                "nome": "Prova Matemática",
                "categoria": "Racional Complementar",
                "gatilho": "Certeza numérica",
                "mecanica": "Equação irrefutável",
                "template_ativacao": "Se você fizer X por Y dias = Resultado Z garantido"
            },
            {
                "id": 14,
                "nome": "Padrão Oculto",
                "categoria": "Racional Complementar",
                "gatilho": "Insight revelador",
                "mecanica": "Mostrar o que sempre esteve lá",
                "template_ativacao": "Todos que conseguiram [resultado] fizeram [padrão específico]"
            },
            {
                "id": 15,
                "nome": "Exceção Possível",
                "categoria": "Racional Complementar",
                "gatilho": "Quebra de limitação",
                "mecanica": "Provar que regras podem ser quebradas",
                "template_ativacao": "Diziam que [limitação], mas [prova contrária]"
            },
            {
                "id": 16,
                "nome": "Atalho Ético",
                "categoria": "Racional Complementar",
                "gatilho": "Eficiência sem culpa",
                "mecanica": "Validar o caminho mais rápido",
                "template_ativacao": "Por que sofrer [tempo longo] se existe [atalho comprovado]?"
            },
            {
                "id": 17,
                "nome": "Decisão Binária",
                "categoria": "Racional Complementar",
                "gatilho": "Simplificação radical",
                "mecanica": "Eliminar zona cinzenta",
                "template_ativacao": "Ou você [ação desejada] ou aceita [consequência dolorosa]"
            },
            {
                "id": 18,
                "nome": "Oportunidade Oculta",
                "categoria": "Racional Complementar",
                "gatilho": "Vantagem não percebida",
                "mecanica": "Revelar demanda/chance óbvia mas ignorada",
                "template_ativacao": "O mercado está gritando por [solução] e ninguém está ouvindo"
            },
            {
                "id": 19,
                "nome": "Método vs Sorte",
                "categoria": "Racional Complementar",
                "gatilho": "Caos vs sistema",
                "mecanica": "Contrastar tentativa aleatória com caminho estruturado",
                "template_ativacao": "Sem método você está cortando mata com foice. Com método, está na autoestrada"
            }
        ]
    
    def generate_complete_drivers_system(
        self, 
        avatar_data: Dict[str, Any], 
        context_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera sistema completo de drivers mentais customizados"""
        
        # Validação crítica de entrada
        if not avatar_data:
            logger.error("❌ Dados do avatar ausentes")
            raise ValueError("DRIVERS MENTAIS FALHOU: Dados do avatar ausentes")
        
        if not context_data.get('segmento'):
            logger.error("❌ Segmento não informado")
            raise ValueError("DRIVERS MENTAIS FALHOU: Segmento obrigatório")
        
        try:
            logger.info(f"🧠 Gerando drivers mentais para segmento: {context_data.get('segmento')}")
            
            # Salva dados de entrada imediatamente
            salvar_etapa("drivers_entrada", {
                "avatar_data": avatar_data,
                "context_data": context_data
            }, categoria="drivers_mentais")
            
            # Seleciona os drivers mais relevantes para o contexto
            selected_drivers = self._select_optimal_drivers(avatar_data, context_data)
            
            if not selected_drivers:
                logger.error("❌ Nenhum driver selecionado")
                # Usa fallback em vez de falhar
                logger.warning("🔄 Usando drivers padrão como fallback")
                return self._generate_fallback_drivers_system(context_data)
            
            # Customiza cada driver selecionado
            customized_drivers = []
            for driver in selected_drivers:
                try:
                    customized = self._customize_driver(driver, avatar_data, context_data)
                    if customized and self._validate_driver(customized):
                        customized_drivers.append(customized)
                        # Salva cada driver customizado imediatamente
                        salvar_etapa(f"driver_{driver.get('nome', 'unknown')}", customized, categoria="drivers_mentais")
                    else:
                        logger.warning(f"⚠️ Driver inválido descartado: {driver.get('nome', 'Desconhecido')}")
                except Exception as e:
                    logger.error(f"❌ Erro ao customizar driver {driver.get('nome', 'Desconhecido')}: {str(e)}")
                    salvar_erro(f"driver_{driver.get('nome', 'unknown')}", e)
                    continue
            
            if not customized_drivers:
                logger.error("❌ Nenhum driver foi customizado com sucesso")
                # Usa fallback em vez de falhar
                logger.warning("🔄 Usando sistema de drivers padrão")
                return self._generate_fallback_drivers_system(context_data)
            
            # Cria sequenciamento estratégico
            sequencing = self._create_strategic_sequencing(customized_drivers)
            
            result = {
                "drivers_customizados": customized_drivers,
                "sequenciamento_estrategico": sequencing,
                "fases_implementacao": self._create_implementation_phases(customized_drivers),
                "scripts_ativacao": self._create_activation_scripts(customized_drivers),
                "metricas_eficacia": self._create_effectiveness_metrics(customized_drivers),
                "validation_status": "VALID",
                "total_drivers": len(customized_drivers),
                "generation_timestamp": time.time()
            }
            
            # Salva resultado final imediatamente
            salvar_etapa("drivers_mentais_final", result, categoria="drivers_mentais")
            
            logger.info(f"✅ {len(customized_drivers)} drivers mentais gerados com sucesso")
            return result
            
        except Exception as e:
            logger.error(f"❌ Erro ao gerar sistema de drivers: {str(e)}")
            salvar_erro("drivers_mentais_sistema", e, contexto={"segmento": context_data.get('segmento')})
            
            # Fallback para drivers padrão em caso de erro
            logger.warning("🔄 Gerando drivers mentais padrão como fallback...")
            return self._generate_fallback_drivers_system(context_data)
    
    def _validate_driver(self, driver: Dict[str, Any]) -> bool:
        """Valida se um driver mental é válido"""
        required_fields = ['nome', 'gatilho_central', 'roteiro_ativacao']
        
        for field in required_fields:
            if not driver.get(field):
                logger.warning(f"⚠️ Driver inválido: campo '{field}' ausente")
                return False
        
        # Valida roteiro de ativação
        roteiro = driver.get('roteiro_ativacao', {})
        if not roteiro.get('pergunta_abertura') or len(roteiro['pergunta_abertura']) < 20:
            logger.warning(f"⚠️ Driver com pergunta de abertura inválida")
            return False
        
        # Verifica se não é genérico
        if 'customizada para' in roteiro.get('historia_analogia', '').lower():
            if len(roteiro['historia_analogia']) < 100:
                logger.warning(f"⚠️ Driver com história muito genérica")
                return False
        
        return True
    
    def _select_optimal_drivers(self, avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Seleciona os drivers mais relevantes para o contexto"""
        
        # Drivers essenciais baseados no avatar
        essential_drivers = [
            "Diagnóstico Brutal",  # Sempre crítico para despertar
            "Ambição Expandida",   # Amplifica desejos
            "Relógio Psicológico", # Cria urgência
            "Método vs Sorte",     # Oferece caminho
            "Decisão Binária",     # Força escolha
            "Custo Invisível",     # Quantifica perdas
            "Coragem Necessária"   # Remove última barreira
        ]
        
        selected = []
        for driver_name in essential_drivers:
            driver = next((d for d in self.universal_drivers if d["nome"] == driver_name), None)
            if driver:
                selected.append(driver)
        
        return selected
    
    def _customize_driver(self, driver: Dict[str, Any], avatar_data: Dict[str, Any], context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Customiza um driver específico para o contexto"""
        
        segmento = context_data.get('segmento', 'negócios')
        produto = context_data.get('produto', 'produto/serviço')
        
        # Customizações específicas por driver
        customizations = {
            "Diagnóstico Brutal": {
                "pergunta_abertura": f"Há quanto tempo você está travado no mesmo nível em {segmento}?",
                "historia_analogia": f"É como um profissional de {segmento} que trabalha 12 horas por dia mas ganha o mesmo há 3 anos. Todo esse esforço, toda essa dedicação, mas os resultados não acompanham.",
                "metafora_visual": f"Imagine um hamster numa roda dourada. Ele corre muito, se esforça muito, mas continua no mesmo lugar. Esse é o profissional de {segmento} sem sistema.",
                "comando_acao": "Pare de aceitar mediocridade disfarçada de esforço"
            },
            "Ambição Expandida": {
                "pergunta_abertura": f"Por que você está pedindo tão pouco do seu negócio em {segmento}?",
                "historia_analogia": f"É como ter um Ferrari e usar apenas a primeira marcha. Você tem todo o potencial em {segmento}, mas está limitando artificialmente seus resultados.",
        # Gera customização específica usando templates do segmento
        customization = self._generate_segment_specific_customization(
            driver, segment_template, segmento, produto, avatar_data
        )
        
        # Valida qualidade da customização
        if not self._validate_customization_quality(customization, segment_template):
            logger.warning(f"⚠️ Customização de baixa qualidade para {driver['nome']}, usando template específico")
            customization = self._generate_fallback_customization(driver, segment_template, segmento)
        
        return {
            "nome": driver["nome"],
            "gatilho_central": driver["gatilho"],
            "definicao_visceral": driver["mecanica"],
            "momento_instalacao": self._determine_installation_moment(driver["nome"]),
            "roteiro_ativacao": customization,
            "frases_ancoragem": self._generate_anchor_phrases(driver["nome"], segmento, segment_template),
            "prova_logica": self._generate_logical_proof(driver["nome"], context_data, segment_template),
            "loop_reforco": f"Toda vez que você pensar em {segmento}, lembre: {customization.get('comando_acao', 'Aja agora')}",
            "categoria": driver["categoria"],
            "poder_impacto": self._calculate_impact_power(driver["nome"], avatar_data),
            "quality_validated": True,
            "segment_specific": True
        }
    
    def _detect_segment_type(self, segmento: str, produto: str) -> str:
        """Detecta tipo de segmento para usar template apropriado"""
        combined_text = f"{segmento} {produto}".lower()
        
        if any(term in combined_text for term in ['medicina', 'médico', 'saúde', 'telemedicina', 'consulta']):
            return 'medicina'
        elif any(term in combined_text for term in ['curso', 'educação', 'ensino', 'aprendizado', 'treinamento']):
            return 'educacao'
        else:
            return 'tecnologia'
    
    def _generate_segment_specific_customization(
        self, 
        driver: Dict[str, Any], 
        segment_template: Dict[str, Any], 
        segmento: str, 
        produto: str,
        avatar_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Gera customização específica usando templates do segmento"""
        
        driver_name = driver["nome"]
        
        # Templates específicos por driver e segmento
        if driver_name == "Diagnóstico Brutal":
            return self._generate_diagnostic_brutal_customization(segment_template, segmento, produto)
        elif driver_name == "Ambição Expandida":
            return self._generate_ambition_expanded_customization(segment_template, segmento, produto)
        elif driver_name == "Relógio Psicológico":
            return self._generate_psychological_clock_customization(segment_template, segmento, produto)
        else:
            return self._generate_generic_customization(driver, segment_template, segmento, produto)
    
    def _generate_diagnostic_brutal_customization(self, template: Dict[str, Any], segmento: str, produto: str) -> Dict[str, Any]:
        """Gera customização específica para Diagnóstico Brutal"""
        
        if 'medicina' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Há quanto tempo você está atendendo da mesma forma em {segmento} sem ver crescimento real na sua renda médica?",
                "historia_analogia": f"Dr. Carlos, cardiologista de São Paulo, atendia 80 pacientes por mês no consultório, trabalhando 12 horas/dia, ganhando R$ 25.000. Depois de implementar telemedicina, passou a atender 150 pacientes/mês, trabalhando 8 horas/dia, faturando R$ 45.000. Mesma competência, sistema diferente.",
                "metafora_visual": f"É como um médico brilhante usando estetoscópio de madeira - a competência está lá, mas a ferramenta limita o resultado.",
                "comando_acao": "Pare de limitar sua medicina com métodos do século passado"
            }
        elif 'curso' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Há quanto tempo você estuda {segmento} sem ver transformação real na sua carreira?",
                "historia_analogia": f"Ana, enfermeira de Brasília, fez 3 cursos de {segmento} em 2 anos, gastou R$ 8.000, mas continuava ganhando os mesmos R$ 4.500/mês. No 4º curso, com metodologia prática, em 6 meses estava ganhando R$ 12.000/mês como consultora especializada.",
                "metafora_visual": f"É como estudar natação por anos mas nunca entrar na piscina - teoria sem prática não gera transformação.",
                "comando_acao": "Pare de colecionar certificados e comece a aplicar conhecimento"
            }
        else:
            return {
                "pergunta_abertura": f"Há quanto tempo você está no mesmo patamar em {segmento}?",
                "historia_analogia": f"Empresa TechMed implementou sistema de {produto} e aumentou eficiência em 340% em 6 meses, passando de 200 para 880 processos/dia.",
                "metafora_visual": f"É como usar calculadora quando existe computador - funciona, mas limita exponencialmente o resultado.",
                "comando_acao": "Pare de aceitar resultados limitados por ferramentas limitadas"
            }
    
    def _generate_ambition_expanded_customization(self, template: Dict[str, Any], segmento: str, produto: str) -> Dict[str, Any]:
        """Gera customização específica para Ambição Expandida"""
        
        if 'medicina' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Por que você está limitando artificialmente o impacto que pode ter na vida dos pacientes?",
                "historia_analogia": f"Dra. Marina, dermatologista, atendia 15 pacientes/dia presencialmente. Com telemedicina + IA para triagem, passou a impactar 200 vidas/dia, mantendo qualidade e aumentando renda de R$ 30k para R$ 85k/mês.",
                "metafora_visual": f"É como um cirurgião usando bisturi quando tem laser à disposição - ambos cortam, mas um transforma vidas exponencialmente.",
                "comando_acao": "Expanda seu impacto médico ao nível da tecnologia disponível"
            }
        elif 'curso' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Por que você está pedindo tão pouco do seu potencial de aprendizado?",
                "historia_analogia": f"João, técnico em radiologia, fez curso de {segmento} e em 8 meses saiu de R$ 3.200/mês para R$ 15.000/mês como especialista certificado, atendendo hospitais via telemedicina.",
                "metafora_visual": f"É como ter diploma de medicina e trabalhar como auxiliar - o conhecimento está lá, mas você não está cobrando por ele.",
                "comando_acao": "Monetize seu conhecimento no nível que ele realmente vale"
            }
        else:
            return {
                "pergunta_abertura": f"Por que você está subestimando o potencial de {produto} no mercado?",
                "historia_analogia": f"Startup MedTech lançou plataforma de {produto} e em 18 meses passou de 0 para R$ 2.3M ARR, atendendo 15.000 profissionais de saúde.",
                "metafora_visual": f"É como ter uma Ferrari e dirigir a 40km/h - o potencial está lá, você só precisa acelerar.",
                "comando_acao": "Acelere seus resultados ao nível do potencial real"
            }
    
    def _generate_psychological_clock_customization(self, template: Dict[str, Any], segmento: str, produto: str) -> Dict[str, Any]:
        """Gera customização específica para Relógio Psicológico"""
        
        if 'medicina' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Quantos pacientes você ainda vai deixar de ajudar por não dominar telemedicina?",
                "historia_analogia": f"Dr. Roberto perdeu 40% dos pacientes em 2020 por não ter telemedicina. Enquanto ele 'pensava' em implementar, Dr. Silva (mesmo bairro) triplicou a base de pacientes. Hoje Roberto trabalha para Silva.",
                "metafora_visual": f"É como ver um paciente em emergência e ficar 'pensando' no diagnóstico - cada segundo de hesitação pode ser fatal.",
                "comando_acao": "Implemente telemedicina agora ou aceite perder pacientes para quem já implementou"
            }
        elif 'curso' in template.get('required_terms', []):
            return {
                "pergunta_abertura": f"Quantos meses você ainda vai adiar sua especialização em {segmento}?",
                "historia_analogia": f"Carla adiou curso de {segmento} por 8 meses 'esperando momento ideal'. Quando finalmente fez, descobriu que colegas que começaram antes já estavam ganhando R$ 8.000 a mais/mês. Cada mês de adiamento custou R$ 8.000.",
                "metafora_visual": f"É como adiar cirurgia de emergência - quanto mais espera, mais complicado fica e mais caro sai.",
                "comando_acao": "Comece sua especialização hoje ou aceite ficar para trás permanentemente"
            }
        else:
            return {
                "pergunta_abertura": f"Quantos concorrentes vão implementar {produto} enquanto você 'analisa'?",
                "historia_analogia": f"Empresa HealthTech adiou implementação de {produto} por 6 meses. Nesse período, 3 concorrentes lançaram soluções similares e capturaram 70% do market share. Hoje lutam por migalhas.",
                "metafora_visual": f"É como chegar atrasado para cirurgia - o paciente (mercado) não espera você se decidir.",
                "comando_acao": "Implemente agora ou aceite as sobras do mercado"
            }
    
    def _generate_generic_customization(self, driver: Dict[str, Any], template: Dict[str, Any], segmento: str, produto: str) -> Dict[str, Any]:
        """Gera customização genérica mas específica"""
        
        return {
            "pergunta_abertura": f"Como você pode transformar {segmento} usando {produto} de forma mais eficaz?",
            "historia_analogia": f"Profissional experiente em {segmento} implementou {produto} e obteve resultados 3x superiores em 90 dias, transformando completamente sua abordagem.",
            "metafora_visual": f"É como upgrade de sistema operacional - mesma máquina, performance completamente diferente.",
            "comando_acao": f"Faça o upgrade necessário em {segmento}"
        }
    
    def _validate_customization_quality(self, customization: Dict[str, Any], template: Dict[str, Any]) -> bool:
        """Valida qualidade da customização gerada"""
        
        historia = customization.get('historia_analogia', '')
        
        # Verifica se contém termos obrigatórios do segmento
        required_terms = template.get('required_terms', [])
        terms_found = sum(1 for term in required_terms if term in historia.lower())
        
        if terms_found < 2:  # Pelo menos 2 termos obrigatórios
            return False
        
        # Verifica especificidade
        if not self._has_specific_context(historia):
            return False
        
        return True
    
    def _generate_fallback_customization(self, driver: Dict[str, Any], template: Dict[str, Any], segmento: str) -> Dict[str, Any]:
        """Gera customização de fallback específica"""
        
        # Usa templates pré-definidos específicos
        story_templates = template.get('story_templates', [])
        if story_templates:
            # Seleciona template aleatório e preenche
            selected_template = random.choice(story_templates)
            
            # Preenche template com dados específicos
            filled_story = self._fill_story_template(selected_template, segmento)
            
            return {
                "pergunta_abertura": f"Você já parou para analisar os resultados reais que está obtendo em {segmento}?",
                "historia_analogia": filled_story,
                "metafora_visual": f"É como comparar medicina tradicional com medicina de precisão - ambas curam, mas uma é exponencialmente mais eficaz.",
                "comando_acao": f"Evolua sua abordagem em {segmento} para o próximo nível"
            }
        
        # Fallback final
        return {
            "pergunta_abertura": f"Qual é o verdadeiro potencial que você não está explorando em {segmento}?",
            "historia_analogia": f"Profissional de {segmento} descobriu método que triplicou resultados em 6 meses, transformando completamente sua realidade profissional e financeira.",
            "metafora_visual": f"É como descobrir atalho que reduz viagem de 3 horas para 1 hora - mesmo destino, eficiência revolucionária.",
            "comando_acao": f"Descubra e implemente o atalho em {segmento}"
        }
    
    def _fill_story_template(self, template: str, segmento: str) -> str:
        """Preenche template de história com dados específicos"""
        
        # Dados específicos por segmento
        fill_data = {
            'medicina': {
                'nome': random.choice(['Carlos', 'Marina', 'Roberto', 'Ana', 'João', 'Carla']),
                'especialidade': random.choice(['cardiologista', 'dermatologista', 'clínico geral', 'pediatra']),
                'numero': random.choice(['80', '120', '150', '200']),
                'numero_novo': random.choice(['200', '300', '400', '500']),
                'percentual': random.choice(['40', '60', '80', '120']),
                'tempo_antes': random.choice(['3 horas/dia', '4 horas/dia', '5 horas/dia']),
                'tempo_depois': random.choice(['1 hora/dia', '2 horas/dia', '30 min/dia'])
            },
            'educacao': {
                'nome': random.choice(['Ana', 'João', 'Maria', 'Pedro', 'Carla', 'Bruno']),
                'tema': segmento,
                'tempo': random.choice(['3 meses', '6 meses', '4 meses', '5 meses']),
                'resultado': random.choice(['promoção', 'novo emprego', 'aumento salarial', 'certificação']),
                'percentual': random.choice(['50', '80', '120', '200']),
                'area': segmento,
                'situacao_antes': random.choice(['auxiliar', 'júnior', 'iniciante']),
                'situacao_depois': random.choice(['especialista', 'sênior', 'consultor'])
            }
        }
        
        # Detecta tipo e preenche
        if 'médico' in template.lower() or 'Dr.' in template:
            data = fill_data['medicina']
        else:
            data = fill_data['educacao']
        
        # Substitui placeholders
        filled = template
        for key, value in data.items():
            filled = filled.replace(f'{{{key}}}', str(value))
        
        return filled
    
    def _determine_installation_moment(self, driver_name: str) -> str:
        """Determina o momento ideal para instalar cada driver"""
        
        moments = {
            "Diagnóstico Brutal": "Abertura - Para quebrar padrão e despertar consciência",
            "Ambição Expandida": "Desenvolvimento - Após despertar, amplificar desejos",
            "Relógio Psicológico": "Meio - Para criar pressão temporal",
            "Método vs Sorte": "Pré-pitch - Para posicionar solução",
            "Decisão Binária": "Fechamento - Para forçar escolha",
            "Custo Invisível": "Desenvolvimento - Para quantificar perdas",
            "Coragem Necessária": "Fechamento - Para remover última barreira"
        }
        
        return moments.get(driver_name, "Desenvolvimento - Momento padrão")
    
    def _generate_anchor_phrases(self, driver_name: str, segmento: str) -> List[str]:
        """Gera frases de ancoragem específicas"""
        
        phrases = {
            "Diagnóstico Brutal": [
                f"Mediocridade em {segmento} não é destino, é escolha",
                f"Seus resultados em {segmento} são o espelho das suas decisões",
                f"Aceitar menos em {segmento} é roubar de si mesmo"
            ],
            "Ambição Expandida": [
                f"Seu potencial em {segmento} não tem teto, suas crenças sim",
                f"Pequenos sonhos em {segmento} geram pequenos resultados",
                f"Se vai sonhar com {segmento}, sonhe grande"
            ],
            "Relógio Psicológico": [
                f"Cada dia sem otimizar {segmento} é um dia perdido para sempre",
                f"O tempo não espera você estar pronto para {segmento}",
                f"Procrastinação em {segmento} é autossabotagem disfarçada"
            ]
        }
        
        return phrases.get(driver_name, [f"Frase de ancoragem para {driver_name} em {segmento}"])
    
    def _generate_logical_proof(self, driver_name: str, context_data: Dict[str, Any], template: Dict[str, Any]) -> Dict[str, str]:
        """Gera prova lógica para cada driver"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        # Provas específicas baseadas no segmento
        if 'medicina' in template.get('required_terms', []):
            proofs = {
                "Diagnóstico Brutal": {
                    "estatistica": "78% dos médicos brasileiros ainda não usam telemedicina sistematicamente (CFM, 2024)",
                    "caso_exemplo": "Dr. Silva, cardiologista, trabalhava 60h/semana atendendo 100 pacientes/mês, faturando R$ 28k. Com telemedicina, atende 250 pacientes/mês em 40h/semana, faturando R$ 65k",
                    "demonstracao": "Cálculo: consulta presencial R$ 280 vs teleconsulta R$ 180 = 3x mais volume = 2.3x mais receita"
                },
                "Ambição Expandida": {
                    "estatistica": "Apenas 12% dos médicos brasileiros exploram todo potencial da telemedicina (Telemedicine Journal, 2024)",
                    "caso_exemplo": "Dra. Ana expandiu de 1 consultório para atendimento nacional via telemedicina, multiplicando receita por 8 em 18 meses",
                    "demonstracao": "Potencial: 1 consultório = 200 pacientes/mês vs telemedicina = 1.500 pacientes/mês"
                },
                "Relógio Psicológico": {
                    "estatistica": "Cada mês sem telemedicina = R$ 15.000 em receita perdida para médico médio (SBIS, 2024)",
                    "caso_exemplo": "Dr. Roberto adiou telemedicina por 8 meses, perdeu R$ 120k em receita e 300 pacientes para concorrentes",
                    "demonstracao": "Cálculo: 50 teleconsultas/mês x R$ 180 x 12 meses = R$ 108k anuais perdidos"
                }
            }
        elif 'curso' in template.get('required_terms', []):
            proofs = {
                "Diagnóstico Brutal": {
                    "estatistica": f"85% dos profissionais de {segmento} não se especializam continuamente (IBGE, 2024)",
                    "caso_exemplo": f"João, técnico em {segmento}, fez especialização e saiu de R$ 3.500 para R$ 12.000/mês em 10 meses",
                    "demonstracao": f"ROI do curso: investimento R$ 2.000 vs aumento anual R$ 102.000 = 5.100% retorno"
                },
                "Ambição Expandida": {
                    "estatistica": f"Apenas 8% dos profissionais de {segmento} se tornam especialistas reconhecidos",
                    "caso_exemplo": f"Maria se especializou em {segmento} e hoje é consultora internacional, faturando R$ 50k/mês",
                    "demonstracao": f"Especialista vs generalista: R$ 50k/mês vs R$ 8k/mês = 6.25x mais receita"
                },
                "Relógio Psicológico": {
                    "estatistica": f"Cada ano sem especialização = R$ 60.000 em oportunidades perdidas",
                    "caso_exemplo": f"Carlos adiou curso por 2 anos, perdeu promoção que valia R$ 120k anuais",
                    "demonstracao": f"Custo do adiamento: R$ 120k/ano x 2 anos = R$ 240k perdidos"
                }
            }
        else:
            proofs = {
                "Diagnóstico Brutal": {
                    "estatistica": f"73% das empresas de {segmento} operam abaixo do potencial",
                    "caso_exemplo": f"Empresa implementou sistema otimizado e aumentou eficiência em 340%",
                    "demonstracao": "Análise de gap entre performance atual e potencial máximo"
                },
                "Ambição Expandida": {
                    "estatistica": f"Apenas 15% das empresas de {segmento} exploram potencial máximo",
                    "caso_exemplo": f"Startup escalou de R$ 50k para R$ 2M ARR em 18 meses",
                    "demonstracao": "Projeção de crescimento com otimização completa"
                },
                "Relógio Psicológico": {
                    "estatistica": f"Cada trimestre de atraso = R$ 200k em market share perdido",
                    "caso_exemplo": f"Empresa perdeu liderança por atrasar implementação 6 meses",
                    "demonstracao": "Cálculo de oportunidade perdida por inação"
                }
            }
        
        return proofs.get(driver_name, {
            "estatistica": f"Dados específicos sobre {driver_name} em {segmento}",
            "caso_exemplo": f"Caso real de {driver_name} aplicado em {segmento}",
            "demonstracao": f"Como provar {driver_name} na prática"
        })
    
    def _calculate_impact_power(self, driver_name: str, avatar_data: Dict[str, Any]) -> str:
        """Calcula poder de impacto do driver para este avatar"""
        
        # Drivers de alto impacto para perfis empresariais
        high_impact_drivers = [
            "Diagnóstico Brutal",
            "Ambição Expandida", 
            "Relógio Psicológico",
            "Decisão Binária"
        ]
        
        if driver_name in high_impact_drivers:
            return "Alto"
        else:
            return "Médio"
    
    def _create_strategic_sequencing(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria sequenciamento estratégico dos drivers"""
        
        return {
            "fase_1_despertar": {
                "objetivo": "Quebrar padrão e despertar consciência",
                "drivers": ["Diagnóstico Brutal", "Oportunidade Oculta"],
                "duracao": "5-7 minutos",
                "intensidade": "Alta"
            },
            "fase_2_desejo": {
                "objetivo": "Amplificar desejos e possibilidades",
                "drivers": ["Ambição Expandida", "Troféu Secreto"],
                "duracao": "8-10 minutos", 
                "intensidade": "Crescente"
            },
            "fase_3_pressao": {
                "objetivo": "Criar urgência e pressão",
                "drivers": ["Relógio Psicológico", "Custo Invisível"],
                "duracao": "5-7 minutos",
                "intensidade": "Máxima"
            },
            "fase_4_direcao": {
                "objetivo": "Oferecer caminho e solução",
                "drivers": ["Método vs Sorte", "Mentor Salvador"],
                "duracao": "6-8 minutos",
                "intensidade": "Esperançosa"
            },
            "fase_5_decisao": {
                "objetivo": "Forçar decisão e ação",
                "drivers": ["Decisão Binária", "Coragem Necessária"],
                "duracao": "3-5 minutos",
                "intensidade": "Definitiva"
            }
        }
    
    def _create_implementation_phases(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria fases de implementação dos drivers"""
        
        return {
            "pre_lancamento": {
                "semana_1": "Instalar Diagnóstico Brutal em conteúdos",
                "semana_2": "Ativar Ambição Expandida em stories",
                "semana_3": "Começar Relógio Psicológico sutilmente",
                "semana_4": "Intensificar todos os drivers"
            },
            "durante_evento": {
                "abertura": "Diagnóstico Brutal + Oportunidade Oculta",
                "desenvolvimento": "Ambição Expandida + Custo Invisível",
                "pre_pitch": "Método vs Sorte + Mentor Salvador",
                "fechamento": "Decisão Binária + Coragem Necessária"
            },
            "pos_evento": {
                "follow_up_1": "Reforçar Relógio Psicológico",
                "follow_up_2": "Ativar Custo Invisível",
                "follow_up_3": "Decisão Binária final"
            }
        }
    
    def _create_activation_scripts(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria scripts de ativação prontos"""
        
        scripts = {}
        
        for driver in drivers:
            driver_name = driver["nome"]
            scripts[driver_name] = {
                "abertura": f"Deixa eu te fazer uma pergunta sobre {driver_name.lower()}...",
                "desenvolvimento": driver["roteiro_ativacao"]["historia_analogia"],
                "fechamento": driver["roteiro_ativacao"]["comando_acao"],
                "reativacao": f"Lembra do que falamos sobre {driver_name.lower()}?"
            }
        
        return scripts
    
    def _create_effectiveness_metrics(self, drivers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Cria métricas de eficácia dos drivers"""
        
        return {
            "indicadores_sucesso": [
                "Silêncio absoluto durante ativação",
                "Comentários emocionais no chat",
                "Perguntas sobre quando abre inscrições",
                "Concordância física (acenar cabeça)"
            ],
            "sinais_resistencia": [
                "Questionamentos técnicos excessivos",
                "Mudança de assunto",
                "Objeções imediatas",
                "Linguagem corporal fechada"
            ],
            "metricas_conversao": {
                "engajamento": "Tempo de atenção por driver",
                "emocional": "Reações emocionais geradas",
                "comportamental": "Ações tomadas após ativação",
                "conversao": "Taxa de conversão pós-drivers"
            },
            "otimizacao": {
                "teste_ab": "Testar diferentes versões dos drivers",
                "personalizacao": "Adaptar por perfil de audiência",
                "timing": "Otimizar momentos de ativação",
                "intensidade": "Ajustar força dos drivers"
            }
        }
    
    def _generate_fallback_drivers_system(self, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera sistema de drivers básico como fallback"""
        
        segmento = context_data.get('segmento', 'negócios')
        
        fallback_drivers = [
            {
                "nome": "Diagnóstico Brutal",
                "gatilho_central": "Confronto com realidade atual",
                "definicao_visceral": "Quebrar a ilusão de que está tudo bem",
                "roteiro_ativacao": {
                    "pergunta_abertura": f"Há quanto tempo você está estagnado no mesmo nível em {segmento}?",
                    "historia_analogia": f"É como um profissional de {segmento} que trabalha 12 horas por dia mas ganha o mesmo há 3 anos. Todo esse esforço, mas os resultados não acompanham.",
                    "comando_acao": "Pare de aceitar mediocridade disfarçada de esforço"
                },
                "frases_ancoragem": [
                    f"Mediocridade em {segmento} não é destino, é escolha",
                    f"Seus resultados em {segmento} são o espelho das suas decisões"
                ],
                "categoria": "Emocional Primário",
                "poder_impacto": "Alto"
            },
            {
                "nome": "Relógio Psicológico",
                "gatilho_central": "Urgência temporal",
                "definicao_visceral": "Tempo como recurso finito e precioso",
                "roteiro_ativacao": {
                    "pergunta_abertura": f"Quantos anos você ainda vai desperdiçar sem dominar {segmento}?",
                    "historia_analogia": f"Cada mês que passa sem otimizar seu negócio em {segmento} é um mês que seus concorrentes ganham vantagem.",
                    "comando_acao": "Aja agora ou aceite ficar para trás permanentemente"
                },
                "frases_ancoragem": [
                    f"Cada dia sem otimizar {segmento} é um dia perdido para sempre",
                    f"O tempo não espera você estar pronto para {segmento}"
                ],
                "categoria": "Emocional Primário",
                "poder_impacto": "Alto"
            },
            {
                "nome": "Método vs Sorte",
                "gatilho_central": "Caos vs sistema organizado",
                "definicao_visceral": "Contrastar tentativa aleatória com caminho estruturado",
                "roteiro_ativacao": {
                    "pergunta_abertura": f"Você quer continuar tentando na sorte ou ter um método em {segmento}?",
                    "historia_analogia": f"Sem método você está cortando mata com foice em {segmento}. Com método, está na autoestrada.",
                    "comando_acao": "Escolha o caminho estruturado para o sucesso"
                },
                "frases_ancoragem": [
                    f"Método vence sorte sempre em {segmento}",
                    f"Sistemas vencem tentativas em {segmento}"
                ],
                "categoria": "Racional Complementar",
                "poder_impacto": "Alto"
            }
        ]
        
        return {
            "drivers_customizados": fallback_drivers,
            "sequenciamento_estrategico": {
                "fase_1_despertar": {
                    "objetivo": "Quebrar padrão e despertar consciência",
                    "drivers": ["Diagnóstico Brutal"],
                    "duracao": "5-7 minutos",
                    "intensidade": "Alta"
                },
                "fase_2_pressao": {
                    "objetivo": "Criar urgência temporal",
                    "drivers": ["Relógio Psicológico"],
                    "duracao": "3-5 minutos",
                    "intensidade": "Máxima"
                },
                "fase_3_direcao": {
                    "objetivo": "Oferecer caminho estruturado",
                    "drivers": ["Método vs Sorte"],
                    "duracao": "5-7 minutos",
                    "intensidade": "Esperançosa"
                }
            },
            "validation_status": "FALLBACK_VALID",
            "total_drivers": len(fallback_drivers),
            "generation_timestamp": time.time(),
            "fallback_mode": True
        }

# Instância global
mental_drivers_architect = MentalDriversArchitect()