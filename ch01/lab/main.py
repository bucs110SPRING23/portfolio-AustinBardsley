import random

#Part A
weeks = 16
print("Weeks:",weeks,type(weeks))
classes = 5
print("Classes:",classes,type(classes))
tuition = 6000
print("Tuition:",tuition,type(tuition))
cost_per_week = ((tuition/classes)/weeks)
print ("Cost Per Week:",cost_per_week,type(cost_per_week))
classes_per_week = 3
print("Classes Per Week:",classes_per_week,type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print("Cost Per Class:",cost_per_class,type(cost_per_class))

#Part B
mylist = [2.6,"yesterday",5,"purple","800"]
selection = random.choice(mylist)
print(selection)