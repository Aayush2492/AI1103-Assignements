import math
from scipy.stats import binom
import matplotlib.pyplot as plt
import array as arr
import numpy as np

p=0.1
#p is the probablity of finding a defective bulb or the probability of success

q=0.9
#q is the probablity of finding a working bulb or the probability of failure 

n=5
#n is the number of defective bulbs

r_values = np.arange(n+1)
#Contains the possible values of r i.e. possible number of defective bulbs

binom_dist = [binom.pmf(r, n, p) for r in r_values ] 
#Array containing the probability distribution for each value of r

print("Theoretical probability of finding 0 defective bulbs : ",binom_dist[0])

sample_size=100000

binom_sim = binom.rvs(n,p,size=sample_size)
#Array containing the simulated probability distribution for each value of r 

count=[0,0,0,0,0,0]
#Creating list for count
prob=[0,0,0,0,0,0]
#Creating list for probability

for i in range(sample_size):
  if binom_sim[i] == 0:
    count[0]+=1
  elif binom_sim[i] == 1:
    count[1]+=1
  elif binom_sim[i] == 2:
    count[2]+=1
  elif binom_sim[i] == 3:
    count[3]+=1
  elif binom_sim[i] == 4:
    count[4]+=1
  elif binom_sim[i] == 5:
    count[5]+=1

for i in range(n+1):
  prob[i]=count[i]/sample_size

print("Simulated probability of finding 0 defective bulbs : ",prob[0])

w=0.4
#width

r2_values = [i+w for i in r_values]

plt.bar(r_values, binom_dist,w,label="Theoretical") 
plt.bar(r2_values, prob,w,label="Simulated") 
plt.title("Plot for the distribution")
plt.xlabel("Number of defective bulb/s")
plt.ylabel("Probability")
plt.xticks(r_values+w/2,r_values)
plt.legend()
plt.show()

print("Note that the simulated and theoretical values are approximately equal")
