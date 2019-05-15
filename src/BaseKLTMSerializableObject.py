# Base Object which is serializable by KLTM, allowing the user to save this data into a Task File

class BaseKLTMSerializableObject:
    path = "" # File Path
    changed = False # True if the file was changed
    created = None # Date that item was created

    # This should return a Dictionary containing any serializable data
    def getDictObject(self):
        return {"_path": self.path, "_changed":self.changed, "created":str(self.created)}
