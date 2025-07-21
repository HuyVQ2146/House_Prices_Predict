# House_Prices_Predict

# Dự đoán giá nhà - Machine Learning Project

## Mục tiêu
Xây dựng mô hình dự đoán giá nhà từ dữ liệu Kaggle.

## Timeline phát triển
- **Bắt đầu:** 21/07/2025
- **Kết thúc (dự kiến):** 10/08/2025

---

## Nhật ký học tập & phát triển

### ✅ Day 1 - 21/07/2025
- Tham gia competition trên Kaggle.
- Tải dữ liệu.
- Làm sơ bộ EDA.
- Bắt đầu làm quen với pandas.
- Bị rối ở bước chọn file location và chạy trong terminal

- Hoàn thành 6 bước để phân tích dữ liệu:
    -**Bước 1**: Import thư viện & đọc dữ liệu
        -Dùng các thư viện như pandas (để phân tích dữ liệu), numpy (để vecto, tối ưu hóa thuật toán), seaborn và matplotlib (để visualize dữ liệu)
        -Sau đó, đọc(1.1) và xem kích thước(1.2) dữ liệu

    -**Bước 2**: Tổng quan dữ liệu
        -Kiểm tra thông tin của training set:
            -(2.1) Thông tin các cột: kiểu dữ liệu, non-null: dùng .info() cho training set (train)
            -(2.2) Thống kê cơ bản cho các cột số: dùng .describe() cho training set (train)

    -**Bước 3**: Kiểm tra missing data từng cột 
        -(3.1) Tính số dữ liệu bị thiếu của từng cột: dùng tổng .sum() của các phần dữ liệu đc đánh dấu là Null(hoặc NaN), tìm bằng hàm .isNull(), của từng cột   
        -(3.2) Sắp xếp các dữ liệu tìm được theo thứ tự số missing data giảm dần để xem những phần dữ liệu nào nên hạn chế sử dụng để train (hoặc để kiếm thêm dữ liệu bù vào)

    -**Bước 4**: Phân phối biến mục tiêu 'SalePrice': vì chúng ta muốn dự đoán  giá nhà nên dữ liệu quan trọng nhất là giá nhà có sẵn (y)
        -Qua biểu đồ cột, ta có góc nhìn tổng quan về giá nhà (giá tầm 120k là có nhiều nhất)

    -**Bước 5**: Phân tích tương qua với cột 'SalePrice' để tìm những cột số nào có tương quan mạnh nhất với SalePrice (để dùng những cột đó làm dữ liệu train model)
        -(5.1) Xét tương quan chỉ với những cột có giá trị số thôi (có thể chuyển sang dạng DataFrame để dễ nhìn hơn)
        -(5.2) Chọn ra top 10 cột có tương quan lớn nhất với cột "SalePrice"

    -**Bước 6**: Kiểm tra một số feature quan trọng
        -Ta chọn ra 2 cột có tương quan cao nhất với 'SalePrice' và visualize ra để xem mối liên hệ giữa chúng qua 2 biểu đồ hộp(6.1) và biểu đồ phân tán(6.2)
