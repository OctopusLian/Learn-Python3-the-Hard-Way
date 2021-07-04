from sys import argv

script,user_name = argv
prompt = ' > '

print(f"Hi {user_name},I'm the {script} script")
print(f"Do you like me {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright,so you said {lives} about liking me.
You live in {lives}.Not sure where that is.
And you have a {computer} computer.Nice.
""")

'''
python .\ex14.py Zed
Hi Zed,I'm the .\ex14.py script
Do you like me Zed?
 > Yes
What kind of computer do you have?
 > Chengdu

Alright,so you said Yes about liking me.
You live in Yes.Not sure where that is.
And you have a Chengdu computer.Nice.
'''