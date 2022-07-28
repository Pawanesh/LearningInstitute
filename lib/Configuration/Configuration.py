import os
import configparser


class Configuration:
    def __init__(self, serviceName):
        configName = serviceName + "-" + os.environ['LI_ENV'] + ".ini"
        configFilePath = os.path.join(os.environ['LI_CONFIG'], configName)

        self.configuration = configparser.SafeConfigParser()
        self.configuration.read(configFilePath)

    def get(self, section, key):
        return self.configuration.get(section, key)