from PIL import Image
import os
from io import BytesIO

def komprimuj_a_convertuj(soubor):
    # Otevření obrázku pomocí PIL
    s_obrazek = Image.open(soubor)
    
    # Kvalita komprese - začínáme na 90, můžete upravit dle potřeby
    kvalita = 90
    
    while True:
        buffer = BytesIO()  # Použití BytesIO místo listu
        # Uložení obrázku do bufferu s danou kvalitou
        s_obrazek.save(buffer, "WEBP", quality=kvalita)
        
        # Pokud je velikost obrázku menší než 1 MB, ukončíme cyklus
        if len(buffer.getvalue()) < 1 * 1024 * 1024:
            break
        
        # Snížení kvality o 5% pro další iteraci
        kvalita -= 5

        # Kontrola, aby kvalita neklesla pod 10%
        if kvalita < 10:
            print(f"Obrázek {soubor} nelze stáhnout pod 1MB s dostatečnou kvalitou.")
            return

    # Smazání původního souboru
    os.remove(soubor)

    # Uložení obrázku s konečnou kvalitou do souboru
    s_obrazek.save(soubor, "WEBP", quality=kvalita)
    print(f"Obrázek {soubor} byl uložen s kvalitou {kvalita}%.")

if __name__ == "__main__":
    # Iterace přes všechny soubory ve složce
    for soubor in os.listdir():
        if soubor.lower().endswith(('.png', '.jpg', '.jpeg')):
            komprimuj_a_convertuj(soubor)
