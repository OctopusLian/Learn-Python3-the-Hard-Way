from sys import argv
script,filename = argv
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename agagin:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

'''
python .\ex15.py ex15_sample.txt
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
Type the filename agagin:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
'''