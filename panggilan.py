umur = int(input(" Masukan umur anda:"))
if umur <=2:
    hasil = "bayi"
elif umur >2 ^ umur <=5:
    hasil = "balita"  
elif umur >5 ^ umur<=12:
    hasil = "anak-anak"
elif umur >12 ^ umur<=17 :
    hasil = "remaja"
elif umur >17 ^ umur<=30:
    hasil = "dewasa"
elif umur >30:
    hasil = "orang tua" 
print("anda termasuk golongan",hasil)         