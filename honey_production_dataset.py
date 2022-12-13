# -*- coding: utf-8 -*-
"""MihikaRaj_111_honey production dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thabEgnBl6XSsv7OhFHmJkWOEUk2fvoL
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv(r"/content/honeyproduction.csv")

"""# **Q1:Explore quantitative variables and qualitative variables in the data set**"""

df.info()

"""# **Q2**:Find the relationship between numerical variables using pair plots and correlation plots. Explain what you infer from these plots. """

x=sns.heatmap(df.corr(),annot=True)

"""# The numcol increases with totalprod"""

sns.pairplot(df)

"""# **Q3:Look at the overall trend of honey production in the US over the years**"""

plt.figure(figsize=(8,5))
plt.bar(x=df['year'],height=df['totalprod'],data=df,color='deeppink')
plt.title('Totalproduction of honey in USA over years',fontsize=20,color='green')
plt.xlabel('year',fontsize=15,color='green')
plt.ylabel('totalprod',fontsize=15,color='red')
plt.show()

"""# The production of honey is highest in 2010 in US.

# **Q4:Are there any patterns that can be observed between total honey production and value of production every year? How has the value of production which in some sense could be tied to demand,changed every year?**
"""

plt.figure(figsize=(8,8))
plt.scatter(df['year'],df['totalprod'],color='black',marker='s')
plt.scatter(df['year'],df['prodvalue'],color='pink',marker='^')
plt.title('Total production of honey over the years',fontsize=20,color='indigo')
plt.xlabel('year',fontsize=15,color='blue')
plt.ylabel('Quatity',fontsize=15,color='red')
plt.show()

"""# *The total honey production inceases with production value.
# *There are cases where production value overshoots the total production in year 2010. 
# *Also,there are cases whereby total production is ahead of production is ahead of production quantity like in year 1998. 
"""



"""# **Q5:Observe the variation in the number of colonies over the years**"""

plt.figure(figsize=(8,5))
plt.title('Variatio in the number of colonies over the years  ',fontsize=20,color='brown')
plt.bar(x=df['year'],height=df['numcol'],data=df,color='purple')
plt.xlabel('year',fontsize=15,color='green')
plt.ylabel('numcol',fontsize=15,color='purple')

"""# **Q6:Analyse the variation of yield per Colony over the years and the production trend at state level and brief out what you observed.**"""

plt.figure(figsize=(9,5))
plt.title('Variatio of yield per colony over the years ',fontsize=20,color='green')
plt.bar(x = df['year'],height=df['yieldpercol'],data=df,color='green')
plt.xlabel('year',fontsize=15,color='blue')
plt.ylabel('yieldpercol',fontsize=15,color='red')

"""# The most prominent Honey production states of US are ND,CA,SD and the SC state of US has the lowest production of honey"""

plt.figure(figsize=(11,8))
plt.title('production value of honey of states',fontsize=20,color='purple')
plt.bar(x = df['state'],height=df['totalprod'],color='red')
plt.xlabel('state',fontsize=15,color='green')
plt.ylabel('totalprod',fontsize=15,color='pink')

"""# It is observed that the variation of yield per Colony remains in the range of 80-120 the trend indicates that the average value of yield per colony was initially high but with the passage of years it declined"""

plt.figure(figsize=(10,5))
plt.title('production value of honey over the years',fontsize=20,color='deeppink')
plt.bar(x=df['year'],height=df['prodvalue'],color='green')
plt.xlabel('year',fontsize=15,color='blue')
plt.ylabel('prodvalue',fontsize=15,color='red')

"""# **Q7:Analyse what effect the declining production trend has had on the value of production**"""

plt.figure(figsize=(11,6))
sns.pointplot(x='year',y='prodvalue',data=df,ci=None,color='orange')
plt.title('Honey production trend',fontsize=20,color='indigo')
plt.xlabel('year',fontsize=15,color='blue')
plt.ylabel('total production',fontsize=15,color='red')
plt.show()

"""# *The total value of production has increased overtime the increasing demand has also add to the value of honey.*"""