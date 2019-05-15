# This module contains all Help Documentation that would be printed to the Standard out, such as in the case of a Help File.

help = """KillList Task Manager (kltm).
A Program to help users organize their hecktic lives into a series of todo lists.

Warning: not everything is implemented. '!' indicates that feature is not implemented yet.

Syntax
------

kltm <command segment(s)>

Command Segments
----------------

Add Task
    -a --add <Task Name> <Task Description> : Adds a task to the list

    Example: $ kltm -a Hello World
    Adds a Task named 'Hello' with description 'World'

View Task
    -v --view [Task Name] : Views Task. If Task Name not present, then all tasks will be shown

!Modify Task
    -m --modify <Task Name> <COMMAND> : Modify an attribute on a task

    Modify Commands
        <variable=value> : Set a Variable to a Value

        Example: $ kltm -m name="Hello World"

        --finished : Set a task to finished

!Delete Task
    -d --delete [arguments] <Task Name> [<Task Name> ...] : Delete a Task by Name

    Arguments
        -f --force : Forces Deletion without asking

    Example: $ kltm -d "Hello World"
    Are you sure you want to delete Task "Hello World"? (Yes/no): Yes
    Task "Hello World" Deleted
    $

!Export Tasks as JSON
    -e --export [Task Name] : Export Tasks as JSON to Standard Out

    Example: $ kltm -e
    { ...<JSON HERE>... }

!Import Task List from JSON
    -i --import <JSON String> : Import Tasks from a JSON String

Currently a work-in progress.
Brady O'Leary - 2019
"""

