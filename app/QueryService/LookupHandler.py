from flask import Response
import json

from Validator import Validator

class LookupHandler:
    def __init__(self, config, logger, resourceManager):
        self.config = config
        self.logger = logger
        self.resourceManager = resourceManager

    def get(self, request):
        response = None
        try:
            queryParam = request.args
            self.logger.log().debug("queryParam: {}".format(queryParam))
            typecode = Validator(self.config, self.logger).get(queryParam, 'typecode', int)
            
            lookup = self.resourceManager.getLookup(typecode)

            response = Response(json.dumps({'Lookup' : lookup}), status=200, mimetype='application/json')
        
        except Exception as e:
            self.logger.log().error("Error: {}".format(e))
            response = Response("Request failed", status=400)

        return response


    def post(self, request):
        return [{}]