# A.I. Sommelier

#### [Visit App on Heroku](https://myclassifierwine.herokuapp.com/)



## PROJECT CASE

Can A.I. accurately predict red wine quality rating? <br>
Anyway, what is quality if not how wine taster's tongue precepts wine's chemical components?<br>  

Let's try to answer that question with machine learning approach, where various classifier algorithms will try to
discover all the patters in wine rating process. As a last part of a project, let's build some artificial sommeliers 
and let them handle real-world wine samples. Everything in a form of python flask application.



## APP STRUCTURE

Flask App has 4 views, each of them representing different stage of machine learning process. Each section ends with downloadable code template.

### Part 1 - Dataset Overview

First, we'll have a closer look on dataset. With numpy, pandas, seaborn and scikit-learn:

![1](https://user-images.githubusercontent.com/26208598/42726492-34abc6d2-878d-11e8-8e3b-77a22d9c08de.GIF)
### Part 2 - Building Classifier 

In the next step we'll build foundations of our classifier while choosing best fitting algorithms:

![2](https://user-images.githubusercontent.com/26208598/42726493-360263c4-878d-11e8-8dad-0f09f086c0e5.GIF)

### Part 3 - Fitting Classifier

Now, it's a time to test our classifiers and see how they're performing:

![1](https://user-images.githubusercontent.com/26208598/51864052-923c2000-233a-11e9-8e94-144d5a7b0d67.JPG)

### Part 4 - Rating Red Wine

Let me introduce you to our A.I. Sommeliers:

![2](https://user-images.githubusercontent.com/26208598/51864053-923c2000-233a-11e9-8882-6620eea72bb5.JPG)


## TOOLS, MODULES & TECHNIQUES

##### Python – web development:
flask | Conda | Heroku | Docker
##### Python – DB:
flask_sqlalchemy
##### Python – data analysis & visualisation:
pandas | numpy | matplotlib | seaborn
##### Python – machine learning:
sklearn | scipy | pandas | numpy | pickle
##### Database Development:
SQLite
##### Testing
selenium | unittest
##### Web Development:
HTML | CSS | Bootstrap | Materialize | JavaScript | JQuery

## Test Suite:

### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/A.I.-Sommelier.svg?branch=master)](https://travis-ci.com/LukaszMalucha/A.I.-Sommelier)

### Test Files:

##### /tests


## INSTALLING REQUIREMENTS (Conda Environment, Cloud9)

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh<br>
chmod a+x Miniconda3-latest-Linux-x86_64.sh<br>
./Miniconda3-latest-Linux-x86_64.sh<br>

NEW TERMINAL

conda create -n py3 python=3 ipython <br>
source activate py3 <br>
conda install pip <br>

pip install numpy <br>
pip install pandas <br>
pip install matplotlib <br>
pip install scikitlearn <br>
pip install scipy <br>

pip install flask

pip freeze --local > requirements.txt


## CREDITS & INSPIRATIONS

##### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ<br>

##### Team Members Portraits:

https://www.pexels.com

Thank you,

Lukasz Malucha