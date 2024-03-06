from crawl_data_design import CrawlDataMethods
from bs4 import BeautifulSoup, ResultSet
from crawl_data_config import RAW_URL_FILENAME, NO_SUBTITLE_URL_FILENAME, SUBTITLE_URL_FILENAME, PATH_NO_SUBTITLE_DATA_TEXT
from crawl_data_config import TITLE, CONTENT
from typing import Any
import requests


class CrawlData(CrawlDataMethods):
    
    def __init__(self):
        super().__init__()
    def crawlDataNormal(self, src: str = NO_SUBTITLE_URL_FILENAME) -> None:
        try:
            fileSrc = open(src, 'r')
        except FileNotFoundError as fnfe:
            print(fnfe)
            exit()
        urls = fileSrc.readlines()
        size = len(urls)
        count = 0
        for i in range(size):
            n = len(urls[i])
            if n > 0 and urls[i][-1] == '\n':
                urls[i] = urls[i][0 : n - 1]
            if self.crawlOneDataNoSubtitle(urls[i], PATH_NO_SUBTITLE_DATA_TEXT):
                count += 1
            else:
                print(f'Thất bại ở {i}')
        print(f'Thành công: {count}/{size}')
        
    def crawlOneDataNoSubtitle(self, url: str, targetPath: str) -> bool:
        try:
            response = requests.get(url)
        except Exception as e:
            print(e)
            return False
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', attrs = {'class' : 'post-title'})
        contents = soup.findChild('div', attrs = {'class' : 'noidung'}).find_all('p')
        title_strip = title.get_text().strip()
        to = open(PATH_NO_SUBTITLE_DATA_TEXT + '/' + title_strip + '.txt', 'w')
        to.write(TITLE)
        to.write('\n')
        to.write(title_strip)
        to.write('\n')
        to.write(CONTENT)
        to.write('\n')
        for content in contents:
            if content['style'] == 'text-align: right;':
                continue
            else:
                to.write(content.get_text().strip())
                to.write('\n')
        to.close()
        return True
        
    def crawlDataHaveSubtitle(self) -> int:
        pass
    def devideDataTypes(self, srcFile: str):
        try:
            rawUrlsFile = open(srcFile, 'r')
        except FileNotFoundError as fnfe:
            print(fnfe)
            exit()
        count = 0
        noTilteFile = open(NO_SUBTITLE_URL_FILENAME, 'a')
        haveTitleFile = open(SUBTITLE_URL_FILENAME, 'a')
        rawUrls = rawUrlsFile.readlines()
        numberUrls = len(rawUrls)
        if numberUrls == 0:
            print("Không có urls trong file {}".format(srcFile))
            return
        for i in range(0, numberUrls):
            currentUrl = rawUrls[i].replace("\n", "") if rawUrls[i] != "" and rawUrls[i][-1] == "\n" else rawUrls[i]
            try:
                response = requests.get(currentUrl)
            except Exception as e:
                print("Phát hiện vài lỗi:{}".format(e))
                print("Lỗi xuất hiện ở url thứ {}".format(i + 1))
                continue
            soup = BeautifulSoup(response.content, "html.parser")
            try:
                contents = soup.findChild("div", attrs = {"class" : 'noidung'}).find_all("p")
            except Exception as e:
                print("Phát hiện vài lỗi:{}".format(e))
                continue
            if self.__checkIsHaveSubtitle(contents):
                haveTitleFile.write(rawUrls[i])
            else:
                noTilteFile.write(rawUrls[i])
            print(f'Đã xong file {i + 1}')
            count += 1
        noTilteFile.close()
        haveTitleFile.close()
        rawUrlsFile.close()
        print("Đã sắp xếp các file theo loại thành công!")
        print(f"Thành công: {count} / {numberUrls}")
    
    def __checkIsHaveSubtitle(self, resultSet: ResultSet[Any]) -> bool:
        for element in resultSet:
            try:
                if element["style"] == "text-align: right;":
                    continue
            except:
                pass
            if element.findChild("strong") is not None:
                return True
        return False
            

'''
if __name__ == '__main__':
    obj = CrawlData()
    obj.devideDataTypes(RAW_URL_FILENAME)
    obj.crawlDataNormal()
''' 