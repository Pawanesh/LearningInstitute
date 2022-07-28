
from collections import defaultdict

class LookupQuery:
    def __init__(self):
        self.typeCode = None


class Lookup:
    def __init__(self, config, logger, databaseManager, resourceManager):
        self.config = config
        self.logger = logger
        self.databaseManager = databaseManager
        self.resourceManager = resourceManager
        self.dict = defaultdict(list)
        self.init()
        

    def init(self):
        try:
            conn = self.databaseManager.getConnection()()
            cursor = conn.cursor()
            cursor.execute(self.getSQL())
            rows = cursor.fetchall()
            for row in rows:
                self.add(row[0], row[1], row[2], row[3])

        except Exception as e:
            self.logger.log().error("Error: {}".format(e))

    def add(self, id, typeCode, value, name):
        self.logger.log().debug("Lookup id: {}, typeCode: {}, value: {}, name: {}".format(id, typeCode, value, name))
        self.dict[typeCode].append((id, typeCode, value, name))

    def getSQL(self):
        sql = """
            SELECT  ID
                    ,TypeCode
                    ,Value
                    ,Name
            FROM
                Lookup 
        """
        return sql

    def get(self, query):
        out = []
        if query.typeCode is not None:
            if query.typeCode in self.dict.keys():
                lookups = self.dict[query.typeCode]
                for lookup in lookups:
                    out.append({
                        'ID' : lookup[0],
                        'TypeCode' : lookup[1],
                        'Value' : lookup[2],
                        'Name' : lookup[3]
                    })
        else:
            for typeCode in self.dict.keys():
                lookups = self.dict[typeCode]
                for lookup in lookups:
                    out.append({
                        'ID' : lookup[0],
                        'TypeCode' : lookup[1],
                        'Value' : lookup[2],
                        'Name' : lookup[3]
                    })
        return out