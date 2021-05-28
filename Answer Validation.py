from os import path, rename
import pandas as pd

n=int(input("Enter the count of questions: "))
q=[]
for i in range(n):
    q.append('Q'+str(i+1))

print("change the column names as follows:")
print(q)

path_xslx=input("Enter the path of the Answers excel file: ")
df =pd.read_excel(path_xslx ,engine='openpyxl')
loc=input("Enter the Path of answer's: ")

file=open(loc,'r')
answers=[]

for line in file:
    answers.append(line)

m_c=[]
for i in range(n):
    m_c.append('Mark'+str(i+1))

for j in range(n):
    for i, row in df.iterrows():
        ans = answers[j]
        predicted1 = df.loc[i,q[j]]
        if (str(ans) == predicted1):
            s=m_c[j]
            df.loc[i,s] = 1

writer = pd.ExcelWriter('Validated Book.xlsx')
df.to_excel(writer,'Validated_sheet')
writer.save()