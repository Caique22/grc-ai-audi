<p align="center">
  <h3 align="center">GRC AI</h3>
  <p align="center">
    GRC Parser
    <br />
    <a href="/../../issues">Report Bug</a>
    ·
    <a href="/../../issues">Request Feature</a>

  </p>
</p>

## Table of contents

1. [About The Microservice](#about-the-microservice)
   - [Built With](#built-with)
2. [Getting Started](#getting-started)
   - [Prerequires](#prerequires)
   - [Installation](#instalation)
3. [Usage](#usage)
   - [Starting the server](#starting-the-server)
   - [Request Examples](#request-examples)

## About The Microservice

This microservice is responsable for requesting the information of a specific issue with it's action plans from GRC

### Built With

Major packages used to build this microservice:

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

## Getting Started

### Prerequires

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Instalation

1. Install the Libraries

```
pip install -r requirements.txt
```

2. Create a .env file at the root folder

```sh
OPENPAGES_URL=
OPENPAGES_USERNAME=
OPENPAGES_PASSWORD=
API_AUTH=
OP_ISSUE_FIELDS=
OP_ACTION_ITEM_FIELDS=
OP_UNIDADES_INTERNACIONAIS=
```

## Usage

### Starting the server

1. Start command

```
uvicorn main:app
```

### Request Examples

Base URL adress: `/explain`

- Parse the information from the Issue
  - HTTP Method: `GET`
  - Required Parameters <br>
    Location: `URL` <br>
    Parameters: `$issue_id` <br>
    Example:
    ```
    localhost:3000/explain?issue_id=AP43928
    ```
