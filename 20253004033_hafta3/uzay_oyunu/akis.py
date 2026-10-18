from typing import Generator
import itertools
from functools import lru_cache

def fibonacci() -> Generator[int, None, None]:
    """Sonsuz bir Fibonacci dizisi üreten üreteç."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Yakıtı tüketim kadar azaltır, bitince durur."""
    kalan = yakit
    while kalan >= tuketim:
        kalan -= tuketim
        yield kalan
    if kalan > 0:
         yield 0

def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyayı satır satır okur."""
    with open(yol, 'r', encoding='utf-8') as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz

def ayristir(satirlar: Generator[str, None, None]) -> Generator[tuple[str, str, int], None, None]:
    """Satırları ayrıştırıp demet döndürür."""
    for satir in satirlar:
        parcalar = satir.split(" ")
        yield (parcalar[0], parcalar[2], int(parcalar[3]))

def uzun_yolculuklar(kayitlar: Generator[tuple[str, str, int], None, None], esik: int) -> Generator[tuple[str, str, int], None, None]:
    """Yakıtı eşikten büyük olanları filtreler."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit

def rota_sayaci(baglantilar: dict):
    """Önbellekli rota sayacı."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        for hedef in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(hedef, adim - 1)
        return toplam
    return rota_sayisi