import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression

#load dataset
data = pd.read_csv('heart.csv')

data_dup = data.duplicated().any

X = data.drop('target', axis=1)
y = data['target']

#  logistic Regrestion
log = LogisticRegression(max_iter=4000)
log.fit(X,y)


#final Prediciton
new_data = pd.DataFrame({
    'age':52,
    'sex':1,
    'cp':0,
    'trestbps':125,
    'chol':212,
    'fbs':0,
    'restecg':1,
    'thalach':129,
    'exang':0,
    'oldpeak':1.0,
    'slope':2,
    'ca':2,
    'thal':3,
},index=[0])

p = log.predict(new_data)
if p[0] == 0:
    print("No Disease")
else:
    print("Disease")

pickle.dump(log, open('mlmodel.pkl','wb'))


