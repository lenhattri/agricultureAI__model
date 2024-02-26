from bs4 import ResultSet
from bs4 import BeautifulSoup

def checkIsHaveSubtitle(resultSet: ResultSet) -> bool:
    for element in resultSet:
        try:
            if element["style"] == "text-align: right;":
                continue
        except:
            pass
        if element.findChild("strong") is not None:
            return True
    return False