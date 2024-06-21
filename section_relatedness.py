import pandas as pd
import numpy as np

from utils import extract_sectors, plot_heatmap

# Đọc dữ liệu từ Excel
file_path = 'Sangche_HCM_Items_51_1000.xlsx'
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
relatedness_jaccard = np.zeros((len(sectors), len(sectors)))

for i in range(len(sectors)):
    for j in range(len(sectors)):
        if co_occurrence_matrix[i][j] > 0:
            relatedness_jaccard[i][j] = co_occurrence_matrix[i][j] / (
                        co_occurrence_matrix[i][i] + co_occurrence_matrix[j][j] - co_occurrence_matrix[i][j])

# Tính Association Strength
relatedness_association = np.zeros((len(sectors), len(sectors)))

for i in range(len(sectors)):
    for j in range(len(sectors)):
        if co_occurrence_matrix[i][j] > 0:
            relatedness_association[i][j] = co_occurrence_matrix[i][j] / (
                        np.sqrt(co_occurrence_matrix[i][i] * co_occurrence_matrix[j][j]))

# Tính Probability
relatedness_prob = np.zeros((len(sectors), len(sectors)))

total_occurrences = np.sum(co_occurrence_matrix)

for i in range(len(sectors)):
    for j in range(len(sectors)):
        if co_occurrence_matrix[i][j] > 0:
            relatedness_prob[i][j] = co_occurrence_matrix[i][j] / total_occurrences

relatedness_jaccard_df = pd.DataFrame(relatedness_jaccard, index=list(sectors), columns=list(sectors))
relatedness_association_df = pd.DataFrame(relatedness_association, index=list(sectors), columns=list(sectors))
relatedness_prob_df = pd.DataFrame(relatedness_prob, index=list(sectors), columns=list(sectors))

print("Jaccard Similarity:")
print(relatedness_jaccard_df)
print("\nAssociation Strength:")
print(relatedness_association_df)
print("\nProbability:")
print(relatedness_prob_df)

plot_heatmap(relatedness_jaccard_df, "Jaccard Similarity")
plot_heatmap(relatedness_association_df, "Association Strength")
plot_heatmap(relatedness_prob_df, "Probability")
