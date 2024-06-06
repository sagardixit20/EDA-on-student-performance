#EDA project on students performance
#importing required libraries
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

#load the CSV file and read it
stu = pd.read_csv(r"C:\Users\ASUS\Documents\datasets for visulaization\StudentsPerformance.csv")
print(stu.head())
#print(stu.shape)

#get columns information
#for col in stu.columns:
#    print(col)

#extract gender from the data set
gen = stu['gender'].value_counts()
#print(gen)
ms = stu['math score'].value_counts()
#print(ms)
#making bar plot for gender
plt.figure(figsize = (5,5))
plt.bar(list(stu['gender'].value_counts()[0:5].keys()),list(stu['gender'].value_counts()[0:5]),color='g')
#print(plt.show())

#extracting level of education from dataset
loe = stu['parental level of education'].value_counts()
#print(loe)
#making a pie chart for parental level of education
plt.figure(figsize = (6,7))
plt.pie(list(stu['parental level of education'].value_counts()),labels=list(stu['parental level of education'].value_counts().keys()),autopct='%0.1f%%')
plt.title('---Parental education---')
#print(plt.show())

#extracting lunch from dataset
lnh = stu['lunch'].value_counts()
#print(lnh)
#making a barplot between the lunch of the parents
plt.figure(figsize=(5,5))
plt.barh(list(stu['lunch'].value_counts()[0:5].keys()),list(stu['lunch'].value_counts()[0:5]),color='g')
#print(plt.show())

#barplot between gender and math score
gmc = stu[['gender','math score']]
gmc = gmc.sort_values(by=['math score'],ascending=False)

plt.figure(figsize = (5,5))
plt.bar(list(gmc['gender'][0:5]),list(gmc['math score'][0:5]),color=['green','blue','red','pink','black'])
#print(plt.show())

#making histogram
plt.hist(stu['writing score'],bins=30,color='r')
print(plt.show())

#scatterplot
sns.scatterplot(x="reading score",y="writing score",data=stu)
#print(plt.show())