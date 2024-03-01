english = int(input("Masukan nilai B. inggris :"))
mtk = int(input("masukan nilai mtk :"))
indo = int(input("masukan nilai B. indo :"))
ipa = int(input("masukan nilai IPA :"))
ips = int(input("masukan nilai IPS :"))

planA = (english+mtk+indo)/3
planB = (english+mtk+indo+ipa+ips)/5

if planA >= 75:
    hasil = "lulus"
elif planB >= 70:
    hasil = "lulus"  
elif mtk >=90 and english >=90:
    hasil = "lulus"    
else :
    hasil = "Tidak lulus"  

print("anda",hasil,"pada semester ini")

