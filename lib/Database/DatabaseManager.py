
import sqlite3
import threading
import os


class Connection:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.conn = None
        dbFilePath = config.get('server::database', 'name')
        try:
            db = os.path.join(os.environ['LI_HOME'], dbFilePath)
            self.conn = sqlite3.connect(db)
        except Exception as e:
            self.logger.log().error("Error: {}".format(e))

    def __call__(self):
        return self.conn
        
    def isValid(self):
        return True



class DatabaseManager:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.lock = threading.RLock()
        self.connections = {}

    def getConnection(self):
        self.lock.acquire()
        id = threading.get_ident() 
        if id in self.connections.keys():
            conn = self.connections[id]
            if not conn.isValid():
                conn = Connection(self.config, self.logger)
                self.connections[id] = conn
        else:
            conn = Connection(self.config, self.logger)
            self.connections[id] = conn
        self.lock.release()
        return conn


    
