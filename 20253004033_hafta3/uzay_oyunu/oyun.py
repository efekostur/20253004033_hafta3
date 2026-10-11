import json

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Kullanıcının mevcut eşyalarına göre durum metni döndürür."""
    if not credits and not engines and not copilot:
        return ""
    
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motor")
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek gezegenleri numaralandırarak bir menü oluşturur."""
    metin = "Nereye gitmek istersin?\n"
    for i, hedef in enumerate(hedefler, 1):
        metin += f"[{i}] {hedef}\n"
        
    return metin.strip()


def galaksi_kur(gezegenler: list, baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """JSON verilerinden okunan bilgilerle oyun haritasını oluşturur."""
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede bulunamadı!")
    
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }


if __name__ == "__main__":
    # JSON dosyasını okuyup sözlüğe çevirme işlemi
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    # Veriyi argüman açılımı (**) ile fonksiyona gönderme
    galaksi = galaksi_kur(**veri)
    
    print(f"Oyun başlatıldı. Konum: {galaksi['konum']}, Yakıt: {galaksi['yakit']}")