import csv


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
            self.Meta= []
            self.fill()
            csvfile.close()
            
       except csv.Error:
            print "There is no File with this name "
            
    
    
   def fill(self):
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
                        
                self.Meta.append(line[2])
     
            
        
    #Print out just for Testing purposes
        print 'X'            
        for i in range (0,len(self.x)):             
            print self.x[i]
        print 'Y'   
        for i in range (0,len(self.y)):             
              print self.y[i] 
        print 'META'      
        for i in range (0,len(self.Meta)):             
              print self.Meta[i]
     
            
            
#test = NewtonImporter("C:\Users\Xandman\Desktop\pfadtest.csv")


