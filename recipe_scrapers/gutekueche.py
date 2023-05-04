from ._abstract import AbstractScraper
from ._utils import normalize_string


class Gutekueche(AbstractScraper):
    @classmethod
    def host(cls):
        return "gutekueche.at"

    def title(self):
       return self.soup.find("title").text.removesuffix("| GuteKueche.at")

    def instructions(self):
        instructions_lis = self.soup.find("section", {"class": "sec rezept-preperation"}).find("ol").find_all("li")
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_lis
        ]
        return " ".join(instructions)