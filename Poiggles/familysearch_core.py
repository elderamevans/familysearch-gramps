# I think we might need a license header here...

# Unsure of what to have imported...

from familysearch import FamilySearch

class FamilySearchCore(object):
    def __init__(self):
        fs = FamilySearch("Gramps/5.0", "a02j0000007rW19AAE")
        # Temporary key until we can get one with desktop login enabled.
        self.login = fs.login
        self.oauth_desktop_login = fs.oauth_desktop_login

    def login_checker(self):
        pass

        # The thought here is to check if they're logged in, or if their session
        # has expired. Either way, we'll need to direct them to a login screen.
        #
        # Currently, access tokens last either 1 hour after inactivity, or
        # 24 hours after logging in, measured by the [milli?]second.