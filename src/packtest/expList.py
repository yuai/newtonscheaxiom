from data_access import Experiment

class ExpList:
    ''' list of experiences '''
    
    dbCount = 0
    
    def __init__(self):
        ''' init '''
        self.expList = [] # all experiences
        ExpList.dbCount = 0  # amount of experiences 
        self.indexList = [] # selected experiences
        
    def addExp(self,exp):
        ''' add experience into the expList'''
        self.expList.append(exp)
        ExpList.dbCount=ExpList.dbCount+1
    
    def addIndexList(self,i):
        ''' add experience into the indexList '''    
        self.indexList.append(i) # add all added experience into indexList[]
    
    def resetIndexList(self):
        ''' reset indexList '''
        self.indexList = []
        
    def getMetaData(self,index):
       ''' return meta data from experience with index '''
       metadata = self.expList[index].load_metadata()
       return metadata
   
    def getExp(self,id):
       ''' return experience with id '''
       return self.expList[id]

    def getValueList(self):
       ''' return values from expList that are in indexList '''
       valueList = []
       for pin in self.indexList:
           values = self.expList[pin].load_values(1)
           valueList.append(values)
       return valueList   

    def getValues(self,id):
       ''' return Values from id  '''
       values = self.expList[id].load_values(1)
       return values
   
    def getMetaList(self):
       ''' return metaData from expList that are in indexList'''
       metaList = []
       for pin in self.indexList:
           metas = self.expList[pin].load_metadata()
           metaList.append(metas)
       return metaList