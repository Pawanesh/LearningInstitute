
from collections import defaultdict


class ClassQuery:
    def __init__(self):
        self.classID = None
        self.subjectID = None

class Class:
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
                self.add(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        except Exception as e:
            self.logger.log().error("Error: {}".format(e))

    def add(self, id, subjectID, startDate, endDate, time, day, name):
        self.logger.log().debug("Class id: {}, subjectID: {}, startDate: {}, endDate: {}, time: {}, day: {}, name: {}".format(id, subjectID, startDate, endDate, time, day, name))
        self.dict[id] = (id, subjectID, startDate, endDate, time, day, name)

    def getSQL(self):
        sql = """
            SELECT  ID
                    ,SubjectID
                    ,StartDate
                    ,EndDate
                    ,Time
                    ,Day
                    ,Name
            FROM
                Class 
        """
        return sql

    def get(self, query):
        out = []
        if query.classID is not None:
            if query.classID in self.dict.keys():
                classData = self.dict[query.classID]
                out.append({
                    'ID' : classData[0],
                    'SubjectID' : classData[1],
                    'StartDate' : classData[2],
                    'EndDate' : classData[3],
                    'Time' : classData[4],
                    'Day' : classData[5],
                    'Name' : classData[6]
                })
        elif query.subjectID is not None:
             for classID in self.dict.keys():
                classData = self.dict[classID]
                if classData[1] == query.subjectID:
                    out.append({
                        'ID' : classData[0],
                        'SubjectID' : classData[1],
                        'StartDate' : classData[2],
                        'EndDate' : classData[3],
                        'Time' : classData[4],
                        'Day' : classData[5],
                        'Name' : classData[6]
                    })
        else:
            for classID in self.dict.keys():
                classData = self.dict[classID]
                out.append({
                    'ID' : classData[0],
                    'SubjectID' : classData[1],
                    'StartDate' : classData[2],
                    'EndDate' : classData[3],
                    'Time' : classData[4],
                    'Day' : classData[5],
                    'Name' : classData[6]
                })
        return out