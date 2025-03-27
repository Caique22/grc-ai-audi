import traceback
import requests
from utils.config import Config
from grc.sox_issue.parser_issue import IssueItemParser
import logging
### 
class Issue:
    def __init__(self):
        self.envs = Config()
        self.parser = IssueItemParser()
        self.query_issue ="SELECT * FROM [SOXIssue] WHERE [Name] = '{0}'"        


    def handle_issue(self, issue_code):
        logging.info("Getting response from the following issue code: {0}...\n".format(issue_code[:4]))
        try:
            
            issue_response = requests.get(f"{self.envs.openpages_url}/grc/api/query?q={self.query_issue.format(issue_code)}", auth=(self.envs.openpages_username, self.envs.openpages_password)).json()
            if len(issue_response["rows"]) == 0:
                return {"not_found": True, "error": "Not found", "code": 404}
            
            issue_response = issue_response["rows"][0]["fields"]["field"]
            
            issue_mapped = self.parser.parse_issue(issue_response)
            return {"resource_id": issue_response[0]["value"], "issue_mapped": issue_mapped }

        except Exception as error:
            logging.error("Error trying to get response from the following issue code: {0}".format(issue_code[:4]))
            logging.error(traceback.format_exc())
            raise error
