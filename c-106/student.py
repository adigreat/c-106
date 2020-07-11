import csv 
import numpy as np
def getDataSource (data_path):
    marksInPercentage=[]
    daysPresent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{"x":marksInPercentage,"y":daysPresent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between marks in percentage and daysPresent:-\n",correlation[0,1])

def setup():
    data_path="./data/Student Marks vs Days Present.csv" 
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
    