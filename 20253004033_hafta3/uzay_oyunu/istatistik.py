import functools

def gezegen_adlari_buyuk(galaksi: dict) -> list[str]:
    """Gezegen adlarını büyük harfe çevirir."""
    # map kullanımı yerine liste üreteci daha okunaklı:
    return [gezegen.upper() for gezegen in galaksi["gezegenler"]]

def en_az_iki_baglantili(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenler."""
    # filter kullanımı yerine liste üreteci daha net anlaşılıyor:
    return [gezegen for gezegen in galaksi["gezegenler"] if len(galaksi["baglantilar"].get(gezegen, [])) >= 2]

def toplam_baglanti_sayisi(galaksi: dict) -> int:
    """Toplam bağlantı sayısı."""
    # reduce yerine sum kullanımı Python'un doğasına daha uygundur:
    return sum(len(baglantilar) for baglantilar in galaksi["baglantilar"].values())

def yolculuk(kaynak: str, hedef: str, hiz: int) -> str:
    return f"{kaynak} -> {hedef} Hız: {hiz}"

hizli_yolculuk = functools.partial(yolculuk, hiz=3)

# Yorum: Yüksek seviyeli ve fonksiyonel (map/filter/reduce) yapılar güçlü olsa da, 
# Python'da liste üreteçleri (list comprehensions) ve 'sum' kullanımı 
# ne yapılmak istendiğini çok daha okunabilir ve anlaşılır kılar.