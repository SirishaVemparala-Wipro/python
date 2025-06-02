class StringModifier:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        self.text = self.text.upper()
        return self

    def add_exclamation(self):
        self.text += "!"
        return self

    def display(self):
        print(self.text)
        return self

sm = StringModifier("hello").to_upper().add_exclamation().display()
