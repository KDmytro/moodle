from src.data.explore_dataset import DataExplorer
from src.features.build_features import FeatureFactory
from src.models.model_factory import ModelFactory

from sklearn.model_selection import train_test_split, StratifiedKFold, StratifiedShuffleSplit, cross_val_predict
from sklearn.metrics import classification_report, roc_curve, auc


from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import svm

import numpy as np
from scipy import interp

import matplotlib.pyplot as plt
plt.ion()

DE = DataExplorer()
logs = DE.get_course_logs()
completions = DE.get_completions()

FF = FeatureFactory(logs,completions)
features = FF.features
FF.make_y()

MF = ModelFactory()

FF.init_data()
FF.make_wk1_features()

X = FF.data.values
y = FF.y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25,
                                                     random_state=123)
wk1_model = MF.fit_wk1_model(X_train,y_train)

y_hat = wk1_model.predict(X_test)
y_proba = wk1_model.predict_proba(X_test)

#
# # Compute ROC curve and ROC area for each class
# fpr = dict()
# tpr = dict()
# roc_auc = dict()
# for i in [0,1]:
#     fpr[i], tpr[i], thresholds = roc_curve(y_test, y_proba[:,i])
#     roc_auc[i] = auc(fpr[i], tpr[i])
#
#
# plt.figure()
# lw = 2
# for i in [0,1]:
#   plt.plot(fpr[i], tpr[i], color=['darkorange','aqua'][i],
#            lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[i])
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()


# Cross Validation ROC

# parameters = {'kernel':('poly', 'rbf'), 'C':[1, 10]}
# svr = svm.SVC()
# clf = GridSearchCV(svr, parameters)

clf = svm.SVC(kernel='poly', probability=True, random_state=123)

cv = StratifiedKFold(n_splits=6)

mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)

i = 0
for (train, test) in cv.split(X, y):
    probas_ = clf.fit(X[train], y[train]).predict_proba(X[test])
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
    i += 1

mean_tpr /= cv.get_n_splits(X, y)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
plt.plot(mean_fpr, mean_tpr, color='g', linestyle='--',
        label='Mean ROC (area = %0.2f)' % mean_auc)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for logistic regression')
plt.legend(loc="lower right")
plt.show()
