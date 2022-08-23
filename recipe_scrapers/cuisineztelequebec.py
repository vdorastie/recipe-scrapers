from ._abstract import AbstractScraper
from ._utils import normalize_string


class Cuisineztelequebec(AbstractScraper):
    @classmethod
    def host(cls):
        return "cuisinez.telequebec.tv"

    def title(self):
        return self.soup.find("header", {"id": "main-content"}).find("article").find("h1").get_text()

    def instructions(self):
        instructions_div = self.soup.find_all("section", {"class": "listesRecette_me__17UDc"})[-1]
        
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "li"
            )
        ]
        return "\n".join(instructions)
