import numpy
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
titanic_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/train.csv')
titanic_data.head()
titanic_data.describe()
import seaborn as sns
sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
list(titanic_data.columns)
titanic_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
titanic_data
titanic_data_new = titanic_data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
titanic_data_new
titanic_data_new.describe()
plt.show()
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
for train_indices, test_indices in split.split(titanic_data, titanic_data[["Survived", "Pclass", "Sex"]]):
    strat_train_set = titanic_data.loc[train_indices]
    strat_test_set = titanic_data.loc[test_indices]
    strat_test_set

plt.subplot(1,2,1)
strat_train_set["Survived"].hist()
strat_train_set["Pclass"].hist()
plt.subplot(1,2,2)
strat_test_set["Survived"].hist()
strat_test_set["Pclass"].hist()
plt.show()
strat_train_set.info()
import sklearn.impute
from sklearn import impute
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder


class AgeImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        imputer = SimpleImputer(strategy="mean")
        X["Age"] = imputer.fit_transform(X[["Age"]])
        return X
from sklearn.preprocessing import OneHotEncoder
class FeatureEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        encoder = OneHotEncoder()
        matrix = encoder.fit_transform(X[["Embarked"]]).toarray()
        column_names = ["C", "S", "Q", "N"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        matrix = encoder.fit_transform(X[["Sex"]]).toarray()   
        column_names = ["Female", "Male"]
        for i in range(len(matrix.T)):
            X[column_names[i]] = matrix.T[i]
        return X


class FeatureDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X.drop(["Emabrked", "Name", "Ticket", "Cabin", "Sex", "N"], axis=1, errors="ignore")

from sklearn.pipeline import Pipeline
pipeline = Pipeline([("ageimputer", AgeImputer()), ("featureencoder", FeatureEncoder()), ("featuredropper", FeatureDropper())])

strat_train_set = pipeline.fit_transform(strat_train_set)
strat_train_set
strat_train_set = strat_train_set.drop('Embarked', axis=1)
strat_train_set.info()

from sklearn.preprocessing import StandardScaler

X = strat_train_set.drop(['Survived'], axis=1)
Y = strat_train_set['Survived']
scaler = StandardScaler()
X_data = scaler.fit_transform(X)
Y_data = Y.to_numpy()
X_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
clf = RandomForestClassifier()
param_grid = [{"n_estimators": [10, 100, 200, 500], "max_depth":[None, 5, 10], "min_samples_split": [2, 3, 4]}]
grid_search = GridSearchCV(clf, param_grid, cv=3, scoring="accuracy", return_train_score=True)
grid_search.fit(X_data, Y_data)
final_clf = grid_search.best_estimator_
final_clf
strat_test_set = pipeline.fit_transform(strat_test_set)
strat_test_set
strat_test_set = strat_test_set.drop('Embarked', axis=1)
strat_test_set.info()
X_test = strat_test_set.drop(['Survived'], axis=1)
Y_test = strat_test_set['Survived']
scaler = StandardScaler()
X_data_test = scaler.fit_transform(X_test)
Y_data_test = Y_test.to_numpy()
final_clf.score(X_data_test, Y_data_test)
final_clf
final_data = pipeline.fit_transform(titanic_data)
final_data
final_data.info()
final_data= final_data.drop(['Embarked', 'S'], axis=1)
X_final = final_data.drop(['Survived'], axis=1)
Y_final = final_data['Survived']
scaler = StandardScaler()
X_data_final = scaler.fit_transform(X_final)
Y_data_final = Y_final.to_numpy()

prod_clf = RandomForestClassifier()
param_grid = [{"n_estimators": [10, 100, 200, 500], "max_depth":[None, 5, 10], "min_samples_split": [2, 3, 4]}]
grid_search = GridSearchCV(prod_clf, param_grid, cv=3, scoring="accuracy", return_train_score=True)
grid_search.fit(X_data_final, Y_data_final)
prod_final_clf = grid_search.best_estimator_
prod_final_clf
titanic_test_data = pd.read_csv('C:/Users/chris/OneDrive/Υπολογιστής/Εργασία Κωνσταντίνα Ζήκου/test.csv')
#titanic_test_data = titanic_test_data.drop(['Q'], axis=1)
final_test_data = pipeline.fit_transform(titanic_test_data)
final_test_data.info()
final_test_data
X_final_test = final_test_data
X_final_test
X_final_test = X_final_test.drop(['Embarked', 'Q'], axis=1)
X_final_test = X_final_test.fillna(method="ffill")
X_final_test = pd.get_dummies(X_final_test)
scaler = StandardScaler()
#X_data_final_test = X_data_final_test.drop(['Embarked', 'S', 'Q', 'Survived'], axis=1)
X_data_final_test = scaler.fit_transform(X_final_test)
#X_data_final_test = X_data_final_test.iloc[:,:10].values
predictions = prod_final_clf.predict(X_data_final_test)
predictions
final_df = pd.DataFrame(titanic_test_data['PassengerId'])
final_df['Survived'] = predictions
final_df.to_csv("data/predictions.csv", index=False)

