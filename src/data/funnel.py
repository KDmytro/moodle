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

        self.init_data()

    def init_data(self):
        #  init funnel df with all unique users form the log as index
        self.data = pd.DataFrame(index=self.logs.username.unique())

    # def make_completion_feature(self, id, feature_name, date):
    #     condition = ((self.logs.contextinstanceid == id) &
    #                 (self.logs.target == 'course_module_completion') &
    #                 (self.logs.timecreated <= date))
    #     feature = self.logs[condition].groupby('username').size()
    #     feature.name = feature_name
    #     self.data = self.data.join(feature)
    #     self.data.fillna(0,inplace=True)

    def make_completion_feature(self, id, feature_name, end_date, start_date=pd.to_datetime(0)):
        condition = ((self.logs.contextinstanceid == id) &
                    (self.logs.target == 'course_module_completion') &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))
        feature = self.logs[condition].groupby('username').size()
        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_total_event_counts(self, feature_name, date):
        condition = ((self.logs.timecreated <= date))
        feature = self.logs[condition].groupby('username').size()
        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_wk1_features(self):

        # week 1
        self.make_completion_feature(54994, "wk1_quiz", "2016-08-14")
        self.make_completion_feature(54989, "wk1_page", "2016-08-14")
        self.make_total_event_counts("wk1_total", "2016-08-14")

    def make_wk2_features(self):

        # week 2 features
        self.make_completion_feature(55000, "wk2_page", "2016-08-21")
        self.make_completion_feature(55001, "wk2_book", "2016-08-21")
        self.make_completion_feature(55005, "wk2_quiz", "2016-08-21")

        self.make_total_event_counts("wk2_total", "2016-08-21")

    def make_wk1_features_to_date(self):
        # week 1 combined
        self.make_completion_feature(54994, "wk2_quiz_wk1", "2016-08-21")
        self.make_completion_feature(54989, "wk2_page_wk1", "2016-08-21")

    def make_wk1_features_catchup(self):
        # week 1 catchup
        self.make_completion_feature(54994, "wk1_quiz_c", "2016-08-14", "2016-08-21")
        self.make_completion_feature(54989, "wk1_page_c", "2016-08-14", "2016-08-21")



    def make_all_features_by_date(self, end_date, start_date=pd.to_datetime(0)):
        # All scorable course components
        min_req = [54994, 54989, 55005, 55000, 55017, 55014, 55012, 55029, 55023, 55027]

        for c in min_req:
            self.make_completion_feature(c, str(c), end_date)

    def make_dict_features_by_date(self, features, end_date, start_date=pd.to_datetime(0)):
        # All scorable course components
        # min_req = [54994, 54989, 55005, 55000, 55017, 55014, 55012, 55029, 55023, 55027]

        for c in features:
            self.make_completion_feature(c, features[c], end_date)

    def make_y(self,min_req=None):
        if not min_req:
            min_req = [54994, 54989, 55005, 55000, 55017, 55014, 55012, 55029, 55023, 55027]

        complete = lambda x: x.sum() == len(min_req)

        condition = self.completions.coursemoduleid.isin(min_req)
        y_completions = self.completions[condition]
        y_completions = y_completions.groupby('username')\
                        .agg({'completionstate':complete})


        self.y = self.data.join(y_completions)['completionstate']
        self.y.fillna(False, inplace=True)

        return self.y


if __name__ == "__main__":
    pass
