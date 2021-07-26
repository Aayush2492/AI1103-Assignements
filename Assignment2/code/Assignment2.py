import math
from scipy.stats import binom
import matplotlib.pyplot as plt
import array as arr
import numpy as np
import random

#r_values = [1,2,3,4,5]
r_values = np.array([1, 2, 3, 4, 5])

theo_prob = [1.0/9.0,2.0/9.0,1.0/3.0,2.0/9.0,1.0/9.0]

data = [1,2,2,3,3,3,3,4,4,5]
#To make the occurence of each value equiprobable, this list contains each value (it's probability*9) times

sample_size=100000

count=[0,0,0,0,0,0]
#Creating list for count

sim_prob=[0,0,0,0,0]
#Creating list for simulated probability

for i in range(sample_size):
  rand_int = random.randint(0, 9)
  #0 and 9 are first and last indices for the list data
  if (rand_int == 0):
    count[0]+=1
  elif (rand_int == 1 or rand_int == 2):
    count[1]+=1
  elif (rand_int == 3 or rand_int == 4 or rand_int == 5 or rand_int == 6):
    count[2]+=1
  elif (rand_int == 7 or rand_int == 8):
    count[3]+=1
  elif rand_int == 9:
    count[4]+=1

for i in range(5):
  sim_prob[i]=count[i]/sample_size

mean=0
for i in range(5):
  mean = mean + r_values[i]*theo_prob[i]

variance=0
for i in range(5):
  variance = variance + ((r_values[i]-mean)**2)*theo_prob[i]
   
print("Mean of data : ",mean)
print("Variance of data : ",variance)
print("\n")
print("Theoretical probability for x=1",theo_prob[0])
print("Theoretical probability for x=2",theo_prob[1])
print("Theoretical probability for x=3",theo_prob[2])
print("Theoretical probability for x=4",theo_prob[3])
print("Theoretical probability for x=5",theo_prob[4])
print("\n")
print("Simulated probability for x=1",sim_prob[0])
print("Simulated probability for x=2",sim_prob[1])
print("Simulated probability for x=3",sim_prob[2])
print("Simulated probability for x=4",sim_prob[3])
print("Simulated probability for x=5",sim_prob[4])
print("\n")
print("Note that the simulated and theoretical values are approximately equal")

w=0.4
#width

r2_values = [i+w for i in r_values]
#r2_values = np.array([1.4, 2.4, 3.4, 4.4, 5.4])

plt.stem(r_values, theo_prob,'b', markerfmt='bo',label="Theoretical") 
plt.stem(r2_values,sim_prob,'g', markerfmt='go',label="Simulated") 
plt.title("Plot for the distribution")
plt.xlabel("Value of k")
plt.ylabel("P(x=k)")
plt.xticks(r_values+w/2,r_values)
#Self note : for xticks r_values should be in array form not list
plt.legend()
plt.show()
