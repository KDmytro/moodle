
run src/models/model_factory.py
clear
clear
run src/models/model_factory.py
run src/models/model_factory.py
run src/models/model_factory.py
run src/models/model_factory.py
run src/models/model_factory.py
run src/models/model_factory.py
logs
logs.info()
logs = DE.get_user_logs()s
logs = DE.get_user_logs()
logs
logs.info()
logs.timecreated.dt.min()
logs.timecreated.dt.date.min()
logs.timecreated.min()
logs.timecreated.dt.week
logs.groupby(logs.timecreated.dt.date).size()
logs.to_csv('data/interim/user_logs.csv')
plt.plot(_20)
plt.show()
plt.ion()
plt.plot(_20)
logs.groupby(logs.timecreated.dt.day).size()
logs.groupby(logs.timecreated.dt.weekday).size()
logs.groupby(logs.timecreated.dt.hour).size()
logs.groupby(logs.timecreated.dt.weekday,logs.timecreated.dt.hour).size()
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size()
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstuck(level=0)
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour])
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=1)
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0).values
hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0).values
np.nan_to_num(hours)
hours = np.nan_to_num(hours)
import seaborn as sns
ax = sns.heatmap(hours)
ax = sns.heatmap(hours[-1:])
ax = sns.heatmap(hours[-1,:])
ax = sns.heatmap(hours[-1:,:])
ax = sns.heatmap(hours[-1:,:])
ax = sns.heatmap(hours[::-1,])
ax = sns.heatmap(hours)
ax = sns.heatmap(hours[::-1,])
ax = sns.heatmap(hours)
history
logs = DE.get_logs()
hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0).values
np.nan_to_num(hours)
hours = np.nan_to_num(hours)
import seaborn as sns
ax = sns.heatmap(hours)
hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
ax = sns.heatmap(hours)
ax = sns.heatmap(hours)
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    ax = sns.heatmap(hours)
plot_heatmap(logs[logs.timecreated <= "2016-08-07"]))
plot_heatmap(logs[logs.timecreated <= "2016-08-07"])
plot_heatmap(logs[logs.timecreated <= "2016-08-07"])
plot_heatmap(logs["2016-08-04" < logs.timecreated <= "2016-08-07"])
plot_heatmap(logs[("2016-08-04" < logs.timecreated) & (logs.timecreated <= "2016-08-07")])
plot_heatmap(logs[("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
FF.init_data()
all_users = FF.data
all_users
all_users = FF.data.reset_index()
all_users
FF.make_y()
all_users = FF.make_y().reset_index()
all_usersy
all_users
all_users.index.rename('username')
all_users
all_users.index.rename('username')
all_users.rename(['username','completed'])
all_users.rename(columns=['username','completed'])
all_users.columns=['username','completed']
all_users
all_users.info()
all_users.set_index('username')
all_users
all_users.set_index('username')
all_users = all_users.set_index('username')
all_users.info()
logs.merge(all_users, on='username')
logs.merge(all_users.reset_index(), on='username')
logs = _
logs
logs['completed']
logs[logs['completed']]
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.imshow(a, cmap='hot', interpolation='nearest')
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.imshow(hours, cmap='hot', interpolation='nearest')
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.imshow(hours)
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.figure(figsize=(20,10))
    plt.imshow(hours, cmap='hot', interpolation='nearest')
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.figure(figsize=(10,10))
    plt.imshow(hours, cmap='hot', interpolation='nearest', aspect='auto')
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.figure(figsize=(10,10))
    ax = plt.imshow(hours, cmap='hot', interpolation='nearest', aspect='auto')
    ax.set_xticks(np.arange(-.5, 10, 1));
    ax.set_yticks(np.arange(-.5, 10, 1));
    ax.set_xticklabels(np.arange(1, 12, 1));
    ax.set_yticklabels(np.arange(1, 12, 1));
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.figure(figsize=(10,10))
    plt.imshow(hours, cmap='hot', interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1));
    ax.set_yticks(np.arange(-.5, 10, 1));
    ax.set_xticklabels(np.arange(1, 12, 1));
    ax.set_yticklabels(np.arange(1, 12, 1));
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    plt.figure(figsize=(7,24))
    plt.imshow(hours, cmap='hot', interpolation='nearest', aspect='auto')
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1));
    ax.set_yticks(np.arange(-.5, 10, 1));
    ax.set_xticklabels(np.arange(1, 12, 1));
    ax.set_yticklabels(np.arange(1, 12, 1));
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
hours = logs.pivot(logs.timecreated.dt.hour,logs.timecreated.dt.weekday,"id")
hours = logs.pivot(timecreated.dt.hour,timecreated.dt.weekday,"id")
hours = logs.pivot(logs.timecreated.dt.hour,logs.timecreated.dt.weekday)
hours = logs.pivot(logs.timecreated.dt.hour,logs.timecreated.dt.weekday,logs.id)
hours = logs.pivot(logs.timecreated.dt.hour,logs.timecreated.dt.weekday,logs.completed)
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    ax = sns.heatmap(hours)
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[~logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
users
users = DE.load_table()
users = DE.load_table('users')
users.info()
users = DE.get_users()
users = DE.load_table('users')
users.timezone.unique()
users.groupby('timezone').size()
users.groupby('timezone').size().sort_values()
users.groupby('timezone').size().sort_values(ascending=False)
import pytz
pytz.timezone(users.timezone.unique())
pytz.timezone(users.timezone.unique()[0])
pytz.timezone(users.timezone.unique()[1])
user_logs = DE.get_user_logs()
user.username
user_logs.username
users[users.username == 'user9171082785710931969'].head(1).T
users.set_index('username')
logs.merge(users, on='username')
logs.merge(users, on='username').timecreated.astimezone('timezone')
logs.columns()
logs.columns
users.columns
logs.merge(users, on='username').columns
logs.merge(users, on='username').timecreated_x.astimezone('timezone')
logs.merge(users, on='username').timecreated_x.dt.astimezone('timezone')
logs.merge(users, on='username').timecreated_x.dt.tz_convert('timezone')
logs.merge(users, on='username').timecreated_x.dt.tz_convert(users.timezone)
logs.merge(users, on='username').timecreated_x.dt.tz_localize(users.timezone)
logs = logs.merge(users[['username','timezone']], on='username')
logs.columns
logs.info()
logs.timecreated.dt.tz_localize(logs.timezone)
logs.timecreated.dt.tz_convert(logs.timezone)
logs.apply(lambda x: x.timecreated.dt.tz_localize(x.timezone))
logs.apply(lambda x: x.timecreated.dt.tz_localize(x.timezone),axis=0)
logs.apply(lambda x: x.timecreated.dt.tz_localize(x.timezone),axis=1)
def convert_timezone(df):
    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize(tz).dt.tz_convert('UTC')
convert_timezone(logs)
def convert_timezone(df):
    df.ix[df.timezone == 99,'timezone'] = 'UTC'
    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize(tz).dt.tz_convert('UTC')
convert_timezone(logs)
df.ix[df.timezone == '99','timezone'] = 'UTC'
logs.ix[logs.timezone == '99','timezone'] = 'UTC'
logs.timezone.unique()
convert_timezone(logs)
DE.load_table()
DE.load_table('users')
run src/models/model_factory.py
convert_timezone(logs)
logs.timezone.unique()
logs = logs.merge(users[['username','timezone']], on='username')
logs.ix[logs.timezone == '99','timezone'] = 'UTC'
convert_timezone(logs)
logs
logs.timezone.unique()
logs.grooupby('timezone').size()
logs.groupby('timezone').size()
logs.groupby('timezone').agg({'username': pd.Series.nunique})
import pandas as pd
logs.groupby('timezone').agg({'username': pd.Series.nunique})
logs.timezone.unique().sorted()
logs.timezone.unique().sort()
logs.timezone.unique()
sorted(logs.timezone.unique())
def convert_timezone(df):
    df.ix[df.timezone == '99','timezone'] = 'UTC'
    df.ix[df.timezone == '-3.0','timezone'] = 'America/Sao_Paulo'
    df.ix[df.timezone == '-5.0','timezone'] = 'America/New_York'
    df.ix[df.timezone == '1.0','timezone'] = 'Europe/London'
    df.ix[df.timezone == '2.0','timezone'] = 'Europe/Paris'
    df.ix[df.timezone == '5.5','timezone'] = 'Asia/Kolkata'

    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize(tz).dt.tz_convert('UTC')
history 130-183
logs = logs.merge(users[['username','timezone']], on='username')
logs.columns
logs = DE.get_logs()
logs.info()
logs = logs.merge(users[['username','timezone']], on='username')
convert_timezone(logs)
logs.groupby('timezone').agg({'username': pd.Series.nunique})
logs.groupby('username').agg({'timecreated': min})
logs_tz = logs.copy()
logs = DE.load_table
logs = DE.load_table(logs)
logs = DE.load_table('logs')
logs.groupby('username').agg({'timecreated': min})
logs = DE.get_logs()
logs.groupby('username').agg({'timecreated': min})
users[users.username == 'user1077796981797027841']
users[users.username == 'user1077796981797027841'].T
logs[logs.username == 'user1077796981797027841'].timecreated.min()
convert_timezone(logs)
logs = logs.merge(users[['username','timezone']], on='username')
def convert_timezone(df):
    df.ix[df.timezone == '99','timezone'] = 'UTC'
    df.ix[df.timezone == '-3.0','timezone'] = 'America/Sao_Paulo'
    df.ix[df.timezone == '-5.0','timezone'] = 'America/New_York'
    df.ix[df.timezone == '1.0','timezone'] = 'Europe/London'
    df.ix[df.timezone == '2.0','timezone'] = 'Europe/Paris'
    df.ix[df.timezone == '5.5','timezone'] = 'Asia/Kolkata'

    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize(tz)#.dt.tz_convert('UTC')
convert_timezone(logs)
logs[logs.username == 'user1077796981797027841'].timecreated.min()
logs[logs.username == 'user1077796981797027841'].timecreated.min().tz_convert('America/Monterrey')
logs[logs.username == 'user1077796981797027841'].timecreated.min().tz_localize('America/Monterrey')
logs = DE.get_logs()
users = DE.get_users()

logs = logs.merge(users[['username','timezone']], on='username')
users
run src/data/explore_dataset.py
run src/data/explore_dataset.py
logs = DE.get_logs()
users = DE.get_users()
logs = logs.merge(users[['username','timezone']], on='username')
logs[logs.username == 'user1077796981797027841'].timecreated.min()
logs[logs.username == 'user1077796981797027841'].timecreated.min().tz_localize("UTC")
logs[logs.username == 'user1077796981797027841'].timecreated.min().tz_localize("UTC").tz_convert("America/Monterrey")
def convert_timezone(df):
    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize('UTC').dt.tz_convert(tz)
logs = DE.get_logs()
users = DE.get_users()

logs = logs.merge(users[['username','timezone']], on='username')
logs[logs.username == 'user1077796981797027841'].timecreated.min()
plot_heatmap(logs[~logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
history 100-
history 100-200
history 10-100
FF.make_y().reset_index()
all_users = FF.make_y().reset_index()
all_users.columns=['username','completed']
logs.merge(all_users.reset_index(), on='username')
logs.columns
logs = logs.merge(all_users.reset_index(), on='username')
plot_heatmap(logs[~logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[~logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
plot_heatmap(logs[~logs['completed']][("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")])
logs[logs.timecreated == "2016-08-11"].groupby(logs.timecreated.dt.hour).size()
logs[logs.timecreated == "2016-08-11"]
logs.timecreated
logs[logs.timecreated.dt.date == "2016-08-11"]
logs.timecreated.dt.date
logs[logs.timecreated.dt.date == "2016-08-11"]
mask = ("2016-08-10" < logs.timecreated) & (logs.timecreated <= "2016-08-11")
logs[mask]
mask = ("2016-08-11" < logs.timecreated) & (logs.timecreated <= "2016-08-11")
logs[mask]
mask = ("2016-08-11" < logs.timecreated) & (logs.timecreated < "2016-08-12")
logs[mask]
logs[mask].size()
logs[mask].shape
logs.groupby(logs.timecreated.dt.date).size()
logs[mask].groupby(logs.timecreated.dt.date).size()
mask = ("2016-08-07" < logs.timecreated) & (logs.timecreated <= "2016-08-14")
logs[mask].groupby(logs.timecreated.dt.date).size()
mask = ("2016-08-11" < logs.timecreated) & (logs.timecreated < "2016-08-12")
logs[mask].groupby(logs.timecreated.dt.hour).size()
mask = ("2016-08-11" < logs.timecreated) & (logs.timecreated < "2016-08-12")
logs[mask].groupby(logs.timecreated.dt.hour).size()
mask = ("2016-08-11 18:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-12 20:00:00")
logs[mask].groupby(logs.timecreated.dt.hour).size()
mask = ("2016-08-11 18:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-12 20:00:00")
logs[mask]
logs[mask].groupby('eventname').size()
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique})
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique}).sort_values(by='username')
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':count}).sort_values(by='username')
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':pd.Series.nunique}).sort_values(by='username')
def get_activity_log_by_time(logs, eventname, start_date, end_date):
    mask = ((start_date < logs.timecreated) &
            (logs.timecreated < end_date) &
            (logs.eventname == eventname))
    return logs[mask]
logins = get_activity_log_by_time(logs,'\core\event\user_loggedin', "2016-08-07", "2016-08-14")
plot_heatmap(logins)
plot_heatmap(logins)
plot_heatmap(logins)
logins = get_activity_log_by_time(logs,'\core\event\course_viewed', "2016-08-07", "2016-08-14")
plot_heatmap(logins)
plot_heatmap(logins[logins.completed])
plot_heatmap(logins[~logins.completed])
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    ax = sns.heatmap(hours)
    return ax
def get_activity_log_by_time(logs, eventname, start_date, end_date):
    mask = ((start_date < logs.timecreated) &
            (logs.timecreated < end_date) &
            (logs.eventname == eventname))
    return logs[mask]

def plot_activity_by_weeks(logs,eventname):
    fig, axs = plt.subplots(1,4)
    logins = get_activity_log_by_time(logs,eventname, "2016-08-07", "2016-08-14")
    axs[0] = plot_heatmap(logins)
    logins = get_activity_log_by_time(logs,eventname, "2016-08-14", "2016-08-21")
    axs[1] = plot_heatmap(logins)
    logins = get_activity_log_by_time(logs,eventname, "2016-08-21", "2016-08-28")
    axs[2] = plot_heatmap(logins)
    logins = get_activity_log_by_time(logs,eventname, "2016-08-28", "2016-09-04")
    axs[3] = plot_heatmap(logins)
plot_activity_by_weeks(logs, '\core\event\user_loggedin')
fig, axs = plt.subplots(1,4)
axs
axs[0]
axs[0] = plot_heatmap(logins)
axs[0] = sns.heatmap(hours)
axs[0] = sns.heatmap(hours)
def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    return sns.heatmap(hours)
plot_activity_by_weeks(logs, '\core\event\user_loggedin')
def plot_heatmap(logs, ax):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    sns.heatmap(hours, ax=ax)

def plot_activity_by_weeks(logs,eventname):
    fig, axs = plt.subplots(1,4)
    logins = get_activity_log_by_time(logs,eventname, "2016-08-07", "2016-08-14")
    plot_heatmap(logins, axs[0])
    logins = get_activity_log_by_time(logs,eventname, "2016-08-14", "2016-08-21")
    plot_heatmap(logins, axs[1])
    logins = get_activity_log_by_time(logs,eventname, "2016-08-21", "2016-08-28")
    plot_heatmap(logins, axs[2])
    logins = get_activity_log_by_time(logs,eventname, "2016-08-28", "2016-09-04")
    plot_heatmap(logins, axs[3])
plot_activity_by_weeks(logs, '\core\event\user_loggedin')
plot_activity_by_weeks(logs[logs.completed], '\core\event\user_loggedin')
plot_activity_by_weeks(logs[~logs.completed], '\core\event\user_loggedin')
fig, axs = plt.subplots(2,4)
axs
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
plot_activity_by_weeks(logs, '\core\event\user_loggedin')
plot_activity_by_weeks(logs, '\core\event\course_module_completion_updated')
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':pd.Series.nunique}).sort_values(by='username')
mask = ("2016-08-11 18:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-12 20:00:00")
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':pd.Series.nunique}).sort_values(by='username')
plot_activity_by_weeks(logs, '\mod_quiz\event\attempt_submitted')
plot_activity_by_weeks(logs, '\core\event\course_module_completion_updated')
def plot_heatmap(logs, ax):
    hours = logs.groupby([logs.timecreated.dt.date,logs.timecreated.dt.hour]).size().unstack(level=0)
    sns.heatmap(hours, ax=ax)
plot_activity_by_weeks(logs, '\core\event\course_module_completion_updated')
mask = ("2016-08-31 14:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-31 16:00:00")
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':pd.Series.nunique}).sort_values(by='username')
logs.edulevel
logs.edulevel.unique()
logs = logs[logs.edulevel != 1]
plot_activity_by_weeks(logs, '\core\event\course_module_completion_updated')
logs.edulevel.unique()
plot_activity_by_weeks(logs, '\mod_quiz\event\attempt_submitted')
plot_activity_by_weeks(logs, '\core\event\user_loggedin')
run src/models/model_factory.py
run src/models/model_factory.py
run()
    cutoff = "2016-08-14"
    FF.init_registered_by(cutoff)
    FF.make_dict_features_by_date(features,cutoff)
    FF.make_y()
    X = FF.data.values
    y = FF.y.values
MF.fit_tree_model(X,y)
run src/models/model_factory.py
run src/models/model_factory.py
