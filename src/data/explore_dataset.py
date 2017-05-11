# -*- coding: utf-8 -*-
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv

import pandas as pd

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main(input_filepath=None, output_filepath=None):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

def load_all():
    log_df = pd.read_csv("data/interim/mdl_logstore_standard_log_100000.csv")

    badge_df = pd.read_csv("data/raw/mdl_badge_issued.csv")
    course_modules_df = pd.read_csv("data/raw/mdl_course_modules.csv")
    completion_df = pd.read_csv("data/raw/mdl_course_modules_completion.csv")
    grades_history_df = pd.read_csv("data/raw/mdl_grade_grades_history.csv")
    user_df = pd.read_csv("data/raw/mdl_user.csv")

def load_table(module_num=None):
    path = "data/raw/"
    modules = [ '../interim/mdl_logstore_standard_log_100000.csv',
                'mdl_logstore_standard_log.csv',
                'mdl_user.csv',
                'mdl_course_modules.csv',
                'mdl_course_modules_completion.csv',
                'mdl_grade_grades_history.csv',
                'mdl_badge_issued.csv']

    if not module_num:
        print module_num
        for i, m in enumerate(modules):
            print i, ': ',m
        module_num = int(raw_input("Enter module number to load: "))

    return pd.read_csv(path+modules[module_num])

# Log File exploration

# Display all componenets with unique user count
def list_components_user_count():
    logs_df[['component','id']].groupby('component')\
                                .agg({'id': pd.Series.nunique})\
                                .sort_values(by='id', ascending=False)
#
#                          id
# component
# core                  42709
# mod_forum             11460
# mod_book               1493
# mod_page                588
# mod_wiki                562
# mod_choice              221
# mod_chat                166
# mod_folder              153
# mod_glossary            133
# mod_quiz                126
# mod_survey               87
# tool_langimport          51
# mod_data                 51
# mod_feedback             43
# mod_lesson               32
# booktool_print           26
# mod_bigbluebuttonbn      13
# mod_workshop             13
# report_log               13
# mod_recordingsbn         10
# gradereport_grader        8
# mod_resource              7
# mod_url                   5
# report_stats              3
# report_outline            2
# mod_lti                   1
# mod_assign                1
# gradereport_user          1
# report_loglive            1
# booktool_exportimscp      1


def users_admins():
    cols = ['report_stats',
        'report_outline',
        'mod_lti',
        'mod_assign',
        'gradereport_user',
        'report_loglive',
        'booktool_exportimscp']

    logs_df[logs_df['component'].isin(cols)][['component','id','username']].sort_values(by='component')

# Out[67]:
#                   component       id                 username
# 7643   booktool_exportimscp   165759  user6442803380426375169
# 7644   booktool_exportimscp   165759  user6442803380426375169
# 36276      gradereport_user   484854  user8042968243406635009
# 42320            mod_assign   560980  user6442803380426375169
# 42321            mod_assign   560980  user6442803380426375169
# 74577               mod_lti  1444465  user8651365659558543361
# 74631        report_loglive  1446111  user7501243803613790209
# 4037         report_outline    53959  user8540069828419911681
# 4038         report_outline    53959  user8540069828419911681
# 74639        report_outline  1446124  user7501243803613790209
# 5993           report_stats    94515  user8540069828419911681
# 5994           report_stats    94515  user8540069828419911681
# 74632          report_stats  1446171  user7501243803613790209
# 74643          report_stats  1446177  user7501243803613790209


def get_course_logs():
    df = load_table(1)
    condition = ((df.edulevel != 1) &
                 (df.courseid == 10464))
    df = df[condition]
    df['timecreated'] = to_datetime(df['timecreated'])

    return df


def get_users():

    df = load_table(2)
    cols = ['username',
            'emailstop',
            'city',
            'lang',
            'timezone',
            'firstaccess',
            'lastaccess',
            'lastlogin',
            'currentlogin',
            'lastip',
            'mailformat',
            'maildigest',
            'maildisplay',
            'autosubscribe',
            'trackforums',
            'timecreated',
            'timemodified']

    df = df[cols]

    df['firstaccess'] = to_datetime(df.firstaccess)
    df['lastaccess'] = to_datetime( df.lastaccess)
    df['lastlogin'] = to_datetime( df.lastlogin)
    df['currentlogin'] = to_datetime( df.currentlogin)
    df['timecreated'] = to_datetime( df.timecreated)
    df['timemodified'] = to_datetime( df.timemodified)

    return df

def to_datetime(date_field):
    return pd.to_datetime(date_field,unit='s')

def log_unique_id_count_by_months():
    logs_df.groupby([logs_df.timecreated.dt.year, logs_df.timecreated.dt.month])\
        .agg({'id': pd.Series.nunique})
#
#                               id
# timecreated timecreated
# 2014        12              4656
# 2015        1             106109
#             2              58377
#             3               7102
#             4                446
#             5                271
#             6               1104
#             7               1326
#             8             111138
#             9              44865
#             10              1655
#             11               459
#             12              2916
# 2016        1             177241
#             2             129957
#             3               3943
#             4               1729
#             5               3900
#             6               4673
#             7              18035
#             8            1072577
#             9             142020
#             10              5800
#             11              2418
#             12              9607
# 2017        1               2402


def log_unique_user_count_by_months():
    logs_df.groupby([logs_df.timecreated.dt.year, logs_df.timecreated.dt.month])\
        .agg({'username': pd.Series.nunique})

# Out[56]:
#                          username
# timecreated timecreated
# 2014        12                 33
# 2015        1                  56
#             2                  58
#             3                  26
#             4                  17
#             5                  22
#             6                  20
#             7                  32
#             8                 114
#             9                 116
#             10                 37
#             11                 30
#             12                 34
# 2016        1                 171
#             2                 183
#             3                 119
#             4                 115
#             5                 172
#             6                 256
#             7                 954
#             8                2160
#             9                2166
#             10                191
#             11                107
#             12                120
# 2017        1                  18

def get_counts(df, groupby, count,ascending=False):
    return df.groupby(groupby).agg({count:pd.Series.nunique}).sort_values(by=count,ascending=ascending)

# Context level
# 'CONTEXT_SYSTEM', 10
# 'CONTEXT_USER', 30
# 'CONTEXT_COURSECAT', 40
# 'CONTEXT_COURSE', 50
# 'CONTEXT_MODULE', 70
# 'CONTEXT_BLOCK', 80
#




def logs_get_user(username):
    return logs_df[logs_df.username == username]
    user_log =course_logs[course_logs.username == 'user6913591088091496449']

def get_activity_counts(username):
    condition = ((aug.edulevel == 2) &
                 (aug.courseid == 10464) &
                 (aug.username == username))
    return get_counts(aug[condition], ['username','eventname'], 'id')


def get_user_activity_by_date(df):
    return df.groupby(['eventname',df.timecreated.dt.date]).agg({'id':pd.Series.nunique})


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
