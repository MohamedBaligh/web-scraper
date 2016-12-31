from openpyxl import load_workbook

wb = load_workbook(filename = 'sample.xlsx')
#print wb.__dict__
x =  wb['abc']
print x['C3'].value
