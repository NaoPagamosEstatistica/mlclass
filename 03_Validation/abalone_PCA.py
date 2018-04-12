import pandas as pd
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
from sklearn import metrics, datasets, preprocessing, linear_model, tree, naive_bayes, svm, neural_network
from sklearn.metrics import recall_score
DETAILED = 0

def printScore(score, X, y_pred):
    if (DETAILED):
        for i in sorted(score):
            print("    ", i, ": ", max(score[i]), ", ", score[i], sep='')
    print("    accuracy_score: ", metrics.accuracy_score(X, y_pred), sep='')
    return(metrics.accuracy_score(X, y_pred))

def tryModels(model, toDo, scoring, X, y):
    best = [0, 0]
    for i in range(len(model)):
        if (not toDo[i]): continue
        print("\n", model[i].__class__.__name__)
        model[i].fit(X, y)
        scores = cross_validate(model[i], X, y, scoring=scoring, cv=10, return_train_score=True)
        score_predict = cross_val_predict(model[i], X, y, cv=10)
        now = printScore(scores, y, score_predict)
        if (now > best[0]):
            best[0] = now
            best[1] = model[i].__class__.__name__
    return(best)

def testColCombination(model, toDo, socring, data, feature_cols):
    best = [0, 0, 0]
    for i in range(54, 2**len(feature_cols)):
        rep = bin(i)[2:]
        rep = '0' * (len(feature_cols) - len(rep)) + rep
        newCols = []
        for j in range(len(feature_cols)):
            if (rep[j] == '1'):
                newCols += [feature_cols[j]]
        print(i, newCols)

        X = data[newCols]
        y = data.type
        now = tryModels(model, toDo, scoring, X, y)
        if (now[0] > best[0]):
            best[0], best[1] = now[0], now[1]
            best[2] = newCols
        print(best)
    return(best)

scoring = ['precision_macro', 'recall_macro']

print('\n - Lendo o arquivo com o dataset sobre diabetes')
data = pd.read_csv('abalone_dataset_sexAsNum.csv')

print(' - Criando modelo preditivo')
model = [KNeighborsClassifier(n_neighbors=19), NearestCentroid(), linear_model.SGDClassifier(loss="hinge", penalty="l2"), tree.DecisionTreeClassifier(), naive_bayes.GaussianNB(), svm.LinearSVC(), neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)]
toDo = [0, 0, 0, 0, 0, 1, 0]

print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo diabetes_dataset')
feature_cols = ['length', 'whole_weight', 'shucked_weight', 'viscera_weight']
#['sex', 'length', 'diameter', 'height',
                #'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight']


X = data[feature_cols]
y = data.type

#pca = PCA(n_components=2)
#pca.fit(X)
#X = pca.transform(X)

bfile = open("best", "w")
print(tryModels(model, toDo, scoring, X, y))
bfile.close()
# 19