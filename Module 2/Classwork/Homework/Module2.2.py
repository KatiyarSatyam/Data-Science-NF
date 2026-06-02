Df1 = pd.DataFrame({
    'Name': ['Aarav Sharma', 'Vihaan Patel', 'Aditya Singh', 'Diya Reddy', 'Isha Gupta'],
    'EmpId': [1001, 1002, 1003, 1004, 1005]
})

Df2 = pd.DataFrame({
    'EmpId': [1001, 1002, 1003, 1004, 1005],
    'Salary': [450000, 520000, 480000, 500000, 470000]
})

Df3 = pd.DataFrame({
    'EmpId': [1001, 1002, 1003, 1004, 1005],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
})

Df4 = pd.DataFrame({
    'EmpId': [1001, 1002, 1003, 1004, 1005],
    'Contact no.': ['+91 98765 43210', '+91 91234 56789', '+91 87654 32109', '+91 76543 21098', '+91 65432 10987']
})

df = pd.merge(Df1, Df2, on='EmpId')
df = pd.merge(df, Df3, on='EmpId')
df = pd.merge(df, Df4, on='EmpId')
df