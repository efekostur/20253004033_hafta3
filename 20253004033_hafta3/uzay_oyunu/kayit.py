def gorev_kaydi(baslik: str, *adimlar, oncelik: str = "normal", **ekler) -> str:
    """Görev başlığını, alt adımlarını ve ek bilgileri formatlayıp metne dönüştürür."""
    sonuc = f"[{oncelik.upper()}] {baslik}\n"
    
    for i, adim in enumerate(adimlar, 1):
        sonuc += f"{i}. {adim}\n"
        
    for anahtar, deger in ekler.items():
        sonuc += f"{anahtar}: {deger}\n"
        
    return sonuc.strip()

if __name__ == "__main__":
    # Parametreleri doğrudan girerek çağırma
    print(gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="yüksek", sorumlu="Ayşe"))
    
    print("-" * 20)
    
    # Listeleri ve sözlükleri açarak (unpacking) çağırma
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    
    print(gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ek_bilgiler))