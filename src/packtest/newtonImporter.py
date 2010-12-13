import csv
import data_access
#import newtonApp
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
            if go > 0:
                print row [0]
                print row [1]
                print row [2]
            
                self.x.append(float(row[0]))
                self.y.append(float(row[1]))
                self.meta.append(row[2])
            go = 1
        print self.x
              
              
    def fillSql(self):
       self.fillArray()
       #self.exp.store_metadata(self.metaDic)
       #testdic =  self.exp.load_metadata()
       #print testdic
       self.exp.store_values(1,*self.data)
       result = self.exp.load_values(1)
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\NewtonTemplate.csv")


