import os
import glob

# Resimlerin bulunduğu klasörün yolu
klasor_yolu = "C:\\Users\\aliha\\OneDrive\\Masaüstü\\Beyin_kis_tespiti\\data\\dataset"

# Klasördeki tüm resim/txt dosyalarını bul
resimler_txt = glob.glob(os.path.join(klasor_yolu, "*.jpg"))
# txt yerine jpg yazarak yeniden adlandırabiliriz... resimler için
# print(resimler_txt)

# Yeniden adlandırma işlemi
for i, eski_ad in enumerate(resimler_txt, start=1):
    yeni_ad = os.path.join(klasor_yolu, f"{i}.jpg")
    os.rename(eski_ad, yeni_ad)
    print(f"{eski_ad} dosyası {yeni_ad} olarak yeniden adlandırıldı.")
