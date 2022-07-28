import os
import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler

import datetime
from pathlib import Path


class Logger:
    def __init__(self, serviceName, config):
        now = datetime.datetime.now()
        logName = serviceName + "_" + os.environ['LI_ENV'] + "_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
        logFilePath = os.path.join(os.path.join(os.environ['LI_LOG'], serviceName), logName)

        print("logFilePath: {}".format(logFilePath))
        format = "%(levelname)s|%(asctime)s|%(name)s|%(message)s|%(pathname)s:%(lineno)d"


        handler = RotatingFileHandler(logFilePath, mode='a', maxBytes=5242880, backupCount=100, encoding=None, delay=0)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(Formatter(format))

        self.logger = logging.getLogger(serviceName)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)
        self.logger.debug("Logger is setup")

    def log(self):
        return self.logger