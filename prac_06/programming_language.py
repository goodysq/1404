class ProgrammingLanguage:
    """Information of programming language"""

    def __init__(self, field, typing, reflection, year):
        """ constructor in ProgrammingLanguage oriented concepts"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine is the language dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return ProgrammingLanguage in string"""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


def test_program():
    """Test the function of ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


if __name__ == "__main__":
    test_program()
