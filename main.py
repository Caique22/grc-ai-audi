from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
import secrets
import logging
from grc.controller import GRC
from utils.config import Config

logging.basicConfig(level=logging.INFO)

envs = Config()
grc = GRC()

app = FastAPI()
security = HTTPBasic()


def handle_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):

    current_password_bytes = credentials.password.encode("utf8")

    correct_password_bytes = envs.api_password.encode("utf8") if envs.api_password is not None else b""
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

@app.get("/issue/details")
def handle_date_explanator(issue_id:str,  auth = Depends(handle_auth)):
    
    if auth:
        try:
            logging.info("Calling Endpoint: {0}... *** \n".format(envs.openpages_url[:10]))
            controller_response = grc.grc_controller(issue_id)
            logging.info("Succesfully processed GRC fields !!")
            return JSONResponse(content=controller_response) if "not_found"  not in controller_response else  JSONResponse(content=controller_response,status_code=controller_response["code"])
        except Exception as error_content:
            raise error_content
        

@app.get("/")
def health():
    return JSONResponse(content={"message": "Server working"})