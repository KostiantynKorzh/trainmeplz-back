import os
import re

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# from sklearn.linear_model import

# from services import dataservice

# def train(classifierType):
#     # load dataset
#     iris_dataset = load_iris()
#
#     # split dataset to train and test values (75:25 here)
#     # X_name - data(values) itself, array
#     # y_name - target values ([0, 1, 2] as [setosa, versicolor, virginica])
#     X_train, X_test, y_train, y_test = train_test_split(
#         iris_dataset['data'], iris_dataset['target'], random_state=0)
#
#     classifier = "emptiness"
#
#     if classifierType == 1:
#         # k-nearest classifier
#         classifier = KNeighborsClassifier(n_neighbors=1)
#     elif classifierType == 2:
#         # logistic regression classifier
#         classifier = LogisticRegression(solver='lbfgs', max_iter=100)
#
#     # train our model
#     classifier.fit(X_train, y_train)
#
#     # making prediction on test values
#     y_pred = classifier.predict(X_test)
#
#     print("Test set predictions:\n {}".format(y_pred))
#     print("Test set score (np.mean): {:.2f}".format(np.mean(y_pred == y_test)))
#
#
# def show_dataset_info():
#     iris = load_iris()
#     print(iris.feature_names)
#     print(iris.target)
#     print(iris.target_names)
#
#
# train(2)


def create_dataset(*labels):
    files = os.listdir(r"C:\Users\Kostiantyn_Korzh\Desktop\self_study\ml\trainmeplz\back\app\images\\")
    label_mapping = map_labels_to_images(labels, files)
    print(label_mapping)


def map_labels_to_images(labels, files):
    label_mapping = {}
    for label in labels:
        label_mapping[label] = []
    for file in files:
        label = parse_label_from_filename(file)
        if label in labels:
            label_mapping[label].append(file)

    return label_mapping


def parse_label_from_filename(filename):
    return re.search('(?<=_label_).*(?=\\.)', filename).group()


create_dataset('qaz', 'sfdfs', 'sdf', 'sfsf')
