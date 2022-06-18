
class Post:
    def __init__(self):
        self.url = ''
        self.title = ''
        self.keywords = ''
        self.description_image = ''
        self.description_text = ''
        self.created_at = None
        self.template = ''

    def __str__(self):
        return self.title

    def __add__(self, other):
        if type(other) == type(dict()):
            for prop, value in other.items():
                self.__dict__[prop] = value
        else:
            for prop, value in other.__dict__.items():
                self.__dict__[prop] = value
        return self
