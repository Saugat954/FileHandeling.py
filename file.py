import os

if(not os.path.exists('data')):
    os.mkdir('fileHAndeling/data')

#to write a text file
f= open('data/myfile.txt','w')
f.write("Hello, My name is Saugat and I live in Brisbane")
f.close()

#to read a file

r =  open('data/myfile.txt','r')
text = r.read
print(text)
r.close()

#to append a file
f= open('data/myfile.txt','a')
f.write(" I am 22 years old")
f.close()
