import csv
import data_access
from fail import Fail

class NewtonImporter:
    def __init__(self,path,e):
        try:
            csvfile = open(path, 'r')
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            self.exp = e
            self.reader = csv.reader(csvfile,delimiter = ';' , dialect = csv.excel)
            self.x = []
            self.y = []
            self.y2 = []
            self.y3 = []
            
            self.data = []
            self.meta= []
            self.fillSql()
            csvfile.close()
            
        except csv.Error:
            print "There is no File with this name "
            
    
    
    def fillArray(self):
        '''fill Method, iterates through every Row of csv file and fills Array'''
        i = 0
        go = 0
    
                
            
        for row in self.reader:
            if go > 0 :
                if(row[1]!="" and row[2]!=""):    
                    self.x.append(float(row[1]))
                    self.y.append(float(row[2]))
                  #  if(row[3]!=""):
                       # self.y2.append(float(row[3]))
                    #if(row[4]!=""):
                     #   self.y3.append(float(row[3]))
                            
                    
                if row[0]!="":
                     self.meta.append(row[0])
            go = 1
            
        self.metaDic = {'date':self.meta[0],'exp_name' :self.meta[1],'actor_name':self.meta[2],
                   'nr_series':self.meta[3],'vn_unit':self.meta[4],'vn_desc':self.meta[5],
                   'vn_fault':self.meta[6],'additional_info':self.meta[7]}
        
        if len(self.y2)>0 and len(self.y3)>0:
            self.values = zip(self.x,self.y,self.y2,self.y3)
        elif len(self.y2)>0:
            
            self.values = zip(self.x,self.y,self.y2)
        elif len(self.y2)==0 and len(self.y3)==0:
            self.values = zip(self.x,self.y)
            
                     
        
        print self.values
        print self.metaDic
        
       
         
    def fillSql(self):
       print 'IMPORTING' 
       self.fillArray()
       self.exp.store_metadata(self.metaDic)
      
       
       self.Id = int(self.meta[3])
       self.exp.store_values(1,self.values)
       
       #____________________Just look if it works
       #testdic =  self.exp.load_metadata()
       result = self.exp.load_values(1)
       print result
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\NewtonTemplate.csv")


