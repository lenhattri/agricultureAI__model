from crawl_data import crawlData
from time import sleep
from config import RAW_URL_FILENAME

try:
    fileUrls = open(RAW_URL_FILENAME, "r")
except:
    '''
        Không có file nên tạo file
    '''
    fileUrls = open(RAW_URL_FILENAME, "w")
    fileUrls.close()
    fileUrls = open(RAW_URL_FILENAME, "r")

urls = fileUrls.readlines()

writeTxtUrl = "/home/rikka/Project/research-LLM1/txt_data/"

for i in range(0, len(urls)):
    #Có thể dư dấu xuống hàng nên dùng urls[i][0 : len(urls[i]) - 1]
    if urls[i][-1] == "\n":
        urls[i] = urls[i][0 : len(urls[i]) - 1]
    currentInfo = crawlData(urls[i])
    currentFile = open(writeTxtUrl + currentInfo["havesubtitle"] + "-" + currentInfo["title"], "w")
    for content in currentInfo["content"]:
        currentFile.write(content)
        currentFile.write("\n")
    currentFile.close()
    
fileUrls.close()