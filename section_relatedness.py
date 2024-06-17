import pandas as pd
import numpy as np

from utils import extract_sectors

# Đọc dữ liệu từ tệp Excel
file_path = 'Sangche_HCM_Items_51_1000.xlsx'  # Thay bằng đường dẫn thực tế tới tệp Excel
df = pd.read_excel(file_path)

# Xây dựng ma trận đồng xuất hiện
sectors = 'ABCDEFGH'
co_occurrence_matrix = np.zeros((len(sectors), len(sectors)))

for ipc_codes in df['Phân loại IPC']:
    present_sectors = extract_sectors(ipc_codes)
    present_sectors = list(present_sectors)
    for i in range(len(present_sectors)):
        for j in range(i, len(present_sectors)):
            sector_i = sectors.index(present_sectors[i])
            sector_j = sectors.index(present_sectors[j])
            co_occurrence_matrix[sector_i][sector_j] += 1
            if sector_i != sector_j:
                co_occurrence_matrix[sector_j][sector_i] += 1

# Tính chỉ số Jaccard
relatedness_matrix = np.zeros((len(sectors), len(sectors)))

for i in range(len(sectors)):
    for j in range(len(sectors)):
        if co_occurrence_matrix[i][j] > 0:
            relatedness_matrix[i][j] = co_occurrence_matrix[i][j] / (
                        co_occurrence_matrix[i][i] + co_occurrence_matrix[j][j] - co_occurrence_matrix[i][j])

# Chuyển đổi ma trận thành DataFrame để dễ dàng xem kết quả
relatedness_df = pd.DataFrame(relatedness_matrix, index=list(sectors), columns=list(sectors))

# Hiển thị ma trận relatedness
print(relatedness_df)
