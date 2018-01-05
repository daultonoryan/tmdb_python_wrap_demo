import requests


KEY = "eb51b083042a71e373dbe80d5cdd6ccd"

class APIKeyError(Exception):
    pass

if KEY == None:
    raise APIKeyError(
        "please enter a valid api key to use this wrapper"
    )
session = requests.Session()
session.params = {}
session.params["api_key"] = KEY

from . import *
