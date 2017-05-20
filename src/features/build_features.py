import pandas as pd

class FeatureFactory(object):

    def __init__(self, logs=None, completions=None):

        if logs is None:
            self.logs = pd.read_csv("data/raw/mdl_logstore_standard_log.csv")

        if completions is None:
            self.completions = pd.read_csv("data/raw/mdl_course_modules_completion.csv")

        self.logs = logs
        self.completions = completions

        self.init_data()

        self.features = {
            54984:'0_forum',
            54985:'0_page_1',
            54986:'0_page_2',
            55043:'0_page_3',
            54988:'1_forum',
            54990:'1_book_1',
            54991:'1_book_2',
            54994:'1_quiz',
            54995:'1_feedback',
            54992:'1_choice',
            54993:'1_page_2',
            54989:'1_page_1',
            55005:'2_quiz',
            55001:'2_book',
            55002:'2_glossary',
            55004:'2_survey',
            55003:'2_wiki',
            55000:'2_page_1',
            55017:'3_quiz',
            55013:'3_book',
            55016:'3_forum',
            55014:'3_data',
            55012:'3_page_1',
            55015:'3_page_2',
            55028:'4_page_2',
            55051:'4_feedback',
            55025:'4_lesson',
            55029:'4_quiz',
            55027:'4_workshop',
            55024:'4_forum',
            55030:'4_page_3',
            55023:'4_page_1',
            55052:'4_page_4',
        }


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


    def init_registered_by(self,date):
        user_index = self.logs[self.logs.timecreated <= date].username.unique()
        self.data = pd.DataFrame(index=user_index)

    def make_completion_feature(self, id, feature_name, end_date, start_date=pd.to_datetime(0)):
        condition = ((self.logs.contextinstanceid == id) &
                    (self.logs.target == 'course_module_completion') &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))
        feature = self.logs[condition].groupby('username').size()
        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_action_count_feature(self, action, feature_name, end_date, start_date=pd.to_datetime(0)):

        condition = ((self.logs.action == action) &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))

        feature = self.logs[condition].groupby('username').size()
        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_event_count_feature(self, eventname, feature_name, end_date, start_date=pd.to_datetime(0)):

        condition = ((self.logs.eventname == eventname) &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))

        feature = self.logs[condition].groupby('username').size()
        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_action_freq(self, action, feature_name, end_date, start_date=pd.to_datetime(0)):

        condition = ((self.logs.action == action) &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))

        feature = self.logs[condition]\
                        .groupby(['username',self.logs.timecreated.dt.date])\
                        .agg({'action':lambda x:1})\
                        .unstack(-1)\
                        .sum(axis=1)

        feature.name = feature_name
        self.data = self.data.join(feature)
        self.data.fillna(0,inplace=True)

    def make_time_since(self, action, feature_name, end_date, start_date=pd.to_datetime(0)):

        condition = ((self.logs.action == action) &
                    (self.logs.timecreated > start_date) &
                    (self.logs.timecreated <= end_date))

        feature = self.logs[condition]\
                        .groupby(['username'])\
                        .apply(lambda x: (pd.to_datetime("2016-08-14") - x.timecreated.max()).days)

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

    def quizzes_over_time(self):
        self.make_completion_feature(54994,'wk1_quiz',"2016-08-14")
        self.make_completion_feature(55005,'wk2_quiz',"2016-08-21")
        self.make_completion_feature(55017,'wk3_quiz',"2016-08-28")
        self.make_completion_feature(55029,'wk4_quiz',"2016-09-07")


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


        self.y = self.data.join(y_completions)['completionstate'].copy()
        self.y.fillna(False, inplace=True)
        self.y.index.rename('username',inplace=True)
        return self.y

    def make_y_nextweek(self,date):
        if not min_req:
            min_req = [54994, 54989, 55005, 55000, 55017, 55014, 55012, 55029, 55023, 55027]


        condition = self.completions.coursemoduleid.isin(wk_req)
        y_completions = self.completions[condition]
        y_completions = y_completions.groupby('username')\
                        .agg({'completionstate':complete})


        self.y = self.data.join(y_completions)['completionstate']
        self.y.fillna(False, inplace=True)

        return self.y


if __name__ == "__main__":
    pass
