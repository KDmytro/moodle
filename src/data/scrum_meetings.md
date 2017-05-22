# Scrum team meetings

* What did you do?
* What are you planning to do?
* What are your issues?

## 05/08/2017
* Reach out to moodle and tell them what I am working on.
* Further understand data structure
  * Read up on Logging model in moodle (https://docs.moodle.org/dev/Logging_2)
  * https://docs.moodle.org/dev/Event_2#Properties
* Trim down irrelevant data, arrive at "working" dataset
* Find relevant papers

## 05/09/2017
* Good progress on data cleaning
  * I have clean history for each user in the course
  * Feature: Time till next event/click
  * Section reference
* ToDo:
  * EDA scripts
  * Research existing papers
  * Decide on your dependent variable
  * Summary statistics
  * Reach out to Moodle Research team
  * Prepare Basic summary statistic report

  * identify passing for each week1
  * make passed_wk1, passed_wk2 features

## 05/10/2017
* Not heard back from moodle
* Completion for each week

Funnel Analysis by week
* Completes Everything
* Completes Quiz and Page
* Completes Quizzes only
* Completes Pages only


## 05/11/2017
* Build model for each week prediction
* Funnel - Viz?

---

* Additional features besides completions
  * Time spent
  * Forum interactions

## 05/12/2017
First draft preso
* Presentation is too long
* remove black backgrounds
* add your github
* restate business problem

Questions for Derren
* Focus on Logistic Regression to understand it deeper?
* Explore automated feature selection process?


## 05/15/2017
* implement cut off on registration date
* try Y as all objects
* Explore Badge in more details
* Impact of Grades?
  * Number of attempts
  * Revisitng
* Log features?



Best model - Logistic w scaled features:
  '''python
  In [356]: MF.fit_model(scale(FF.data.values),y)
  {'penalty': 'l1', 'C': 1, 'class_weight': 'balanced'}
               precision    recall  f1-score   support

        False       0.96      0.79      0.87       380
         True       0.34      0.79      0.48        53

  avg / total       0.89      0.79      0.82       433

  Out[356]:
  LogisticRegression(C=1, class_weight='balanced', dual=False,
            fit_intercept=True, intercept_scaling=1, max_iter=100,
            multi_class='ovr', n_jobs=1, penalty='l1', random_state=None,
            solver='liblinear', tol=0.0001, verbose=0, warm_start=False)

  '''
