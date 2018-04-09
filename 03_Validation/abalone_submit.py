#!/usr/bin/env python3
# -*- coding: utf-8 -*-
SEND = 0

def printScore(score, X, y_pred):
    print(" - Score:")
    for i in sorted(score):
        print("    ", i, ": ", max(score[i]), ", ", score[i], sep='')
    print("    accuracy_score: ", metrics.accuracy_score(X, y_pred), sep='')

"""
Atividade para trabalhar o pré-processamento dos dados.

Criação de modelo preditivo para diabetes e envio para verificação de peformance
no servidor.

@author: Aydano Machado <aydano.machado@gmail.com>
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
from sklearn import metrics, datasets
from sklearn.metrics import recall_score
import requests

print('\n - Lendo o arquivo com o dataset sobre diabetes')
data = pd.read_csv('abalone_dataset_sexAsNum.csv')
dataCopy = pd.read_csv('abalone_dataset_sexAsNumCopy.csv')

# Criando X and y par ao algorítmo de aprendizagem de máquina.
print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo diabetes_dataset')
# Caso queira modificar as colunas consideradas basta algera o array a seguir.
feature_cols = ['sex', 'length', 'diameter', 'height',
                'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight']
#feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                #'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = data[feature_cols]
y = data.type

# Ciando o modelo preditivo para a base trabalhada
print(' - Criando modelo preditivo')
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

#realizando previsões com o arquivo de
print(' - Aplicando modelo e enviando para o servidor')
data_app = pd.read_csv('abalone_app_sexAsNum.csv')
y_pred = neigh.predict(data_app)
#print(*y_pred)

scoring = ['precision_macro', 'recall_macro']
scores = cross_validate(neigh, X, y, scoring=scoring, cv=5, return_train_score=True)
score_predict = cross_val_predict(neigh, X, y, cv=5)
printScore(scores, y, score_predict)

# Enviando previsões realizadas com o modelo para o servidor
URL = "http://aydanomachado.com/mlclass/03_Validation.php"

#TODO Substituir pela sua chave aqui
DEV_KEY = "Não pagamos || estatística ||"

# json para ser enviado para o servidor
data = {'dev_key':DEV_KEY,
        'predictions':pd.Series(y_pred).to_json(orient='values')}

# Enviando requisição e salvando o objeto resposta
if (SEND): r = requests.post(url = URL, data = data)

# Extraindo e imprimindo o texto da resposta
if (SEND): pastebin_url = r.text
if (SEND): print(" - Resposta do servidor:\n", r.text, "\n")
