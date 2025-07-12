# SCATTERPLOTS

import matplotlib.pyplot as plt

#plt.scatter(x,y, color ='color_name', marker = 'marker_style', label = 'label_name')

hours_studied = [1,2,3,4,5,6,7,8,]
exam_scores = [50,55,60,65,70,75,80,85]

#Scatterplot
plt.scatter(hours_studied, exam_scores, color = 'red', marker = '^', label = 'Student data')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Correlation btw hours studied and marks scored')
plt.legend()
plt.grid(True)

plt.show()
