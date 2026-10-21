import random
trials = 10000
even_count = 0
for i in range(trials):
    roll = random.randint(1, 6)
    if roll % 2 == 0:
        even_count += 1
probability = even_count / trials
print("Even rolls:", even_count)
print("Estimated probability:", probability)