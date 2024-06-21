import pandas as pd
import matplotlib.pyplot as plt

from utils import extract_sectors

if __name__ == '__main__':
    # Đọc dữ liệu từ Excel
    file_path = 'Sangche_HCM_Items_51_1000.xlsx'
    df = pd.read_excel(file_path)

    # Áp dụng hàm trên cột "Phân loại IPC" và đếm số lượng bằng sáng chế cho mỗi ngành
    sector_count = {sector: 0 for sector in 'ABCDEFGH'}

    for ipc_codes in df['Phân loại IPC']:
        sectors = extract_sectors(ipc_codes)
        for sector in sectors:
            if sector in sector_count:
                sector_count[sector] += 1

    sector_df = pd.DataFrame(list(sector_count.items()), columns=['Ngành', 'Số lượng'])

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    bars = plt.bar(sector_df['Ngành'], sector_df['Số lượng'], color='skyblue')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom')  # va: vertical alignment

    plt.xlabel('Ngành')
    plt.ylabel('Số lượng bằng sáng chế')
    plt.title('Số lượng bằng sáng chế theo ngành của thành phố Hồ Chí Minh')
    plt.show()
