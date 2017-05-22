cutoff = '2016-08-14'

from src.data.explore_dataset import DataExplorer
from src.features.build_features import FeatureFactory
from src.models.model_factory import ModelFactory

import statsmodels.api as sm

from sklearn.preprocessing import scale, normalize

import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


DE = DataExplorer()
logs = DE.get_logs()
completions = DE.get_completions()

FF = FeatureFactory(logs,completions)
FF.init_registered_by(cutoff)
y = FF.make_y()
y_wk2 = FF.make_y_wk2()
y_wk3 = FF.make_y_wk3()
y_wk4 = FF.make_y_wk4()

FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("viewed", "n_viewed", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\mod_forum\event\post_created", "n_posts_created", start_date="2016-08-07", end_date=cutoff)
FF.make_time_since("loggedin", "last_login", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\core\event\message_sent", "n_msg_sent", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\core\event\user_enrolment_created", "n_prior_enrollment", end_date=cutoff)

# logs[(logs.timecreated < "2016-08-21") &(logs.eventname == '\core\event\user_enrolment_created')].groupby(logs.username).size()

# wk0
FF.make_completion_feature(54984, '0_forum', cutoff)
FF.make_completion_feature(54985, '0_page_1', cutoff)
FF.make_completion_feature(54986, '0_page_2', cutoff)
FF.make_completion_feature(55043, '0_page_3', cutoff)

# wk1 req
FF.make_completion_feature(54988, '1_forum', cutoff)
FF.make_completion_feature(54990, '1_book_1', cutoff)
FF.make_completion_feature(54991, '1_book_2', cutoff)
FF.make_completion_feature(54994, '1_quiz', cutoff)
FF.make_completion_feature(54995, '1_feedback', cutoff)
FF.make_completion_feature(54992, '1_choice', cutoff)
FF.make_completion_feature(54993, '1_page_2', cutoff)
FF.make_completion_feature(54989, '1_page_1', cutoff)

# wk2 req
# FF.make_completion_feature(55005, '2_quiz', cutoff)
# FF.make_completion_feature(55001, '2_book', cutoff)
# FF.make_completion_feature(55002, '2_glossary', cutoff)
# FF.make_completion_feature(55004, '2_survey', cutoff)
# FF.make_completion_feature(55003, '2_wiki', cutoff)
# FF.make_completion_feature(55000, '2_page_1', cutoff)



df =pd.DataFrame(scale(FF.data))
df.columns = FF.data.columns

logit = sm.Logit(y.values, df)
result = logit.fit()
print result.summary()
logit = sm.Logit(y_wk2.values, df)
result = logit.fit()
print result.summary()
logit = sm.Logit(y_wk3.values, df)
result = logit.fit()
print result.summary()
logit = sm.Logit(y_wk4.values, df)
result = logit.fit()
print result.summary()

MF = ModelFactory()

print "MF df ~ y"
MF.fit_model(df.values,y.values)
MF.fit_tree_model(df.values,y.values)
MF.fit_SVC(df.values,y.values)
print "MF df ~ y_wk2"
MF.fit_model(df.values,y_wk2.values)
MF.fit_tree_model(df.values,y_wk2.values)
MF.fit_SVC(df.values,y_wk2.values)
print "MF df ~ y_wk3"
MF.fit_model(df.values,y_wk3.values)
MF.fit_tree_model(df.values,y_wk3.values)
MF.fit_SVC(df.values,y_wk3.values)
print "MF df ~ y_wk4"
MF.fit_model(df.values,y_wk4.values)
MF.fit_tree_model(df.values,y_wk4.values)
MF.fit_SVC(df.values,y_wk4.values)
