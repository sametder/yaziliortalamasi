yazili1 = float(input('1.Yazili Notunuzu Girin: '))
yazili2 = float(input('2.Yazili Notunuzu Girin: '))
sozlu = float(input('Sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if  (ortalama >= 0) and (ortalama<25):
    print(f'Ortalamaniz: {ortalama} notunuz: 0')

elif  (ortalama >= 25) and (ortalama<44):
    print(f'Ortalamaniz: {ortalama} notunuz: 1')

elif  (ortalama >= 45) and (ortalama<55):
    print(f'Ortalamaniz: {ortalama} notunuz: 2')
    
elif  (ortalama >= 55) and (ortalama<70):
    print(f'Ortalamaniz: {ortalama} notunuz: 3')

elif  (ortalama >= 70) and (ortalama<85):
    print(f'Ortalamaniz: {ortalama} notunuz: 4')

elif  (ortalama >= 85) and (ortalama<=100):
    print(f'Ortalamaniz: {ortalama} notunuz: 5')

else: 
    print('Yanliş bilgi girdiniz! ')