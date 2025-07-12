import matplotlib.pyplot as plt

x = [1,2,3,4]       # Horizontal axis
y = [10,20,15,25]   # Vertical values

plt.plot(x, y)       # Command to create a line graph
plt.bar(x, y)       # Command to create a bar graph

plt.show()          # Command to display the created plot

# Testing Labels

a=['Mon', 'Tues', 'Wed', 'Thur', 'Fri'] # x-axis
b=[10, 15, 7, 21, 13]                   # y-axis

plt.plot(a,b)

plt.title("Sample data for Week 1 Sales")

plt.xlabel('Day of the Week')
plt.ylabel('Sales per Day')

plt.show