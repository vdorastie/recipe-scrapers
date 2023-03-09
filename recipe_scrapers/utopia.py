from ._abstract import AbstractScraper
from ._utils import normalize_string


class Utopia(AbstractScraper):
    @classmethod
    def host(cls):
        return "utopia.de"

    def title(self):
        return self.soup.find("div", {"id": "main-content"}).find("h1").get_text()

    def instructions(self):
        instructions_div = self.soup.find("div", {"id": "main-content"}).find("ol")

        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "li"
            )
        ]
        return " ".join(instructions)