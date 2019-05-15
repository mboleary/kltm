# This module is responsible for reading and writing to files on the disk. It translates between the File On-disk, and the actual format being used

from main import KLTM_DIR
import os
import json

def test():
    print("readwrite Works.", KLTM_DIR)

# Returns a Task Tree, an object with all tasks and categories included in it
def getTaskTree():
    taskTree = {}
    # read all files in a directory
    cwd = os.getcwd()
    os.chdir(cwd + "/" + KLTM_DIR)
    queue = list(os.scandir())
    while len(queue) > 0:
        curr = queue.pop()
        f = open(curr.path, "r")
        fstr = f.read()
        fdict = json.loads(fstr)
        f.close()
        fname = curr.path[2:]
        fdict["_path"] = fname
        fdict["_changed"] = False
        fdict["__type"] = "task" # Keeps track of types in hierarchy
        taskTree[fname] = fdict
    return taskTree

# Writes Task Tree back to directory
# @param tree - Dictionary Tree to write back
# @param force - Boolean Force overwrite all files
def writeTaskTree(tree, force = False):
    cwd = os.getcwd()
    os.chdir(cwd + "/" + KLTM_DIR)
    # @TODO Revise for when implementing categories
    keys = list(tree.keys())
    for key in keys:
        item = tree[key]
        if force or item["_changed"]:
            path = item["_path"]
            if "_changed" in item:
                del item["_changed"]
            if "_path" in item:
                del item["_path"]
            if "__type" in item:
                del item["__type"]
            wstr = json.dumps(tree[key])
            f = open(path, "w")
            f.write(wstr)
            f.close()

# Delete a Task File from the Directory
def deleteTask(task):
    path = task["_path"]
    print("Removing Task at ", path)
    os.remove(path)