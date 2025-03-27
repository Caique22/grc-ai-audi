import json
import logging
from dateutil import parser
from utils.config import Config

class IssueItemParser:
    def __init__(self):
         self.envs = Config()
    def parse_issue(self, issue_payload_api):

        if self.envs.openpages_issue_fields:
            formatted_fields = self.envs.openpages_issue_fields.split(";")
            formatted_fields = {key: None for key in formatted_fields}
            mapped_fields = formatted_fields
        else:
            mapped_fields ={
        "Itau-Shared:Discipline":  None,
        "Itau-IssRO:novo_nivelrisco": None,
        "OPSS-AudEval:Discussion Date": None,
        "Itau-Issue:Data Máxima para Implementação": None,
        "OPSS-Iss:Status": None,
        "Location": None,
        "Itau-IssRO:data_limite_excecao_gov": None
        }

        logging.info("Mapping Issue Fields... \n")
        for field in issue_payload_api:
                            
            field_name = field["name"]
            if field_name in mapped_fields: 
                if field.get('dataType') == 'ENUM_TYPE': 
                    if field.get('enumValue', {}):
                        mapped_fields[field_name] = field['enumValue']['localizedLabel'].replace(" (assuncao)", "")
                    else:
                        mapped_fields[field_name] = 'Não informado'

                elif field.get('dataType') == 'DATE_TYPE':
                    if field.get('value'):
                        mapped_fields[field_name] = parser.parse(field['value']).strftime("%d/%m/%Y")
                        
                    else:
                        mapped_fields[field_name] = 'Não informado'
                elif field.get('dataType') == 'MULTI_VALUE_ENUM':
                    if field.get('multiEnumValue', {}).get('enumValue'):
                        mapped_fields[field_name] = []
                        for value in field['multiEnumValue']['enumValue']:
                            mapped_fields[field_name].append(value['localizedLabel'])
                    else:
                        mapped_fields[field_name] = 'Sem valor'
                elif field.get('dataType') == 'STRING_TYPE':

                    if field.get('value'):
                        if self.envs.openpages_unidades_internacionais:
                            unidades_internacionais = self.envs.openpages_unidades_internacionais.split(";")
                            
                        else:
                            unidades_internacionais = ["Europa", "Unidos", "Paraguai", "Uruguai", "Chile", "Colombia", "Oca"]
                        
                        unidades_encontradas = [unidade for unidade in unidades_internacionais if unidade in field.get('value')]

                        if unidades_encontradas:
                            mapped_fields[field_name] = "Unidades Internacionais"

                    else:
                        mapped_fields[field_name] = field.get('value')
                else:
                    mapped_fields[field_name] = field.get('value')
            
        mapped_fields = {k.replace("OPLC-SOXIssue:", "").replace("OPSS-Iss:", "").replace("Itau-Issue:", "").replace("Itau-IssRO:", "").replace("Itau-Shared:", "").replace("OPSS-AudEval:", "").replace(" ", "_").lower(): v for k, v in mapped_fields.items()}
        updated_data = {
        key.replace("data_máxima_para_implementação", "data_maxima_para_implementacao"): value
        for key, value in mapped_fields.items()
    }

        logging.info("Successfully Mapped Issue fields \n")

        return updated_data