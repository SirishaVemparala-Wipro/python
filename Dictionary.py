# Define a dictionary with names and ages
dict={"alice":25,"james":13,"charlie": 87,"Kim":14}

# Find the name of the oldest person
oldest_person=max(dict,key=dict.get)

print("oldest person: ",oldest_person)