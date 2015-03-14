# %load explore_enron_data.py
#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))



print len(enron_data.keys())
print len(enron_data.values()[0].keys())
print enron_data.keys()
import re
name = re.compile("(\w+),[ ](\w+)")
poi_names = []

with open("../final_project/poi_names.txt", "r") as f:
    for line in f:
        m = name.search(line)
        if m is not None: 
            poi_names.append(m.group(1) + " " + m.group(2))

print poi_names 
print len(poi_names)
poi_names_indata = [name for name in enron_data.keys() if enron_data[name]['poi'] == True]
print len(poi_names_indata)
print poi_names_indata
print enron_data["SKILLING JEFFREY K"]['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['PRENTICE JAMES']
print enron_data['COLWELL WESLEY']
print enron_data["SKILLING JEFFREY K"]

quantified_salaries = [ executive['salary'] for executive in enron_data.values() if executive['salary'] != 'NaN']
print len(quantified_salaries)
known_emails = [ executive['email_address'] for executive in enron_data.values() if executive['email_address'] != 'NaN']
print len(known_emails)
known_payments = [ executive['total_payments'] for executive in enron_data.values() if executive['total_payments'] != 'NaN']
print len(known_payments)


known_payments_poi = [ executive for executive in enron_data.keys() if enron_data[executive]['total_payments'] != 'NaN' and executive in poi_names_indata]
print len(known_payments_poi) == len(poi_names_indata)


