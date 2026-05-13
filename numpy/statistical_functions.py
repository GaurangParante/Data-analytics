import numpy as np
import statistics as stats

baked_food = [200,300,150,130,200,280,170,188]

a = np.array(baked_food)
print(np.mean(a)) # Sum of all the values/number of values
print(np.median(a)) # Central value after sorting
print(stats.mode(a)) 
print(np.std(a)) # standard deviation
print(np.var(a)) # variance == standard deviation ** 2


# - 1 represent inversely proportional relationship
# + 1 represent proportional relationship
# 0 means no relationship

tobacco_cunsumption = [30,50,10,30,50,40]
deaths = [100,120,70,100,120,112]
print(np.corrcoef(tobacco_cunsumption,deaths))

price = [300,100,350,150,200]
sales = [10,20,7,17,3]
print(np.corrcoef(price,sales))