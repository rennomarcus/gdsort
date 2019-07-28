class Func:
    name = ''
    content = []

    def __init__(self, name):
        self.name = name
        self.content = []

    def add_content(self, content):
        self.content.append(content)

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name