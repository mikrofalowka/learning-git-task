lista_zakupow = {
    "warzywniak":["cukinia","baklazan","dynia"],
    "miesny":["kurczak","boczek","szynka"],
    "kwiaciarnia":["tulipany","ziemia","nawoz","pelargonia"]
}

ilosc_produktow = 0

for sklep, artykul in lista_zakupow.items():
    print(f"Ide do {str(sklep).title()} i kupuje tam {str(artykul).title()}")
    ilosc_produktow = ilosc_produktow + len(lista_zakupow[sklep])

print(f"W sumie kupuje {ilosc_produktow} produktow")