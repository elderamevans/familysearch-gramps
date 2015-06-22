# I think we might need a license header here...

# Unsure of what to have imported...
from .familysearch_gramps import FamilySearchGramps
from .gramps_familysearch import GrampsFamilySearch

from familysearch import FamilySearch

class Poiggles(FamilySearchGramps, GrampsFamilySearch):
    def __init__(self):
        super().__init__()