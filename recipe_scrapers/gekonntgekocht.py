from ._abstract import AbstractScraper
from ._utils import normalize_string


class Gekonntgekocht(AbstractScraper):
    @classmethod
    def host(cls):
        return "gekonntgekocht.de"

    def title(self):
        return self.soup.find("h1", {"itemprop": "name"}).get_text()

    def instructions(self):
        instructions_p = self.soup.find_all("p", {"itemprop": "recipeInstructions"})
		
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_p
        ]
        return " ".join(instructions)