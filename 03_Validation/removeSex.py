import pandas as pd
k = {'M': 1, 'F': 2, 'I': 3}

def removeSex(data):
    for j in range(len(data)):
        data.set_value(j, "sex", k[data["sex"][j]])

dataset = pd.read_csv("abalone_dataset.csv")
app = pd.read_csv("abalone_app.csv")

removeSex(dataset)
removeSex(app)

dataset.to_csv("abalone_dataset_sexAsNum.csv", index=False)
app.to_csv("abalone_app_sexAsNum.csv", index=False)
