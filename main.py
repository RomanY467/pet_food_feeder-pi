from time import sleep
import gspread

from Feed_Servo import feed

# This is the path to the json file downloaded from Google API
path = "/Users/romancuellar/Documents/DataCamp/" \
    "Projects/FoodFeeder/credentials.json"

# This is the name of the spreadsheet
sa = gspread.service_account(filename=path)
sh = sa.open("Chacho")

# This is the name of the sheet
wks = sh.worksheet("info")

print("Rows: " + str(wks.row_count))
print("Columns: " + str(wks.col_count))

# Chequea cada 20 segundos si hay que activar el alimento
# Detecta si se ha cambiado el valor de "Testeo" a "Si"
while (1):
    # get value from B1
    valorActivar = wks.acell('B1').value
    valorTestear = wks.acell('B3').value

    if (valorActivar == "Si"):
        print("Alimentando...")
        # Aqui va el modulo de alimentar
        # Setea el valor de B1 a "No"
        wks.update_acell('B1', "No")
        feed()
        Activar = False
        sleep(5)
    elif (valorActivar == "No"):
        print("No alimentar")
        sleep(5)
    else:
        print("Formato incorrecto en B1")

    if (valorTestear == "Si"):
        print("Testeando...")
        # Setea el valor de B3 a "No"
        wks.update_acell('B3', "No")
        sleep(5)
