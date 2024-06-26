import pandas as pd
import economic_complexity as ec
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu "tự sinh" từ file excel
df = pd.read_excel('data_sample.xlsx')
# print(df)

# Chuyển đổi pivot table để tính RCA
tbl = pd.pivot_table(df, index=['City'], columns=['Section'], values='Patents').reset_index().set_index(
    'City').dropna(axis=1, how="all").fillna(0).astype(float)

# RCA
rca = ec.rca(tbl)

# Xây dựng chỉ số ECI và PCI qua package economic_complexity
eci_value, pci_value = ec.complexity(rca)

# Tạo dataframe chứa cột ECI và PCI
eci = eci_value.to_frame(name="ECI").reset_index()
pci = pci_value.to_frame(name="PCI").reset_index()

print("3 Highest ECIs")
print(eci.sort_values(by='ECI', ascending=False).head(3))
print("\n3 Highest PCIs")
print(pci.sort_values(by='PCI', ascending=False).head(3))

# Vẽ biểu đồ cho 5 thành phố có ECI cao nhất
top_eci = eci.sort_values(by='ECI', ascending=False).head(3)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_eci, x='ECI', y='City', palette='viridis')
plt.title('Top 3 Cities by ECI')
plt.xlabel('ECI')
plt.ylabel('City')

# Thêm giá trị lên các thanh
for index, value in enumerate(top_eci['ECI']):
    plt.text(value, index, f'{value:.2f}', va='center')

plt.show()

# Vẽ biểu đồ cho 5 ngành có PCI cao nhất
top_pci = pci.sort_values(by='PCI', ascending=False).head(3)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_pci, x='PCI', y='Section', palette='viridis')
plt.title('Top 3 Sections by PCI')
plt.xlabel('PCI')
plt.ylabel('Section')

# Thêm giá trị lên các thanh
for index, value in enumerate(top_pci['PCI']):
    plt.text(value, index, f'{value:.2f}', va='center')

plt.show()
