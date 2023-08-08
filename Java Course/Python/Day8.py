row1 = int(input("Enter the no. of row 1 : "))
col1 = int(input("Enter the no. of col 1 : "))
arr1 = []
for i in range(row1):
    subarr1 = []
    for j in range(col1):
        print("Enter the value for ",i,"X",j,end=": ")
        subarr1.append(int(input()))
    arr1.append(subarr1)

row2 = int(input("Enter the no. of row 2 : "))
col2 = int(input("Enter the no. of col 2 : "))
arr2 = []
for i in range(row2):
    subarr2 = []
    for j in range(col2):
        print("Enter the value for ",i,"X",j,end=": ")
        subarr2.append(int(input()))
    arr2.append(subarr2)

sum=[]
if (row1==row2 and col1==col2):
    for i in range(row1):
        subsum = []
        for j in range(col1):
            subsum.append(arr1[i][j] + arr2[i][j])
        sum.append(subsum)
print("The sum of two matrix is ",sum)

sub=[]
if (row1==row2 and col1==col2):
    for i in range(row1):
        subsub = []
        for j in range(col1):
            subsub.append(arr1[i][j] - arr2[i][j])
        sub.append(subsub)
print("The sub of two matrix is ",sub)