import xlrd

wb = xlrd.open_workbook('D:\Book1.xlsx')
sheet = wb.sheet_by_name('Sheet1')

for r in range(1, sheet.nrows):
    invoicedate = str(sheet.cell(r,0).value)
    print(invoicedate)