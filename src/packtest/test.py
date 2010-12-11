import csv
import data_access
import xyplotApp


class NewtonImporter:
    
   '''Object opens csv file, reads tables and writes them into
   3 Arrays:X-Coordinates as floats
            Y-Coordinates as floats
            Meta-Data     as String'''
   def __init__(self,path):
       
       '''Constructor of NewtonImporter, initialzises Arrays and fills them 
       with csv content''' 
       try:
            csvfile = open(path, "rb")
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            self.reader = csv.reader(csvfile, dialect)
            self.x = []
            self.y = []
            self.data = []
            self.Meta= []
            self.fillSql()
            csvfile.close()
            
       except csv.Error:
            print "There is no File with this name "
            
    
    
   def fillArray(self):
        '''fill Method, iterates through every Row of csv file and fills Array'''
        i = 0
        for row in self.reader:
            
            if i > 0:
                break
            for line in self.reader:
                
                if i > 0:
                    break
                
                if line > 0:
                    try:    
                        self.x.append(float(line[0]))
                        self.y.append(float(line[1]))
                    except ValueError:
                        print "Wrong Template, read an String instead of an float"
                        i = 1
                if line[2]!= "":          
                    self.Meta.append(line[2])
                
       # metaDic = {'date':self.Meta[0],'exp_name'}
       
                                
        self.data.append(self.x)
        self.data.append(self.y)
     
            
        
    #Print out just for Testing purposes
        print 'X__________'            
        for i in range (0,len(self.x)):             
            print self.x[i]
        print 'Y__________'   
        for i in range (0,len(self.y)):             
              print self.y[i] 
        print 'META_______'      
        for i in range (0,len(self.Meta)):             
              print self.Meta[i]
              
              
   def fillSql(self):
       self.fillArray()
       xyplotApp.e.store_values(15,self.data)
       #result = e.load_values(1)
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\pfadtest.csv")

