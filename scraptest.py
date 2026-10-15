import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Tentukan target URL baru (Contoh: Mengambil judul artikel dari blog/situs target)
url = "https://chomsky.info/"  # Kamu bisa mengganti URL ini dengan situs lain yang ingin di-scrap
response = requests.get(url)

# 2. Cek apakah request berhasil (Status 200 berarti sukses)
if response.status_code == 200:
    print("Berhasil terhubung ke website!\n")
    
    # 3. Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. Cari elemen target (Contoh: mengambil semua judul teks dari tag heading atau link artikel)
    # Di sini kita ambil semua tag judul artikel atau heading (misal: h2 atau a)
    elements = soup.find_all("a") 
    
    data_list = []
    for item in elements:
        text = item.get_text(strip=True)
        if text:  # Pastikan tidak kosong
            data_list.append(text)
            print("-", text)

    # 5. Konversi data ke format CSV menggunakan Pandas
    if data_list:
        df = pd.DataFrame(data_list, columns=["Judul_Artikel"])
        df.to_csv("hasil_scraping_baru.csv", index=False)
        print("\nData berhasil disimpan ke file 'hasil_scraping_baru.csv'!")
    else:
        print("Tidak ada teks yang ditemukan dengan tag tersebut.")
else:
    print(f"Gagal terhubung ke website. Status code: {response.status_code}")