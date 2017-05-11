from src.data.funnel import Funnel
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_predict
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


class ModelFactory(object):

    def __init__(self):
        self.features = {
            54984:'0_forum',
            54985:'0_page_1',
            54986:'0_page_2',
            55043:'0_page_3',
            54988:'1_forum',
            54990:'1_book_1',
            54991:'1_book_2',
            54994:'1_quiz',
            54995:'1_feedback',
            54992:'1_choice',
            54993:'1_page_2',
            54989:'1_page_1',
            55005:'2_quiz',
            55001:'2_book',
            55002:'2_glossary',
            55004:'2_survey',
            55003:'2_wiki',
            55000:'2_page_1',
            55017:'3_quiz',
            55013:'3_book',
            55016:'3_forum',
            55014:'3_data',
            55012:'3_page_1',
            55015:'3_page_2',
            55028:'4_page_2',
            55051:'4_feedback',
            55025:'4_lesson',
            55029:'4_quiz',
            55027:'4_workshop',
            55024:'4_forum',
            55030:'4_page_3',
            55023:'4_page_1',
            55052:'4_page_4',
        }

        self.cv = StratifiedShuffleSplit(n_splits=2, test_size=0.2, random_state=123)

        self.clf_LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
        self.clf_RF = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)

        self.funnel = Funnel(logs, completions)
        self.funnel.make_y()


    def print_coefs(labels,coefs):
        print "Coefficients:"
        for c in sorted(zip(labels,coefs), key = lambda t: -abs(t[1])):
            print "{} : {}".format(c[0],c[1])



    def fit_wk1_model():

        print "Week 1 all features model"

        if not self.models["wk1"]:
            self.funnel.init_data()
            self.funnel.make_dict_features_by_date(features,'2016-08-14')

            X = funnel.data.values
            y = funnel.y.values

        for train_index, test_index in cv.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        # y_hat = cross_val_predict(clf_LR, X_train, y_train, cv=10)
        clf_LR.fit(X_train,y_train)
        y_hat = clf.predict(X_test)

        self.models["wk1"] = {
                                "model":clf_LR,
                                "data":X,
                                "y":y
                             }

    def print_scores(model):
        self.models[model]
        print "Scores:"
        print classification_report(y_test,y_hat)
        print_coefs(funnel.data.columns,clf_LR.coef_[0])
        print "\n---\n"

    # # clf.fit(X_train,y_train)
    # y_hat = cross_val_predict(clf_RF, X_train, y_train, cv=10)
    # # y_hat = clf.predict(X_test)
    #
    # print "Scores:"
    # print classification_report(y_train,y_hat)
    # # print_coefs(funnel.data.columns,clf.feature_importances)
    # print "\n---\n"
    #
    #



if __name__ == "__main__":
    pass
