# To  compare 2 different datasets using Scatter plot
# For comparing 2  groups

import matplotlib.pyplot as plt

plt.scatter([1,2,3],[50,60,70], color = 'blue', marker = 'o', label = 'Class A')
plt.scatter([1,2,3],[60,98,80], color = 'green', marker = '^', label = 'Class B')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Comparison of two classes')
plt.legend()
plt.grid(True)

plt.show()
