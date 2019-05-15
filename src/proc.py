# This is a general-purpose Processing Module containing functions to help process things

def test():
    print("Proc Works.")

# Find all Tasks by a given name
# @param: name (string) - Name to find
# @param: tree (Dict) - Tree of all tasks
# @return: (String, Dict) - Tuple of Index and Task
# @TODO: Modify to allow for categories
def findTasksByName(name, tree):
    results = []
    keys = tree.keys()
    for k in keys:
        task = tree[k]
        if "name" in task and task["name"] == name:
            results.append((k, task))
    return results