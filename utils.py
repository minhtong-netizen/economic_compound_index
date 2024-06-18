import matplotlib.pyplot as plt
import seaborn as sns


# Hàm để lấy các ngành từ cột "Phân loại IPC"
def extract_sectors(ipc_code):
    valid_sectors = 'ABCDEFGH'
    sectors_set = set()
    for code in ipc_code.split(','):
        code = code.strip()
        if len(code) > 0:
            if code[0] in valid_sectors:
                sectors_set.add(code[0])
            if code[3] in valid_sectors:
                sectors_set.add(code[3])

    return sectors_set


# Hàm vẽ heatmap
def plot_heatmap(data, title):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap='viridis', fmt='.2f', linewidths=.5)
    plt.title(title)
    plt.show()
