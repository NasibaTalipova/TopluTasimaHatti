# Şehir Toplu Taşıma Planlaması

## Proje Tanımı
Bu proje, Şehrin'nin üç farklı mahallesi için en uygun toplu taşıma hattını belirlemek üzerine tasarlanmıştır. Mahallelerin **nüfus yoğunluğu, mevcut ulaşım altyapısı, maliyet, çevresel etki ve sosyal fayda** gibi kriterleri değerlendirilerek **Softmax algoritması** ile her mahalleye ait bir ağırlık hesaplanmış ve en uygun mahalle belirlenmiştir.

Sonuçlar, **OpenStreetMap (Folium) kütüphanesi** kullanılarak harita ücerinde görselleştirilmiştir.

## Kullanılan Teknolojiler
- **Python** (NumPy, Folium, Matplotlib)
- **Softmax Algoritması** (Optimum mahalle seçimi için)
- **OpenStreetMap & Folium** (Harita görselleştirme)

## Softmax Algoritması ile Ağırlık Hesaplama
Softmax fonksiyonu, mahallelere ait kriterleri normalize ederek ağırlıkların belirlenmesini sağlar. Bu sayede **en uygun mahalle** en yüksek ağırlığa sahip olan mahalle olarak seçilir.

```python
import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Sayısal stabilite için maksimum değer çıkarılıyor
    return exp_x / exp_x.sum()
```

### Kriterlerin Belirlenmesi
Her mahalleye ait kriterler aşağıdaki gibi bir **sözlük (dictionary)** formatında tutulur ve **NumPy dizisine** çevrilerek işlenmeye hazır hale getirilir:

```python
mahalleler = {
    "A Mahallesi": [800, 7, -50, -20, 60],
    "B Mahallesi": [500, 5, -30, -15, 45],
    "C Mahallesi": [1000, 8, -70, -25, 75]
}

data = np.array(list(mahalleler.values()))
weights = softmax(data.sum(axis=1))
```
- **Nüfus Yoğunluğu**: Daha yüksek yoğunluk daha fazla toplu taşıma ihtiyacı anlamına gelir.
- **Mevcut Ulaşım Altyapısı**: Daha yüksek değerler daha iyi mevcut altyapıyı gösterir.
- **Maliyet Analizi**: Negatif değerler maliyetin çıktısı olarak ele alınır.
- **Çevresel Etki**: Negatif değerler olumsuz çevresel etkileri gösterir.
- **Sosyal Fayda**: Daha yüksek sosyal fayda değerleri olumlu etkiyi temsil eder.

### En Uygun Mahallenin Seçilmesi

Softmax sonucu en büyük değere sahip mahalle **en uygun mahalle** olarak belirlenir:

```python
en_uygun = list(mahalleler.keys())[np.argmax(weights)]
print(f"En uygun güzergah: {en_uygun}")
```

## OpenStreetMap ile Harita Görselleştirme
Harita görselleştirme için **Folium kütüphanesi** kullanılmıştır. Seçilen mahalle harita üzerinde işaretlenir.

```python
import folium

harita = folium.Map(location=[41.7333, 27.2167], zoom_start=13)
koordinatlar = {
    "A Mahallesi": [41.735, 27.210],
    "B Mahallesi": [41.740, 27.220],
    "C Mahallesi": [41.750, 27.230]
}

for mahalle, coord in koordinatlar.items():
    folium.Marker(location=coord, popup=f"{mahalle}").add_to(harita)

folium.Marker(
    location=koordinatlar[en_uygun],
    popup=f"En Uygun: {en_uygun}",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(harita)
```

### Haritanın Kaydedilmesi ve Kullanımı
Harita **kirklareli_transport.html** olarak kaydedilir ve bir web tarayıcısında açılabilir.

```python
harita.save("kirklareli_transport.html")
print("Harita 'kirklareli_transport.html' olarak kaydedildi.")
```

## Projenin Çalıştırılması

Bu projenin çalıştırılması için **Python 3.x** ve gerekli kütüphanelerin yüklenmiş olması gerekmektedir.

### Bağımlılıkları Yükleme

```bash
pip install numpy folium
```

### Kodu Çalıştırma

```bash
python transport_planning.py
```

Bu komut çalıştırıldıktan sonra **kirklareli_transport.html** dosyası oluşturulacak ve tarayıcıda harita görüntülenebilecektir.

## Sonuç ve Değerlendirme
- **Softmax algoritması**, mahallelerin objektif olarak değerlendirilmesini sağladı.
- **Ağırlık hesaplaması** ile en uygun güzergah belirlendi.
- **Folium kullanılarak harita üzerinde görselleştirme yapıldı.**

Bu proje, veri odaklı karar verme süreçlerinde **makine öğrenmesi tabanlı bir yaklaşım** sunmaktadır. Gelecekte, **gerçek zamanlı veri kaynakları** ve **optimizasyon algoritmaları** ile sistem geliştirilebilir.

