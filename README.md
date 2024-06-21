# economic_compound_index
Tống Đức Minh 20216855

# Yêu Cầu
+ Tải các package (có thể sử dụng qua pip)
+ `pip install pandas`
+ `pip install numpy`
+ `pip install economic_complexity`
+ `pip install matplotlib`

# Bộ Dữ Liệu
## Bằng sáng chế thành phố Hồ Chí Minh
+ File excel: Sangche_HCM_Items_51_1000.xlsx

## Bộ dữ liệu dùng để tính chỉ số ECI và PCI
+ File excel: data_sample.xlsx
+ Đây là bộ dữ liệu được sinh ngẫu nhiên để tính toán chỉ số ECI giữa các thành phố và PCI giữa các ngành
+ Cột 'Country': tên thành phố
+ Cột 'Section': mã ngành
+ Cột 'Patents': số lượng bằng sáng chế theo mã ngành của từng thành phố (dữ liệu được sinh ngẫu nhiên)

## Chú thích các ngành theo chuẩn IPC
A: CÁC NHU CẦU CỦA ĐỜI SỐNG CON NGƯỜI\
B: CÁC QUY TRÌNH CÔNG NGHỆ; GIAO THÔNG VẬN TẢI\
C: HOÁ HỌC; LUYỆN KIM\
D: DỆT; GIẤY\
E: XÂY DỰNG; MỎ\
F: CƠ KHÍ; CHIẾU SÁNG; CẤP NHIỆT; VŨ KHÍ; KỸ THUẬT NỔ\
G: VẬT LÝ\
H: ĐIỆN

# Đếm số lượng bằng sáng chế theo từng ngành của thành phố Hồ Chí Minh
+ File tính toán: section_count.py

# Tính chỉ số Relatedness giữa các ngành của thành phố Hồ Chí Minh
+ File tính toán: section_relatedness.py

# Tính chỉ số ECI (Economic Complexity Index) giữa các thành phố và PCI (Product Complexity Index) giữa các ngành
+ File tính toán: eci_calculate.py

# Tính chỉ số Relatedness giữa các thành phố và các ngành
+ File tính toán: section_city_relatedness.py