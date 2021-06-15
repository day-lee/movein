'''Provides accessible template from Post object'''
class Post:
    def __init__(self, id, author, title, subtitle, dates, image, body):
        self.id = id
        self.author = author
        self.title = title
        self.subtitle = subtitle
        self.dates = dates
        self.image = image
        self.body = body

