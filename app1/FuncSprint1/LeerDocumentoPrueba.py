from openpyxl import load_workbook

excel = load_workbook("C:/Users/FABIAN/Documents/GitHub/asistenteHorariosInstructores2/FINAL BANIN.xlsx")

hoja1 = excel['REGULAR']

filas = hoja1.rows
columnas= hoja1.columns



instructores = [cell.value for cell in next (columnas)]

print(instructores)