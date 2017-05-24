usr_wk0 = logs[(logs.courseid == 10464) & (logs.eventname == "\core\event\user_enrolment_created") & (logs.timecreated <= "2016-08-14")].username.unique()


usr_wk1 = logs[(logs.courseid == 10464) &
                (logs.eventname == "\core\event\user_enrolment_created") &
                (logs.timecreated > "2016-08-07") &
                (logs.timecreated <= "2016-08-14")].username.unique()

usr_wk2 = logs[(logs.courseid == 10464) &
                (logs.eventname == "\core\event\user_enrolment_created") &
                (logs.timecreated > "2016-08-14") &
                (logs.timecreated <= "2016-08-21")].username.unique()

usr_wk3 = logs[(logs.courseid == 10464) &
                (logs.eventname == "\core\event\user_enrolment_created") &
                (logs.timecreated > "2016-08-21") &
                (logs.timecreated <= "2016-08-28")].username.unique()

usr_wk4 = logs[(logs.courseid == 10464) &
                (logs.eventname == "\core\event\user_enrolment_created") &
                (logs.timecreated > "2016-08-28") &
                (logs.timecreated <= "2016-08-07")].username.unique()

usr_wk1_data = pd.DataFrame(index=usr_wk1)

logs


FF.init_registered_by("2016-08-14")
FF.make_y_wk1()
y_wk1 = FF.make_y_wk1()
y_wk1.sum()
y_wk1.count()
FF.make_completion_feature(54994, '1_quiz', "2016-08-14")
FF.data['1_quiz'].sum()
FF.data['1_quiz'].count()


FF.init_registered_by("2016-08-21")
y_wk2 = FF.make_y_wk2()
print y_wk2.sum()
print y_wk2.count()
FF.make_completion_feature(55005, '2_quiz', "2016-08-21")
print FF.data['2_quiz'].sum()
print FF.data['2_quiz'].count()


FF.init_registered_by("2016-08-28")
y_wk3 = FF.make_y_wk3()
print y_wk3.sum()
print y_wk3.count()
FF.make_completion_feature(55017, '3_quiz', "2016-08-28")
print FF.data['3_quiz'].sum()
print FF.data['3_quiz'].count()

FF.init_registered_by("2017-09-06")
y_wk4 = FF.make_y_wk4()
print y_wk4.sum()
print y_wk4.count()
FF.make_completion_feature(55029, '4_quiz', "2017-09-06")
print FF.data['4_quiz'].sum()
print FF.data['4_quiz'].count()

[u'seaborn-darkgrid',
 u'seaborn-notebook',
 u'classic',
 u'seaborn-ticks',
 u'grayscale',
 u'bmh',
 u'seaborn-talk',
 u'dark_background',
 u'ggplot',
 u'fivethirtyeight',
 u'seaborn-colorblind',
 u'seaborn-deep',
 u'seaborn-whitegrid',
 u'seaborn-bright',
 u'seaborn-poster',
 u'seaborn-muted',
 u'seaborn-paper',
 u'seaborn-white',
 u'seaborn-pastel',
 u'seaborn-dark',
 u'seaborn',
 u'seaborn-dark-palette']

# User Activity
plt.style.use('seaborn-dark-palette')
x = [0,1,2,3,4]
registered = [1314, 1799, 1997, 2130, 2162]
completed_quiz = [0, 587, 380, 403, 550]
completed_all = [0, 206, 266, 287, 474]
x_labels = ["2016-08-07", "2016-08-14", "2016-08-21", '2016-08-28',"2016-09-04"]

plt.title("User Activity", fontsize=20)
plt.fill_between(x, 0, registered, alpha=0.30)
plt.plot(x,registered,label = 'Registered')
plt.plot(x,completed_quiz, label = 'Active')
plt.plot(x,completed_all, label = 'Completed All')
plt.xticks(x, x_labels)
legend = plt.legend(loc='upper left', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')


# Model Accuracy overtime
plt.style.use(u'seaborn-darkgrid')
x = [0,1,2,3]
recall = [0.78, 0.85, 0.86, 0.89]
f1 = [0.74, 0.88, 0.91, 0.94]
x_labels = ["Week 0", "Week 1", "Week 2", "Week 3"]

plt.ylim([0.5,1])
plt.title("Model score over time", fontsize=20)
# plt.fill_between(x, 0, registered, alpha=0.30)
plt.plot(x,recall,label = 'Recall')
plt.plot(x,f1, label = 'F1 score')
plt.xticks(x, x_labels)
plt.axhline(y=0.714,c='gray',ls="--")
legend = plt.legend(loc='upper left', shadow=True)
# frame = legend.get_frame()
# frame.set_facecolor('0.90')
model_score.png

# Standar Log
plt.style.use(u'seaborn-darkgrid')
plt.title("Standard Log - Counts", fontsize=20)
plt.legend(loc='best', shadow=True)
plt.plot(logs.groupby(logs.timecreated.dt.date).size())

standard_log.png
