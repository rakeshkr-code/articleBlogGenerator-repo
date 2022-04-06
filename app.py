import os
from flask import Flask, session
from flask_restful import Resource, Api

from application import config
from application.config import LocalDevelopmentConfig
from application.database import db


app, api = None, None


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "ThisSecretKey"
    if os.getenv('ENV', "development")=="production":
        raise Exception("Currently No Production development is setup !")
    else:
        print("Starting Local Development...")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app, api

app, api = create_app()


## IMPORT ALL THE CONTROLLERS SO THEY AE LOADED...
from application.controllers import *

## IMPORT ALL THE APIS SO THEY AE LOADED...
# from 


if __name__=="__main__":
    #run..
    app.run(
        debug = True
    )
