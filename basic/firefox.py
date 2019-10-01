import openpyxl
from openpyxl import Workbook
from unidecode import unidecode


my_list = ['первый', "второй", "третий"]
# my_list = [1, 2, 3]

wb = Workbook()
ws = wb.active
file_name = "001_file.xlsx"
# file_opened = openpyxl.load_workbook(filename=file_name, read_only=False)
# active_sheet = file_opened.active
# data_file = active_sheet.values
# data_file = list(data_file)
ws.append(my_list)
wb.save(file_name)

# my_file = open("000_file.txt", "w")

wb.close()
