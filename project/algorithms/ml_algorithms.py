## PREPROCESSING
from sklearn.model_selection import train_test_split
import pandas as pd
from collections import Counter
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler

## DATASETS & MODELS
import os.path
import pickle

my_path = os.path.abspath(os.path.dirname(__file__))
wine_quality = os.path.join(my_path, "../../static/datasets/winequality-red.csv")
accuracies_initial_dataset = os.path.join(my_path, "../../static/datasets/accuracies_initial.csv")
accuracies_tune_dataset = os.path.join(my_path, "../../static/datasets/accuracies_tune.csv")
accuracies_test_dataset = os.path.join(my_path, "../../static/datasets/accuracies_test.csv")

## PICKLED MODELS

model_rf_pickled = os.path.join(my_path, "../../static/models/rf.pkl")
model_gtb_pickled = os.path.join(my_path, "../../static/models/gtb.pkl")
model_vot_pickled = os.path.join(my_path, "../../static/models/vot.pkl")

## Load saved models

model_rf = pickle.load(open(model_rf_pickled, "rb"))
model_gtb = pickle.load(open(model_gtb_pickled, "rb"))
model_vot = pickle.load(open(model_vot_pickled, "rb"))


########################## DATASET CHARACTERISTICS #####################################################################

def dataset_characteristics():
    dataset = pd.read_csv(wine_quality)
    dataset_head = dataset.head(10)
    describe = dataset.describe()
    describe = describe.iloc[1:, :]
    rows = len(dataset.index)
    columns = len(dataset.columns)
    counter = Counter(dataset['quality'])
    counter_dict = dict(counter)
    counter_df = pd.DataFrame.from_dict(counter, orient='index').reset_index()
    counter_df = counter_df.rename(columns={'index': 'Quality', 0: 'Records'})
    counter_sort = counter_df.sort_values(by=['Quality'])
    return (dataset_head, describe, rows, columns, counter_sort, counter_dict)


def build_classifier():
    dataset = pd.read_csv(wine_quality)
    dataset = shuffle(dataset)
    X = dataset.iloc[:, :11].values
    y = dataset.iloc[:, 11:].values
    X_head = dataset.iloc[:5, :11]
    y_head = dataset.iloc[:5, 11:]

    sc_X = StandardScaler()
    X_transformed = sc_X.fit_transform(X)

    X_transformed = sc_X.fit_transform(X)
    X_transformed_df = pd.DataFrame(X_transformed)
    X_transformed_df = X_transformed_df.iloc[:5, :11]
    X_transformed_df = X_transformed_df.rename(
        columns={0: 'fixed acidity', 1: 'volatile acidity', 2: 'citric acid', 3: 'residual sugar',
                 4: 'chlorides', 5: 'free sulfur dioxide', 6: 'total sulfur dioxide', 7: 'density',
                 8: 'pH', 9: 'Quality', 10: 'sulphates', 11: 'alcohol', })
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    X_train_len = len(X_train)
    X_test_len = len(X_test)

    accuracies_initial = pd.read_csv(accuracies_initial_dataset)

    return (X_head, y_head, X_transformed, X_transformed_df, X_train_len, X_test_len, accuracies_initial)
