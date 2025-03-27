from dotenv import load_dotenv
import os
load_dotenv()

class Config:

    def __init__(self) -> None:
        self.__assert_environment_variables()

    def __assert_environment_variables(self):


        required_environments = [
            "OPENPAGES_URL",
            "OPENPAGES_USERNAME",
            "OPENPAGES_PASSWORD",
            "API_AUTH"
        ]

        for required_environment in required_environments:
            assert required_environment in os.environ, f"The environment variable {required_environment} is missing."


    @property
    def openpages_url(self):
        return os.environ.get("OPENPAGES_URL")

    @property
    def openpages_username(self):
        return os.environ.get("OPENPAGES_USERNAME")

    @property
    def openpages_password(self):
        return os.environ.get("OPENPAGES_PASSWORD")    
    @property
    def api_password(self):
        return os.environ.get("API_AUTH")
        
    @property
    def openpages_issue_fields(self):
        return os.environ.get("OP_ISSUE_FIELDS") 
   
    @property
    def openpages_action_item_fields(self):
        return os.environ.get("OP_ACTION_ITEM_FIELDS") 
   
    @property
    def openpages_unidades_internacionais(self):
        return os.environ.get("OP_UNIDADES_INTERNACIONAIS") 
   