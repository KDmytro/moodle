# all_users = FF.make_y().reset_index()
# all_users.columns=['username','completed']
# logs = logs.merge(all_users.reset_index(), on='username')



def convert_timezone(df):
    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize('UTC').dt.tz_convert(tz)


# mask = ("2016-08-11 18:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-12 20:00:00")
# logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':count}).sort_values(by='username')


def get_activity_log_by_time(logs, eventname, start_date, end_date):
    mask = ((start_date < logs.timecreated) &
            (logs.timecreated < end_date) &
            (logs.eventname == eventname))
    return logs[mask]

def plot_heatmap(logs, ax):
    hours = logs.groupby([logs.timecreated.dt.date,logs.timecreated.dt.hour]).size().unstack(level=0)
    sns.heatmap(hours, ax=ax)

def plot_activity_by_weeks(logs,eventname):
    fig, axs = plt.subplots(2,4)
    for i in [1,0]:
        logins = get_activity_log_by_time(logs[logs.completed == bool(i)],eventname, "2016-08-07", "2016-08-14")
        plot_heatmap(logins, axs[i][0])
        logins = get_activity_log_by_time(logs[logs.completed == bool(i)],eventname, "2016-08-14", "2016-08-21")
        plot_heatmap(logins, axs[i][1])
        logins = get_activity_log_by_time(logs[logs.completed == bool(i)],eventname, "2016-08-21", "2016-08-28")
        plot_heatmap(logins, axs[i][2])
        logins = get_activity_log_by_time(logs[logs.completed == bool(i)],eventname, "2016-08-28", "2016-09-04")
        plot_heatmap(logins, axs[i][3])

#
# logs = DE.get_logs()
# users = DE.get_users()
#
# logs = logs.merge(users[['username','timezone']], on='username')
# convert_timezone(logs)
#
# logs[logs.username == 'user1077796981797027841'].timecreated.min()
#

mask = ("2016-08-07" < logs.timecreated) & (logs.timecreated < "2016-08-14")
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':count}).sort_values(by='username')

logs = DE.get_logs()
mask = ("2016-08-07" < logs.timecreated) & (logs.timecreated < "2016-08-14")
logs[mask].groupby('username').agg({'action':lambda x:(x=='loggedin').sum()})


FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date="2016-08-14")


condition = ((FF.logs.action == 'loggedin') &
            (FF.logs.timecreated > '2016-08-07') &
            (FF.logs.timecreated <= '2016-08-14'))





logs = DE.get_logs()
FF = FeatureFactory(logs,completions)

FF.init_registered_by(cutoff)
FF.make_dict_features_by_date(features,cutoff)
FF.make_y()

X = FF.data.values
y = FF.y.values

MF.fit_model(X,y)
MF.fit_tree_model(X,y)

FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("created", "n_created", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("viewed", "n_viewed", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\core\event\message_sent", "n_msg_sent", start_date="2016-08-07", end_date=cutoff)

FF.make_event_count_feature("\mod_forum\event\post_created", "n_posts_created", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\mod_chat\event\message_sent", "n_messages", start_date="2016-08-07", end_date=cutoff)


X = FF.data.values
X = FF.data[[ u'n_viewed',u'1_forum', u'1_book_1', u'1_quiz', u'1_feedback', u'n_created', u'n_msg_sent']]


[
u'0_page_3',
u'0_forum',
u'0_page_1',
u'0_page_2',
u'1_forum',
u'1_page_1',
u'1_book_1',
u'1_book_2',
u'1_choice',
u'1_page_2',
u'1_quiz',
u'1_feedback',
u'n_posts_created',
u'n_messages'
u'2_page_1',
u'2_book',
u'2_glossary',
u'2_wiki',
u'2_survey',
u'2_quiz',
u'3_page_1',
u'3_book',
u'3_data',
u'3_page_2',
u'3_forum',
u'3_quiz',
u'4_page_4',
u'4_feedback',
u'4_page_1',
u'4_forum',
u'4_lesson',
u'4_workshop',
u'4_page_2',
u'4_quiz',
u'4_page_3',


MF.fit_model(X,y)
MF.fit_tree_model(X,y)




import statsmodels.api as sm
logit = sm.Logit(FF.y.values, FF.data)
result = logit.fit()
print result.summary()




FF.init_data()
FF.make_y()
y = FF.y


logs = logs[logs.timecreated <= "2016-08-14"].merge(y.reset_index(),on='username')

log_event_counts = logs.groupby(['component', 'action','target','completionstate']).size().unstack(-1).fillna(0)
log_event_counts.columns = ["passed","failed"]
log_event_counts['balance'] = log_event_counts.apply(lambda x: (x.passed - x.failed)/x.sum(),axis=1)

log_event_counts[abs(log_event_counts.balance) >= 0.5]

Out[343]:
                                                        passed  failed   balance
component       action     target
booktool_print  printed    chapter                        14.0    50.0 -0.562500
core            created    calendar_event                  0.0     2.0 -1.000000
                           enrol_instance                  0.0     6.0 -1.000000
                           group                           0.0     4.0 -1.000000
                deleted    user_enrolment                  5.0    22.0 -0.629630
                unassigned role                            5.0    22.0 -0.629630
                updated    calendar_event                  0.0    18.0 -1.000000
mod_certificate viewed     course_module                   0.0     2.0 -1.000000
mod_chat        sent       message                        87.0   267.0 -0.508475
                viewed     course_module_instance_list     0.0     1.0 -1.000000
mod_forum       created    post                          734.0  2290.0 -0.514550
                deleted    discussion                      4.0    12.0 -0.500000
                           discussion_subscription        45.0   194.0 -0.623431
                           subscription                    4.0    12.0 -0.500000
                moved      discussion                      0.0     4.0 -1.000000
mod_lesson      viewed     content_page                    0.0     6.0 -1.000000
                           course_module                   0.0     6.0 -1.000000
mod_resource    viewed     course_module                   0.0     2.0 -1.000000
mod_survey      viewed     course_module                   0.0     2.0 -1.000000
mod_wiki        viewed     course_module                   0.0     2.0 -1.000000
mod_workshop    viewed     course_module                   0.0    10.0 -1.000000
report_log      viewed     user_report                     0.0     2.0 -1.000000
report_loglive  viewed     report                          0.0     4.0 -1.000000
tool_recyclebin created    course_bin_item                 0.0     4.0 -1.000000



 logs[(logs.courseid == 10464) &
     (logs.eventname == '\core\event\user_enrolment_created')].groupby(logs.timecreated.dt.week).size()

     




In [387]: cols = [u'0_page_3',
     ...: u'0_forum',
     ...: u'1_page_1',
     ...: u'1_book_1',
     ...: u'1_quiz',
     ...: u'1_feedback',
     ...: u'n_posts_created',
     ...: u'n_messages'
     ...: ]

In [388]: logit = sm.Logit(FF.y.values, FF.data[cols])
     ...: result = logit.fit()
     ...: print result.summary()
     ...:
Optimization terminated successfully.
         Current function value: 0.597063
         Iterations 8
                           Logit Regression Results
==============================================================================
Dep. Variable:                      y   No. Observations:                 1804
Model:                          Logit   Df Residuals:                     1796
Method:                           MLE   Df Model:                            7
Date:                Fri, 19 May 2017   Pseudo R-squ.:                 0.03264
Time:                        11:24:05   Log-Likelihood:                -1077.1
converged:                       True   LL-Null:                       -1113.4
                                        LLR p-value:                 4.240e-13
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
0_page_3            0.2625      0.129      2.040      0.041       0.010       0.515
0_forum            -0.2363      0.107     -2.199      0.028      -0.447      -0.026
1_page_1           -0.7787      0.057    -13.714      0.000      -0.890      -0.667
1_book_1            0.6662      0.146      4.567      0.000       0.380       0.952
1_quiz              0.7926      0.182      4.346      0.000       0.435       1.150
1_feedback          0.6513      0.190      3.422      0.001       0.278       1.024
n_posts_created     0.2133      0.054      3.959      0.000       0.108       0.319
n_messages          0.0530      0.054      0.981      0.327      -0.053       0.159
===================================================================================





# Calculate night or day
number of days with logins

group by user
    group by day
      count number of logins
        unstack days



DE = DataExplorer()
logs = DE.get_logs()

logs = logs[logs.timecreated <= "2016-08-14"]
FF = FeatureFactory(logs,completions)
cutoff = "2016-08-14"
FF.init_registered_by(cutoff)
FF.make_y()

FF.make_wk1_features()
FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("created", "n_created", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("viewed", "n_viewed", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\core\event\message_sent", "n_msg_sent", start_date="2016-08-07", end_date=cutoff)

FF.make_event_count_feature("\mod_forum\event\post_created", "n_posts_created", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\mod_chat\event\message_sent", "n_messages", start_date="2016-08-07", end_date=cutoff)

MF = ModelFactory()

#
# Week2 drop out prediction
#

DE = DataExplorer()
logs = DE.get_logs()
FF.logs = DE.get_logs()


from src.features.build_features import FeatureFactory
FF = FeatureFactory(logs,completions)
cutoff = "2016-08-14"
FF.init_registered_by(cutoff)
y = FF.make_y()
y_wk2 = FF.make_y_wk2()
y_wk3 = FF.make_y_wk3()
y_wk4 = FF.make_y_wk4()


FF.make_action_count_feature("loggedin", "n_logins", start_date="2016-08-07", end_date=cutoff)
FF.make_action_count_feature("viewed", "n_viewed", start_date="2016-08-07", end_date=cutoff)
FF.make_event_count_feature("\mod_forum\event\post_created", "n_posts_created", start_date="2016-08-07", end_date=cutoff)
FF.make_time_since("loggedin", "last_login", start_date="2016-08-07", end_date=cutoff)
FF.make_completion_feature(54994, "wk1_quiz", "2016-08-14")
FF.make_completion_feature(54989, "wk1_page", "2016-08-14")

cols = FF.data.columns

logit = sm.Logit(y_wk2, FF.data[cols])
result = logit.fit()
print result.summary()

         Current function value: 0.501123
         Iterations 7
                           Logit Regression Results
==============================================================================
Dep. Variable:        completionstate   No. Observations:                 2163
Model:                          Logit   Df Residuals:                     2157
Method:                           MLE   Df Model:                            5
Date:                Sat, 20 May 2017   Pseudo R-squ.:                 -0.3442
Time:                        01:59:36   Log-Likelihood:                -1083.9
converged:                       True   LL-Null:                       -806.40
                                        LLR p-value:                     1.000
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
n_logins           -0.0806      0.026     -3.125      0.002      -0.131      -0.030
n_viewed            0.0008      0.000      2.114      0.035    6.04e-05       0.002
n_posts_created     0.1110      0.044      2.541      0.011       0.025       0.197
last_login         -0.3278      0.036     -9.020      0.000      -0.399      -0.257
wk1_quiz            2.1248      0.208     10.231      0.000       1.718       2.532
wk1_page           -1.0673      0.101    -10.575      0.000      -1.265      -0.870
===================================================================================

# Fitting models
MF.fit_model(scale(FF.data.values),y_wk2)
MF.fit_tree_model(scale(FF.data.values),y_wk2)
MF.fit_SVC(scale(FF.data.values),y_wk2)

{'penalty': 'l1', 'C': 0.1, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.97      0.80      0.88       380
       True       0.36      0.79      0.49        53

avg / total       0.89      0.80      0.83       433

{'max_leaf_nodes': 4, 'max_depth': 3, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.97      0.80      0.88       380
       True       0.36      0.79      0.49        53

avg / total       0.89      0.80      0.83       433

{'kernel': 'rbf', 'C': 0.1, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.96      0.79      0.87       380
       True       0.35      0.79      0.48        53

avg / total       0.89      0.79      0.82       433


logit = sm.Logit(y_wk3, FF.data[cols])
result = logit.fit()
print result.summary()

Optimization terminated successfully.
         Current function value: 0.514090
         Iterations 7
                           Logit Regression Results
==============================================================================
Dep. Variable:        completionstate   No. Observations:                 2163
Model:                          Logit   Df Residuals:                     2157
Method:                           MLE   Df Model:                            5
Date:                Sat, 20 May 2017   Pseudo R-squ.:                 -0.3133
Time:                        02:05:43   Log-Likelihood:                -1112.0
converged:                       True   LL-Null:                       -846.73
                                        LLR p-value:                     1.000
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
n_logins           -0.0123      0.025     -0.502      0.616      -0.060       0.036
n_viewed            0.0014      0.001      2.243      0.025       0.000       0.003
n_posts_created    -0.0148      0.031     -0.470      0.638      -0.076       0.047
last_login         -0.3426      0.036     -9.477      0.000      -0.413      -0.272
wk1_quiz            1.5336      0.187      8.195      0.000       1.167       1.900
wk1_page           -0.9322      0.089    -10.444      0.000      -1.107      -0.757
===================================================================================


MF.fit_model(scale(FF.data.values),y_wk3)
MF.fit_tree_model(scale(FF.data.values),y_wk3)
MF.fit_SVC(scale(FF.data.values),y_wk3)

{'penalty': 'l2', 'C': 0.001, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.94      0.77      0.85       376
       True       0.31      0.68      0.43        57

avg / total       0.86      0.76      0.79       433

{'max_leaf_nodes': 10, 'max_depth': 4, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.93      0.82      0.87       376
       True       0.33      0.56      0.41        57

avg / total       0.85      0.79      0.81       433

{'kernel': 'rbf', 'C': 0.1, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.94      0.81      0.87       376
       True       0.34      0.65      0.44        57

avg / total       0.86      0.79      0.81       433


logit = sm.Logit(y_wk4, FF.data[cols])
result = logit.fit()
print result.summary()

         Current function value: 0.573517
         Iterations 6
                           Logit Regression Results
==============================================================================
Dep. Variable:        completionstate   No. Observations:                 2163
Model:                          Logit   Df Residuals:                     2157
Method:                           MLE   Df Model:                            5
Date:                Sat, 20 May 2017   Pseudo R-squ.:                -0.09072
Time:                        02:07:48   Log-Likelihood:                -1240.5
converged:                       True   LL-Null:                       -1137.3
                                        LLR p-value:                     1.000
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
n_logins           -0.0048      0.024     -0.204      0.838      -0.051       0.041
n_viewed            0.0005      0.000      1.148      0.251      -0.000       0.001
n_posts_created     0.0931      0.049      1.914      0.056      -0.002       0.188
last_login         -0.3522      0.033    -10.772      0.000      -0.416      -0.288
wk1_quiz            1.3976      0.149      9.395      0.000       1.106       1.689
wk1_page           -0.5016      0.073     -6.898      0.000      -0.644      -0.359
===================================================================================


MF.fit_model(scale(FF.data.values),y_wk4)
MF.fit_tree_model(scale(FF.data.values),y_wk4)
MF.fit_SVC(scale(FF.data.values),y_wk4)

{'penalty': 'l2', 'C': 0.001, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.92      0.75      0.82       338
       True       0.46      0.76      0.57        95

avg / total       0.82      0.75      0.77       433

{'max_leaf_nodes': None, 'max_depth': 3, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.92      0.70      0.80       338
       True       0.43      0.79      0.56        95

avg / total       0.81      0.72      0.75       433

{'kernel': 'rbf', 'C': 0.1, 'class_weight': 'balanced'}
             precision    recall  f1-score   support

      False       0.90      0.77      0.83       338
       True       0.45      0.68      0.55        95

avg / total       0.80      0.75      0.77       433



cutoff = '2016-08-21'

from src.data.explore_dataset import DataExplorer
from src.features.build_features import FeatureFactory
from src.models import ModelFactory

DE = DataExplorer()
logs = DE.get_logs()
completions = DE.get completions()

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
FF.make_completion_feature(55005, '2_quiz', cutoff)
FF.make_completion_feature(55001, '2_book', cutoff)
FF.make_completion_feature(55002, '2_glossary', cutoff)
FF.make_completion_feature(55004, '2_survey', cutoff)
FF.make_completion_feature(55003, '2_wiki', cutoff)
FF.make_completion_feature(55000, '2_page_1', cutoff)



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
