
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import RFECV
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_selection import chi2

from sklearn.metrics import f1_score, make_scorer

import operator


run src/init_script.py
logs.inof()
logs.info()
logs(~logs.realusername.isna())
logs(~logs.realusername.isnull())
logs(~logs.realusername.isnull)
logs(-logs.realusername.isnull)
logs(-logs.realusername.isnull())
logs[-logs.realusername.isnull()]
logs.groupby('username').size().sort_values(scending=Flase)
logs.groupby('username').size().sort_values(scending=False)
logs.groupby('username').size().sort_values(ascending=False)
user_logs DE.get_user_logs('user5726338535498186753')
user_logs = DE.get_user_logs('user5726338535498186753')
user_logs
user_logs = DE.get_user_logs('user5575198275574693889')
user_logs
user_logs.sort_values(by='timecreated')


logs.username.nunique()
FF.y.sum()
FF.y.count()

course_logs = DE.get_course_logs()
course_logs.columns
course_logs.info()
course_logs.username.nunique()

course_logs[course_logs.timecreated < "2016-08-14"]
course_logs[course_logs.timecreated < "2016-08-14"].username.nunique()

run src/init_script.py

FF.features = FF.features

FF.init_registered_by("2016-08-14")
FF.make_y()

FF.make_dict_features_by_date(features,'2016-08-14')

X = FF.data.values
y = FF.y.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25,
                                                     random_state=123)
wk1_model = MF.fit_wk1_model(X_train,y_train)

y_hat = wk1_model.predict(X_test)
y_proba = wk1_model.predict_proba(X_test)

print classification_report(y_test,y_hat)

def print_coefs(labels,coefs):
    print "Coefficients:"
    for c in sorted(zip(labels,coefs), key = lambda t: -abs(t[1])):
        print "{} : {}".format(c[0],c[1])

print_coefs(FF.data.columns,wk1_model.coef_[0])

y.sum()
y.count()
y.shape
553./1770
1- _


print classification_report(y_test,y_hat)

wk1_model.score(X_test,y_test)

clf = LogisticRegression(C=0.1, class_weight='balanced', penalty='l2')

clf.fit(X_train,y_train)
clf.score(X_test,y_test)


# GridSearch for best params on LR
param_grid = {
                'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                'penalty': ['l1','l2'],
                'class_weight'=['balanced', None]
             }

clf = GridSearchCV(LogisticRegression(), param_grid)
clf.fit(X_train,y_train)
clf.cv_results_
clf.best_params_

clf = LogisticRegression(C=0.1, class_weight='balanced', penalty='l1')
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
y_hat = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)

print classification_report(y_test,y_hat)
print_coefs(FF.data.columns,clf.coef_[0])

FF.init_registered_by("2016-08-14")
FF.make_dict_features_by_date(features,'2016-08-14')

FF.data.info()
FF.data.sum()

print_coefs(FF.data.columns,clf.coef_[0])

selector = SelectPercentile(f_classif, percentile=10)

X = FF.data.values
y = FF.y

selector.fit(X,y)

X_indices = np.arange(X.shape[-1])
scores = -np.log10(selector.pvalues_)
scores /= scores.max()

plt.bar(X_indices - .45, scores, width=.2,
        label=r'Univariate score ($-Log(p_{value})$)', color='darkorange')

selector.pvalues_
selector.scores_
selector.score_func



selector = SelectPercentile(chi2, percentile=10)
selector.fit(X,y)
selector.scores_
selector.pvalues_

feat_pvals = dict(zip(FF.data.columns, np.nan_to_num(selector.pvalues_)))
sorted(feat_pvals.items(), key=operator.itemgetter(1),reverse=True)
feat_scores = dict(zip(FF.data.columns, np.nan_to_num(selector.scores_)))
sorted(feat_scores.items(), key=operator.itemgetter(1),reverse=True)


FF.data.columns[selector.support_]
selector.grid_scores_

X = FF.data.iloc[:,selector.support_].values

selector = RFECV(LogisticRegression(C=0.1, class_weight='balanced', penalty='l1'), step=1, cv=5)
selector.fit(X,y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25,
                                                     random_state=123)
y_hat = selector.estimator_.predict(X_test)
print classification_report(y_test,y_hat)



def print_coefs(labels,coefs):
    print "Coefficients:"
    for c in sorted(zip(labels,coefs), key = lambda t: -abs(t[1])):
        print "{} : {}".format(c[0],c[1])


#  WEEK 1 - Data Setup, Feature Selection, GridSearch, Test Scores

FF.init_registered_by("2016-08-14")
FF.make_dict_features_by_date(FF.features,'2016-08-14')

FF.make_y()

X = FF.data.values
y = FF.y.values

# selector = SelectPercentile(chi2, percentile=10)
# selector.fit(X,y)
# selector.scores_
# selector.pvalues_
#
# feat_pvals = dict(zip(FF.data.columns, np.nan_to_num(selector.pvalues_)))
# sorted(feat_pvals.items(), key=operator.itemgetter(1),reverse=True)
# feat_scores = dict(zip(FF.data.columns, np.nan_to_num(selector.scores_)))
# sorted(feat_scores.items(), key=operator.itemgetter(1),reverse=True)

selector = RFECV(LogisticRegression(C=0.1, class_weight='balanced', penalty='l1'), step=1, cv=5)
selector.fit(X,y)
X_sub = FF.data.iloc[:,selector.support_].values


X_train, X_test, y_train, y_test = train_test_split(X_sub, y, test_size=.25,
                                                     random_state=123)

f1_weighted_scorer = make_scorer(f1_score, average='weighted')


# GridSearch for best params on LR
param_grid = {
                'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                'penalty': ['l1','l2'],
                'class_weight': ['balanced', None]
             }


clf = GridSearchCV(LogisticRegression(), param_grid, scoring=f1_weighted_scorer)
clf.fit(X_train,y_train)
# clf.cv_results_
print clf.best_params_

y_hat = clf.best_estimator_.predict(X_test)
print classification_report(y_test,y_hat)
print_coefs("",FF.data.columns[selector.support_],clf.best_estimator_.coef_[0])
