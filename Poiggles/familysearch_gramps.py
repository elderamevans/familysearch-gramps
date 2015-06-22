# I think we might need a license header here...

# Unsure of what to have imported...

from .familysearch_core import FamilySearchCore


class FamilySearchGramps(FamilySearchCore):
    def __init__(self):
        super().init()

    def commit_new_gramps_person(self):
        pass

    def commit_existing_gramps_person(self):
        pass

    def read_fs_person(self, pid):
        """pid: Person ID of person to be read"""
        return fs.get(fs.person(pid))
    
    def update_gramps_givenname(self):
        pass
