# TEAMMATE NET IDS: vaa238 and wl1622 
#


import numpy as np
import pandas as pd
import csv


# In[2]:


filename = 'train.csv'
df = pd.read_csv(filename, header = 0, delimiter = ',')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.dtypes


# In[7]:


df.isnull().any()


# In[8]:


df.shape


# In[9]:


#test.describe()


# In[10]:


df.loc[df['OVERAGE'] == -2]


# In[11]:


test = df
test.loc[test['OVERAGE'] == -2]


# In[12]:


#test = test.drop(index=8498, axis =0)


# In[13]:


#test.iloc[8498]


# In[14]:


#df.iloc[8498]


# In[15]:


#df = test
#df.info()


# In[16]:


df['LEAVE'].value_counts()


# In[17]:


df.groupby('LEAVE').mean()


# In[18]:


df['COLLEGE'] = df['COLLEGE'].astype(str)


# In[19]:


df.groupby('LEAVE').mean()


# for x in df['COLLEGE']:
#     if x is 'one':
#         df['COLLEGE'].str.replace('one','1')
#     else: 
#         df['COLLEGE'].str.replace('zero','0')

# In[20]:


df.groupby('REPORTED_SATISFACTION').mean()


# In[21]:


df.groupby('COLLEGE').mean()


# In[22]:


df.groupby('REPORTED_USAGE_LEVEL').mean()


# In[23]:


df.groupby('CONSIDERING_CHANGE_OF_PLAN').mean()


# Observations on features that seem to have an effect:
# Categorical Data    
#     1. college: seems to barely make a difference, .02 more likely to leave if person went to college
#     2. REPORTED_SATISFACTION: unsat has slightly over 50% chance of leaving and very_unsat has a bit lower than half chance of leaving. These are the 2 highest chances of leaving based on sat ranking. ALSO, sat ranking may be tied with the OVERAGE. These 2 categories had the highest overage, so maybe there are high overcharge fees or they just got upset about being overcharged. 
#     3. REPORTED_USAGE_LEVEL: very high usage has slightly over 50% churn (highest in group) followed by very little. So the rates are probably expensive if you're a heavy user or too pricey to be for a casual user
#     4. CONSIDERING_CHANGE_OF_PLAN: Those who had the highest overage are most looking into changing plans. Those with highest overage also happen to have lowest estimated house value. HOWEVER!!! Those that chose to leave are "perhaps" (51.7) and the next are "no"(49.69) and then "actively looking into it"(.4959). Maybe if we were to average all these values on a scale where perhaps is 3 and no is 2, the values in between the range of 2-3, this could tell us something. 
# 
# Number Data
#     1. INCOME: those who left had higher income than those who didnt
#     2. OVERAGE: those who left had ALMOST DOUBLE overage than those who didn't
#     3. LEFTOVER: those who left had more leftover minutes per month
#     4. HOUSE: those who left had cheaper house value
#     5. HANDSET $$: those who left had more expensive handsets
#     6. OVER 15 MIN: those who left had more over 15 min calls (maybe related to overage)
#     7. AVG CALL DURATION: those who left had slightly lover avg call duration but both are pretty close to 6 min
#     
# why are income and house indirectly related here?    
# correlation between high overage and cheaper house value
# correlation between income and handset price
# correlation between satisfaction and high overage = higher overage, less satisfaction
# 
# Features to include:
#     ***OVERAGE --> higher overage, more chance of leaving
#     LEFTOVER --> those who had more leftover minutes, less usage = higher chance of leaving
#     House value? --> those who had cheaper houses AND high overage are more likely to leave

# In[24]:


df.groupby('LEAVE').mean()


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.crosstab(df['REPORTED_SATISFACTION'],df['LEAVE']).plot(kind='bar')
plt.title('Turnover Frequency for Overage')
plt.xlabel('REPORTED_SATISFACTION')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.crosstab(df['COLLEGE'],df['LEAVE']).plot(kind='bar')
plt.title('Turnover Frequency for Overage')
plt.xlabel('college')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.crosstab(df['REPORTED_USAGE_LEVEL'],df['LEAVE']).plot(kind='bar')
plt.title('Turnover Frequency for Overage')
plt.xlabel('REPORTED_USAGE_LEVEL')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')


# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
pd.crosstab(df['CONSIDERING_CHANGE_OF_PLAN'],df['LEAVE']).plot(kind='bar')
plt.title('Turnover Frequency for Overage')
plt.xlabel('CONSIDERING_CHANGE_OF_PLAN')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')


# Categorical Data
# 
#     REPORTED_SATISFACTION: highest reportings of very unsatisfied followed by very satisfied
#     COLLEGE: more variability in people staying vs leaving in those who didnt go to college
#     REPORTED_USAGE_LEVEL: most variety in people who report little, also most people by far report little usage, then very high then very little
#     CONSIDERING_CHANGE_OF_PLAN: most people report considering, which also has most variance, then actively looking into it, then no. 
#     
# Conclusions: Don't really trust the categorical data. 
# 
# 

# In[29]:


table=pd.crosstab(df['CONSIDERING_CHANGE_OF_PLAN'],df['LEAVE'])
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')


# In[30]:


table=pd.crosstab(df['COLLEGE'],df['LEAVE'])
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')


# In[31]:


table=pd.crosstab(df['REPORTED_USAGE_LEVEL'],df['LEAVE'])
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')


# In[32]:


table=pd.crosstab(df['REPORTED_SATISFACTION'],df['LEAVE'])
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')


# # Manipulating data for training model and Feature Selection

# In[33]:


from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn import metrics, datasets, linear_model, model_selection
from scipy.stats import linregress
import seaborn as sns


# In[34]:


cat_vars=['COLLEGE','REPORTED_SATISFACTION', 'REPORTED_USAGE_LEVEL', 'CONSIDERING_CHANGE_OF_PLAN']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    df1=df.join(cat_list)
    df=df1


# In[35]:


df.head()


# In[36]:


df.drop(df.columns[[0,8,9,10]], axis=1, inplace=True) #drop categorical data
df.columns.values


# In[37]:


#25 columns
df.columns.shape


# In[38]:


df.head()


# In[39]:


df_vars=df.columns.values.tolist()
y=['LEAVE']
X=[i for i in df_vars if i not in y]


# The Recursive Feature Elimination (RFE) works by recursively removing variables and building a model on those variables that remain. It uses the model accuracy to identify which variables (and combination of variables) contribute the most to predicting the target attribute.
# 
# 
# 'OVER_15MINS_CALLS_PER_MONTH', 
# 'COLLEGE_one',
# 'COLLEGE_zero',
# 'REPORTED_SATISFACTION_avg',
# 'REPORTED_SATISFACTION_sat',
# 'REPORTED_SATISFACTION_very_sat',
# 'REPORTED_SATISFACTION_very_unsat',
# 'REPORTED_USAGE_LEVEL_avg',
# 'REPORTED_USAGE_LEVEL_high',
# 'REPORTED_USAGE_LEVEL_little',
# 'REPORTED_USAGE_LEVEL_very_high',
# 'CONSIDERING_CHANGE_OF_PLAN_actively_looking_into_it',
# 'CONSIDERING_CHANGE_OF_PLAN_considering',
# 'CONSIDERING_CHANGE_OF_PLAN_never_thought',
# 'CONSIDERING_CHANGE_OF_PLAN_no'
# 
# 
# 
# i agree with these ones!
# 'OVERAGE', 'LEFTOVER', 
# but it really thinks these are important:
# 'OVER_15MINS_CALLS_PER_MONTH', 'AVERAGE_CALL_DURATION'

# In[40]:


#Standardization##########
#from sklearn import preprocessing

#scaler = preprocessing.MinMaxScaler()
#X_train_scale = scaler.fit_transform(df[X])


# In[41]:


lrmodel = LogisticRegression()
lrfe = RFE(lrmodel, 10) #pick number of columns you want
lrfe = lrfe.fit(df[X], df[y])
print(lrfe.support_)
print(lrfe.ranking_)


# In[42]:


#### Features for LR
lrfeatures = [
 'COLLEGE_one',
 'COLLEGE_zero',
 'REPORTED_SATISFACTION_avg',
 'REPORTED_SATISFACTION_sat',
 'REPORTED_SATISFACTION_unsat',

 'REPORTED_USAGE_LEVEL_high',

 'CONSIDERING_CHANGE_OF_PLAN_actively_looking_into_it',
 'CONSIDERING_CHANGE_OF_PLAN_considering',
 'CONSIDERING_CHANGE_OF_PLAN_never_thought',
 'CONSIDERING_CHANGE_OF_PLAN_no'
]


# In[43]:


## for Random Forest
rfmodel = RandomForestClassifier()
rfrfe = RFE(rfmodel, 5) #pick number of columns you want#########################
rfrfe = rfrfe.fit(df[X], df[y])
print(rfrfe.support_)
print(rfrfe.ranking_)


# ### features for RT
# rffeatures = ['INCOME',
#  'OVERAGE',
#  'LEFTOVER',
#  'HOUSE',
#  'HANDSET_PRICE',
#  'OVER_15MINS_CALLS_PER_MONTH',
#  'AVERAGE_CALL_DURATION',
#  'COLLEGE_one',
#  'COLLEGE_zero', #########
#  'REPORTED_SATISFACTION_very_unsat',
#  'CONSIDERING_CHANGE_OF_PLAN_actively_looking_into_it',#######
#  'CONSIDERING_CHANGE_OF_PLAN_considering'
# ]

# # Features for RT*****

# ###### KEEP THIS, its 67.2
# 
# rffeatures = ['INCOME',
#  'OVERAGE',
#  'LEFTOVER',
#  'HOUSE',
#  'HANDSET_PRICE',
#  'OVER_15MINS_CALLS_PER_MONTH',
#  'AVERAGE_CALL_DURATION',
#  'COLLEGE_one',
#  'REPORTED_SATISFACTION_very_unsat',
#  'CONSIDERING_CHANGE_OF_PLAN_considering'
# ]

# ######X features important
# rffeatures = ['INCOME',
#  'OVERAGE',
#  'LEFTOVER',
#  'HOUSE',
#  'HANDSET_PRICE',
#  'OVER_15MINS_CALLS_PER_MONTH',
#  'AVERAGE_CALL_DURATION',
#  'COLLEGE_one',
#  'COLLEGE_zero',
#  'REPORTED_SATISFACTION_avg',
#  'REPORTED_SATISFACTION_unsat',
# ]

# In[44]:


rffeatures = ['INCOME',
 'OVERAGE',
 'LEFTOVER',
 'HOUSE',
 'HANDSET_PRICE']


# 67.somethin'
# rffeatures = ['INCOME',
#  'OVERAGE',
#  'LEFTOVER',
#  'HOUSE',
#  'HANDSET_PRICE',
#  'OVER_15MINS_CALLS_PER_MONTH',
#  'AVERAGE_CALL_DURATION', 
#   ###college_one
#  'REPORTED_SATISFACTION_very_unsat', 
#  'REPORTED_USAGE_LEVEL_little',  ####          
#  'CONSIDERING_CHANGE_OF_PLAN_considering']              

# ###rffeatures important #### 67.3! :D
# rffeatures = ['INCOME',
#  'OVERAGE',
#  'LEFTOVER',
#  'HOUSE',
#  'HANDSET_PRICE',
#  'OVER_15MINS_CALLS_PER_MONTH',
#  'AVERAGE_CALL_DURATION',
#  'COLLEGE_one',
#  'COLLEGE_zero',
#  'CONSIDERING_CHANGE_OF_PLAN_actively_looking_into_it',
#  'CONSIDERING_CHANGE_OF_PLAN_considering',
#  'REPORTED_SATISFACTION_very_unsat'] 

# In[45]:


#rffeatures = X
#rffeatures


# In[46]:


X


# In[47]:


## for SVC
#svcmodel = SVC()
#svcrfe = RFE(svcmodel, 15) #pick number of columns you want
#svcrfe = svcrfe.fit(df[X], df[y])
#print(svcrfe.support_)
#print(svcrfe.ranking_)


# In[48]:


## for decision tree
dtmodel = DecisionTreeClassifier()
dtrfe = RFE(dtmodel, 10) #pick number of columns you want
dtrfe = dtrfe.fit(df[X], df[y])
print(dtrfe.support_)
print(dtrfe.ranking_)


# In[49]:


### decision tree features
dtfeatures = ['INCOME',
 'OVERAGE',
 'LEFTOVER',
 'HOUSE',
 'HANDSET_PRICE',
 'OVER_15MINS_CALLS_PER_MONTH',
 'AVERAGE_CALL_DURATION',
 'COLLEGE_one',

 'REPORTED_USAGE_LEVEL_little',
              
 'CONSIDERING_CHANGE_OF_PLAN_considering'
]


# In[50]:


#### without changing the categorical data ######
test = pd.read_csv(filename, header = 0, delimiter = ',')
test.drop(test.columns[[0,8,9,10]], axis=1, inplace=True) #drop categorical data
test.columns.values


# In[51]:


test_vars=test.columns.values.tolist()
testy=['LEAVE']
testX=[i for i in test_vars if i not in testy]


# In[52]:


testX


# In[53]:


## Logistic regression feature selection
lrfe = RFE(lrmodel, 4) #pick number of columns you want
lrfe = lrfe.fit(test[testX], test[testy])
print(lrfe.support_)
print(lrfe.ranking_)


# In[54]:


lrtestfeatures = ['OVERAGE',
 'LEFTOVER',
 'OVER_15MINS_CALLS_PER_MONTH',
 'AVERAGE_CALL_DURATION']


# In[55]:


## for Random Forest
rfrfe = RFE(rfmodel, 4) #pick number of columns you want
rfrfe = rfrfe.fit(test[testX], test[testy])
print(rfrfe.support_)
print(rfrfe.ranking_)


# In[56]:


rftestfeatures = ['INCOME',
 'OVERAGE',
 'HOUSE',
 'HANDSET_PRICE',
]


# In[57]:


## for decision tree
dtrfe = RFE(dtmodel, 4) #pick number of columns you want
dtrfe = dtrfe.fit(test[testX], test[testy])
print(dtrfe.support_)
print(dtrfe.ranking_)


# In[58]:


dttestfeatures = ['INCOME',
 'OVERAGE',
 'HOUSE',
 'HANDSET_PRICE',
]


# In[59]:


#test_vars=test.columns.values.tolist()
#yt=['LEAVE']
#Xt=[i for i in test_vars if i not in yt]

#testmodel = LogisticRegression()
#rfe = RFE(testmodel, 4) #pick number of columns you want, this tests which cols might be most important
#rfe = rfe.fit(test[Xt], test[yt])
#print(rfe.support_)
#print(rfe.ranking_)


# In[60]:


#Xt
#Xtest


# # Logistic Regression

# In[61]:


from sklearn.model_selection import train_test_split
y=df['LEAVE']
lr_X=df[lrfeatures]
lr_testX=df[lrtestfeatures]

#for manipulated features
lr_X_train, lr_X_test, lr_y_train, lr_y_test = train_test_split(lr_X, y, test_size=0.3, random_state=0)
lr = LogisticRegression()
lr.fit(lr_X_train, lr_y_train)

#for unchanged features - categoricals
lr_Xt_train, lr_Xt_test, lr_yt_train, lr_yt_test = train_test_split(lr_testX, y, test_size=0.3, random_state=0)
lrtest = LogisticRegression()
lrtest.fit(lr_Xt_train, lr_yt_train)


# In[62]:


#manipulated features stats
from sklearn.metrics import mean_squared_error, accuracy_score, r2_score
lr_y_pred1 = lr.predict(lr_X_test)
lr_lin_mse1 = mean_squared_error(lr_y_pred1, lr_y_test)
lr_lin_rmse1 = np.sqrt(lr_lin_mse1)

print('Logistic regression accuracy: {:.3f}'.format(accuracy_score(lr_y_test, lr.predict(lr_X_test))))
print('Coefficients: \n', lr.coef_)
print("Mean squared error: %.2f"% lr_lin_rmse1) #how off the prediction is
print('Variance/R^2 score: %.4f' % r2_score(lr_y_test, lr_y_pred1)) #closer to 1 = less error


# In[63]:


#unmanipulated features stats
lr_y_pred2 = lrtest.predict(lr_Xt_test)
lr_lin_mse2 = mean_squared_error(lr_y_pred2, lr_yt_test)
lr_lin_rmse2 = np.sqrt(lr_lin_mse2)

print('Logistic regression accuracy: {:.3f}'.format(accuracy_score(lr_yt_test, lrtest.predict(lr_Xt_test))))
print('Coefficients: \n', lrtest.coef_)
print("Mean squared error: %.2f"% lr_lin_rmse2) #how off the prediction is
print('Variance/R^2 score: %.4f' % r2_score(lr_yt_test, lr_y_pred2)) #closer to 1 = less error


# # Random Forest

# In[64]:


#y=df['LEAVE']
rf_X=df[rffeatures]
rf_testX=df[rftestfeatures]

## TO IMPROVE MODEL WE CAN CHANGE TEST SIZE, RANDOM_STATE, PARAMETERS IN THE CLASSIFIER MODEL
#for manipulated features
rf_X_train, rf_X_test, rf_y_train, rf_y_test = train_test_split(rf_X, y, test_size=0.3, random_state=0)
rf = RandomForestClassifier(max_features= 'auto', n_estimators= 2000, random_state=100, min_samples_leaf = 55)
rf.fit(rf_X_train, rf_y_train)

#for unchanged features - categoricals
rf_Xt_train, rf_Xt_test, rf_yt_train, rf_yt_test = train_test_split(rf_testX, y, test_size=0.3, random_state=0)
rftest = RandomForestClassifier()
rftest.fit(rf_Xt_train, rf_yt_train)


# In[65]:


#try to do better than 67.6 !!! :D 69.8, 70.6.!!!!
#for manipulated features
print('Random Forest Accuracy: {:.3f}'.format(accuracy_score(rf_y_test, rf.predict(rf_X_test))))


# In[66]:


#for unchanged features - categoricals
print('Random Forest Accuracy: {:.3f}'.format(accuracy_score(rf_yt_test, rftest.predict(rf_Xt_test))))


# # Support Vector Machine

# In[67]:


#y=df['LEAVE']
sv_X=df[X]
sv_testX=df[testX]

#for manipulated features
sv_X_train, sv_X_test, sv_y_train, sv_y_test = train_test_split(sv_X, y, test_size=0.3, random_state=0)
svc = SVC()
svc.fit(sv_X_train, sv_y_train)


# In[68]:


print('Support vector machine accuracy: {:.3f}'.format(accuracy_score(sv_y_test, svc.predict(sv_X_test))))


# In[69]:


#svc = SVC()
#svc.fit(Xt_train, yt_train)
## with test, Support vector machine accuracy: 0.507
#print('Support vector machine accuracy: {:.3f}'.format(accuracy_score(yt_test, svc.predict(Xt_test))))


# Cross validation attempts to avoid overfitting while still producing a prediction for each observation dataset. We are using 10-fold Cross-Validation to train our Random Forest model.

# # Decision Tree

# In[70]:


#y=df['LEAVE']
dt_X=df[dtfeatures]
dt_testX=df[dttestfeatures]

#for manipulated features
dt_X_train, dt_X_test, dt_y_train, dt_y_test = train_test_split(dt_X, y, test_size=0.3, random_state=0)
dtClf = DecisionTreeClassifier()
dtClf.fit(dt_X_train, dt_y_train)
dt_y_pred = dtClf.predict(dt_X_test)

#for unchanged features - categoricals
dt_Xt_train, dt_Xt_test, dt_yt_train, dt_yt_test = train_test_split(dt_testX, y, test_size=0.3, random_state=0)
dttestClf = DecisionTreeClassifier()
dttestClf.fit(dt_Xt_train, dt_yt_train)
dt_yt_pred = dttestClf.predict(dt_Xt_test)


# In[71]:


print('Manipulated Decision Tree Accuracy: {:.3f}'.format(accuracy_score(dt_y_test, dtClf.predict(dt_X_test))))
print('Unmanipulated col set Decision Tree Accuracy: {:.3f}'.format(accuracy_score(dt_yt_test, dttestClf.predict(dt_Xt_test))))


# # Neural Network and Standardization

# In[72]:


# Convert string to number
import pandas as pd
import numpy as np

def ConvertStrToNumColumn(col):
    # print(col)
    if( type(col[0]) == str):
        strDic = {}
        xCategory = 0
        for i, row in enumerate(col):
            if row in strDic.keys():
                col[i] = strDic[row]
            else:
                col[i] = xCategory;
                strDic[row] = xCategory
                xCategory += 1;

    return col

def ConvertStrToNumMatrix(readFileName, writeFileName):
    targetMatrix = pd.read_csv(readFileName).values

    for colNum in range(targetMatrix.shape[1]):
        targetMatrix[:, colNum] = ConvertStrToNumColumn(targetMatrix[:, colNum])

    np.savetxt(writeFileName, targetMatrix)

ConvertStrToNumMatrix('train.csv', 'trainNum.txt')
ConvertStrToNumMatrix('test.csv', 'testNum.txt')

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier

trainData = np.loadtxt('trainNum.txt')
# testData = np.loadtxt('testNum.txt')

np.random.shuffle(trainData)

X_train = trainData[:, :-1]
y_train = trainData[:, -1]; y_train = y_train.astype(float)

from sklearn.neural_network import MLPClassifier
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.1)

#Standardization##########
min_max_scaler = preprocessing.MinMaxScaler()
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.fit_transform(X_test)
##########################
numFetures = X_train.shape[1]
neuralClf = MLPClassifier(hidden_layer_sizes=(numFetures, numFetures, numFetures
            , numFetures), max_iter=500)
neuralClf.fit(X_train, y_train)
score = neuralClf.score(X_test, y_test)
print(score)


# # Cross Validation

# In[73]:


#LR unmanipulated
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, lr_Xt_train, lr_yt_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


# In[74]:


#rf manipulated, 67.5!
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = RandomForestClassifier()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, rf_X_train, rf_y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


# In[75]:


#dt manipulated
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = DecisionTreeClassifier()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, dt_X_train, dt_y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))


# # Confusion Matrices

# In[76]:


##RANDOM FOREST
from sklearn.metrics import classification_report
print(classification_report(rf_y_test, rf.predict(rf_X_test)))


# In[77]:


y_pred = rf.predict(rf_X_test)
forest_cm = metrics.confusion_matrix(y_pred, rf_y_test, [1,0])
sns.heatmap(forest_cm, annot=True, fmt='.2f',xticklabels = ["Left", "Stayed"] , yticklabels = ["Left", "Stayed"] )
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.title('Random Forest')
plt.savefig('random_forest')


# In[78]:


## LOGISTIC REGRESSION
print(classification_report(lr_yt_test, lrtest.predict(lr_Xt_test)))


# In[79]:


logreg_y_pred = lrtest.predict(lr_Xt_test)
logreg_cm = metrics.confusion_matrix(logreg_y_pred, lr_yt_test, [1,0])
sns.heatmap(logreg_cm, annot=True, fmt='.2f',xticklabels = ["Left", "Stayed"] , yticklabels = ["Left", "Stayed"] )
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.title('Logistic Regression')
plt.savefig('logistic_regression')


# In[80]:


dt_y_pred = dtClf.predict(dt_X_test)
dt_cm = metrics.confusion_matrix(dt_y_pred, dt_y_test, [1,0])
sns.heatmap(dt_cm, annot=True, fmt='.2f',xticklabels = ["Left", "Stayed"] , yticklabels = ["Left", "Stayed"] )
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.title('Decision Tree')
plt.savefig('Decision_Tree')


# In[81]:


## Support Vector Machine
#print(classification_report(sv_y_test, svc.predict(df[X])))


# In[82]:


#svc_y_pred = svc.predict(Xt_test)
#svc_cm = metrics.confusion_matrix(svc_y_pred, yt_test, [1,0])
#sns.heatmap(svc_cm, annot=True, fmt='.2f',xticklabels = ["Left", "Stayed"] , yticklabels = ["Left", "Stayed"] )
#plt.ylabel('True class')
#plt.xlabel('Predicted class')
#plt.title('Support Vector Machine')
#plt.savefig('support_vector_machine')


# # ROC Curve

# In[83]:


from sklearn.metrics import roc_auc_score, roc_curve
#lr test, dt manipulated, rf manipulated
logit_roc_auc = roc_auc_score(lr_yt_test, lrtest.predict(lr_Xt_test))
fpr, tpr, thresholds = roc_curve(lr_yt_test, lrtest.predict_proba(lr_Xt_test)[:,1])

rf_roc_auc = roc_auc_score(rf_y_test, rf.predict(rf_X_test))
rf_fpr, rf_tpr, rf_thresholds = roc_curve(rf_y_test, rf.predict_proba(rf_X_test)[:,1])

dt_roc_auc = roc_auc_score(dt_y_test, dtClf.predict(dt_X_test))
dt_fpr, dt_tpr, dt_thresholds = roc_curve(dt_y_test, dtClf.predict_proba(dt_X_test)[:,1])

plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot(rf_fpr, rf_tpr, label='Random Forest (area = %0.2f)' % rf_roc_auc)
plt.plot(dt_fpr, dt_tpr, label='Decision Tree (area = %0.2f)' % dt_roc_auc)

plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for LR and RF')
plt.legend(loc="lower right")
plt.savefig('ROC')
plt.show()


# # Random Forest Feature Importance, can help us choose features

# In[84]:


### Random Forest Model Feature Importance
feature_labels = np.array(rffeatures)
importance = rf.feature_importances_
feature_indexes_by_importance = importance.argsort()
for index in feature_indexes_by_importance:
    print('{}-{:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))


# X features important
# COLLEGE_zero-0.98%
# COLLEGE_one-1.12%
# REPORTED_SATISFACTION_unsat-1.61%
# REPORTED_SATISFACTION_sat-1.67%
# REPORTED_SATISFACTION_avg-1.87%
# AVERAGE_CALL_DURATION-6.86%
# OVER_15MINS_CALLS_PER_MONTH-8.87%
# LEFTOVER-10.04%
# OVERAGE-13.25%
# INCOME-15.17%
# HANDSET_PRICE-15.34%
# HOUSE-23.21%
# 
# rffeatures important
# COLLEGE_zero-0.98%
# COLLEGE_one-1.12%
# CONSIDERING_CHANGE_OF_PLAN_considering-1.61%
# CONSIDERING_CHANGE_OF_PLAN_actively_looking_into_it-1.67%
# REPORTED_SATISFACTION_very_unsat-1.87%
# AVERAGE_CALL_DURATION-6.86%
# OVER_15MINS_CALLS_PER_MONTH-8.87%
# LEFTOVER-10.04%
# OVERAGE-13.25%
# INCOME-15.17%
# HANDSET_PRICE-15.34%
# HOUSE-23.21%

# In[85]:


X


# In[86]:


rffeatures


# # Predicting testing data

# In[87]:


filename2 = 'test.csv'
pred = pd.read_csv(filename2, header = 0, delimiter = ',')
pred.columns.values


# In[88]:


pred.shape


# In[89]:


col_vars=['COLLEGE','REPORTED_SATISFACTION', 'REPORTED_USAGE_LEVEL', 'CONSIDERING_CHANGE_OF_PLAN']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(pred[var], prefix=var)
    pred1=pred.join(cat_list)
    pred=pred1


# In[90]:


pred.head()


# In[91]:


pred.drop(pred.columns[[0,8,9,10]], axis=1, inplace=True) #drop categorical data
pred.columns.values  


# In[92]:


#print(pred)
rffeatures


# In[93]:


testcol=rffeatures
predX=pred[testcol]

#predX


# In[94]:


newdf = pd.DataFrame(columns=['LEAVE'])

for x in newdf:
    #newdf['ID'] = newdf.index
    #newdf['LEAVE'] = logregtest.predict(predX)   #logregtest expects 3 samples, logreg expects 14
    newdf['LEAVE'] = rf.predict(predX)


# In[95]:


#print(newdf)


# In[96]:


newdf.head()


# In[97]:


#newdf.to_csv('RFoutputnewest.csv')


# Notes:
# 
# - I want to know the accuracy when all columns are included
# - To see accuracy of LR with testing where the extra categoricals are included, must
#     mess with the shape of the output DF
#     

# In[98]:


newdf.shape


# In[ ]:




