
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
