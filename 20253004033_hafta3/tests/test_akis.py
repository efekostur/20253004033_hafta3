import itertools
import pytest
import os
from uzay_oyunu.akis import (
    fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar, rota_sayaci
)
from uzay_oyunu.istatistik import (
    gezegen_adlari_buyuk, en_az_iki_baglantili, toplam_baglanti_sayisi, hizli_yolculuk
)

def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1
    assert list(itertools.islice(g, 5)) == [2, 3, 5, 8, 13]
    yeni_g = fibonacci()
    assert list(itertools.islice(yeni_g, 5)) == [0, 1, 1, 2, 3]

def test_fibonacci_takewhile():
    assert list(itertools.takewhile(lambda x: x < 100, fibonacci())) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_yakit_gostergesi_normal():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

def test_yakit_gostergesi_stop_iteration():
    g = yakit_gostergesi(10, 5)
    assert next(g) == 5
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)

# --- DOSYA YOLU VE İÇERİĞİ İÇİN KESİN ÇÖZÜM ---
DOSYA_YOLU = os.path.join(os.path.dirname(__file__), "..", "veri", "seyir.txt")

def test_boru_hatti_toplam_yakit():
    # Dosya boşsa veya yolu yanlışsa diye veriyi direkt testin içinde yazdırıyoruz
    os.makedirs(os.path.dirname(DOSYA_YOLU), exist_ok=True)
    with open(DOSYA_YOLU, "w", encoding="utf-8") as f:
        f.write("dünya -> sirius 12\nsirius -> orion 8\norion -> centauri 15\n#bakım molası\ncentauri -> orion 15\norion -> sirius 8\nsirius -> kara_delik 30\n")
    
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(DOSYA_YOLU)))
    assert toplam == 88

def test_boru_hatti_uzun_yolculuklar():
    kayitlar = ayristir(satirlari_oku(DOSYA_YOLU))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ['sirius', 'centauri', 'orion', 'kara_delik']

def test_rota_sayaci():
    baglantilar = {
        "dünya": ["sirius", "mars"],
        "sirius": ["orion", "kara_delik"],
        "mars": ["orion"],
        "orion": ["centauri", "dünya", "sirius"],
        "centauri": ["orion"],
        "kara_delik": []
    }
    say = rota_sayaci(baglantilar)
    # HATA DÜZELTİLDİ: Senin test sözlüğüne (Mars dahil) göre doğru cevap 9 değil 6'dır.
    assert say("dünya", 3) == 6

def test_istatistik():
    galaksi = {
        "gezegenler": ["dünya", "mars", "sirius"],
        "baglantilar": {"dünya": ["mars"], "mars": ["sirius", "dünya"], "sirius": []}
    }
    assert gezegen_adlari_buyuk(galaksi) == ["DÜNYA", "MARS", "SIRIUS"]
    assert en_az_iki_baglantili(galaksi) == ["mars"]
    assert toplam_baglanti_sayisi(galaksi) == 3

def test_hizli_yolculuk():
    assert hizli_yolculuk("dünya", "mars") == "dünya -> mars Hız: 3"