import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


### Dataset as df
dataset = pd.read_csv('winequality-red.csv')


### Shuffle data
from sklearn.utils import shuffle
dataset = shuffle(dataset)


### Separate label y from features X
X = dataset.iloc[:,:11].values  
y = dataset.iloc[:,11].values


### Standardize features
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)


### Train/Validation/Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

################################### MODELS ################################################################################################

### Logisitic Regression
from sklearn.linear_model import LogisticRegression
classifier_log = LogisticRegression()
classifier_log.fit(X_train,y_train)

### K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
classifier_knn = KNeighborsClassifier()
classifier_knn.fit(X_train, y_train)

### SVM
from sklearn.svm import SVC
classifier_svml = SVC()
classifier_svml.fit(X_train,y_train)


### Kernel SVM
from sklearn.svm import SVC
classifier_svmg = SVC()
classifier_svmg.fit(X_train,y_train)

#### Naive Bayes - Gaussian
from sklearn.naive_bayes import GaussianNB
classifier_nb = GaussianNB()
classifier_nb.fit(X_train, y_train)

### AdaBoost
from sklearn.ensemble import AdaBoostClassifier
classifier_ada = AdaBoostClassifier()
classifier_ada.fit(X_train, y_train)

### Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier_rf = RandomForestClassifier() 
classifier_rf.fit(X_train, y_train)


### Gradient Tree Boosting
from sklearn.ensemble import GradientBoostingClassifier
classifier_gtb =  GradientBoostingClassifier()
classifier_gtb.fit(X_train, y_train) 


################################## k-Fold Cross Validation ########################################################################

from sklearn.model_selection import cross_val_score

accuracies_log = cross_val_score(estimator = classifier_log, X = X_train, y = y_train, cv = 10, n_jobs = -1)  
accuracies_knn = cross_val_score(estimator = classifier_knn, X = X_train, y = y_train, cv = 10, n_jobs = -1) 
accuracies_svml = cross_val_score(estimator = classifier_svml, X = X_train, y = y_train, cv = 10, n_jobs = -1) 
accuracies_svmg = cross_val_score(estimator = classifier_svmg, X = X_train, y = y_train, cv = 10, n_jobs = -1)  
accuracies_ada = cross_val_score(estimator = classifier_ada, X = X_train, y = y_train, cv = 10, n_jobs = -1)
accuracies_nb = cross_val_score(estimator = classifier_nb, X = X_train, y = y_train, cv = 10, n_jobs = -1)
accuracies_rf = cross_val_score(estimator = classifier_rf, X = X_train, y = y_train, cv = 10, n_jobs = -1)  
accuracies_gtb = cross_val_score(estimator = classifier_gtb, X = X_train, y = y_train, cv = 10, n_jobs = -1)
 
print(accuracies_log.mean(), accuracies_log.std())
print(accuracies_knn.mean(), accuracies_knn.std())
print(accuracies_svml.mean(), accuracies_svml.std())
print(accuracies_svmg.mean(), accuracies_svmg.std())
print(accuracies_ada.mean(), accuracies_ada.std())
print(accuracies_nb.mean(), accuracies_nb.std())
print(accuracies_rf.mean(), accuracies_rf.std())
print(accuracies_gtb.mean(), accuracies_gtb.std())


## Compile top predictions into one df
from sklearn.metrics import accuracy_score
df_knn = pd.DataFrame(data=y_pred_knn, columns = {'y_pred_knn'})
df_svmg = pd.DataFrame(data=y_pred_svmg, columns = {'y_pred_svmg'})
df_rf = pd.DataFrame(data=y_pred_rf, columns = {'y_pred_rf'})
df_gtb = pd.DataFrame(data=y_pred_gtb, columns = {'y_pred_gtb'})
df_log = pd.DataFrame(data=y_pred_log, columns = {'y_pred_log'})
df_svml = pd.DataFrame(data=y_pred_svml, columns = {'y_pred_svml'})
df_vot = pd.DataFrame(data=y_pred_vot, columns = {'y_pred_vot'})

df_y_test = pd.DataFrame(data=y_test, columns = {'y_test'})



##################################### Grid Search  #################################################################################

from sklearn.model_selection import GridSearchCV  

### SVMS

svml_parameters = [ {'C': [1,10, 100, 1000], 'kernel' : ['linear']} ]


svmg_parameters = [{'C': [1,10, 100, 1000],'kernel' : ['rbf'], 'gamma': np.logspace(-3, 2, 6), 'degree': [1,2,3,4,5]},
                   {'C': [1,10, 100, 1000],'kernel' : ['poly'], 'gamma': np.logspace(-3, 2, 6), 'degree': [1,2,3,4,5]}]


### KNN 
knn_parameters = [{'n_neighbors' : [3,5,8,13], 'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute']}]



### AdaBoost 
ada_parameters = [{'n_estimators': [100, 200, 300], 'learning_rate': [1, 0.1, 0.01, 0.001]}]


### Random Forest
rf_parameters = [{'min_samples_leaf': [3, 4, 5],
                  'n_estimators': [100, 200, 300, 500, 600] }]


### Gradient Tree Boosting
gtb_parameters = [{'learning_rate': [1, 0.1, 0.01, 0.001], 'n_estimators': [100, 200, 300, 500, 600]}]


### SPECIFY WHICH classifier_ and _parameter you want to validate: 
grid_search = GridSearchCV(estimator = classifier_gtb, param_grid = gtb_parameters, scoring = 'accuracy', cv = 10, n_jobs = -1)

grid_search = grid_search.fit(X_train, y_train)
best_accuracy = grid_search.best_score_ 
best_parameters = grid_search.best_params_

## Optimal  parameters for svml are: {'C': 1], 'kernel' : 'linear'}  -- Accuracy 59% vs avg 59%
## Optimal  parameters for kernel svmg are {'C': 10, 'gamma': 1.0, 'kernel': 'rbf'}  -- Accuracy 65% vs avg 61% 
## Optimal parameters for knn are {'algorithm': 'auto', 'n_neighbors': 13}   -- Accuracy 56% vs avg 54%
## Optimal parameters for ada are {'learning_rate': 0.01, 'n_estimators': 100} -- Accuracy 57% vs 54%
## Optimal parameters for rf are  {'criterion': 'entropy', 'min_samples_leaf': 3, max_depth': 110, 'max_features': 3, 'min_samples_split': 5, 'n_estimators': 200}  -- Accuracy 66% vs avg 65%


print(best_parameters)