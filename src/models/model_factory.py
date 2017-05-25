# from src.data.funnel import Funnel
from src.data.explore_dataset import DataExplorer
from src.features.build_features import FeatureFactory

from sklearn.feature_selection import SelectPercentile, f_classif, chi2

from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_predict
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, roc_curve, auc, accuracy_score
from sklearn.dummy import DummyClassifier

from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, SGDClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

import statsmodels.api as sm

import operator
import numpy as np
import matplotlib.pyplot as plt


class ModelFactory(object):

    def __init__(self):



        self.cv = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=123)

        self.clf_LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
        self.clf_LRCV = LogisticRegressionCV(Cs=1.0,
                                            class_weight='balanced',
                                            solver='liblinear',
                                            penalty='l1',
                                            cv=10)
        self.clf_RF = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)

        self.f, self.ax = plt.subplots()
        self.ax.set_xlim([0.0, 1.0])
        self.ax.set_ylim([0.0, 1.05])
        self.ax.set_xlabel('False Positive Rate')
        self.ax.set_ylabel('True Positive Rate')
        self.ax.set_title('ROC Curves')
        self.ax.legend(loc="lower right")



    def fit_wk1_model(self,X,y):

        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        self.wk1_model = self.clf_LR.fit(X_train,y_train)

        return self.wk1_model

    def fit_model(self,X,y,by_date='2016-08-14'):

        # Train test split using StratifiedShuffleSplit
        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # Feature Selection
        # selector = SelectPercentile(chi2, percentile=100)
        #
        # selector.fit(X_train, y_train)
        # # X_train = selector.transform(X_train)
        # # X_test = selector.transform(X_test)
        #
        # selector.scores_
        # selector.pvalues_

        # feat_pvals = dict(zip(FF.data.columns, np.nan_to_num(selector.pvalues_)))
        # sorted(feat_pvals.items(), key=operator.itemgetter(1),reverse=True)
        # feat_scores = dict(zip(FF.data.columns, np.nan_to_num(selector.scores_)))
        # feat_scores = sorted(feat_scores.items(), key=operator.itemgetter(1),reverse=True)


        # GridSearch for best params on LR
        param_grid = {
                        'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                        'penalty': ['l1','l2'],
                        'class_weight': ['balanced']
                     }


        clf = GridSearchCV(LogisticRegression(), param_grid, scoring='recall',cv=5)
        clf.fit(X_train,y_train)
        # best params
        print clf.best_params_

        # Calculate and print accuracy scores
        y_predict = clf.best_estimator_.predict(X_test)

        print classification_report(y_test,y_predict)
        print accuracy_score(y_test,y_predict)
        self.plot_roc(y_test, clf.best_estimator_.predict_proba(X_test), "LR")
        return clf.best_estimator_

        # self.print_coefs(FF.data.columns[selector.get_support()],
        #                     clf.best_estimator_.coef_[0],
        #                     # np.nan_to_num(selector.scores_),
        #                     np.nan_to_num(selector.pvalues_))


        # clf = GridSearchCV(LogisticRegression(), param_grid, scoring='roc_auc', cv=5)
        # clf.fit(X_train[:,selector.get_support()],y_train)

        # print clf.best_params_

        # y_predict = clf.best_estimator_.predict(X_test[:,selector.get_support()])
        # print classification_report(y_test,y_predict)
        # self.print_coefs(FF.data.columns[selector.get_support()],clf.best_estimator_.coef_[0],selector.pvalues_)


    def fit_tree_model(self,X,y,by_date='2016-08-14'):

        # Train test split using StratifiedShuffleSplit
        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # GridSearch for best params on LR
        param_grid = {
                        'max_depth': np.arange(3, 10),
                        'max_leaf_nodes' : [None, 3,4,5,10,15,20],
                        'class_weight': ['balanced']
                     }


        clf = GridSearchCV(DecisionTreeClassifier(), param_grid, scoring='roc_auc',cv=5)
        clf.fit(X_train,y_train)
        # best params
        print clf.best_params_

        # Calculate and print accuracy scores
        y_predict = clf.best_estimator_.predict(X_test)


        # Print Scores and plot ROC curve
        print classification_report(y_test,y_predict)
        self.plot_roc(y_test, clf.best_estimator_.predict_proba(X_test), "DTree")
        return clf.best_estimator_

    def fit_dummy(self,X,y):
        # Train test split using StratifiedShuffleSplit
        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        clf = DummyClassifier(strategy='stratified',random_state=123)
        clf.fit(X_train,y_train)

        # Calculate and print accuracy scores
        y_predict = clf.predict(X_test)

        # Print Scores and plot ROC curve
        print classification_report(y_test,y_predict)
        self.plot_roc(y_test, clf.predict_proba(X_test))

    def fit_SVC(self,X,y):

        # Train test split using StratifiedShuffleSplit
        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # GridSearch for best params on LR
        param_grid = {
                        'C': [0.001, 0.1],
                        'kernel': ['rbf'],
                        'class_weight': ['balanced']
                     }


        clf = GridSearchCV(SVC(probability=True), param_grid, scoring='roc_auc',cv=5)
        clf.fit(X_train,y_train)
        # best params
        print clf.best_params_

        # Calculate and print accuracy scores
        y_predict = clf.best_estimator_.predict(X_test)

        print classification_report(y_test,y_predict)
        self.plot_roc(y_test, clf.best_estimator_.predict_proba(X_test), "SVC")
        return clf.best_estimator_

    def fit_SGD(self,X,y):

        # Train test split using StratifiedShuffleSplit
        for train_index, test_index in self.cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # GridSearch for best params on LR
        param_grid = {
                        'C': [0.001, 0.1],
                        'kernel': ['rbf'],
                        'class_weight': ['balanced']
                     }


        # clf = GridSearchCV(SGDClassifier(), param_grid, scoring='roc_auc',cv=5)
        clf = SGDClassifier(loss='log').fit(X_train,y_train)

        # Calculate and print accuracy scores
        y_predict = clf.predict(X_test)

        print classification_report(y_test,y_predict)
        self.plot_roc(y_test, clf.predict_proba(X_test))
        return clf

    def print_scores(self,model):
        model
        print "Scores:"
        print classification_report(y_test,y_hat)
        print_coefs(funnel.data.columns,clf_LR.coef_[0])
        print "\n---\n"

    def print_coefs(self,labels,coefs,pvals):
        print "Coefficients:"
        # for c in sorted(zip(labels,coefs,pvals), key = lambda t: -abs(t[1])):
        for c in sorted(zip(labels,coefs, pvals), key = lambda t: -abs(t[1])):
            print "{} : {}, {}".format(c[0],c[1],c[2])


    def plot_roc(self,y,y_probas,label=""):

        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = roc_curve(y, y_probas[:, 1])
        roc_auc = auc(fpr, tpr)
        self.ax.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % (label, roc_auc))
        self.ax.legend(loc="lower right")
        # plt.show()

def run_wk1():
    # Week 1 model
    print "\n\nWeek1 Model results:"

    cutoff = "2016-08-14"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date=cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values

    wk1_model = MF.fit_model(X,y)

def run_all():
    # Week 1 model
    print "\n\nWeek1 Model results:"

    cutoff = "2016-08-14"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values

    wk1_model = MF.fit_model(X,y)

    # Week 2 model
    print "\n\nWeek2 Model results:"

    cutoff = "2016-08-21"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values

    wk2_model = MF.fit_model(X,y)

    # Week 3 model
    print "\n\nWeek3 Model results:"

    cutoff = "2016-08-28"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values

    wk3_model = MF.fit_model(X,y)

    # Week 4 model
    print "\n\nWeek4 Model results:"

    cutoff = "2016-09-04"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values

    wk4_model = MF.fit_model(X,y)

if __name__ == "__main__":

    DE = DataExplorer()
    logs = DE.get_logs()
    completions = DE.get_completions()

    FF = FeatureFactory(logs,completions)
    features = FF.features

    MF = ModelFactory()
