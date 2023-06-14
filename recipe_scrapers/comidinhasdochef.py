# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class ComidinhasDoChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "comidinhasdochef.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1", {"class": "t-secondary"}).get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "accordeon-text"})
        
        instructions = [
            normalize_string(instruction.get_text(strip=True, separator=" "))
            for instruction in instructions_div.find_all(
                "li"
            )
        ]
        return "\n".join(instructions)

    def ratings(self):
        return self.schema.ratings()
