from ._abstract import AbstractScraper
from ._utils import normalize_string


class Daskochrezept(AbstractScraper):
    @classmethod
    def host(cls):
        return "daskochrezept.de"

    def title(self):
        return self.soup.find("h1", {"class": "recipe--heading__title"}).get_text()

    def instructions(self):
        instructions_divs = self.soup.find_all("div", {"class": "recipe-step__text"})
        instructions_ps = [instruction_div.find("p") for instruction_div in instructions_divs]
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_ps
        ]
        return " ".join(instructions)