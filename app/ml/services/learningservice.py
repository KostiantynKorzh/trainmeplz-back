from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

from app.ml.services.dataservice import create_dataset_for_labels


class Model:

    def __init__(self, *labels):
        self.dataset = create_dataset_for_labels(labels)

    def train(self):
        dataset = self.dataset

        X_train, X_test, y_train, y_test = train_test_split(
            dataset['data'], dataset['target'], random_state=0)

        classifier = LogisticRegression(solver='lbfgs', max_iter=100)

        classifier.fit(X_train, y_train)

        y_pred = classifier.predict(X_test)

        print(X_test)

        print("Test set predictions:\n {}".format(y_pred))
        print("Test set score (np.mean): {:.2f}".format(np.mean(y_pred == y_test)))
