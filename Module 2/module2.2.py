
import pandas as pd

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'D': ['a','b','c','d']})
pd.merge(Df1,Df2)

"""On and How

#Inner
"""

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'C': ['a','b','c','d']})
pd.merge(Df1,Df2, on='A', how='inner', indicator=True)

"""#Outer


"""

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'C': ['a','b','c','d']})
pd.merge(Df1,Df2, on='A', how='outer',indicator=True)

"""#Left"""

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'C': ['a','b','c','d']})
pd.merge(Df1,Df2, on='A', how='left',indicator=True)

"""#Right"""

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,2,3,4], 'C': ['a','b','c','d']})
pd.merge(Df1,Df2, on='A', how='right',indicator=True)

Df1= pd.DataFrame( { 'A': [1,2,3,4], 'B': ['A','B','C','D']})
Df2= pd.DataFrame( { 'A': [1,5,7,3], 'C': ['a','b','c','d']})
pd.merge(Df1,Df2, on='A', how='right')

"""#SUFFIX"""

Df1= pd.DataFrame( { 'A': [1,2,3,4,5], 'B': ['A','B','C','D','E']})
Df2= pd.DataFrame( { 'A': [1,2,3,4,5], 'C': ['a','b','c','d','e']})
pd.merge(Df1,Df2, left_index=True , right_index=True)

"""#SUFFIX"""

Df1= pd.DataFrame( { 'A': [1,2,3,4,5], 'B': ['A','B','C','D','E']})
Df2= pd.DataFrame( { 'A': [1,2,3,4,5], 'B': ['a','b','c','d','e']})
pd.merge(Df1,Df2, left_index=True , right_index=True , suffixes=('_2019', '_2020'))
