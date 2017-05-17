all_users = FF.make_y().reset_index()
all_users.columns=['username','completed']
logs = logs.merge(all_users.reset_index(), on='username')



def convert_timezone(df):
    for tz in df.timezone.unique():
        mask = (df.timezone == tz)
        df.ix[mask, 'timecreated'] = \
        df.ix[mask, 'timecreated'].dt.tz_localize('UTC').dt.tz_convert(tz)
    # df.ix[df.timezone == '99','timezone'] = 'UTC'
    # df.ix[df.timezone == '-3.0','timezone'] = 'America/Sao_Paulo'
    # df.ix[df.timezone == '-5.0','timezone'] = 'America/New_York'
    # df.ix[df.timezone == '1.0','timezone'] = 'Europe/London'
    # df.ix[df.timezone == '2.0','timezone'] = 'Europe/Paris'
    # df.ix[df.timezone == '5.5','timezone'] = 'Asia/Kolkata'


mask = ("2016-08-11 18:00:00" < logs.timecreated) & (logs.timecreated < "2016-08-12 20:00:00")
logs[mask].groupby('eventname').agg({'username':pd.Series.nunique, 'id':count}).sort_values(by='username')


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


logs = DE.get_logs()
users = DE.get_users()

logs = logs.merge(users[['username','timezone']], on='username')
convert_timezone(logs)

logs[logs.username == 'user1077796981797027841'].timecreated.min()



                                timecreated
username
user1002410981378228225 2016-08-15 10:29:14
user1003176640903118849 2016-07-11 20:49:18
user1011513786604978177 2016-08-23 04:29:24
user101338288765272065  2016-08-22 14:51:44
user1022941294420295681 2016-08-23 00:34:40
user102321797621350401  2016-03-26 19:29:44
user1024654170327613441 2016-08-24 10:25:49
user1025316407040016385 2016-07-27 21:12:14
user103715351300145153  2016-06-08 23:21:15
user1037658047104679937 2016-08-19 03:06:15
user1038703339065311233 2016-03-18 11:49:58
user1041565019940061185 2016-06-23 10:11:57
user1042190010696073217 2016-05-26 10:08:04
user1053467362159755265 2016-07-20 07:15:41
user1055964752498393089 2016-08-16 23:54:52
user1067394699855134721 2016-08-07 22:11:13
user1069303198637883393 2016-07-25 07:41:32
user1074852601326993409 2016-08-07 09:37:47
user1077796981797027841 2016-08-17 06:51:57
user1082015833682608129 2015-03-30 17:30:00
user1085115618954313729 2016-08-18 15:29:05
user1094355240364277761 2016-06-24 18:48:35
user1097634469369610241 2016-08-22 18:06:32
user1098462156812189697 2016-07-23 16:54:13
user1098915258682048513 2016-08-24 17:55:53
user1104517725692100609 2016-05-06 16:40:46
user1106997957636390913 2016-08-08 19:41:10
user1107826976518832129 2016-08-14 07:44:06
user1110488443198111745 2016-08-09 23:49:42
user1111099440950673409 2016-08-05 02:31:21
