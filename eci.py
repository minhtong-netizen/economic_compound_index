# import pandas as pd
# import numpy as np
#
# # TODO: This is still in development stage
#
# # Đọc dữ liệu từ tệp Excel
# file_path = 'Sangche_HCM_Items_51_1000.xlsx'  # Thay bằng đường dẫn thực tế tới tệp Excel
# df = pd.read_excel(file_path)
#
#
# # Hàm để lấy các ngành từ cột "Phân loại IPC"
# def extract_sectors(ipc_code):
#     valid_sectors = 'ABCDEFGH'
#     sectors = set()
#     for code in ipc_code.split(','):
#         code = code.strip()
#         if len(code) > 3 and code[0] in valid_sectors and code[3] in valid_sectors:
#             sectors.add(code[0])
#             sectors.add(code[3])
#     return sectors
#
#
# # Tạo ma trận xuất hiện ngành
# sectors = 'ABCDEFGH'
# sector_count = {sector: 0 for sector in sectors}
#
# for ipc_codes in df['Phân loại IPC']:
#     present_sectors = extract_sectors(ipc_codes)
#     for sector in present_sectors:
#         if sector in sector_count:
#             sector_count[sector] += 1
#
# # Tạo ma trận tần suất xuất hiện
# frequency_matrix = np.zeros((1, len(sectors)))
#
# for ipc_codes in df['Phân loại IPC']:
#     present_sectors = extract_sectors(ipc_codes)
#     for sector in present_sectors:
#         if sector in sectors:
#             sector_idx = sectors.index(sector)
#             frequency_matrix[0][sector_idx] += 1
#
# # Tạo ma trận đồng phức tạp (Adjacency Matrix)
# adjacency_matrix = np.dot(frequency_matrix.T, frequency_matrix)
#
# # Tính giá trị riêng và vector riêng
# eig_values, eig_vectors = np.linalg.eig(adjacency_matrix)
#
# print(eig_values, type(eig_values))
#
# # Chọn vector riêng tương ứng với giá trị riêng lớn thứ hai
# eig_vector_complexity = eig_vectors[:, np.argsort(eig_values)[-2]]
#
# # Chuẩn hóa vector riêng để có chỉ số phức tạp (ECI)
# eci = eig_vector_complexity - np.mean(eig_vector_complexity)
# eci = eci / np.std(eci)
#
# # Tạo DataFrame kết quả
# eci_df = pd.DataFrame(eci, index=list(sectors), columns=['ECI'])
# eci_df = eci_df.sort_values(by='ECI', ascending=False)
#
# # Hiển thị kết quả
# print(eci_df)
