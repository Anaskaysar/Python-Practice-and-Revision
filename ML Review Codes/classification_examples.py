import numpy as np

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

print(type(data))

data.keys()

data.data

data.data.shape

data.target

data.target_names

data.target.shape

data.feature_names

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=.33)


from sklearn.ensemble import RandomForestClassifier

model= RandomForestClassifier()

model.fit(X_train, y_train)

model.score(X_train, y_train)
model.score(X_test, y_test)


predictions = model.predict (X_test)

predictions


N = len(y_test)
predictions == y_test
np.sum(predictions == y_test)/N
