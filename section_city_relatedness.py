import pandas as pd
import economic_complexity as ec
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file Excel
file_path = 'data_sample.xlsx'
df = pd.read_excel(file_path)

# Chuyển đổi pivot table để tính RCA
tbl = pd.pivot_table(df, index=['City'], columns=['Section'], values='Patents').reset_index().set_index('City').dropna(
    axis=1, how="all").fillna(0).astype(float)

# Tính RCA
rca = ec.rca(tbl)

# proximity
phi = ec.proximity(rca)

# relatedness
relatedness = ec.relatedness(rca, proximities=phi)

relatedness_df = pd.DataFrame(relatedness)

# Vẽ biểu đồ
plt.figure(figsize=(12, 8))
sns.heatmap(relatedness_df, annot=True, cmap='coolwarm')
plt.title('Relatedness between Cities and Sectors')
plt.xlabel('Sectors')
plt.ylabel('Cities')
plt.show()
