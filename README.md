Sign up, Log in, don’t Drop out
==============================

For this project I conducted an analysis of student engagement in an online course. One of the main issues with online courses is related to low student engagement and high dropout rates. I wanted to analyze student click activity within a course to see if I can identify any interesting patterns among its usage. Based on my findings I was able to develop a predictive model that can help instructors identify students who are at risk of dropout. I used Python/SQL to build my pipeline and for my modeling I used Logistic Regression to identify the most significant factors in predicting student dropout.


## Background
One of the main issues related to online learning, particularly in MOOCs (massive open online courses), is related to high dropout rate among students. Despite the fact that this topic has been covered extensively in the news and literature, many practitioners and actual instructors still do not have a good understanding of the issue. Surprising there are very few tools currently available to facilitators that provide insight. In this project I want to conduct an analysis of the student log data from a LearnMoodle.com MOOC and build a predictive model that can help instructors identify student at risk of drop out as early as one week into the course.

## Dataset
The source of this data is the August 2016 session of the “Teaching with Moodle” MOOC, hosted at https://learn.moodle.net/ . Sessions of this course are delivered twice per year by employees of Moodle PTY LTD. This session was delivered in a fully online format from August 7 to September 4, 2016. There were 6119 students enrolled in this course, and 2 facilitators. Only data from students agreeing to allow their data to be used in research was included in this data set (2167 student).

## Main presentation
https://github.com/KDmytro/moodle/blob/master/reports/Moodle%20-%20Galvanize%20Capstone%20-%20Final%20preso.pdf

## Clickstream Data analysis
![User Activity](/reports/figures/user_activity.png)
Initial cli analysis revealed an expected pattern of declining number of active users, though not as rapid as some other more popular MOOC courses. This can partially be explained by the type of learners in the course - instructors and Moodle platform administrators.  For many of these students


## Model
![Model Accuracy over Time](/reports/figures/model_score.png)

## Future work
1. Generalize model to be applied to any course
2. Provide detailed information about user drop out risk. Use Decision tree algorithm
3. Develop PHP plug-in for Moodle

## Questions:
Feel free to reach out to me at __kdmytro@gmail.com__

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │    
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │    
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    │
    ├── src                <- Source code for use in this project.
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── explore_data.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── build_model.py
    │   │   └── model_score_overtime.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py


--------
