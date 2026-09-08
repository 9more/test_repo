import requests
from pathlib import Path


def download_file(url, output_path):
    output_path = Path(output_path)

    if output_path.exists():
        print(f"File already exists: {output_path}")
        return

    response = requests.get(url, stream=True, timeout=60)

    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    downloaded = 0

    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)

                if total_size:
                    progress = downloaded / total_size * 100
                    print(f"\rDownloading: {progress:.1f}%", end="")

    print("\nDownload complete.")


url = "https://www.kaggle.com/api/v1/datasets/download/abhinav89/telecom-customer"
output_path = "data/raw/telecom-customer.zip"

download_file(url, output_path)
