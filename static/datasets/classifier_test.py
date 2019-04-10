### Red Wine Classification

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


### Dataset as df
dataset = pd.read_csv('winequality-red.csv')


### Shuffle data
from sklearn.utils import shuffle
dataset = shuffle(dataset)

### labels/features split
X = dataset.iloc[:,:11].values  
y = dataset.iloc[:,11:].values


### Standarize Features
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)


### Train/Validation/Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)



################################ Optimal Hyperparameters Models #################################################################################

## SVM
from sklearn.svm import SVC
classifier_svml = SVC(C = 1, kernel = 'linear')
classifier_svml.fit(X_train,y_train)

### Kernel SVM
from sklearn.svm import SVC
classifier_svmg = SVC( C=10, gamma = 1.0, kernel = 'rbf')
classifier_svmg.fit(X_train,y_train)

### Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier_rf = RandomForestClassifier(n_estimators = 200, criterion = 'entropy', 
                                       min_samples_leaf = 3, max_depth = 110,
                                       max_features = 3, min_samples_split = 5) 
classifier_rf.fit(X_train, y_train)


### Gradient Tree Boosting
from sklearn.ensemble import GradientBoostingClassifier
classifier_gtb =  GradientBoostingClassifier(n_estimators = 450, learning_rate = 0.1, max_features = 0.1 )
classifier_gtb.fit(X_train, y_train) 


## Vote Classifier
from sklearn.ensemble import VotingClassifier

classifier_vot = VotingClassifier(
                estimators = [
                               ('svmg', SVC( C=10, gamma = 1.0, kernel = 'rbf')), 
                               ('rf', RandomForestClassifier(n_estimators = 200, criterion = 'entropy', 
                                       min_samples_leaf = 3, max_depth = 110,
                                       max_features = 3, min_samples_split = 5)),
                               ('gtb', GradientBoostingClassifier(n_estimators = 450, learning_rate = 0.1, max_features = 0.1 ))],
                                voting = 'hard')
                               
classifier_vot.fit(X_train, y_train)                         



################################## TESTING ##########################################################################################

y_pred_svml = classifier_svml.predict(X_test)
y_pred_svmg = classifier_svmg.predict(X_test)
y_pred_rf = classifier_rf.predict(X_test)
y_pred_gtb = classifier_gtb.predict(X_test)
y_pred_vot = classifier_vot.predict(X_test)

from sklearn.metrics import accuracy_score

ac_svml = accuracy_score(y_test, y_pred_svml)
ac_svmg = accuracy_score(y_test, y_pred_svmg)
ac_rf = accuracy_score(y_test, y_pred_rf)
ac_gtb = accuracy_score(y_test, y_pred_gtb)
ac_vot = accuracy_score(y_test, y_pred_vot)

print(ac_svml, ac_svmg, ac_rf, ac_gtb, ac_vot)

#################################### DATAFRAME - PREDICTIONS ###############################################################################


## Compile top predictions into one df
from sklearn.metrics import accuracy_score
df_svmg = pd.DataFrame(data=y_pred_svmg, columns = {'y_pred_svmg'})
df_rf = pd.DataFrame(data=y_pred_rf, columns = {'y_pred_rf'})
df_gtb = pd.DataFrame(data=y_pred_gtb, columns = {'y_pred_gtb'})
df_svml = pd.DataFrame(data=y_pred_svml, columns = {'y_pred_svml'})
df_vot = pd.DataFrame(data=y_pred_vot, columns = {'y_pred_vot'})


df_y_test = pd.DataFrame(data=y_test, columns = {'y_test'})


### Construct DataFrame out of current ml predictions:
        
l2_frames = [df_svmg,  df_rf, df_gtb, df_svml, df_vot, df_y_test]
l2_df = pd.concat(l2_frames, axis=1)




### Save Models:

pickle.dump(classifier_rf, open("rf.pkl","wb"))

pickle.dump(classifier_gtb, open("gtb.pkl","wb"))

pickle.dump(classifier_vot, open("vot.pkl","wb"))































