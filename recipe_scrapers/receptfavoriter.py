from ._abstract import AbstractScraper
from ._utils import normalize_string


class ReceptFavoriter(AbstractScraper):
    @classmethod
    def host(cls):
        return "receptfavoriter.se"

    def title(self):
       return self.soup.find("title").text

    def instructions(self):
        instructions_lis = self.soup.find("div", {"class": "recipe-preparation legible"}).find_all("span", {"itemprop":"text"})
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_lis
        ]
        return " ".join(instructions)