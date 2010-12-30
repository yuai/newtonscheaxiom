import csv
from infoWindow import Fail
from data_access import Experiment

'''
@author: Daniel Xander
'''
class NewtonImporter:
    '''This class opens a csv file and fills its content into arrays.These arrays are then written
    into an SQLlite file by using the data_access.py class Experiment.In order to read the content
    correctly the csv file must be written in the officiallTemplate form'''
    
    def __init__(self,path,storePath,DBCount):
        '''Constructor opens csv file , sets defaults and starts SQL writing process'''
        try:
            
            self.collen = self.lookForLen(path)
            self.csvfile = open(path, 'r')
            dialect = csv.Sniffer().sniff(self.csvfile.read(1024))
            self.csvfile.seek(0)
            self.exp = None
            self.store = storePath
            self.reader = csv.reader(self.csvfile,delimiter = ';' , dialect = csv.excel)
            self.values = []
            self.data = []
            self.meta= []
            self.FillSQL = 0        
            self.stringI = str(DBCount)
            self.fillSql()
            self.csvfile.close()
            
        except csv.Error:
            Fail( "You are trying to open an file which is  not \n compatible with this Programm.\n This Programm can only read Data in the .csv file Format")
                             
    def lookForLen(self,path):
        '''This function is neccessary to identify the number of y-collumns in order to
        fill in arrays correct.It returns the length of the FIRST row, therefore it is important
        to fill in the csv file correctly '''
        collen = 0
        try:
            lenTest = open(path, 'r')
            reader = csv.reader(lenTest,delimiter = ';' , dialect = csv.excel)
            i = 0
        
            for row in reader:#Only way i found to get len of an reader object Line.
                collen = len(row)
                break  
        

            lenTest.close() 
        except csv.Error:
            print ' Opening Fail Window in except of _init_ ' 
        return collen      
    
    def fillArray(self):
        '''fill Method, iterates through every Row of csv file and fills arrays and 
        dictionary with data'''
        i = 0
        go = 0
        
        for i in range(0,self.collen-1):
            self.values.append([])
        try:
            for row in self.reader:
                if go > 0 :
                    append = 0
                    for i in range (1,self.collen):
                        if(row[i]=="" or row[i]=="NaN"):#Looking if row is empty or has an Nonvalue
                            append =1
                        
                    if(append !=1):
                        for i in range (1,self.collen):
                            self.values[i-1].append(float(row[i]))
                  
                    if row[0]!="":
                         self.meta.append(row[0])
                go = 1
        
        except ValueError:
            Fail("Could not import File\n One of your x, or y value is not an number.Maybe its an word or a wrong\n identification for an nonvalue.The right should be NaN")
            self.FillSQL = 1        
       
        try:   
            self.metaDic = {'date':self.meta[0],'exp_name' :self.meta[1],'actor_name':self.meta[2],
                       'nr_series':self.meta[3],'vn_unit':self.meta[4],'vn_desc':self.meta[5],
                       'vn_fault':self.meta[6],'additional_info':self.meta[7]}
        except IndexError:
            if self.FillSQL == 0:
                Fail("Could not import File\nIt seems you didn't fill in your metadata into the csv file the right way.\n Look again at the official Template, your expermient must be filled in exactly as \n given in the file" )
                self.FillSQL = 1  
       
        
        self.values = zip(*self.values)#Have to transpose array in order to match given SQL standard
         
    def fillSql(self):
        '''This method writes the data of the value arrays and the metadictionary into an
        SQLLite file where it is stored'''
        self.fillArray()#First getting data out of csv File
        
        if self.FillSQL == 0: #Only start filling if no Error occurred while writing the arrays
            self.exp = Experiment(self.store+self.stringI+'.db',self.collen-2)
            self.exp.store_metadata(self.metaDic)
            self.exp.store_values(1,self.values)
       
    def getExperiment(self):
        '''This Functions sends back an experiment Object filled with the data of an SQLLite File'''
        try:
            if self.exp != None:
                return self.exp   
       
        except AttributeError:
            return None    
