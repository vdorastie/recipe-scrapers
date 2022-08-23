from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Cucchiaio(AbstractScraper):
    @classmethod
    def host(cls):
        return "cucchiaio.it"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find('title').get_text()

    def total_time(self):
        block = self.soup.find("div", {"class": "scheda-ricetta-new"})
        if block:
            return sum(map(get_minutes, block.findAll("tr")))
        return 0

    def yields(self):
        header = self.soup.find("td", text="PORZIONI")
        if header:
            value = header.find_next("td")
            return get_yields(value)
        return None

    def image(self):
        data = self.soup.find("div", {"class": "auto"}).find("img", {"class": "image"})
        if data:
            data = data.get("src")
        return data

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "row mx-0 mb-f30"})
        
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "p"
            )
        ]
        return "\n".join(instructions)

    def ratings(self):
        return None
