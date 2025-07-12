  # To show the distribution of continuos data by dividing into ranges (bins)

#plt.hist(data, bins = no_of_bins, color="color_name", edgecolor = 'color_name")

# HISTOGRAM

import matplotlib.pyplot as plt

scores = [45, 67, 77, 58, 67, 92, 82,74, 81, 66, 39, 57, 48, 75, 59, 79, 88, 63, 63, 65, 78, 10, 96, 57, 36, 57, 85, 75, 34, 67, 97, 18, 7, 76, 35, 56, 87, 75, 45, 56, 38, 56, 97, 87, 35, 65, 88, 72, 42, 85, 92 ]

plt.hist(scores, bins= 5, color = 'purple', edgecolor = 'black')
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.title("Score Distribution of Students")
plt.show()

# Height of bar = No of students falling within that particular range

