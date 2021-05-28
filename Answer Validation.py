import pandas as pd

df =pd.read_excel('Answers.xlsx',engine='openpyxl')

answers = ['free()','#include','* / % + - =','ZeroHello World','Error: expression syntax','Program prints hii 1 time.','float','Compile error','It is a type name defined in stdio.h','2','6','Opens text file in both reading and appending mode','Runs infinitely without printing anything','return','#define CUBE(X) (X*X*X)','In first statement, 4 specifies an array size, whereas in second statement it specifies a particular element of array','5','Runtime error','1,2,3,4','Infinite loop']

q=[]
for i in range(20):
    q.append('Q'+str(i+1))

m_c=[]
for i in range(20):
    m_c.append('Mark'+str(i+1))

for j in range(20):
    for i, row in df.iterrows():
        ans = answers[j]
        predicted1 = df.loc[i,q[j]]
        if (str(ans) == predicted1):
            s=m_c[j]
            df.loc[i,s] = 1

writer = pd.ExcelWriter('new_book.xlsx')
df.to_excel(writer,'new_sheet')
writer.save()