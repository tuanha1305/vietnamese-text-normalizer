# Vietnamese Text Normalizer

Công cụ chuyển đổi văn bản tiếng Việt từ các bảng mã cũ (VNI, TCVN3) sang Unicode chuẩn UTF-8.

## Tính năng

- Chuyển đổi từ bảng mã VNI/TCVN3 sang Unicode
- Xử lý file đầu vào và xuất ra file UTF-8
- Kiểm tra tính hợp lệ của file đầu vào và thư mục đầu ra
- Xử lý lỗi một cách chi tiết và rõ ràng

## Yêu cầu hệ thống

- Python 3.6 trở lên
- Thư viện `vietnamese` (cài đặt qua pip)

## Cài đặt

1. Clone repository này về máy của bạn:
```bash
git clone https://github.com/tuanha1305/vietnamese-text-normalizer.git
cd vietnamese-text-normalizer
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

### Cú pháp cơ bản

```bash
python vietnamese_normalizer.py --input <file_đầu_vào> --output <file_đầu_ra>
```

hoặc sử dụng phiên bản rút gọn:

```bash
python vietnamese_normalizer.py -i <file_đầu_vào> -o <file_đầu_ra>
```

### Ví dụ

```bash
python vietnamese_normalizer.py --input equipshoplog_2025_04_10.log --output equipshoplog_2025_04_10_utf8.log
```

Kết quả:
```
✔️ Đã tạo equipshoplog_2025_04_10_utf8.log
```

## Quy trình xử lý

1. Đọc file đầu vào dưới dạng nhị phân (binary)
2. Giữ nguyên các byte trong file bằng cách giải mã với latin-1
3. Chuyển đổi từ VNI/TCVN3 sang Unicode bằng thư viện `vietnamese`
4. Lưu kết quả dưới dạng UTF-8

## Xử lý lỗi

Script sẽ kiểm tra và báo lỗi trong các trường hợp sau:

- File đầu vào không tồn tại
- File đầu vào không phải là file
- Thư mục chứa file đầu ra không tồn tại
- Lỗi xảy ra trong quá trình đọc, chuyển đổi hoặc ghi file

## Giấy phép

[MIT License](LICENSE)

## Liên hệ

Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng tạo issue trên repository hoặc liên hệ qua email: example@example.com
