"""
Téléchargement du dataset CO₂ depuis Our World in Data.

Source : https://github.com/owid/co2-data
Licence : Creative Commons BY

Usage :
    python data/download_data.py
"""

import os
import sys
from pathlib import Path

import requests
from tqdm import tqdm

SCRIPT_DIR = Path(__file__).parent
RAW_DIR = SCRIPT_DIR / "raw"
SAMPLE_DIR = SCRIPT_DIR / "sample"

# Sources de données
SOURCES = {
    "owid-co2-data.csv": "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv",
    "owid-co2-codebook.csv": "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-codebook.csv",
}


def download_file(url: str, filepath: Path, retries: int = 3) -> bool:
    """Télécharge un fichier avec barre de progression."""
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, stream=True, timeout=60)
            response.raise_for_status()

            total_size = int(response.headers.get("content-length", 0))

            with open(filepath, "wb") as f:
                with tqdm(
                    total=total_size, unit="B", unit_scale=True,
                    desc=f"  {filepath.name}", leave=True,
                ) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
            return True

        except requests.RequestException as e:
            if attempt < retries:
                print(f"  ⚠️  Tentative {attempt}/{retries} échouée : {e}")
            else:
                print(f"  ❌ Échec après {retries} tentatives : {e}")
                return False
    return False


def create_sample(n_rows: int = 500) -> None:
    """Crée un petit échantillon pour tests."""
    import pandas as pd

    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    sample_path = SAMPLE_DIR / f"sample_{n_rows}.csv"

    if sample_path.exists():
        print(f"\n✓ Échantillon déjà présent : {sample_path.name}")
        return

    source = RAW_DIR / "owid-co2-data.csv"
    if not source.exists():
        print("\n⚠️  Données non trouvées pour créer l'échantillon.")
        return

    print(f"\n📝 Création de l'échantillon...")
    df = pd.read_csv(source, nrows=n_rows)
    df.to_csv(sample_path, index=False)
    print(f"  ✓ {sample_path.name} créé ({len(df)} lignes)")


def main():
    print("=" * 60)
    print("📥 Téléchargement des données CO₂")
    print("   Source : Our World in Data (GitHub)")
    print("=" * 60)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    for filename, url in SOURCES.items():
        filepath = RAW_DIR / filename

        if filepath.exists() and filepath.stat().st_size > 0:
            print(f"\n✓ {filename} déjà présent ({filepath.stat().st_size / 1e6:.1f} Mo)")
            success += 1
            continue

        print(f"\n↓ Téléchargement de {filename}...")
        if download_file(url, filepath):
            success += 1

    create_sample()

    print("\n" + "=" * 60)
    print(f"📊 Bilan : {success}/{len(SOURCES)} fichiers OK")
    print("=" * 60)


if __name__ == "__main__":
    main()
