
from Database.DatabaseManager import DatabaseManager
from ResourceManager.Lookup import Lookup, LookupQuery
from ResourceManager.Subject import Subject, SubjectQuery
from ResourceManager.Class import Class, ClassQuery

class ResourceManager:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.databaseManager = DatabaseManager(self.config, self.logger)

        self.logger.log().info("Loading lookup")
        self.lookup = Lookup(self.config, self.logger, self.databaseManager, self)
        self.subject = Subject(self.config, self.logger, self.databaseManager, self)
        self.classData = Class(self.config, self.logger, self.databaseManager, self)

    def getSubject(self, subjectID):
        query = SubjectQuery()
        query.id = subjectID
        return self.subject.get(query)

    def getLookup(self, typeCode):
        query = LookupQuery()
        query.typeCode = typeCode
        return self.lookup.get(query)

    
    def getClass(self, id):
        query = ClassQuery()
        query.id = id
        return self.classData.get(query)