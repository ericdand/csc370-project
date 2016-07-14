class SaidditPost(object):
    def __init__(self):
        self.upvotes = 0
        self.downvotes = 0
    
    def __init__(self, title, text, author, published_date, url=None):
        self.upvotes = 0
        self.downvotes = 0
        self.title = title
        self.text = text
        self.author = author
        self.published_date = published_date
        self.url = url
