from newtonApp import NewtonApp
from data_access import Experiment

class ExpList:
        
    ''' List for experiments '''
    expList = []
    ''' Amount of Databases or experiments '''  
    dbCount = 0
    
    def __init__(self):
        ''' init '''
        ExpList.expList = []
        ExpList.dbCount = 0       
        
    def addExp(self,exp):
        ExpList.expList.append(exp)
        ExpList.dbCount=ExpList.dbCount+1
        
    def getMetaData(self,index):
       ''' get meta data from experience index '''
       metadata = ExpList.expList[index].load_metadata()
       return metadata
   
    def getExp(self,index):
       return ExpList.expList[index]

    def getValueList(self):
       ''' load values from exTable'''
       valueList = []
       for pin in NewtonApp.indexList:
           values = ExpList.expList[pin].load_values(1)
           valueList.append(values)
       return valueList
   
    def getValues(self,index):
       ''' get Values from index  '''
       values = ExpList.expList[index].load_values(1)
       return values
   
    def getMetaList(self):
       ''' load metaData from exTable'''
       metaList = []
       for pin in NewtonApp.indexList:
           metas = ExpList.expList[pin].load_metadata()
           metaList.append(metas)
       return metaList