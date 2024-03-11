
class CrawlDataMethods:
    
    def __init__(self):
        pass
    
    '''
        Phương thức này lấy dữ liệu và lưu vào 1 file khác
        Trả về 1 số đại diện cho số lần lấy dữ liệu thành công
    '''
    def crawlData(self) -> None:
        pass
    
    '''
        Trả về 1 từ điển chứa các thành phần nội dung lấy được từ 1 trong trang có url
    '''
    def crawlOneData(self, url: str) -> dict:
        pass
    
    '''
        Dùng nếu cần phân chia các loại dữ liệu trong 1 trang thành các loại khác nhau để xử lý
    '''
    def devideDataTypes(self, srcFile: str):
        pass