# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:

    def __init__(self, name, desc, item_name="", item_desc=""):
        self.name = name
        self.desc = desc
        self.item_name = item_name
        self.item_desc = item_desc

    def __str__(self):
        return f"{self.name} - {self.desc}"
