
from collections import defaultdict

class SubjectQuery:
    def __init__(self):
        self.id = None
        self.name = None
        self.difficultyLevel = None

class Subject:
    def __init__(self, config, logger, databaseManager, resourceManager):
        self.config = config
        self.logger = logger
        self.databaseManager = databaseManager
        self.resourceManager = resourceManager
        self.dict = {}
        self.init()
        

    def init(self):
        try:
            conn = self.databaseManager.getConnection()()
            cursor = conn.cursor()
            cursor.execute(self.getSQL())
            rows = cursor.fetchall()
            for row in rows:
                self.add(row[0], row[1], row[2])

        except Exception as e:
            self.logger.log().error("Error: {}".format(e))

    def add(self, id, name, difficultyLevel):
        self.logger.log().debug("Subject id: {}, name: {}, difficultyLevel: {}".format(id, name, difficultyLevel))
        self.dict[id] = (id, name, difficultyLevel)

    def getSQL(self):
        sql = """
            SELECT  ID
                    ,Name
                    ,DifficultyLevel
            FROM
                Subject 
        """
        return sql

    def get(self, query):
        out = []
        if query.id is not None:
            if query.id in self.dict.keys():
                subject = self.dict[query.id]
                out.append({
                    'ID' : subject[0],
                    'Name' : subject[1],
                    'DifficultyLevel' : subject[2]
                })
        else:
            for id in self.dict.keys():
                subject = self.dict[id]
                out.append({
                'ID' : subject[0],
                'Name' : subject[1],
                'DifficultyLevel' : subject[2]
                })
        return out