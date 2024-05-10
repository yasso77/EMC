import pyodbc

class reportModel():
     cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=localhost;Database=dbVisionClinic;Port=myport;User ID=sa;Password=Pa$$w0rd')

     def calcualteEvalulationDegreeOnDateBasis(self,repDate):        
        cursor = self.cnxn.cursor()	
        cursor.execute("SELECT * FROM EMP") 
        row = cursor.fetchone() 
        
       
