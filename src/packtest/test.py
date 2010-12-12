import csv
import data_access
import xyplotApp

class NewtonImporter:
    
   '''Object opens csv file, reads tables and writes them into
   3 Arrays:X-Coordinates as floats
            Y-Coordinates as floats
            Meta-Data     as Strings
            later the Metadatarray is portet to a Dictionary and all Data
            is written to an SqlLite File '''
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
                
        self.metaDic = {'date':self.Meta[0],'exp_name':self.Meta[1],'actor_name':self.Meta[2],
                   'nr_series':self.Meta[3],'vn_unit':self.Meta[4],'vn_desc':self.Meta[5],
                   'vn_fault':self.Meta[6],'additional_info':self.Meta[7]}
       
                                
        self.data.append(self.x)
        self.data.append(self.y)
       #test, looking if everything is in the right place in the dictionary
        print(self.metaDic)
            
        
    
       
              
              
   def fillSql(self):
       self.fillArray()
       xyplotApp.e.store_values(15,self.data)
       #result = e.load_values(1)
       
       
       
       
                
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\pfadtest.csv")


