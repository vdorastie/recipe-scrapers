from ._abstract import AbstractScraper
from ._utils import normalize_string


class Ricettasprint(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricettasprint.it"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "td-ss-main-content"})
        
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "p"
            )
        ]
        return "\n".join(instructions)
