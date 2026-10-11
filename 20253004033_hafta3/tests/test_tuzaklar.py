# Eğer listeyi parametrede varsayılan olarak depo=[] diye tanımlasaydık, 
# liste hafızada asılı kalır ve her geminin yakıtı birbirine karışırdı.
# Bu tuzağı çözmek için 'None kalıbı' kullanıyoruz.

def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_bagimsiz_calismali():
    # İki farklı uzay gemisine yakıt ekliyoruz
    gemi1 = yakit_ekle(10)
    gemi2 = yakit_ekle(20)
    
    # Eğer None kalıbı çalışıyorsa, listeler birbirine karışmamış olmalı
    assert gemi1 == [10]
    assert gemi2 == [20]