import logging
from grc.sox_issue.handle_issue import Issue
from grc.sox_item.handle_action_plan import ActionPlan

class GRC:

    def __init__(self) -> None:
        self.issue = Issue()
        self.action_plan = ActionPlan()

    def grc_controller(self, issue_code) :
        try:

            issue_response = self.issue.handle_issue(issue_code)
            if "not_found" in issue_response:
                return (issue_response)
            action_plan_mapped = self.action_plan.handle_action_plan(issue_response["resource_id"])
            action_plan_and_issue_merged = {**action_plan_mapped, **issue_response["issue_mapped"]} 
            return action_plan_and_issue_merged
            
        except Exception as error:
            logging.error(f"ERROR LOG (grc_controller): {error}")
            raise error        




