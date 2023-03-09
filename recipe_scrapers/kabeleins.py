from ._abstract import AbstractScraper
from ._utils import normalize_string


class Kabeleins(AbstractScraper):
    @classmethod
    def host(cls):
        return "kabeleins.de"

    def title(self):
        return self.soup.find("header").get_text()

    def instructions(self):
        instructions_p = self.soup.find_all("p", {"class": "css-g85ual"})
		
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_p
        ]
        return " ".join(instructions)