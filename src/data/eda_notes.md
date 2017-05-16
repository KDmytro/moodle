
CONTEXT is important

Context levels:
'CONTEXT_SYSTEM', 10
'CONTEXT_USER', 30
'CONTEXT_COURSECAT', 40
'CONTEXT_COURSE', 50
'CONTEXT_MODULE', 70
'CONTEXT_BLOCK', 80

## edulevel
https://docs.moodle.org/dev/Event_2#Level_property

The 'edulevel' property helps define the educational value of the event. It is intentional that the list is limited to only 3 different constants as having too many options would make it harder for developers to pick the right one(s). We also have to keep in mind that this is not supposed to answer all the questions about a particular event, other event properties like the courseid, the context, the component name can be used with the level to get more granular reports.



Teachers:

User - 'user8540069828419911681' seems to be the primary instructor for the course
also - user8873948499972980737


# Identifying course info

Course Id =  '10464' ????

In [92]: get_counts(aug, 'courseid','username')[:10]
Out[92]:
          username
courseid
0             2160
10464         2142  <---
1             1191
10951          111
12053           47
10470           24
10506           23
11344           22
11178           21
11679           21


edulevel = 1, count of courses grouped by username:

In [105]: get_counts(aug[aug.edulevel == 1], 'courseid','username')[:10]
Out[105]:
          username
courseid
10464         1362  <---
10951           45
11178           12
11842           10
11240            9
10993            8
10967            7
11866            7
11679            7
10489            6


In [16]: get_counts(aug[(aug.edulevel == 2) & (aug.courseid == 1)], ['contextid', 'contextlevel'],'username')
Out[16]:
                        username
contextid contextlevel
2         50                 992
171517    70                 449
67        70                 181
98        70                  58
93        70                  28
71        70                  20

Overall we have only 2168 unique users who took the course
In [140]: len(course_logs.username.unique())
Out[140]: 2168



Total activity count over time
In [179]: logs_df.groupby([logs_df.timecreated.dt.year,logs_df.timecreated.dt.month]).agg({'id':pd.Series.nunique})
Out[179]:

Year        Month         Count
-------------------------------
2016        3               574
            4               354
            5               779
            6              1267
            7              3914
            8            465613
            9             62593
            10             1964
            11               15
            12               32

Total activity by user [2168 rows x 1 columns]


In [189]: logs_df.groupby(['username']).agg({'id':pd.Series.nunique}).sort_values(by='id')
Out[189]:

                            id
username
user4296055795331629057      5
user6171537755726675969      5
user2804548721562353665      5
user703388091146043393       5
user8260123881541468161      5
user4538156917054242817      5
user5575198275574693889      5
user7208078364010086401      5
user4025352944491692033      6
user6134724259592798209      6
user714497140021264385       6
user5726338535498186753      6
user1799031095849648129      6
user4103594239168872449      6
user7183847047584284673      6
user4752991357293821953      6
user7939475646290329601      6
user7550534261346926593      6
user4780975929675481089      6
user8024953209241993217      7
user8000735872934739969      7
user7310529642010509313      7
user8139950017994555393      7
user8210769510400000001      7
user7456425411858137089      7
user7957926649700286465      7
user6772254619302100993      7
user3150190273452048385      7
user6571785096615952385      7
user2972367404648103937      7
...                        ...
user5079710713501450241    999
user7843022942953799681   1007
user1651746380823134209   1023
user1149626259668467713   1031
user3132550026723590145   1052
user2943964197509136385   1079
user1360079167546195969   1132
user9081585137665179649   1156
user5394195829596618753   1162
user4743079388818440193   1173
user6875750016737083393   1190
user1406505393194008577   1195
user8280041345700069377   1204
user428220802190540801    1283
user3974045222224003073   1316
user5572813159976140801   1352
user8796387446511108097   1427
user5064388258759180289   1553
user1671143131736702977   1657
user9042698327673536513   1755
user2836743929557155841   2113
user6168325103009398785   2456
user8540069828419911681   2562
user1619922760513880065   3302
user6994576020762263553   3733
user113100542036672513    5851
user2959087468848087041   6500
user7959886181284446209   7061
user6442803380426375169  13627
user7619359643386511361  16930




id                                              0
confirmed                                       1
deleted                                         0
suspended                                       0
mnethostid                                      1

idnumber                                      NaN
firstname           WjLE Pjb a VUQhOz yem tGdQmvn
lastname               r  nrmZZflGFBbefW REfdbNtc
email              lhIh LplRfJO kFOnSFr vgzdkgCX
icq                                           NaN
skype                                         NaN
yahoo                                         NaN
aim                                           NaN
msn                                           NaN
phone1                                        NaN
phone2                                        NaN
institution                                   NaN
department                                    NaN
address                                       NaN
country                                        AU
theme                                         NaN
picture                                         0
url                                           NaN
description                                   NaN
descriptionformat                               1
trustbitmask                                    0
lastnamephonetic                              NaN
firstnamephonetic                             NaN
middlename                                    NaN
alternatename                                 NaN
calendartype                            gregorian

USER FILE FEATURE SELECTION

username                   user186977097674129409

emailstop                                       0

city                                        Tu jq
lang                                        en_us
timezone                                       99

firstaccess                   2016-03-22 16:27:12
lastaccess                    2016-08-12 20:20:33
lastlogin                     2016-08-01 17:42:19
currentlogin                  2016-08-12 16:34:51
lastip                                    RQZq ov

mailformat                                      1
maildigest                                      0
maildisplay                                     0
autosubscribe                                   1
trackforums                                     1

timecreated                   2016-03-22 16:17:55
timemodified                  2017-02-15 04:19:11





DROP off rate:

In [39]: logs.groupby('username').agg({'timecreated':lambda x: pd.to_datetime('2016-08-14')>x.max()}).mean()
Out[39]:
timecreated    0.199262
dtype: float64

In [40]: logs.groupby('username').agg({'timecreated':lambda x: pd.to_datetime('2016-08-21')>x.max()}).mean()
Out[40]:
timecreated    0.338561
dtype: float64

In [41]: logs.groupby('username').agg({'timecreated':lambda x: pd.to_datetime('2016-08-28')>x.max()}).mean()
Out[41]:
timecreated    0.464945
dtype: float64

In [42]: logs.groupby('username').agg({'timecreated':lambda x: pd.to_datetime('2016-09-04')>x.max()}).mean()
Out[42]:
timecreated    0.684041
dtype: float64



Number of Completion before specific date:
completions.groupby('username').agg(lambda x: (x['timemodified'] <= pd.to_datetime('2016-08-14')).sum() )
