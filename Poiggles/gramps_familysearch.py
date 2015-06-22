# I think we might need a license header here...

# Unsure of what to have imported...
from .familysearch_core import FamilySearchCore

class GrampsFamilySearch(FamilySearchCore):
    def __init__(self):
        super().init()
        self.person_template = {"persons": []}
        self.name_template = {"names": []}
        self.nameform_template = {"nameForms": []}
        self.parts_template = {"parts": []}

    def commit_new_familysearch_person(self, person):
        """
        person: json object new FamilySearch person to be uploaded and created.
        """
        return fs.post(fs.person(), person)

    def commit_existing_familysearch_person(self, pid, person):
        """person: json object representing person to be uploaded
        pid: string representing FamilySearch Person ID
        """
        return fs.post(fs.person(pid), person)

    def read_gramps_person(self):
        pass

    def update_familysearch_givenname(
            self, givenname, person=None, reason="", names=0):
        """givenname: String to update given name to
        person: Optional dict to upate existing person dict onto.
        """
        if person is None:
            person = self.person_template
            person["persons"].append(self.name_template)
            person["persons"][0]["names"].append(self.nameform_template)
        if names:
            person["persons"][0]["names"][names].append(self.nameform_template)
        return person

    def update_familysearch_surname(
            self, surname, person=None, reason="", names=0):
        """givenname: String to update given name to
        person: Optional dict to upate existing person dict onto.
        """
        if person is None:
            person = self.person_template
            person["persons"].append(self.name_template)
            person["persons"][0]["names"].append(self.nameform_template)
        if names:
            person["persons"][0]["names"][names].append(self.nameform_template)
            
        person["persons"][0]["names"][names]["parts"]
        return person
        