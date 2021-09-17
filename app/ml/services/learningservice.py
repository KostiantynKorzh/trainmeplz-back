import numpy as np
from sklearn.linear_model import LogisticRegression

from app.ml.services.dataservice import create_dataset_for_labels


class Model:

    def __init__(self, *labels):
        self.dataset = create_dataset_for_labels(labels)
        self.classifier = None

    def train(self):
        dataset = self.dataset

        # X_train, X_test, y_train, y_test = train_test_split(
        #     dataset['data'], dataset['target'], random_state=0)

        X_train = dataset['data']
        # X_test = dataset['data'][1].reshape(1, -1)
        y_train = dataset['target']
        # y_test = 0

        self.classifier = LogisticRegression(solver='lbfgs', max_iter=100)

        self.classifier.fit(X_train, y_train)

        print('Learning finished successfully')

    def test(self, test_data):
        test_input = test_data['data'].reshape(1, -1)
        test_output = test_data['target']
        model_prediction = self.classifier.predict(test_input)

        print("Test set predictions:\n {}".format(model_prediction))
        print("Test set score (np.mean): {:.2f}".format(np.mean(test_output == model_prediction)))

        return model_prediction
