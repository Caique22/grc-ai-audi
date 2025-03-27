import requests
import logging 
from utils.config import Config
from grc.sox_item.parser_action_plan import ActionItemParser

class ActionPlan:
    def __init__(self) -> None:
        self.envs = Config()
        self.parser = ActionItemParser()
        self.query_action_item = "SELECT * FROM [SOXTask] WHERE [Resource ID] IN ({0})"

    def handle_action_plan(self, resource_id):

        logging.info("Merging all action plans ID's associated to this issue code...\n")
        op_action_plan_ids = self.__get_all_action_plan_ids(resource_id)        
        logging.info("Found {0} Action plans \n".format(len(op_action_plan_ids)))
        try:
            logging.info("Getting response from each action plan associated...\n")
            if op_action_plan_ids:
                action_plan_ids_formatted = ",".join(str(loop) for loop in op_action_plan_ids)
                action_plans_response = requests.get(f"{self.envs.openpages_url}/grc/api/query?q={self.query_action_item.format(action_plan_ids_formatted)}", auth=(self.envs.openpages_username, self.envs.openpages_password)).json()['rows']
                action_plans_response_formatted = [loop['fields']['field'] for loop in action_plans_response]
                action_plan_mapped = self.parser.parse_action_plan(action_plans_response_formatted)
            else:
                action_plan_mapped = {"dev_ti": "Sem plano de ação"}
            return {**action_plan_mapped,"action_item_count":len(op_action_plan_ids) }
        
        except Exception as error:
            logging.error("Error trying to get response from each associated action plan")
            raise error

    def __get_all_action_plan_ids(self, resource_id):
        logging.info(f"Getting children from Issue ResourceID: {resource_id[:2]}...")

        try:
            association_response = requests.get(f"{self.envs.openpages_url}/grc/api/contents/{resource_id}/associations/children", auth=(self.envs.openpages_username, self.envs.openpages_password)).json()
            association_ids = []
            for association in association_response:
                if association["typeDefinitionId"] == "7":
                    association_ids.append(association["id"])
            return association_ids
            
        except Exception as error:
            logging.error(f"Error action plan id (__get_all_action_plan_ids): {resource_id[:2]}...")
            raise error