from sklearn.linear_model import LinearRegression
from math import isnan
import pandas as pd
linreg = LinearRegression()

cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']
toFill = [1, 2, 3, 4, 5]

dataWithNull = pd.read_csv('diabetes_dataset.csv').astype('float')
dataWithoutNull = dataWithNull.dropna()

trainDataX = dataWithoutNull.iloc[:,[0, 6, 7]]
trainDataY = dataWithoutNull.iloc[:,[1, 2, 3, 4, 5]]

linreg.fit(trainDataX, trainDataY)

testData = dataWithNull.iloc[:,[0, 6, 7]]
#print(testData)
r = pd.DataFrame(linreg.predict(testData))
print(r)

for k in range(len(toFill)):
    i = toFill[k]
    for j in range(len(dataWithNull[cols[i]])):
        if (isnan(dataWithNull[cols[i]][j])):
            dataWithNull.set_value(j, cols[i], r[k][j])
print(dataWithNull)
dataWithNull.to_csv("diabetes_LinearRegression_dataset.csv", index=False)