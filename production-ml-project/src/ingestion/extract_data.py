from zipfile import ZipFile
from pathlib import Path

archive_path = Path("data/raw/telecom-customer.zip")
output_dir = Path("data/raw")


with ZipFile(archive_path, "r") as archive:
    archive.extractall(output_dir)

print("Dataset extracted successfully.")
