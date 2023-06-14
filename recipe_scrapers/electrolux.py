from ._abstract import AbstractScraper
from ._utils import normalize_string


class Electrolux(AbstractScraper):
    @classmethod
    def host(cls):
        return "electrolux.ch"

    def title(self):
        return self.soup.find("title").text

    def instructions(self):
        instructions_lis = self.soup.find_all("div", {"class": "fiftyfifty__rte"})
        instructions = [normalize_string(instruction.get_text(strip=True, separator=" ")) for instruction_list in instructions_lis for instruction in instruction_list.find_all('p')]
        return " ".join(instructions)