import openpyxl
from openpyxl import Workbook
from unidecode import unidecode


# a = []
# b = []
# ass = ()
# print(type(ass))
# a.append(5)
# a.append(6)
# b.append(a)
# a = []
# a.append(45)
# b.append(a)
# print(a)
# print(b)


wb = Workbook()
ws = wb.active
file_name = "001_cosmo_file.xlsx"
# ws.append(b[2])
wb.save(file_name)

# my_file = open("000_file.txt", "w")

wb.close()
