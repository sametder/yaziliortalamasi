vize = int(input("Vize sinav notunu giriniz(%30 Ortalama Etkisi): "))
vize = (vize * 30 / 100)
final = int(input("Final sinav notunu giriniz(%40 Ortalama Etkisi): "))
if final < 40 :
    print("Final notu 40'dan düşük bu sebeple kaldiniz! ")
else:
    final = (final * 40 / 100)
final_uygulamasi = int(input("Final uygulama notunu giriniz(%30 Ortalama Etkisi): "))
if final_uygulamasi < 40 :
    print("Uygulama notu 40'dan düşük bu sebeple kaldiniz! ")
else:
    final_uygulamasi = (final_uygulamasi * 30 / 100)
ortalama = final + final_uygulamasi + vize
if ortalama > 85:
    print(f'AA ile geçtiniz, tebrikler ve ortalamaniz: {ortalama}')
elif ortalama <85 and ortalama >= 70:
    print(f'BB ile geçtiniz, tebrikle ve ortlamaniz: {ortalama}')
elif ortalama < 70 and ortalama >= 55:
    print(f'CC ile geçtiniz, tebrikle ve ortlamaniz: {ortalama}')
elif ortalama < 55 and ortalama >= 40:
    print(f'DC ile geçtiniz, tebrikle ve ortlamaniz: {ortalama}')
else:
    print(f'Kaldiniz, ortalama: {ortalama}')