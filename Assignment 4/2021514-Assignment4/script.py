import matplotlib.pyplot as plt

# Cwnd values extracted from the output
cwnd_values = [1, 19.8 ,       
11.3 ,       
4.24 ,       
9.90 ,       
11.3 ,       
11.3 ,       
8.48 ,       
8.48 ,       
8.48 ,       
7.07 ,       
11.3 ,       
12.7 ,       
9.90 ,       
8.48 ,       
7.07 ,       
7.07 ,       
8.48 ,       
7.07 ,       
9.90 ,       
8.48 ,       
5.66 ,       
8.48 ,       
8.48 ,       
5.66 ,       
11.3 ,       
8.48 ,       
7.07 ,       
9.90 ,       
11.3 ,       
7.07 ,       
11.3 ,       
11.3 ,       
5.66 ,       
4.24 ,       
7.07 ,       
7.07 ,       
11.3 ,       
7.07 ,       
5.66 ,       
11.3 ,       
8.48 ,       
11.3 ,       
11.3 ,       
8.48 ,       
11.3 ,       
9.90 ,       
11.3 ,       
7.07 ,       
9.90 ,       
7.07 ,       
5.66 ,       
5.66 ,       
5.66 ,       
7.07 ,       
9.90 ,       
7.07 ,       
9.90 ,       
11.3 ,       
11.3 ,       
8.48]

print(len(cwnd_values))
time_intervals = range(len(cwnd_values))

# Plot cwnd values against time
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, cwnd_values, marker='o', linestyle='-', color='b')
plt.title('Congestion Window (cwnd) vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Congestion Window (cwnd in KBytes)')
plt.tight_layout()

plt.show()
