# Defines a Task Placeholder when loaded from JSON

from BaseKLTMSerializableObject import BaseKLTMSerializableObject

class TaskPlaceholder(BaseKLTMSerializableObject):

    def __init__(self, path):
        self.path = path

    def getDictObject(self):
        return {"path":self.path}
