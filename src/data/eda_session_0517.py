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
