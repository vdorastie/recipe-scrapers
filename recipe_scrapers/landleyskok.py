from ._abstract import AbstractScraper
from ._utils import normalize_string


class LandleySkok(AbstractScraper):
    @classmethod
    def host(cls):
        return "landleyskok.se"

    def title(self):
       return self.soup.find("title").text

    def instructions(self):
        instructions_lis = self.soup.find("div", {"class": "post-content"}).find_all("p", {"class":"instructions howto"})
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_lis
        ]
        return " ".join(instructions)