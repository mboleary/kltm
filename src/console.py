# This module is responsible for generating text-based drawings of things to display in a console

import json
import datetime

def test():
    print("Console Works.")

def interactive():
    print("Interactive Mode.")

# Pretty Prints the Task List
# @param: task - Dictionary All Tasks as a dictionary
def getPrettyTextForAll(tree):
    title = "Main Task List"
    maxSize = len(title) # Get Max Size for Pretty Printing
    tasks = sorted(tree.keys(), key=lambda x: sorter(x, tree), reverse=False)
    lines = []
    
    for tname in tasks:
        t = tree[tname]
        line = ""
        if not ("name" in t and "finished" in t and "description" in t and "created" in t):
            line += "Invalid Entry in file " + str(tname) + ":"
            line += json.dumps(t, indent=4)
        else: 
            line += "[" + ("x" if t["finished"] else " ") + "]"
            line += t["name"] + " | " + t["created"]
            line += "\n\t" + t["description"]
        lines.append(line)
    seperator = ""
    for i in range(0, maxSize):
        seperator += "="
    return [title, seperator, *lines]

def sorter(x, tree):
    # Format: 2019-05-13 12:50:39.325198
    # --------01234567890123456789012345
    # --------0---------1---------2-----
    if "created" in tree[x]:
        isofmt = tree[x]["created"]
        #print(isofmt[0:4], isofmt[5:7], isofmt[8:10], isofmt[11:13], isofmt[14:16], isofmt[17:19])
        a = datetime.datetime(int(isofmt[0:4]), int(isofmt[5:7]), int(isofmt[8:10]), int(isofmt[11:13]), int(isofmt[14:16]), int(isofmt[17:19]))
        #print(a.timestamp())
        return int(a.timestamp())
    return -1

def getPrettyText(task):
    return ""