# Load libraries
import pandas
from pandas.plotting import scatter_matrix
#import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR, SVC

class predictor:
    # class attribute
    category = "Prediction Class"

    # instance attribute
    def __init__(self, time, kwh, chargerType):
        self.time = time
        self.kwh = kwh
        self.chargerType = chargerType

    # Prediction Method
    # returns the predicted Location
    def predict(self):
        names = ['Time', 'kwh', 'type', 'site']
        data = pandas.read_csv('removed0kwh30min.csv', names=names)
        array = data.values

        X = array[:, 0:3]

        Y = array[:, 3]

        test_size = 0.2
        seed = 9
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size,
                                                                            random_state=seed)
        clf = SVC(C=30.0, cache_size=200, class_weight=None, coef0=0.0,
                  decision_function_shape='ovo', degree=3, gamma='scale', kernel='rbf',
                  max_iter=-1, probability=False, random_state=None, shrinking=False,
                  tol=1e-4, verbose=False)

        model = clf.fit(X_train, Y_train)
        # Create new observation
        new_observation = [[self.time, self.kwh, self.chargerType]]

        # Predict class
        print('Prediction Accuracy:')
        output = model.predict(X_test)

        acc = accuracy_score(Y_test, output.round())
        print(acc)

        singlePred = model.predict(new_observation)
        print('Predicted Location Id')
        print(singlePred)

        return singlePred
