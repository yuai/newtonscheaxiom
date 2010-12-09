import csv


class NewtonImporter:
    
    
    def __init__(self,name):
        try:
            csvfile = open(name, "rb")
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            self.reader = csv.reader(csvfile, dialect)
            self.x = []
            self.y = []
            self.fillXY()
            #self.fillY()
            
        except csv.Error:
            print "Es ist keine Datei mit diesem namen Vorhanden"
            
    
    
    def fillXY(self):
        
        for row in self.reader:
            for line in self.reader:
                if line > 0:
                    self.x.append( float(line[0]))
                    self.y.append(float(line[1]))
        for i in range (0,len(self.x)):             
            print self.x[i]
        print 'WINN'    
        for i in range (0,len(self.y)):             
              print self.y[i] 
            
            
  
                 
                     
              
            
       
    
    
   
    
   
            
        
        
            
            
        
            
        
              
        
            
        
            
        
test = NewtonImporter("test.t.csv")


