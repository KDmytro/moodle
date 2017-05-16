# from src.data.funnel import Funnel
from src.data.explore_dataset import DataExplorer
from src.features.build_features import FeatureFactory

from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_predict
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


class ModelFactory(object):

    def __init__(self):



        self.cv = StratifiedShuffleSplit(n_splits=2, test_size=0.2, random_state=123)

        self.clf_LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
        self.clf_LRCV = LogisticRegressionCV(Cs=1.0,
                                            class_weight='balanced',
                                            solver='liblinear',
                                            penalty='l1',
                                            cv=10)
        self.clf_RF = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)




    def print_coefs(self,labels,coefs):
        print "Coefficients:"
        for c in sorted(zip(labels,coefs), key = lambda t: -abs(t[1])):
            print "{} : {}".format(c[0],c[1])



    def fit_wk1_model(self,X,y):

        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        self.wk1_model = self.clf_LR.fit(X_train,y_train)

        return self.wk1_model

    def fit_model(by_date='2016-08-14'):

        # Init new feature matrix
        FF.init_registered_by(by_date)
        FF.make_dict_features_by_date(FF.features,by_date)

        FF.make_y()

        X = FF.data.values
        y = FF.y.values

        # Train/Test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25,
                                                             random_state=123)

        # GridSearch for best params on LR
        param_grid = {
                        'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                        'penalty': ['l1','l2'],
                        'class_weight': ['balanced', None]
                     }


        clf = GridSearchCV(LogisticRegression(), param_grid, scoring='roc_auc',cv=5)
        clf.fit(X_train,y_train)
        # clf.cv_results_
        print clf.best_params_

        y_predict = clf.best_estimator_.predict(X_test)
        print classification_report(y_test,y_predict)
        print_coefs(FF.data.columns,clf.best_estimator_.coef_[0])



    def fit_wk2_model(self,X,y):

        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        self.wk2_model = self.clf_LR.fit(X_train,y_train)

        return self.wk2_model

    def fit_wk3_model(self,X,y):

        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        self.wk3_model = self.clf_LR.fit(X_train,y_train)

        return self.wk3_model

    def fit_wk4_model(self,X,y):

        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        self.wk4_model = self.clf_LR.fit(X_train,y_train)

        return self.wk4_model


    def print_scores(self,model):
        model
        print "Scores:"
        print classification_report(y_test,y_hat)
        print_coefs(funnel.data.columns,clf_LR.coef_[0])
        print "\n---\n"



if __name__ == "__main__":

    DE = DataExplorer()
    logs = DE.get_course_logs()
    completions = DE.get_completions()

    FF = FeatureFactory(logs,completions)
    features = FF.features

    MF = ModelFactory()


    # Week 1 model
    FF.init_registered_by("2016-08-14")
    FF.make_dict_features_by_date(features,'2016-08-14')
    X = FF.data.values
    y = FF.y.values

    wk1_model = MF.fit_wk1_model(X,y)

    # Week 2 model
    FF.init_data()
    FF.make_dict_features_by_date(features,'2016-08-21')
    X = FF.data.values
    y = FF.y.values

    wk2_model = MF.fit_wk2_model(X,y)

    # Week 3 model
    FF.init_data()
    FF.make_dict_features_by_date(features,'2016-08-28')
    X = FF.data.values
    y = FF.y.values

    wk3_model = MF.fit_wk3_model(X,y)

    # Week 4 model
    FF.init_data()
    FF.make_dict_features_by_date(features,'2016-09-07')
    X = FF.data.values
    y = FF.y.values

    wk4_model = MF.fit_wk4_model(X,y)
