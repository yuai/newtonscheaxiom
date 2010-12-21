import csv
import data_access
from fail import Fail
from data_access import Experiment

class NewtonImporter:
    def __init__(self,path,DBCount):
        try:
            
            self.collen = self.lookForLen(path)
            self.csvfile = open(path, 'r')
            dialect = csv.Sniffer().sniff(self.csvfile.read(1024))
            self.csvfile.seek(0)
            self.exp = None
            self.reader = csv.reader(self.csvfile,delimiter = ';' , dialect = csv.excel)
            self.values = []
            self.data = []
            self.meta= []
            self.stringI = str(DBCount)
            self.fillSql()
            self.csvfile.close()
            
        except csv.Error:
            Fail( "You are trying to open an file which is  not \n compatible with this Programm.\n This Programm can only read Data in the .csv file Format")
            
            
            
            
            
    def lookForLen(self,path):
        collen = 0
        try:
            lenTest = open(path, 'r')
            reader = csv.reader(lenTest,delimiter = ';' , dialect = csv.excel)
            i = 0
        #This is very very inefficient still trying to figure out how to get a row list 
            for row in reader:
                if i == 0:
                    collen = len(row)
                i=i+1  
        

            lenTest.close() 
        except csv.Error:
            print ' Opening Fail Window in except of init ' 
        return collen  
                
            
    
    
    def fillArray(self):
        '''fill Method, iterates through every Row of csv file and fills Array'''
       
        i = 0
        go = 0
        
        for i in range(0,self.collen-1):
            self.values.append([])
        
        for row in self.reader:
            if go > 0 :
                append = 0
                for i in range (1,self.collen):
                    if(row[i]=="" or row[i]=="NaN"):
                        append =1
                        
                if(append !=1):
                    for i in range (1,self.collen):
                        
                        self.values[i-1].append(float(row[i]))
                        
                        
              
                if row[0]!="":
                     self.meta.append(row[0])
            
                    
            go = 1
       
           
        self.metaDic = {'date':self.meta[0],'exp_name' :self.meta[1],'actor_name':self.meta[2],
                   'nr_series':self.meta[3],'vn_unit':self.meta[4],'vn_desc':self.meta[5],
                   'vn_fault':self.meta[6],'additional_info':self.meta[7]}
        
     
        self.values = zip(*self.values)
         
    def fillSql(self):
       print 'IMPORTING' 
       self.fillArray()
       self.exp = Experiment('C:/Users/db/test'+self.stringI+'.db',self.collen-2)
       self.exp.store_metadata(self.metaDic)
       self.exp.store_values(1,self.values)
       
    def getExperiment(self):
        if self.exp != None:
            return self.exp
        else:
            return None   
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\NewtonTemplate.csv")


