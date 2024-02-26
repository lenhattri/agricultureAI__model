from bs4 import BeautifulSoup
from bs4 import ResultSet

def checkHaveSubtitle(contents: ResultSet) -> bool:
    for content in contents:
        if content.findChild("strong") is not None:
            return True
    return False