#
#
#
# 1. load logs data
# 2. get list of users
import pandas as pd

class Funnel(object):

def __init__(self, logs, completions=None):
    self.logs = logs
    self.completions = completions

    #  init funnel df with all unique users form the log as index
    self.funnel = pd.DataFrame(index=logs.username.unique())


def make_completion_feature(id, feature_name, date):
    condition = ((self.logs.contextinstanceid == id) &
                (self.logs.target == 'course_module_completion') &
                (self.logs.timecreated <= date))
    feature = self.logs[condition].groupby('username').size()
    feature_count.name = feature_name
    self.funnel = self.funnel.join(quiz_wk1)

def make_features(logs):


    # week 1
    make_completion_feature(54994, "wk1_quiz", "2016-08-14")

    make_completion_feature(54989, "wk1_page", "2016-08-14")

    # week 2 quiz
    # make_completion_feature(55005, "quiz_wk2", "2016-08-21")
    #
    # # week 3 quiz
    # make_completion_feature(55017, "quiz_wk3", "2016-08-28")
    #
    # # week 4 quiz
    # make_completion_feature(55029, "quiz_wk4", "2016-09-07")

def make_y(funnel,completions):
    min_req = [54994, 54989, 55005, 55000, 55017, 55014, 55012, 55029, 55023, 55027]

    user_completions = completions[completions.coursemoduleid.isin(min_req)]
    user_completions = user_completions.groupby('username')\
                    .agg({'completionstate':lambda x: x.sum() == 10})


    funnel.join(user_completions)
    funnel.join(user_completions).fillna(False,inplace=True)

    return funnel


if __name__ == "__main__":
    pass
