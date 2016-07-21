from flask_login import UserMixin

class SaidditUser(UserMixin):
    def __init__(self, id, subscriptions):
        self.id = id
        self.subscriptions = subscriptions

    def get_id(self):
        return unicode(self.id)
    
