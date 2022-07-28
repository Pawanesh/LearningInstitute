        
class Validator:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def get(self, param, key, type):
        value = None
        try:
            value = type(param[key])
        except Exception as e:
            self.logger.log().error("Invalid input, Error: {}".format(e))
            value = None
        return value



