from os import environ

from flask import Flask
from flask_restful import Api

from api.urls import URLS
from constants import API_VERSION, SERVICE_NAME


app = Flask(__name__)
api = Api(app, prefix=f'/api/{API_VERSION}/{SERVICE_NAME}')

for resource in URLS:
    api.add_resource(resource.api, resource.url)

if __name__ == '__main__':
    if environ.get('DEBUG'):
        debug = True
    else:
        debug = False
    app.run(debug=debug)
