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
