import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

y = funnel.pop('completionstate')
X_train, X_test, y_train, y_test = train_test_split(funnel.values, y.values, test_size=0.33, random_state=42)

clf_l1_LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf_l1_LR.fit(X, y)

coef_l1_LR = clf_l1_LR.coef_.ravel()
