from flask import Flask, request, Response
from flask_restx import Api, Resource, fields

import os
from pathlib import Path

from Configuration.Configuration import Configuration
from Logger.Logger import Logger
from ResourceManager.ResourceManager import ResourceManager

from SubjectHandler import SubjectHandler
from LookupHandler import LookupHandler
from ClassHandler import ClassHandler

class QueryService:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        self.app = Flask(__name__)
        self.api = Api(self.app, version='1.0', title='LI Query API',
                description='A simple LI Query API',
            )

    def getAPI(self):
        return self.api
        
    def run(self):
        self.logger.log().info("Running Query Service")
        self.app.run(debug=False, port=int(self.config.get('server::main', 'port')))


serviceName = Path(__file__).stem
config = Configuration(serviceName)
logger = Logger(serviceName, config)

service = QueryService(config, logger)
resourceManager = ResourceManager(config, logger)

api = service.getAPI()

postData = api.model( "PostData", {
    "classID" : fields.String(description="classID", required=True)
})


@api.route('/subject', endpoint='subject')
@api.doc(params={'id': 'SubjectID'})
class Subject(Resource):
    def get(self):
        return SubjectHandler(config, logger, resourceManager).get(request) 
    
    @api.expect(postData)
    def post(self):
        return SubjectHandler(config, logger, resourceManager).post(request) 

@api.route('/lookup', endpoint='lookup')
@api.doc(params={'typecode': 'TypeCode'})
class Lookup(Resource):
    def get(self):
        return LookupHandler(config, logger, resourceManager).get(request) 
    
    @api.expect(postData)
    def post(self):
        return LookupHandler(config, logger, resourceManager).post(request) 

@api.route('/class', endpoint='class')
@api.doc(params={'ClassID': 'ClassID', 'SubjectID': 'SubjectID'})
class Class(Resource):
    def get(self):
        return ClassHandler(config, logger, resourceManager).get(request) 
    
    @api.expect(postData)
    def post(self):
        return ClassHandler(config, logger, resourceManager).post(request) 

if __name__ == '__main__':
    try:
        service.run()
    except Exception as e:
        print(e)
    