from sys import argv
script,filename = argv

print(f"We're going to erase {filename}.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it.")
target.close()

'''
python .\ex16.py test.txt
We're going to erase test.txt.
?
Opening the file...
Now I'm going to ask you for three lines.
line 1:111111111
line 2:222222222
line 3:333333333333
I'm going to write these to the file.
And finally,we close it.
'''