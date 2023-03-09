from ._abstract import AbstractScraper
from ._utils import normalize_string


class Utopia(AbstractScraper):
    @classmethod
    def host(cls):
        return "utopia.de"

    def title(self):
        return self.soup.find("div", {"id": "main-content"}).find("h1").get_text()

    def instructions(self):
        instructions_div = self.soup.find("div", {"id": "main-content"}).find_all("ol")
		instructions_ils = [instruction_ol.find_all("li") for instruction_ol in instructions_div]
		instructions_ils = [item for sublist in instructions_ils for item in sublist]
		
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_ils
        ]
        return " ".join(instructions)