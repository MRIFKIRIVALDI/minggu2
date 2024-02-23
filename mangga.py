mangga = int(input("Berapa kg mangga yang di beli :"))
if mangga <= 2 :
    harga = 20_000 * mangga
elif mangga >2 ^ mangga<=5 :
    harga = 18_000 * mangga
else :
    harga = 16_000 * mangga   
    
print("harga yang harus di bayar untuk membeli",mangga,"kilo mangga adalah",harga)