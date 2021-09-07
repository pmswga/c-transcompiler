import os
import re
from pprint import pprint

def isFunction(string):
    return re.match("\w+ \w+\(\w*\)", string) != None

    
def isFunctionHaveEmptyArgs(string):
    return re.match("\w+ \w+\(\)", string) != None
    

function_list = []

decisions = []

content = ""
new_code = []

with open("examples/example_1.c", "r") as f:
    content = f.readlines()


for line in content:
    if line != '\n':
        if isFunction(line):
            function_list.append(line)
        
        if isFunctionHaveEmptyArgs(line):
            new_line = line
            new_line = new_line.replace("()", "(void)")

            decisions.append({"from": line, "to": new_line})
            line = new_line

    new_code.append(line)
            

print("Summary")


print("Function list:")
pprint(function_list)

print()
print("Decisions:")
pprint(decisions)


print()
print(new_code)

with open("examples/example_1_.c", "w") as f:
    f.writelines(new_code)

