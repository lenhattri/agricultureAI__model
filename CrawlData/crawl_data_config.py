
'''
    _Hướng dẫn sử dụng_
    Hãy tạo 3 file txt là RAW_URL_FILENAME, NO_SUBTITLE_URL_FILENAME, SUBTITLE_URL_FILENAME
    Rồi chép url cần crawl data vào RAW_URL_FILENAME
    Thay đổi thư mục của PATH_NO_SUBTITLE_DATA_TEXT
'''


'''
    Tên file url tổng hợp, còn thô chưa phân loại
'''
RAW_URL_FILENAME = "raw_url.txt"

'''
    Tên file url không chứa các subtitle, có thể dùng title của bài viết làm input và
    nội dung làm output luôn
'''
NO_SUBTITLE_URL_FILENAME = "no_title_url.txt"

'''
    Tên file url có chứa các subtitle, cần xử lí khác biệt
'''
SUBTITLE_URL_FILENAME = "title_url.txt"

'''
    Đường dẫn đến nơi chứa dữ liệu text
    Cái này có thể sử a tùy theo máy
    Hãy đặt nó trước khi chạy phương thức crawlDataNormal
'''
PATH_NO_SUBTITLE_DATA_TEXT = '/home/rikka/Project/Agriculture_AI/venv/src/CrawlData/DataText/DataNoSubtitle'

'''
    Để phân biệt title và content trong file text
'''
TITLE = '_title: '
CONTENT = '_content: '

