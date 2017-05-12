


In [500]: execfile('src/models/funnel_model_cv.py')

---
Week 1 Logistic Regression model
---
Scores:
             precision    recall  f1-score   support

      False       0.84      0.87      0.85      1236
       True       0.64      0.59      0.62       498

avg / total       0.78      0.79      0.78      1734

Coefficients:
wk1_quiz : 1.49075458909
wk1_page : 0.127188789821
wk1_total : 0.0050277197966

---
Week 1 all features Logistic Regression model
---
Scores:
             precision    recall  f1-score   support

      False       0.81      0.87      0.84       309
       True       0.61      0.50      0.55       125

avg / total       0.75      0.76      0.76       434

Coefficients:
0_page_3 : 0.300449447791
0_page_1 : 0.137435931725
0_forum : 0.0706155091989
0_page_2 : -0.0502786417167
1_forum : 0.768049637924
1_page_1 : -0.00469179462678
1_book_1 : 0.489747105693
1_book_2 : -0.26721174676
1_choice : 0.0514395819692
1_page_2 : 0.133602587035
1_quiz : 0.957224290706
1_feedback : 0.543212855446
2_page_1 : 0.0400553093256
2_book : 0.0
2_glossary : 0.0
2_wiki : 0.0
2_survey : 0.0
2_quiz : 0.0
3_page_1 : 0.0400553093256
3_book : 0.0
3_data : -0.502809972732
3_page_2 : 0.0
3_forum : 0.0
3_quiz : 0.0
4_page_1 : 0.0400553093256
4_forum : 0.0
4_lesson : 0.0
4_workshop : 0.0
4_page_2 : 0.0
4_quiz : 0.0
4_page_3 : 0.0
4_page_4 : 0.0
4_feedback : 0.0


---
Random Forest
---
Scores:
             precision    recall  f1-score   support

      False       0.81      0.88      0.84       309
       True       0.62      0.47      0.54       125

avg / total       0.75      0.76      0.75       434


---

funnel = Funnel(logs, completions)
funnel.quizzes_over_time()
funnel.make_y()
hist_data = funnel.data.copy()
hist_data = hist_data.join(funnel.y.copy())
quiz_hist = pd.melt(hist_data, id_vars=['completionstate'], value_vars=['wk1_quiz', 'wk2_quiz','wk3_quiz','wk4_quiz'])
quiz_hist.groupby(['variable', 'value']).count()

Out[525]:
                completionstate
variable value
wk1_quiz 0.0               1578
         1.0                590
wk2_quiz 0.0               1786
         1.0                382
wk3_quiz 0.0               1762
         1.0                406
wk4_quiz 0.0               1506
         1.0                662


In [529]: hist_data.groupby(['wk1_quiz', 'wk2_quiz','wk3_quiz','wk4_quiz','completionstate']).size()
Out[529]:
wk1_quiz  wk2_quiz  wk3_quiz  wk4_quiz  completionstate
0.0 0.0	0.0	0.0	False		1248
0.0 0.0	0.0	0.0	True		    5
0.0 0.0	0.0	1.0	False		  31
0.0	0.0	0.0	1.0	True		   92
0.0	0.0	1.0	0.0	False		  13
0.0	0.0	1.0	0.0	True		    0
0.0	0.0	1.0	1.0	False		   6
0.0	0.0	1.0	1.0	True		   85
0.0	1.0	0.0	0.0	False		  21
0.0	1.0	0.0	0.0	True		    1
0.0	1.0	0.0	1.0	True		   35
0.0	1.0	0.0	1.0	True		    0
0.0	1.0	1.0	0.0	False		   2
0.0	1.0	1.0	0.0	True		    2
0.0	1.0	1.0	1.0	True		   37
0.0	1.0	1.0	1.0	True		    0
1.0	0.0	0.0	0.0	False		 162
1.0	0.0	0.0	0.0	True		    1
1.0	0.0	0.0	1.0	False		   8
1.0	0.0	0.0	1.0	True		   66
1.0	0.0	1.0	0.0	False		   6
1.0	0.0	1.0	0.0	True		    0
1.0	0.0	1.0	1.0	False		   4
1.0	0.0	1.0	1.0	True		   59
1.0	1.0	0.0	0.0	False		  30
1.0	1.0	0.0	0.0	True		    4
1.0	1.0	0.0	1.0	False		   5
1.0	1.0	0.0	1.0	True		   53
1.0	1.0	1.0	0.0	False		   9
1.0	1.0	1.0	0.0	True		    2
1.0	1.0	1.0	1.0	False		   0
1.0	1.0	1.0	1.0	True		  181




-------------------------
Week 1 all features model


Logistic Regression Scores:
             precision    recall  f1-score   support
      False       0.83      0.91      0.86      1236
       True       0.69      0.53      0.60       498
avg / total       0.79      0.80      0.79      1734

Random Forest: Scores:
             precision    recall  f1-score   support
      False       0.82      0.91      0.86      1236
       True       0.70      0.50      0.58       498
avg / total       0.78      0.79      0.78      1734


-------------------------
Week 2 all features model
Scores:
             precision    recall  f1-score   support
      False       0.88      0.92      0.90      1236
       True       0.77      0.69      0.73       498
avg / total       0.85      0.85      0.85      1734

Scores:
             precision    recall  f1-score   support
      False       0.86      0.91      0.89      1236
       True       0.75      0.64      0.69       498
avg / total       0.83      0.84      0.83      1734

-------------------------

Week 3 all features model
Scores:
             precision    recall  f1-score   support
      False       0.95      0.92      0.93      1236
       True       0.81      0.89      0.85       498
avg / total       0.91      0.91      0.91      1734

Scores:
             precision    recall  f1-score   support
      False       0.95      0.92      0.93      1236
       True       0.82      0.88      0.84       498
avg / total       0.91      0.91      0.91      1734

-------------------------

Week 4 all features model
Scores:
             precision    recall  f1-score   support
      False       0.99      0.97      0.98      1236
       True       0.94      0.96      0.95       498
avg / total       0.97      0.97      0.97      1734

Scores:
             precision    recall  f1-score   support
      False       0.99      0.97      0.98      1236
       True       0.93      0.96      0.95       498
avg / total       0.97      0.97      0.97      1734



# ------------------------------
# ModelFactory: Week 1 - all LOs
# ------------------------------

# Scores:
             precision    recall  f1-score   support

      False       0.88      0.77      0.82       405
       True       0.50      0.68      0.58       137

avg / total       0.78      0.75      0.76       542

# Coefficients:
1_forum : 0.994836986974
1_book_1 : 0.683228744567
1_quiz : 0.673524874656
1_feedback : 0.617447471855
3_data : -0.452692961904
0_page_3 : 0.285716297419
1_book_2 : -0.24369266246
1_choice : 0.103738686854
1_page_1 : -0.0687224891645
0_forum : 0.0661934796414
