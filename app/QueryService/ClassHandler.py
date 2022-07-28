from flask import Response
import json

from Validator import Validator

class ClassHandler:
    def __init__(self, config, logger, resourceManager):
        self.config = config
        self.logger = logger
        self.resourceManager = resourceManager

    def get(self, request):
        response = None
        try:
            queryParam = request.args
            self.logger.log().debug("queryParam: {}".format(queryParam))
            id = Validator(self.config, self.logger).get(queryParam, 'id', int)  
            self.logger.log().debug("id: {}".format(id))
            
            classData = self.resourceManager.getClass(id)

            response = Response(json.dumps({'Class' : classData}), status=200, mimetype='application/json')
        
        except Exception as e:
            self.logger.log().error("Error: {}".format(e))
            response = Response("Request failed", status=400)
        
        return response

    def post(self, request):
        return [{}]