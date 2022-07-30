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
            classID = Validator(self.config, self.logger).get(queryParam, 'ClassID', int)  
            self.logger.log().debug("ClassID: {}".format(classID))

            subjectID = Validator(self.config, self.logger).get(queryParam, 'SubjectID', int)  
            self.logger.log().debug("SubjectID: {}".format(subjectID))
            
            classData = self.resourceManager.getClass(classID, subjectID)

            response = Response(json.dumps({'Class' : classData}), status=200, mimetype='application/json')
        
        except Exception as e:
            self.logger.log().error("Error: {}".format(e))
            response = Response("Request failed", status=400)
        
        return response

    def post(self, request):
        return [{}]