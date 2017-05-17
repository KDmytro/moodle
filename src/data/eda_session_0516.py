

def plot_heatmap(logs):
    hours = logs.groupby([logs.timecreated.dt.weekday,logs.timecreated.dt.hour]).size().unstack(level=0)
    ax = sns.heatmap(hours)


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
