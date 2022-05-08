#  Final Project Ironhack Data Analytics

*Antonio José Arenal Armesto*

*Álvaro Benayas Aranda*

## Content
- [Project Description](#project)
- [Dataset](#dataset)
- [Workflow](#workflow)
    * [Import Data](#preprocessing)
    * [Preprocessing](#preprocessing)
- [Images](#images)


<a name="project"></a>

## Project Description

The banking entities "Final Bank" and "City Bank" are going to merge soon, after a leadership meeting of both companies, different projects are agreed upon to guarantee a successful transition.

Among the projects that demand, we have the task of estimating which client of "City Bank" will accept the "Final Bank" credit card that will be offered in the transfer of their accounts to a single entity.

To do this and following the LOPD, we have a model based on the dependent variable that stores the decision to accept the card or not of customers already transferred.


<a name="dataset"></a>

## Dataset

The dataset we will be using are given up by both companies and we will have to purge and clean to proceed to the analisys.


<a name="workflow"></a>

## Workflow

### Import Data

We've imported all the Dataset in a pandas dataframe, using the chunk method, as the original data csv is huge.

<a name="preprocessing"></a>

### Preprocessing

We've classified all the variables on my dataset:

**CATEGORICAL:**
* Reward
* Mailer Type
* Income Level	
* Credit Rating	

**BOOLEAN:**
* Offer Accepted
* Overdraft Protection	
* Own Your Home	

**ORDINAL:**
* Customer Number

**NUMERICAL:**
* Bank Accounts Open	
* Credit Cards Held	
* Homes Owned	
* Household Size	
* Average Balance	
* Q1 Balance	
* Q2 Balance	
* Q3 Balance	
* Q4 Balance	


<a name="images"></a>


## Images

**Main app**

![img](/img/img1.jpg?raw=true "Main app")


**Prediction results**

![img](/img/img2.jpg?raw=true "Prediction results")
