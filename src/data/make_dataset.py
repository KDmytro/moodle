# -*- coding: utf-8 -*-
import os
import click
import logging
from dotenv import find_dotenv, load_dotenv

import pandas as pd

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

def load_all():
    log_df = pd.read_csv("data/interim/mdl_logstore_standard_log_100000.csv")

    badge_df = pd.read_csv("mdl_badge_issued.csv ")
    course_modules_df = pd.read_csv("mdl_course_modules.csv")
    completion_df = pd.read_csv("mdl_course_modules_completion.csv")
    grades_history_df = pd.read_csv("mdl_grade_grades_history.csv")
    user_df = pd.read_csv("data/interim/mdl_user.csv.csv")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
