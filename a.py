#  Program to append the contents of file in another file


#  Entering the file names
firstfile = input("Enter the name of the first file  ")
secondfile = input("Enter the name of the second file  ")

# Open both files in read mode only to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print("Content of the first file before apending -\n",f1.read())
print("Content of the first file before apending -\n",f2.read())


f1.close()
f2.close()


f1 = open(firstfile,'a+')
f2 = open(secondfile,'r')

#f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Content of the first file after apending -\n",f1.read())
print("Content of the first file after apending -\n",f2.read())


f1.close()
f2.close()