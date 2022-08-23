from ._abstract import AbstractScraper
from ._utils import normalize_string


class Recetasdeescandalo(AbstractScraper):
    @classmethod
    def host(cls):
        return "recetasdeescandalo.com"

    def title(self):
        return self.soup.find("title").get_text()

    def instructions(self):
        instructions_div = self.soup.find("div", {"id": "receta"}).find("ol")
        
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "li"
            )
        ]
        return "\n".join(instructions)
