import openpyxl


def load(path):
    wb = openpyxl.load_workbook(path)
    ws = wb.active

    list = []

    for row in ws.iter_rows(values_only=True):
        list.append([row[0], row[1], row[2]])
    
    return list