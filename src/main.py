#!/usr/bin/python3

# KLTM - Kill List Task Manager

import sys
import datetime

# Local Imports
import console
import proc
import readwrite
import consoleDocs

# Local Class Imports
from TaskPlaceholder import TaskPlaceholder
from Task import Task
from BaseKLTMSerializableObject import BaseKLTMSerializableObject

KLTM_DIR = "../tmp/" # Directory that KLTM defaults to

def getArgsAsString(args):
    s = ""
    for arg in args:
        s += arg + " "
    return s

def main():
    # All possible Flags
    fAdd = False
    fView = False
    fDelete = False
    fModify = False
    fMarkFinished = False
    fAddTaskName = ""
    fAddTaskDesc = ""
    fViewTaskName = ""

    # Mode Parsing Flags
    pfFoundMode = False

    # Overall Mode Flags
    needsWrite = False # Set to true to write to the changed files

    if len(sys.argv) <= 1:
        print(consoleDocs.help)
        return
    else:
        # Print Help and Quit
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] =="/h":
            print(consoleDocs.help)
            return

        tree = readwrite.getTaskTree()
        #print(tree)

        if sys.argv[1] == "-i" or sys.argv[1] == "--interactive" or sys.argv[1] == "/i":
            console.interactive()
            return
        ignore = sys.argv[0]
        for arg in sys.argv:
            # Ignore the first argument, as this is the name of the program
            if arg == ignore:
                continue

            # Find Mode to operate in
            if not pfFoundMode and (arg == "-a" or arg == "--add" or arg == "/a" or arg == "+"):
                fAdd = True
                pfFoundMode = True
                continue
            elif not pfFoundMode and (arg == "-m" or arg == "--modify" or arg == "/m"):
                fModify = True
                pfFoundMode = True
                print("NOT IMPLEMENTED", file=sys.stderr)
                continue
            elif not pfFoundMode and (arg == "-v" or arg == "--view" or arg == "/v"):
                fView = True
                pfFoundMode = True
                print("NOT COMPLETELY IMPLEMENTED", file=sys.stderr)
                continue
            elif not pfFoundMode and (arg == "-d" or arg == "--delete" or arg == "/d" or arg == "-"):
                fDelete = True
                pfFoundMode = True
                print("NOT IMPLEMENTED", file=sys.stderr)
                continue
            elif not pfFoundMode:
                print("Invalid Syntax on ", arg, " in ", getArgsAsString(sys.argv), consoleDocs.help, file=sys.stderr)
                return

            # Add a new entry
            if pfFoundMode and fAdd and fAddTaskName == "":
                fAddTaskName = arg
                continue
            if pfFoundMode and fAdd and fAddTaskName != "" and fAddTaskDesc == "":
                fAddTaskDesc = arg
                # At this point entry is finished.
                t = Task(fAddTaskName, fAddTaskDesc)
                t.changed = True
                t.created = datetime.datetime.now()
                taskName = fAddTaskName
                if taskName in tree:
                    idx = 1
                    while taskName + str(idx) in tree:
                        idx += 1
                    taskName += str(idx)
                t.path = taskName
                tree[taskName] = t.getDictObject()
                # Reset so that we can parse more arguments
                pfFoundMode = False
                fAdd = False
                needsWrite = True
                continue

            # View a specific Task
            if pfFoundMode and fView and fViewTaskName == "":
                fViewTaskName = arg
                pfFoundMode = False
                if fViewTaskName == "":
                    lines = console.getPrettyTextForAll(tree)
                    for line in lines:
                        print(line)
                else:
                    if fViewTaskName in tree:
                        print(console.getPrettyText(tree[fViewTaskName]))
                    else:
                        results = proc.findTasksByName(fViewTaskName, tree)
                        if len(results) == 1:
                            print(console.getPrettyText(tree[results[0]]))
                        elif len(results) > 1:
                            print("Multiple Results Found... Pick a Number to view more")
                            for res in results:
                                print(console.getPrettyText(tree[res[1]]))
                    
        # If View was the only argument
        if pfFoundMode and fView:
            lines = console.getPrettyTextForAll(tree)
            for line in lines:
                print(line)

        # Perform Writes only if something was changed
        if needsWrite:
            readwrite.writeTaskTree(tree)
if __name__ == "__main__":
    main()