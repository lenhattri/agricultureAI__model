import requests
from bs4 import BeautifulSoup
from check_have_subtitle import checkHaveSubtitle

count = 0

def crawlData(url: str) -> dict:
    global count
    res = {}
    try:
        response = requests.get(url)
    except Exception as e:
        print("There are errors:{}".format(e))
    soup = BeautifulSoup(response.content, "html.parser")

    #Lấy tiêu đề của trang

    title = soup.find("h1", attrs = {"class" : "post-title"})
    res["title"] = title.get_text().strip()

    #Lấy nội dung

    contents = soup.findChild("div", attrs = {"class" : 'noidung'}).find_all("p")
    res["content"] = []

    check = checkHaveSubtitle(contents)
    count = count + 1
    res["havesubtitle"]  = str(count - 1) + "Not"
    for content in contents:
        if check:
            res["havesubtitle"] = str(count - 1)
        res["content"].append(content.get_text().strip())
    return res

