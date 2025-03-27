from ibm_watson_machine_learning import APIClient
import os 
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("APIKEY")
PROJECT_ID = os.getenv("PROJECT_ID")
SPACE_ID = os.getenv("SPACE_ID")

project_id=PROJECT_ID
space_id=SPACE_ID
api_key=APIKEY


def llm_model_function(api_key, project_id):
    def TaggingForOP(api_key=api_key, project_id=project_id):
        
        from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
        from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
        from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
        from ibm_watson_machine_learning.foundation_models import Model
        
        

        credentials = {
            "url": "https://us-south.ml.cloud.ibm.com",
            "apikey": api_key
        }
        
        #These needs to be fine tuned. This is a very basic parameters list.
        parameters = {
            GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
            GenParams.MIN_NEW_TOKENS: 5,
            GenParams.MAX_NEW_TOKENS: 200,
            GenParams.STOP_SEQUENCES:["\n"]
        }
        #Need to check with WML team if this can be run only once.
        model = Model(
            model_id="meta-llama/llama-3-70b-instruct",
            params=parameters,
            credentials=credentials,
            project_id=project_id)
        
        def score(payload):
            input_text = payload.get("input_data")[0].get("values")[0][0]
            prompt_text=f"""Você é um assistente e sua função é realizar classificações. 
            As classes disponíveis são:
            -ESG # ESG
            -CIBER ATTACK # CIBER ATTACK
            -PREVENÇÃO A FRAUDES # PREVENÇÃO A FRAUDES

            Uma mesma entrada, pode conter mais de uma classe. A saída deverá ser apenas a classe de retorno. Se a saída tiver duas classes ou mais, retorne separando por #.

            Input: "a) Insuficiência no controle de descarte de equipamentos, conforme cenários destacados a seguir. Situações similares foram
            reportadas no AP999999, emitido em 12/08/2021 (Anexo D).
            • Falta de verificação dos equipamentos direcionados para descarte versus o efetivamente enviado. No lote do dia 08/03/2023, ocorreram diferenças de 14 frutas excedentes, 4 bananas faltantes e 113 abacaxis faltantes;
            • Ausência de alçada definida para autorização dos descartes. No lote de janeiro de 2023, 203.0123 equipamentos foram autorizados pelo faxineiro da área;
            • 3 meias enviados para descarte entre 2020 e 2022 com status ""descarte pendente"", sem justificativas para as pendências;
            • 71 escova de dente com o mesmo número de série e inventário, destinados mais de uma vez para descarte e em datas distintas;
            • 01 Tiranossauro que consta na relação de descarte no dia 03/10/2000, contudo aparece na lista de equipamentos em estoque do dia 27/02/2001.
            b) Falta de processo estruturado para acompanhar a destinação de papel higiêncio descartados, assim como não há formalização e/ou aprovação por alçada competente para a prestação deste serviço realizado.
            c) Em fevereiro de 2023, constatamos a retirada de meias, fornecedor não homologado, sendo que estas foram destinados para descarte.
            Causas:
            • Insuficiência nos controles associados ao processo de descarte sustentável.
            • Ausência de processo estruturado para o reaproveitamento coisas.
            • Falta de conferência e alçada definida de meias destinados a descarte.
            Consequências/Impactos:
            • Riscos reputacional e ambiental (ESG) pela possibilidade de descarte inadequado de meias usadas (PS-27 Política De Responsabilidade Social, Ambiental e Climática).
            • Risco reputacional por iniciar relacionamentos com fornecedor sem análise da área de compras.
            • Ineficiência operacional no processo de descarte, levando a custos extras com armazenagem e transporte."
            Output:ESG # ESG

            Input:"Régua de Sensibilidade:
            1. Na avaliação e re-performance dos valores de proporcionalidade e relevância por cliente e setor da régua de sensibilidade, identificamos divergências nos valores apresentados, conforme abaixo:
            A Gerência de Compliance Socioambiental informou que os valores apresentados não eram os vigentes e encaminhou e-mail 
            Há necessidade de adequação do processo e da governança, considerando:
            • Ausência de controles de verificação dos materiais elaborados.
            • Ausência de controle de formalização da aprovação dos valores de concentração por cliente e por setor utilizados no cálculo da régua de sensibilidade.
            2. Em relação à automatização da Régua de Sensibilidade, verificamos:
            • Um cliente com o campo "Setor" zerado na base do NORISK, classificado com exposição "Baixa" pela Gerência de Compliance Socioambiental.
            • Um cliente com o campo "Exposição" zerado que, após o processo de automatização, ficou sem classificação.
            Sendo necessário melhorias no processo e criação de controles conforme abaixo:
            • Necessidade de definição de critérios de exceção para classificação em ""Baixa", "Média" ou "Alta Exposição", quando as informações na base de dados não estão preenchidas adequadamente.
            • Criação de controle para informar quando aparecem clientes com campo em branco nas bases de dados utilizadas para o cálculo da Régua de Sensibilidade, impactando em ausência de classificação para o cliente.
            Heat Map
            Na avaliação da governança e da metodologia existentes para a Gestão Climática, não identificamos formalização do racional utilizado para a priorização de Risco de Crédito quando da utilização do Heat Map, não considerando os demais riscos como exemplo: Risco de Negócio e Estratégia que aparece como relevante.
            Causas: Não priorização da definição de controle nos processos de Gestão de Risco Climático.
            Consequências/Impactos:
            • Falha operacional na execução do processo.
            • Perda de rastreabilidade das alterações realizadas ao longo do tempo.
            • Sensibilização incorreta de clientes e setores no uso no processo de avaliação."
            Output:ESG # ESG

            Input:"Falta de Monitoramento Contínuo Descrição: Não há monitoramento contínuo das redes, o que aumenta o risco de ciberataques passarem despercebidos. Causa: Ferramentas de segurança insuficientes. Consequência: Potencial atraso na identificação e mitigação de ameaças."
            Output:CIBER ATTACK # CIBER ATTACK

            Input:"Apontamento: Controles de Acesso Deficientes Observou-se que o processo de revisão de acessos é falho, permitindo que usuários sem necessidade continuem com acesso a sistemas críticos. Essa falha decorre da ausência de revisões periódicas das permissões de acesso. A consequência direta é o aumento da exposição da organização a ameaças, tanto internas quanto externas."
            Output:CIBER ATTACK # CIBER ATTACK

            Input:"Falta de Mecanismos de Detecção de Fraudes Durante a auditoria, foi identificado que a organização não possui mecanismos eficazes de detecção de fraudes em tempo real. Essa falha se deve à ausência de ferramentas automatizadas de monitoramento de transações. Como consequência, a organização fica vulnerável a atividades fraudulentas que podem passar despercebidas, resultando em perdas financeiras."
            Output:PREVENÇÃO A FRAUDES # PREVENÇÃO A FRAUDES

            Input:"Controles Internos Inadequados Verificou-se que os controles internos voltados para a prevenção de fraudes são inadequados, especialmente nos processos de aprovação de transações financeiras. A falta de segregação de funções é uma das principais causas desse problema. Como resultado, há um risco elevado de fraudes internas, onde um único funcionário pode realizar e aprovar transações fraudulentas sem detecção imediata.
            Considerando o cenário atual do tema ESG, com crescente aumento das regulamentações e da necessidade de publicação de dados financeiros relacionadas ao tema, maiores preocupações relativas a aspectos de greenwashing e risco de reputação, há necessidade de revisão da governança e definições de controles e novos processos envolvendo mais áreas da Instituição.O processo atual de elaboração e aprovação dos relatórios com conteúdo ESG (Relatório ESG, Relatório Anual Integrado e Relatório Climático), não possui etapas formais para aprovação da estratégia, do conteúdo, do formato e dos indicadores a serem publicados nos relatórios. Apesar do envolvimento de outras áreas responsáveis pelo tema como Sustentabilidade e Riscos SAC, atualmente o processo é de inteira responsabilidade da área de Relações com Investidores, considerando definição i) da estratégia de comunicação dos relatórios e ii) do padrão e formato do relatório (quantos são, separados ou unificados) e a iii) priorização, redução ou detalhamento de temas / informações. Neste contexto, verificamos necessidade de revisão e formalização da governança considerando a estruturação e a aprovação da estratégia de elaboração e divulgação das informações nos relatórios, com o objetivo de mitigar riscos de divulgação de informações incorretas / incompletas e de refletir a estratégia ESG da Instituição, considerando: Relevância dada dos temas e como abordá-los na estratégia de reporte, buscando uma visão global mais do que de ações pontuais e/ou produtos específicos; Integração da estratégia ESG na estratégia de negócios; Integração das demandas dos todos os stakeholders e reforço da centralidade no cliente; Definição e formalização de direcionamento para as áreas parceiras sobre o que é esperado para cada indicador / conteúdo enviado para incluir no relatório; Olhar crítico e mitigação do risco de greenwashing.Causas:Tema em amadurecimento na Instituição, processo novo e abrangente, com envolvimento de diversas áreas da instituição..Consequências/Impactos:Possibilidade de os relatórios não refletirem a visão e atuação estratégia do banco em relação ao tema ESG. Possibilidade de divulgação de informações incorretas / incompletas - risco de greenwashing."
            Output:PREVENÇÃO A FRAUDES # PREVENÇÃO A FRAUDES # ESG

            Input:""a) Insuficiência no controle de descarte de equipamentos, conforme cenários destacados a seguir. Situações similares foram
            reportadas no AP999999, emitido em 12/08/2021 (Anexo D).
            • Falta de verificação dos equipamentos direcionados para descarte versus o efetivamente enviado. No lote do dia 08/03/2023, ocorreram diferenças de 14 frutas excedentes, 4 bananas faltantes e 113 abacaxis faltantes;
            • Ausência de alçada definida para autorização dos descartes. No lote de janeiro de 2023, 203.0123 equipamentos foram autorizados pelo faxineiro da área;
            • 3 meias enviados para descarte entre 2020 e 2022 com status ""descarte pendente"", sem justificativas para as pendências;
            • 71 escova de dente com o mesmo número de série e inventário, destinados mais de uma vez para descarte e em datas distintas;
            • 01 Tiranossauro que consta na relação de descarte no dia 03/10/2000, contudo aparece na lista de equipamentos em estoque do dia 27/02/2001.
            b) Falta de processo estruturado para acompanhar a destinação de papel higiêncio descartados, assim como não há formalização e/ou aprovação por alçada competente para a prestação deste serviço realizado.
            c) Em fevereiro de 2023, constatamos a retirada de meias, fornecedor não homologado, sendo que estas foram destinados para descarte.
            Causas:
            • Insuficiência nos controles associados ao processo de descarte sustentável.
            • Ausência de processo estruturado para o reaproveitamento coisas.
            • Falta de conferência e alçada definida de meias destinados a descarte.
            Consequências/Impactos:
            • Riscos reputacional e ambiental (ESG) pela possibilidade de descarte inadequado de meias usadas (PS-27 Política De Responsabilidade Social, Ambiental e Climática).
            • Risco reputacional por iniciar relacionamentos com fornecedor sem análise da área de compras.
            • Ineficiência operacional no processo de descarte, levando a custos extras com armazenagem e transporte.

            Apontamento: Controles de Acesso Deficientes Observou-se que o processo de revisão de acessos é falho, permitindo que usuários sem necessidade continuem com acesso a sistemas críticos. Essa falha decorre da ausência de revisões periódicas das permissões de acesso. A consequência direta é o aumento da exposição da organização a ameaças, tanto internas quanto externas."
            Output:ESG # ESG, CIBER ATTACK # CIBER ATTACK
            Input:"Falta de Mecanismos de Detecção de Fraudes Durante a auditoria, foi identificado que a organização não possui mecanismos eficazes de detecção de fraudes em tempo real. Essa falha se deve à ausência de ferramentas automatizadas de monitoramento de transações. Como consequência, a organização fica vulnerável a atividades fraudulentas que podem passar despercebidas, resultando em perdas financeiras."
            a) Insuficiência no controle de descarte de equipamentos, conforme cenários destacados a seguir. Situações similares foram
            reportadas no AP999999, emitido em 12/08/2021 (Anexo D).
            • Falta de verificação dos equipamentos direcionados para descarte versus o efetivamente enviado. No lote do dia 08/03/2023, ocorreram diferenças de 14 frutas excedentes, 4 bananas faltantes e 113 abacaxis faltantes;
            • Ausência de alçada definida para autorização dos descartes. No lote de janeiro de 2023, 203.0123 equipamentos foram autorizados pelo faxineiro da área;
            • 3 meias enviados para descarte entre 2020 e 2022 com status ""descarte pendente"", sem justificativas para as pendências;
            • 71 escova de dente com o mesmo número de série e inventário, destinados mais de uma vez para descarte e em datas distintas;
            • 01 Tiranossauro que consta na relação de descarte no dia 03/10/2000, contudo aparece na lista de equipamentos em estoque do dia 27/02/2001.
            b) Falta de processo estruturado para acompanhar a destinação de papel higiêncio descartados, assim como não há formalização e/ou aprovação por alçada competente para a prestação deste serviço realizado.
            c) Em fevereiro de 2023, constatamos a retirada de meias, fornecedor não homologado, sendo que estas foram destinados para descarte.
            Causas:
            • Insuficiência nos controles associados ao processo de descarte sustentável.
            • Ausência de processo estruturado para o reaproveitamento coisas.
            • Falta de conferência e alçada definida de meias destinados a descarte.
            Consequências/Impactos:
            • Riscos reputacional e ambiental (ESG) pela possibilidade de descarte inadequado de meias usadas (PS-27 Política De Responsabilidade Social, Ambiental e Climática).
            • Risco reputacional por iniciar relacionamentos com fornecedor sem análise da área de compras.
            • Ineficiência operacional no processo de descarte, levando a custos extras com armazenagem e transporte.

            Apontamento: Controles de Acesso Deficientes Observou-se que o processo de revisão de acessos é falho, permitindo que usuários sem necessidade continuem com acesso a sistemas críticos. Essa falha decorre da ausência de revisões periódicas das permissões de acesso. A consequência direta é o aumento da exposição da organização a ameaças, tanto internas quanto externas."
            Output:PREVENÇÃO A FRAUDES # PREVENÇÃO A FRAUDES # ESG # CIBER ATTACK

            Input:{input_text}
            Output:"""
            
            result=model.generate_text(prompt=prompt_text)
            score_response = {
                "predictions": [{"fields": ["Response_message_field"], 
                                 "values": [[result]]
                                }]
            } 
            return score_response
        return score
    return TaggingForOP


def deploy_function_to_wml(prompt_function, prompt_function_name, api_key, project_id, space_id):
    wml_credentials = {"url": "https://us-south.ml.cloud.ibm.com", "apikey": api_key}
    wml_client = APIClient(wml_credentials)
    client = wml_client
    wml_client.set.default_space(space_id)
    software_spec_id =  client.software_specifications.get_id_by_name('runtime-24.1-py3.11')
    function_meta_props = {
         client.repository.FunctionMetaNames.NAME: str(prompt_function_name),
         client.repository.FunctionMetaNames.SOFTWARE_SPEC_ID: software_spec_id
    }
    function_artifact = client.repository.store_function(meta_props=function_meta_props, function=prompt_function)
    function_uid = client.repository.get_function_id(function_artifact)
    hardware_spec_id = client.hardware_specifications.get_id_by_name('ML')
    deploy_meta = {
        client.deployments.ConfigurationMetaNames.NAME: str(prompt_function_name),
        client.deployments.ConfigurationMetaNames.ONLINE: {},
        client.deployments.ConfigurationMetaNames.HARDWARE_SPEC:{ "id": hardware_spec_id}
    }
    deployment_details = client.deployments.create(function_uid, meta_props=deploy_meta)
    return deployment_details['metadata']['id']
    


prompt_function=llm_model_function(api_key, project_id) #This is function reference
prompt_function_name='AutoTagOP' #This is function name
deployment_id = deploy_function_to_wml(prompt_function, prompt_function_name, api_key, project_id, space_id)