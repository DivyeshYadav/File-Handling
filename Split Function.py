with open("Codingal.txt","w") as f:
    f.write("Hi my name is Divyesh Yadav, I am 9 years old")
f.close()

with open("Codingal.txt","r") as r:
    data = r.readlines()
    for line in data:
        word = line.split()
        print(word)
r.close()

file = open("my.txt","x")
print(file)