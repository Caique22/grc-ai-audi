from datetime import  datetime
from dateutil import parser
import logging
from utils.config import Config


class ActionItemParser:
    def __init__(self):
        self.action_plan_payload = {}
        self.envs = Config()


    def parse_action_plan(self, action_plan_response):
    
        try:
            formatted_fields = self.envs.openpages_action_item_fields.split(";")
            formatted_fields = {key: None for key in formatted_fields}
            mapped_fields = formatted_fields

            action_plans_closed = []

            logging.info("Mapping Action Plans fields \n")

            for action_item in action_plan_response:
                for field in action_item:
                    field_name = field["name"]
                    if field_name == 'OPSS-AI:Status' and field.get('enumValue', {}).get('name') == 'Closed':
                        action_plans_closed.append(action_item)

            for item in action_plans_closed:
                logging.info("Action plan {0} is Closed, then will not be considered".format(item))
                action_plan_response.remove(item)

            for action_item in action_plan_response:
                
                for field in action_item:
                    field_name = field["name"]
                    if field_name in mapped_fields:
                        if field.get('dataType') == 'ENUM_TYPE':
                            if field.get('enumValue', {}):
                               if "Impacto" in field['enumValue']['localizedLabel']:
                                  mapped_fields[field_name] = "Desenvolvimento TI - Impacto(RR/RO)"
                               else: 
                                  mapped_fields[field_name] = "Não"
                            else:
                               mapped_fields[field_name] = 'Não informado'
                        elif field.get('dataType') == 'DATE_TYPE':
                            if field.get('value'):
                                mapped_fields[field_name] = parser.parse(field['value']).strftime("%d/%m/%Y")
                            else: mapped_fields[field_name] = None
                        else:
                            mapped_fields[field_name] = field['value']

            mapped_fields = {k.replace("Itau-AItem:", "").replace(" ", "_").replace(":", "").lower(): v for k, v in mapped_fields.items()}

            if mapped_fields:

                return mapped_fields

            else:
                return {"dev_ti": "Sem plano de ação"}

        except Exception as error:
            logging.error(error)
            raise error
