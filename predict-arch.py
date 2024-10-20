import numpy as np 
import pandas as pd 
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

df = pd.read_csv('dataset.csv')
print(df.shape)

X = df.drop(columns=['placed'])
y = df['placed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

### Regression.

scaler = StandardScaler()
X_train_tfm = scaler.fit_transform(X_train)
X_test_tfm = scaler.transform(X_test)

regress_score = accuracy_score(y_test,
	LogisticRegression().fit(X_train_tfm, y_train).predict(X_test_tfm))

print(f'Regression: {regress_score}')

### Random Forest Classifier.

rfc_score = accuracy_score(y_test,
	RandomForestClassifier().fit(X_train, y_train).predict(X_test))

print(f'Random Forest Classifier: {rfc_score}')

### Support Vector Machine.

svc = SVC(kernel='rbf')
svc_model = svc.fit(X_train, y_train)
svc_score = accuracy_score(y_test, svc_model.predict(X_test))

print(f'Support Vector Machine: {svc_score}')

### 'pickle / joblib' File.
pickle.dump(svc_model, open('predict.pkl', 'wb'))