class Writer:
    def skills(self):
        print("Writing skills")

class Speaker:
    def skills(self):
        print("Speaking skills")

class Author(Writer, Speaker):
    def skills(self):
        Writer.skills(self)
        Speaker.skills(self)

a = Author()
a.skills()
