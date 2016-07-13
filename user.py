class SaidditUser(UserMixin):
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return unicode(self.id)
    
