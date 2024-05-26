import urllib.request
import tarfile
import os

# URL of the file (using IP address)
url = "ftp://192.35.51.30/pub/cert-data/r4.2.tar.bz2"  # Replace with the actual IP address you found
local_filename = "r4.2.tar.bz2"

try:
    # Download the file with a timeout
    response = urllib.request.urlopen(url, timeout=60)  # 60 seconds timeout
    with open(local_filename, "wb") as local_file:
        local_file.write(response.read())
    print("Download complete.")

    # Extract the downloaded .tar.bz2 file
    with tarfile.open(local_filename, "r:bz2") as tar:
        tar.extractall(path="extracted_files")

    # Optional: Display the names of extracted files
    extracted_files = os.listdir("extracted_files")
    print("Extracted Files:", extracted_files)

    # Optional: Clean up by removing the downloaded tar.bz2 file
    os.remove(local_filename)

    print("Download and extraction complete.")

except urllib.error.URLError as e:
    print("URL error:", e)
except urllib.error.HTTPError as e:
    print("HTTP error:", e)
except Exception as e:
    print("An error occurred:", e)
