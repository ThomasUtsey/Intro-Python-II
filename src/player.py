import textwrap

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():

    lives = True

    def __init__(self, char_name, location, item=[]):
        self.char_name = char_name
        self.location = location
        self.item = item

    def __str__(self):
        value = f"You the great adventurer {self.char_name},find yourself in the {self.location}"
        dedented_text = textwrap.dedent(value).strip()
        wrapped_text = textwrap.fill(dedented_text, width=60)
        return wrapped_text
