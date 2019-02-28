import pandas as pd
from collections import Counter

df = pd.read_excel('ptsc.xlsx')
HNI = ['HNIP04801','HNIP31102','HNIP40201','HNIP46602','HNIP20201']
df1 = pd.DataFrame()
for i in HNI:
    df1 = df1.append(df[df['Tiêu đề'].str.contains('HNIP04801', regex=True)])

count = Counter(df1['Nguyên nhân chi tiết'])
print (count)