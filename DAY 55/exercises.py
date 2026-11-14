#exercise 1
import random
experiments=100
even=0
for i in range(experiments):
    result=random.randint(1,6)
    if result%2==0:
        even+=1
probability=even/experiments
print("probability: ",probability)

#exercise 2
success = 0.80
failure = 1 - success
print("Probability of success:", success)
print("Probability of failure:", failure)
print("Distribution: Bernoulli")