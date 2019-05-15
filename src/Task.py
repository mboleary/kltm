# contains class definition for Task List Item

from BaseKLTMSerializableObject import BaseKLTMSerializableObject

class Task(BaseKLTMSerializableObject):
    name = ""
    description = ""
    finished = False
    def __init__(self, name, description):
        self.name = name
        self.finished = False
        self.description = description

    # Returns a Dictionary Object to allow for JSONification into a file
    def getDictObject(self):
        ret1 = super().getDictObject()
        ret2 = {"name": self.name, "finished": self.finished, "description": self.description}
        return {**ret1, **ret2}

    def setFinished(self, finished):
        self.finished = finished
