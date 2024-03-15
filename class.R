df <- data.frame(timestamp,sales)
rm(list = ls())
#Load the dataset

#to find the no. of columns
df = read.csv("/Users/nebink/Desktop/123e.csv",header=TRUE)
print('Number of columns: ')
print(ncol(df))
 
#to find the no. of rows


print('Number of columns: ')
print(ncol(df))
#to find the name of the rows

print('name of rows: ')
print(rownames(df))

#to find the name of the columns

print('name of columns: ')
print(colnames(df))


#to find the object type

print('Object Type: ')
print(typeof(df))

print("Top 6 rows")
print(head(df))

print("bottom 6 rows")
print(tail(df))

print("2nd row=")
print(df[2,])

print("2nd column=")
print(df[,2])


