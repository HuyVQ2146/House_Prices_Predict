# Exploratory Data Analysis - Phân tích dữ liệu khám phá

### 1. Import thư viện & đọc dữ liệu
print("1. Import thư viện & đọc dữ liệu")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
print("1.1. Đọc dữ liệu")
train = pd.read_csv("house_prices/train.csv")
test = pd.read_csv("house_prices/test.csv")

# Xem kích thước dữ liệu
print(f"Training set's shape: {train.shape}")
print(f"Test set's shape: {test.shape}")
print()

print("1.2. train.head()")
print(train.head())
print()
print()


### 2. Tổng quan dữ liệu
print("2. Tổng quan dữ liệu")

# Thông tin các cột: kiểu dữ liệu, non-null
print("2.1. Thông tin training set")
train.info()
print()

# Thống kê cơ bản cho các cột số
print("2.2. Thống kê cơ bản cho các cột số training set")
print(train.describe())
print()
print()


### 3. Kiểm tra missing data từng cột 
print("3. Kiểm tra missing data từng cột")
print("3.1. Tính số dữ liệu bị thiếu của từng cột")
missing = train.isnull().sum()
print(missing)
print()
# Sắp xếp từ cao xuống thấp
print("3.2. Sắp xếp từ cao xuống thấp")
missing[missing > 0].sort_values(ascending=False)
print(missing[missing > 0].sort_values(ascending=False))
print()
print()


### 4. Phân phối biến mục tiêu (SalePrice)
print("4. Phân phối biến mục tiêu (SalePrice)")

# Từ cột "SalePrice" trong training set tạo biểu đồ cột
# ~ kde=True giúp tạo đường cong mật độ xác suất cho biểu đồ
sns.histplot(train["SalePrice"], kde=True)

plt.title("Hình 4. Phân phối SalePrice")
# Show biểu đồ ra
plt.show()
print("Hình 4. Phân phối SalePrice")
print()
print()


### 5. Phân tích tương qua với cột 'SalePrice'
print("5. Phân tích tương qua với cột 'SalePrice'")

# Mục tiêu: Tìm những cột số nào có tương quan mạnh nhất với SalePrice.
# ~ Chỉ tính toán với các cột kiểu số (numeric) trong DataFrame – tức là loại bỏ toàn bộ các cột chứa text (object), category, datetime, v.v.
# ~ corr() tính hệ số tương quan (default: 'Pearson') giữa các cột số.
# ~ Hệ số tương quan Pearson (Pearson correlation coefficient) là một chỉ số thống kê đo mức độ tuyến tính giữa hai biến số liên tục. 
#   Nó được ký hiệu là r, giá trị nằm trong khoảng: −1 ≤ r ≤ 1
correlation = train.corr(numeric_only=True) # default: method='pearson'

# chuyển correlation thành DataFrame để print cho dễ nhìn
corr_df = pd.DataFrame(correlation)
print(f"5.1. Các cột có hệ số tương quan với 'SalePrice': \n{corr_df}")
top_corr = correlation['SalePrice'].sort_values(ascending=False)
print()

print(f"5.2. Top 10 cột có hệ số tương quan với 'SalePrice' lớn nhất: \n{top_corr[:10]}")
print()
print()


### 6. Kiểm tra 1 số feature quan trọng
print("6. Kiểm tra một số feature quan trọng")
# Chọn 2 đặc trưng có hệ số tương quan với SalePrice lớn nhất

# Trong boxplot (biểu đồ hộp), dữ liệu được chia như sau:
# ~ Hộp (box): thể hiện khoảng giữa 25% đến 75% (Q1 đến Q3) – còn gọi là interquartile range (IQR).
# ~ Vạch giữa hộp: là median (trung vị).
# ~ "Râu" (whiskers): kéo dài đến giá trị nằm trong phạm vi: [Q1−1.5×IQR,Q3+1.5×IQR]
# ~ Điểm tròn ngoài râu: là outliers, tức là các điểm dữ liệu quá thấp hoặc quá cao vượt khỏi khoảng đó.
sns.boxplot(x="OverallQual", y="SalePrice", data=train)
plt.title("OverallQual vs. SalePrice")
plt.show()
print("Hình 6.1: Tương quan giữa OverallQual và SalePrice")
print()

sns.scatterplot(x="GrLivArea", y="SalePrice", data=train)
plt.title("GrLivArea vs. SalePrice")
plt.show()
print("Hình 6.2: Tương quan giữa GrLivArea và SalePrice")
print()
print()
