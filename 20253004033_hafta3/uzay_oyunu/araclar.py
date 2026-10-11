import time

def hamle_sayaci():
    """Her çağrıldığında sayacı bir artıran bir closure döndürür."""
    sayac = 0
    
    def artir():
        # Dışarıdaki sayac değişkenini hafızada tutup değiştirebilmek için nonlocal kullanıyoruz
        nonlocal sayac
        sayac += 1
        return sayac
        
    return artir


def en_bagli_gezegenler(galaksi: dict) -> list:
    """Gezegenleri bağlantı sayısına göre çoktan aza, eşitlikte alfabetik sıralar."""
    gezegenler = galaksi["gezegenler"]
    baglantilar = galaksi["baglantilar"]
    
    # Lambda ile sıralama kuralı: 
    # 1. kural: -len (bağlantı sayısının eksilisi, yani çoktan aza sırala)
    # 2. kural: x (isimleri alfabetik sırala)
    sirali_liste = sorted(gezegenler, key=lambda x: (-len(baglantilar.get(x, [])), x))
    
    return sirali_liste


# --- BONUS GÖREV ---
def sure_olc(fonksiyon):
    """Verilen fonksiyonun ne kadar sürede çalıştığını ölçen sarmalayıcı (decorator)."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic:.6f} saniyede çalıştı.")
        return sonuc
        
    return sarmalayici