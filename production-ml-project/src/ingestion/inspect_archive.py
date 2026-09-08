from zipfile import ZipFile

archive_path = "data/raw/telecom-customer.zip"

with ZipFile(archive_path, "r") as archive:
    print(archive.namelist())
