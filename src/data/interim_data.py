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

def log_unique_user_count_by_months():
    logs_df.groupby([logs_df.timecreated.dt.year, logs_df.timecreated.dt.month])\
        .agg({'username': pd.Series.nunique})

def get_counts(df, groupby, count,ascending=False):
    return df.groupby(groupby).agg({count:pd.Series.nunique}).sort_values(by=count,ascending=ascending)


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

def quiz_attempts():
    logs[logs.eventname == '\mod_quiz\event\attempt_submitted']





if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
