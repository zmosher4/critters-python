# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Donkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.walking = True

class Goat:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.walking = True

class Alpaca:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.walking = True

class Camel:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.walking = True

class Copperhead:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.swimming = True

class RatSnakes:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.swimming = True

class Swordfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.swimming = True

class JellyFish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.swimming = True

class PufferFish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.swimming = True

class Mallard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.slithering = True

class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.slithering = True

class Goose:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.slithering = True

class Swan:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.slithering = True

class Frog:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today
        self.slithering = True


miss_fuzz = Llama("Miss Fuzz", "domestic llama")
print(miss_fuzz.name)