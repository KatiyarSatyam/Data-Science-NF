import pandas as pd

"""DATA MANIPULATION WITH PANDAS

#-> SERIES

#Type checking
"""

#type checking
l1 = [2,4,6,8,10]
var = pd.Series(l1)
print(var)
print(type(var))

"""#Changing indexing"""

#changing indexing
l1 = [2,4,6,8,10]
var = pd.Series(l1, index = ["a","b","c","d","e"])
print(var)

"""#Changing datatype"""

#changing datatype
l1 = [2,4,6,8,10]
var = pd.Series(l1, dtype = "float")
print(var)

"""#Assigning name to file"""

#assigning name to file
l1 = [2,4,6,8,10]
var = pd.Series(l1, dtype = "float", name = "Pandasfile")
print(var)

"""#Same value at every index"""

#same value at every index
var2 = pd.Series(5, index = [1,2,3,4,5])
print(var2)

"""#Only same index value add"""

#only same index value add
var2 = pd.Series(5, index = [2,7,9,13,15])
var3 = pd.Series(10, index = [1,5,9,11,13])
print(var2+var3)

"""#Converting dictionary to series"""

#converting dictionary to series
mydic = {
    "name" : "A",
    "rollno": 21,
    "age" : 22,
}
var4 = pd.Series(mydic)
print(var4)

"""#Converting list to series"""

#converting list to series
mydic = {
    "name":["A", "B", "C"],
    "rollno": [21, 22, 25],
    "age": [22, 20, 25],
}
var5 = pd.Series(mydic)
print(var5)

"""#Sum of series element

"""

myseries= [ 2,3,4,5,6]
v =pd.Series(myseries)
sum = v.sum()
print("Sum of Serires :", sum)

"""#Mean of series element"""

myseries= [ 2,3,4,5,6]
v =pd.Series(myseries)
mean = v.mean()
print("Mean of Serires :", mean)

"""#Max of series element"""

myseries= [ 2,3,4,5,6]
v =pd.Series(myseries)
max = v.max()
print("Max of Serires :", max)

"""#Min of series element"""

myseries= [ 2,3,4,5,6]
v =pd.Series(myseries)
min = v.max()
print("Min of Serires :", min)

"""#Indexing and slicing"""

myseries= [ 2,3,4,5,6]
v =pd.Series(myseries)
s1 = v[0]
print(s1)
s2 =v[1:3]
print(s2)

"""#Vectorized Operation"""

list1 = [1,2,3,4]
var = pd.series(list1)

"""#-> DATAFRAME"""

import pandas as pd

list = [2,4,6,8,10]
df = pd.DataFrame(list)
print(df)
print(type(df))

"""#INDEXING"""

info = {
    "name" : "Arpit",
    "Age" : 20,
    "Marks" : 90.5,
    "Status" : True
}
df = pd.DataFrame(info, index = ["A","B","C"])
print(df)

"""#LIST"""

info = {
    "name" : ["Arpit", "Tanishq", "Sonam"],
    "Age" : [20, 23, 24],
    "Marks" : [90.5, 90.3, 90.9],
    "Status" : True
}
df = pd.DataFrame(info)
print(df)

"""#COLUMNS"""

info = {
    "name" : ["Arpit", "Tanishq", "Sonam"],
    "Age" : [20, 23, 24],
    "Marks" : [90.5, 90.3, 90.9],
    "Status" : True
}
df = pd.DataFrame(info, columns = ["name", "Marks"])
print(df)

"""#

#INDEX VALUE
"""

info = {
    "name" : ["Arpit", "Tanishq", "Sonam"],
    "Age" : [20, 23, 24],
    "Marks" : [90.5, 80, 98],
    "Status" : True
}
df = pd.DataFrame(info)
print(info['name'][2])

"""#NESTED LIST"""

list1 = [["A","B","C","D"],["a", "b", "c", "d"]]
df = pd.DataFrame(list1)
print(df)

"""#Dataframe from Series"""

SR = {
     "S" :pd.Series([2,4,6,8,10]),
     "R" :pd.Series(["a","b","c","d","e"])
}
df = pd.DataFrame(SR)
#print(df)
df #create table

"""#Create Column from Previous columns"""

df = pd.DataFrame({ 'A': [2,4,6,8,], 'B':[3,5,7,9]})
df ['C'] = df['A'] + df['B']
df

"""#Comparing Values"""

df = pd.DataFrame({ 'A': [2,4,6,8,], 'B':[3,5,7,9]})
df ['C'] = df['A'] + df['B']
df['try']= df['A'] > 4
df[ 'try2'] = df['C']<5
df

"""#inserting columns"""

df = pd.DataFrame ({'A': [1,2,3,4]})
df.insert(1, "name", df["A"])
df.insert(2, "name2", ["A", "B", "C", "D"])
df

