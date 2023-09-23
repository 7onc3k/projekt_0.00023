import os
from PIL import Image
import pillow_avif

def kompresuj_obrazek(soubor, kvalita=85):
    with Image.open(soubor) as obrazek:
        obrazek = obrazek.convert("RGB")
        avif_soubor = os.path.splitext(soubor)[0] + ".avif"
        obrazek.save(avif_soubor, "AVIF", quality=kvalita)
    os.remove(soubor)

def main():
    aktualni_slozka = os.path.dirname(os.path.realpath(__file__))
    seznam_obrazku = [s for s in os.listdir(aktualni_slozka) if s.lower().endswith(('.png', '.jpg', '.jpeg'))]
    celkovy_pocet = len(seznam_obrazku)
    
    for index, soubor in enumerate(seznam_obrazku, 1):
        cesta_k_souboru = os.path.join(aktualni_slozka, soubor)
        try:
            kompresuj_obrazek(cesta_k_souboru)
            procentualni_hotovost = (index / celkovy_pocet) * 100
            print(f"Obrázek {soubor} byl úspěšně převeden na AVIF. Hotovo: {procentualni_hotovost:.2f}%")
        except Exception as chyba:
            print(f"Při převodu obrázku {soubor} do AVIF došlo k chybě: {chyba}")

if __name__ == "__main__":
    main()