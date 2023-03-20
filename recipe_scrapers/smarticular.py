from ._abstract import AbstractScraper
from ._utils import normalize_string


class Smarticular(AbstractScraper):
    @classmethod
    def host(cls):
        return "smarticular.net"

    def title(self):
        return self.soup.find("h1", {"class": "page-title"}).text

    def instructions(self):
        instructions_lis = self.soup.find("div", {"class": "article-main"}).find("ol").find_all("li")
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_lis
        ]
        return " ".join(instructions)