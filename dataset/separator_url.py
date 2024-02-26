from bs4 import BeautifulSoup
from config import RAW_URL_FILENAME, NO_SUBTITLE_URL_FILENAME, SUBTITLE_URL_FILENAME
import requests
from check_type_of_url import checkIsHaveSubtitle

'''
    count dùng để đếm số lượng thành công
'''
count = 0

'''
    Hàm này sẽ lọc giá trị ở trong 
    Trả về giá trị bool cho biết hàm có chạy thành công không!
'''
def rerangeUrlByType(srcFile: str = RAW_URL_FILENAME):
    global count
    count = 0
    try:
        fileUrls = open(srcFile, "r")
    except:
        fileUrls = open(srcFile, "w")
        fileUrls.close()
        print("Hãy thêm url vào file: {}".format(srcFile))
        return
    
    noTilteFile = open(NO_SUBTITLE_URL_FILENAME, "a")
    haveTitleFile = open(SUBTITLE_URL_FILENAME, "a")
    rawUrlsFile = open(srcFile, "r")
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
        if checkIsHaveSubtitle(contents):
            haveTitleFile.write(rawUrls[i])
        else:
            noTilteFile.write(rawUrls[i])
        count += 1
    fileUrls.close()
    noTilteFile.close()
    haveTitleFile.close()
    rawUrlsFile.close()
    print("Đã sắp xếp các file theo loại thành công!")
    print(f"Thành công: {count} / {numberUrls}")

rerangeUrlByType()