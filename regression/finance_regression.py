# %load finance_regression.py
#!/usr/bin/python

"""
    starter code for the regression mini-project
    
    loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project)

    draws a little scatterplot of the training/testing data

    you fill in the regression code where indicated

"""    


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### your regression goes here!
### please name it reg, so that the plotting code below picks it up and 
### plots it correctly


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(feature_train, target_train)

print reg.coef_
print reg.intercept_

r_squared_score_train = reg.score(feature_train, target_train)
r_squared_score_test = reg.score(feature_test, target_test)
print r_squared_score_train
print r_squared_score_test

#add a hack here
reg.fit(feature_test, target_test)
print reg.coef_