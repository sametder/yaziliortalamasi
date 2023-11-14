# Kullanıcıdan notları al
vize_notu = float(input("Vize notunuzu girin: "))
final_notu = float(input("Final notunuzu girin: "))
final_uygulama_notu = float(input("Final uygulaması notunuzu girin: "))

# Notları kontrol et ve ortalama hesapla
if final_notu < 40 or final_uygulama_notu < 40:
    ortalama = (vize_notu * 0.3) + (final_notu * 0.4) + (final_uygulama_notu * 0.3)  # Eğer final veya final uygulaması notu 40'ın altındaysa dersten kalacak
    durum = "Başarisiz"
else:
    # Ortalama hesapla
    ortalama = (vize_notu * 0.3) + (final_notu * 0.4) + (final_uygulama_notu * 0.3)

    # Başarı durumunu belirle
    if ortalama >= 85:
        durum = "AA"
    elif 70 <= ortalama < 85:
        durum = "BB"
    elif 55 <= ortalama < 70:
        durum = "CC"
    elif 40 <= ortalama < 55:
        durum = "DC"
    else:
        durum = "Başarisiz"

# Sonucu ekrana yazdır
print("Ortalamaniz:", ortalama)
print("Başari Durumu:", durum)