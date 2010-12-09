import csv


class NewtonImporter:
    
    
    def __init__(self,name):
        try:
            csvfile = open(name, "rb")
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            self.reader = csv.reader(csvfile, dialect)
            self.x = []
            self.fillX()
            
        except csv.Error:
            print "Es ist keine Datei mit diesem namen Vorhanden"
            
    def fillX(self):
        for row in self.reader:
            if len(row)>0 :
                print row[0]
        
            
            
        
            
        
              
        
            
        
            
        
test = NewtonImporter("officialTemplate.csv")


