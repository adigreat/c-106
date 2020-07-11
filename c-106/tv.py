import csv 
import numpy as np
def getDataSource (data_path):
    sizeOfTV=[]
    averageTimeSpent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sizeOfTV.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":sizeOfTV,"y":averageTimeSpent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of TV and average time spent watching tv in a week:-\n",correlation[0,1])

def setup():
    data_path="./data/Size of TV,	Average time spent watching TV in a week (hours).csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
    