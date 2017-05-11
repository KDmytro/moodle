from src.data.funnel import Funnel
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_predict
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression

def print_coefs(labels,coefs):
    print "Coefficients:"
    for c in zip(labels,coefs):
        print "{} : {}".format(c[0],c[1])

features = {
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

cv = StratifiedShuffleSplit(n_splits=3, test_size=0.2, random_state=0)
clf_l1_LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)

funnel = Funnel(logs, completions)
funnel.make_y()

print "\n---\n"

print "Week 1 model"

funnel.init_data()
funnel.make_wk1_features()

X_train, X_test, y_train, y_test = train_test_split(funnel.data.values, funnel.y.values, test_size=0.25, random_state=123)

clf_l1_LR.fit(X_train,y_train)

cv=cv

y_hat = clf_l1_LR.predict(X_test)

print "Scores:"
print classification_report(y_test,y_hat)
print_coefs(funnel.data.columns,clf_l1_LR.coef_[0])
print "\n---\n"

print "Week 1 all features model"

funnel.init_data()
funnel.make_dict_features_by_date(features,'2016-08-14')

X_train, X_test, y_train, y_test = train_test_split(funnel.data.values, funnel.y.values, test_size=0.25, random_state=123)
clf_l1_LR.fit(X_train,y_train)
y_hat = clf_l1_LR.predict(X_test)
f1_score(y_test,y_hat)
print "Scores:\n Precision: {}\n Recall: {}\n F1: {}".format(*precision_recall_fscore_support(y_test,y_hat))
print_coefs(funnel.data.columns,clf_l1_LR.coef_[0])
print "\n---\n"


print "Week 2 model"

funnel.init_data()
funnel.make_wk2_features()

X_train, X_test, y_train, y_test = train_test_split(funnel.data.values, funnel.y.values, test_size=0.25, random_state=123)
clf_l1_LR.fit(X_train,y_train)
y_hat = clf_l1_LR.predict(X_test)
f1_score(y_test,y_hat)
print "Scores:\n Precision: {}\n Recall: {}\n F1: {}".format(*precision_recall_fscore_support(y_test,y_hat))
print_coefs(funnel.data.columns,clf_l1_LR.coef_[0])
print "\n---\n"

print "Week 1+2 model"

funnel.init_data()
funnel.make_wk1_features()
funnel.make_wk2_features()

X_train, X_test, y_train, y_test = train_test_split(funnel.data.values, funnel.y.values, test_size=0.25, random_state=123)
clf_l1_LR.fit(X_train,y_train)
y_hat = clf_l1_LR.predict(X_test)
print "Scores:\n Precision: {}\n Recall: {}\n F1: {}".format(*precision_recall_fscore_support(y_test,y_hat))
print_coefs(funnel.data.columns,clf_l1_LR.coef_[0])
print "\n---\n"

print "Week 1+2 all model"

funnel.init_data()
# funnel.make_wk1_features()
funnel.make_wk1_features_to_date()
funnel.make_wk2_features()
# funnel.make_wk1_features_catchup()

X_train, X_test, y_train, y_test = train_test_split(funnel.data.values, funnel.y.values, test_size=0.25, random_state=123)
clf_l1_LR.fit(X_train,y_train)
y_hat = clf_l1_LR.predict(X_test)
print "Scores:\n Precision: {}\n Recall: {}\n F1: {}".format(*precision_recall_fscore_support(y_test,y_hat))
print_coefs(funnel.data.columns,clf_l1_LR.coef_[0])
print "\n---\n"


if __name__ == "__main__":
    pass
