from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_selection import chi2

from sklearn.metrics import f1_score, roc_auc_score, make_scorer

import operator

def print_coefs(labels,coefs):
    print "Coefficients:"
    for c in sorted(zip(labels,coefs), key = lambda t: -abs(t[1])):
        print "{} : {}".format(c[0],c[1])

execfile('src/init_script.py')

#  WEEK 2 - Data Setup, Feature Selection, GridSearch, Test Scores

FF.init_registered_by("2016-08-28")
FF.make_dict_features_by_date(FF.features,'2016-08-28')

FF.make_y()

X = FF.data.values
y = FF.y.values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25,
                                                     random_state=123)

# scorer = make_scorer(f1_score, average='weighted')
# scorer = make_scorer(roc_auc_score, average='weighted')


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

y_hat = clf.best_estimator_.predict(X_test)
print classification_report(y_test,y_hat)
print_coefs(FF.data.columns,clf.best_estimator_.coef_[0])



# Feature selection via Recursive Feature Elimination

# selector = RFECV(clf.best_estimator_, step=1, cv=5)
# selector.fit(X_test,y_test)
# X_train_sub = X_train[:,selector.support_]
# X_test_sub = X_test[:,selector.support_]

# selector = SelectPercentile(chi2, percentile=10)
# selector.fit(X,y)
# selector.scores_
# selector.pvalues_
#
# feat_pvals = dict(zip(FF.data.columns, np.nan_to_num(selector.pvalues_)))
# sorted(feat_pvals.items(), key=operator.itemgetter(1),reverse=True)
# feat_scores = dict(zip(FF.data.columns, np.nan_to_num(selector.scores_)))
# sorted(feat_scores.items(), key=operator.itemgetter(1),reverse=True)


# clf = GridSearchCV(LogisticRegression(), param_grid, scoring=scorer)
# clf.fit(X_train_sub,y_train)
# # clf.cv_results_
# print clf.best_params_
#
#
# y_hat = clf.best_estimator_.predict(X_test_sub)
# print classification_report(y_test,y_hat)
# print_coefs(FF.data.columns[selector.support_],clf.best_estimator_.coef_[0])
