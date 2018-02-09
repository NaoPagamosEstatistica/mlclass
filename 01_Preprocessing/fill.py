import pandas as pd
from math import isnan

def getMedianFromArray(array):
    if (len(array) % 2):
        return(array[len(array) // 2])
    else:
        return((array[len(array) // 2] + array[len(array) // 2 - 1]) / 2)

def getMedian(data, cols):
    median = {}
    for i in cols:
        validValues, values = [], 0
        for j in data[i]:
            if (not isnan(j)):
                validValues += [j]
                values += 1
        median[i] = getMedianFromArray(validValues)
    return(median)

def getAverage(data, cols):
    average = {}
    for i in cols:
        a, values = 0, 0
        for j in data[i]:
            if (not isnan(j)):
                a += j
                values += 1
        average[i] = a / values
    return(average)

def getMinMax(data, cols):
    minimum, maximum = {}, {}
    for i in cols:
        validValues = []
        for j in data[i]:
            if (not isnan(j)):
                validValues += [j]
        minimum[i] = min(validValues)
        maximum[i] = max(validValues)
    return(minimum, maximum)

def normalize(data, cols):
    minimum, maximum = getMinMax(data, cols)
    for i in cols:
        for j in range(len(data[i])):
            data.set_value(j, i, (data[i][j] - minimum[i]) / (maximum[i] - minimum[i]))
            #data.set_value(j, i, (data[i][j]) / (maximum[i]))

def fixFile(data, cols):
    average = getAverage(data, cols)
    median = getMedian(data, cols)
    minimum, maximum = getMinMax(data, cols)
    for i in cols: # Put values
        for j in range(len(data[i])):
            if (isnan(data[i][j])):
                data.set_value(j, i, median[i])

def removeRows(data, cols):
    removed = {}
    for i in cols:
        for j in range(len(data[i]) - 1, 0, -1):
            if (j in removed): continue
            if (isnan(data[i][j])):
                print("dropping:", j)
                data = data.drop([j])
                removed[j] = 1
                #removeRows(data, cols)
    return(data)

cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']
dataSet = pd.read_csv('diabetes_average_dataset_NoPedi.csv').astype('float')
fixFile(dataSet, cols)
normalize(dataSet, cols)
dataSet.to_csv("diabetes_average_dataset_NoPedi_NormByMinMax.csv", index=False)

dataApp = pd.read_csv('diabetes_app_NoPedi.csv').astype('float')
normalize(dataApp, cols)
print(dataApp)
dataApp.to_csv("diabetes_app_NoPedi_NormByMinMax.csv", index=False)
