# economic_compound_index

# Yêu Cầu
+ Tải các package (có thể sử dụng qua pip)
+ `pip install pandas`
+ `pip install numpy`
+ `pip install economic_complexity`

# Bộ Dữ Liệu
## Bằng sáng chế thành phố Hồ Chí Minh
+ File excel: Sangche_HCM_Items_51_1000.xlsx

## Bộ dữ liệu dùng để tính chỉ số ECI và PCI
+ File excel: data_sample.xlsx
+ Đây là bộ dữ liệu được sinh ngẫu nhiên để tính toán chỉ số ECI giữa các thành phố và PCI giữa các ngành
+ Cột 'Country': tên thành phố
+ Cột 'Section': mã ngành
+ Cột 'Patents': số lượng bằng sáng chế theo mã ngành của từng thành phố (dữ liệu được sinh ngẫu nhiên)

# Đếm số lượng bằng sáng chế theo từng ngành của thành phố Hồ Chí Minh
+ File tính toán: section_count.py

# Tính chỉ số Relatedness giữa các ngành của thành phố Hồ Chí Minh
+ File tính toán: section_relatedness.py

# Tính chỉ số ECI (Economic Complexity Index) giữa các thành phố
+ File tính toán: eci_calculate.py