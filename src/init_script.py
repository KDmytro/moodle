# init script


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
