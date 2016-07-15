from flask_login import UserMixin

class SaidditUser(UserMixin):
    def __init__(self, id):
        self.id = id
        self.subscriptions = []

    def get_id(self):
        return unicode(self.id)
    
