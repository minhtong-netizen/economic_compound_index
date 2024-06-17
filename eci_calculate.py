import pandas as pd
import economic_complexity as ec

# Đọc dữ liệu "tự sinh" từ file excel
df = pd.read_excel('data_sample.xlsx')
print("Dataframe")
print(df)

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

print("5 Highest ECIs")
print(eci.sort_values(by='ECI', ascending=False).head(5))
print("\n5 Highest PCIs")
print(pci.sort_values(by='PCI', ascending=False).head(5))

# rcas = rca
# print(rcas)
#
# # drop columns / rows only if completely nan
# rcas_clone = rcas.copy(deep=True)
# rcas_clone = rcas_clone.dropna(how="all")
# rcas_clone = rcas_clone.dropna(how="all", axis=1)
#
# if rcas_clone.shape != rcas.shape:
#     print(
#             "RCAs contain columns or rows that are entirely comprised of NaN values."
#     )
#     # if drop:
#     #     rcas = rcas_clone
#
# kp = rcas.sum(axis=0)  # sum columns
# kc = rcas.sum(axis=1)  # sum rows
# kp0 = kp.copy()
# kc0 = kc.copy()
#
# iterations = 20
# for i in range(1, iterations):
#     kc_temp = kc.copy()
#     kp_temp = kp.copy()
#     kp = rcas.T.dot(kc_temp) / kp0
#     if i < (iterations - 1):
#         kc = rcas.dot(kp_temp) / kc0
#
# geo_complexity = (kc - kc.mean()) / kc.std()
# prod_complexity = (kp - kp.mean()) / kp.std()
#
#
# print(geo_complexity)
