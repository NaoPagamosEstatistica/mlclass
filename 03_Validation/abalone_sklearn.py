#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
from sklearn import metrics, datasets
from sklearn.metrics import recall_score
SEND = 0

def printScore(score, X, y_pred):
    for i in sorted(score):
        print("    ", i, ": ", max(score[i]), ", ", score[i], sep='')
    print("    accuracy_score: ", metrics.accuracy_score(X, y_pred), sep='')

print('\n - Lendo o arquivo com o dataset sobre diabetes')
data = pd.read_csv('abalone_dataset_sexAsNum.csv')
dataCopy = pd.read_csv('abalone_dataset_sexAsNumCopy.csv')

print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo diabetes_dataset')
feature_cols = ['sex', 'length', 'diameter', 'height',
                'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight']
X = data[feature_cols]
y = data.type

print(' - Criando modelo preditivo')
model = [KNeighborsClassifier(n_neighbors=15), LinearRegression(fit_intercept=False), NearestCentroid()]
toDo = [1, 0, 1]

scoring = ['precision_macro', 'recall_macro']
for i in range(len(model)):
    if (not toDo[i]): continue
    print("\n", model[i].__class__.__name__)
    model[i].fit(X, y)
    scores = cross_validate(model[i], X, y, scoring=scoring, cv=10, return_train_score=True)

    score_predict = cross_val_predict(model[i], X, y, cv=10)
    printScore(scores, y, score_predict)
