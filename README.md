
# Overview

Agriculture AI - model finetuning part

# Technologies

 - Python, Pytorch

# Contributors

- Lê Nhật Trí DPM225491
- Huỳnh Nhựt Phát DPM225455
- Đào Duy Thành DTH225764
- Lê Chí Hiếu DTH225642

# Conventions

- Khi code 1 hàm phải comment chức năng của hàm, params hàm dùng, kiểu dữ liệu trả về(Nếu dùng python3 syntax chỉ cần viết chức năng của hàm)
- Follow theo cấu trúc folder
- Code push vào branch riêng và tạo pull request. Không commit trực tiếp vào master

# Research Method

- Chọn model nguồn
- Phân tích cách model xử lý ngôn ngữ tiếng việt.
- Cào data từ websites [khuyến nông quốc gia](https://khuyennongvn.gov.vn/) và các ebooks về lĩnh vực nông nghiệp.
- Tiền xử lý data(format, loại bỏ data nhiễu, làm sạch data...).
- Chuyển dữ liệu thô thành các các ma trận vector.
- Tiến hành tinh chỉnh model.
- Test model .
- 
**Các bước thực hiện:** Cào một lượng data nhỏ -> Finetuning(Tinh chỉnh, training model) -> Chạy thử -> Thay đổi thông số và cào thêm data -> Lặp lại.

Sau khi ta đã có model hoàn thiện sẽ kéo model qua website để demo.

# Data format

```json
        [
            {
                "instruction": "Hãy tính tổng 2 số",
                "input":"2,3",
                "output":"Tổng là 5"

            },
            {
                "instruction": "Hãy tính tổng 2 số",
                "input":"4,6",
                "output":"Tổng là 10"
                
            }
        ]
```

