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

X = FF.data.values
X = FF.data[[ u'n_viewed',u'1_forum', u'1_book_1', u'1_quiz', u'1_feedback', u'n_created', u'n_msg_sent']]

MF.fit_model(X,y)
MF.fit_tree_model(X,y)




import statsmodels.api as sm
logit = sm.Logit(y, X)
result = logit.fit()
print result.summary()
