import numpy as np
import folium

# Sentetik veri oluşturma (Nüfus Yoğunluğu, Ulaşım Altyapısı, Maliyet, Çevresel Etki, Sosyal Fayda)
mahalleler = {
    "İstasyon Mahallesi": [800, 7, -50, -20, 60],
    "Pınar Mahallesi": [500, 5, -30, -15, 45],
    "Karakaş Mahallesi": [1000, 8, -70, -25, 75]
}

# Softmax fonksiyonu
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Sayısal stabilite için max çıkarma
    return exp_x / exp_x.sum()

# Verileri numpy dizisine çevirme ve Softmax hesaplama
data = np.array(list(mahalleler.values()))
weights = softmax(data.sum(axis=1))

# Sonuçları yazdırma
en_uygun = list(mahalleler.keys())[np.argmax(weights)]
print("Mahalle Ağırlıkları:")
for i, mahalle in enumerate(mahalleler.keys()):
    print(f"{mahalle}: {weights[i]:.2f}")
print(f"\nEn uygun güzergah: {en_uygun}")

# Harita çıktısı oluşturma
harita = folium.Map(location=[41.7333, 27.2167], zoom_start=13)
koordinatlar = {
    "İstasyon Mahallesi": [41.735, 27.210],
    "Pınar Mahallesi": [41.740, 27.220],
    "Karakaş Mahallesi": [41.750, 27.230]
}

# Mahalleleri haritaya ekleme
for mahalle, coord in koordinatlar.items():
    folium.Marker(location=coord, popup=f"{mahalle}").add_to(harita)

# En uygun güzergahı işaretleme
folium.Marker(location=koordinatlar[en_uygun],
              popup=f"En Uygun: {en_uygun}",
              icon=folium.Icon(color="red", icon="info-sign")).add_to(harita)

# Haritayı kaydetme
harita.save("kirklareli_transport.html")
print("Harita 'kirklareli_transport.html' olarak kaydedildi.") 
