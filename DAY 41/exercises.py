import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [32, 34, 33, 35, 31]
plt.plot(days, temperature)
plt.xlabel("Day")
plt.ylabel("temperature")
plt.title("weather analysis")
plt.show()