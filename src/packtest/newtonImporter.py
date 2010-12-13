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
                if(row[0]!="" and row[1]!=""):    
                    self.x.append(float(row[0]))
                    self.y.append(float(row[1]))
                if row[2]!="":
                     self.meta.append(row[2])
            go = 1
            
        self.metaDic = {'date':self.meta[0],'exp_name' :self.meta[1],'actor_name':self.meta[2],
                   'nr_series':self.meta[3],'vn_unit':self.meta[4],'vn_desc':self.meta[5],
                   'vn_fault':self.meta[6],'additional_info':self.meta[7]}
              
        self.values = zip(self.x,self.y)
       
         
    def fillSql(self):
       self.fillArray()
       self.exp.store_metadata(self.metaDic)
      
       
       self.Id = int(self.meta[3])
       self.exp.store_values(self.Id,self.values)
       
       #____________________Just look if it works
       testdic =  self.exp.load_metadata()
       print testdic
       result = self.exp.load_values(1)
       print result
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\NewtonTemplate.csv")


