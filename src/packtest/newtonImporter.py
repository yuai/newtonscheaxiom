import csv
import data_access
from fail import Fail

class NewtonImporter:
    def __init__(self,path,e):
        try:
            
            self.collen = self.lookForLen(path)
            self.csvfile = open(path, 'r')
            dialect = csv.Sniffer().sniff(self.csvfile.read(1024))
            self.csvfile.seek(0)
            self.exp = e
            self.reader = csv.reader(self.csvfile,delimiter = ';' , dialect = csv.excel)
            self.values = []
            self.data = []
            self.meta= []
            
            self.fillSql()
            self.csvfile.close()
            
        except csv.Error:
            print "There is no File with this name "
            
            
            
            
            
    def lookForLen(self,path):
        
        collen = 0
        lenTest = open(path, 'r')
        reader = csv.reader(lenTest,delimiter = ';' , dialect = csv.excel)
        
        for row in reader:
            print row
            collen = len(row)
        

        lenTest.close() 
        return collen  
                
            
    
    
    def fillArray(self):
        '''fill Method, iterates through every Row of csv file and fills Array'''
       
        i = 0
        go = 0
        
        for i in range(0,self.collen-1):
            self.values.append([])
        
        for row in self.reader:
            if go > 0 :
                if(row[1]!="" and row[2]!=""):
                    for i in range (1,self.collen):
                        self.values[i-1].append(float(row[i]))
                        
                        
              
                if row[0]!="":
                     print row[0]
                     self.meta.append(row[0])
            
                    
            go = 1
       
           
        self.metaDic = {'date':self.meta[0],'exp_name' :self.meta[1],'actor_name':self.meta[2],
                   'nr_series':self.meta[3],'vn_unit':self.meta[4],'vn_desc':self.meta[5],
                   'vn_fault':self.meta[6],'additional_info':self.meta[7]}
        
     
            
                     
        
        print self.values
        print self.metaDic
        self.values = zip(*self.values)
        print self.values
       
         
    def fillSql(self):
       print 'IMPORTING' 
       self.fillArray()
       self.exp.store_metadata(self.metaDic)
      
       self.exp.store_values(1,self.values)
       
       #____________________Just look if it works
       #testdic =  self.exp.load_metadata()
       result = self.exp.load_values(1)
       print result
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\NewtonTemplate.csv")


