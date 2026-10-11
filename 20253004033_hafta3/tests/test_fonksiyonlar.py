def test_envanter_metni():
    from uzay_oyunu.oyun import envanter_metni
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""

def test_hedef_menusu():
    from uzay_oyunu.oyun import hedef_menusu
    assert hedef_menusu(["centauri", "sirius"]) == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"