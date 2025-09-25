# literasi
buatkan tabel dari json ke excel dalam 1 file 
ChatGPT said:

✅ Tabel sudah berhasil dibuat ke dalam Excel satu file dengan multi-sheet.
Silakan unduh di sini: Literasi3_Tabel.xlsx 

You said:
tolong rapikan bentuk excel itu ada garis tabel
ChatGPT said:

📊 File Excel sudah dirapikan dengan garis tabel di setiap sel yang berisi data.
Silakan unduh di sini: Literasi3_Tabel_Bergrids.xlsx 

You said:
buatkan kode program semua itu  file json tersebut ke csv
ChatGPT said:

Oke, saya akan buatkan kode program Python yang bisa membaca file JSON seperti punyamu, lalu mengubah semua bagian data menjadi file CSV terpisah.

Berikut contoh kodenya:

import json
import pandas as pd

# Baca file JSON
with open("NabilaCheisyaFadhilah_V3925032_Literasiiii3.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil masing-masing bagian JSON ke DataFrame
df_files = pd.DataFrame(data.get("data_file", []))
df_logs = pd.DataFrame(data.get("data_log_aktivitas", []))
df_locks = pd.DataFrame(data.get("data_perangkat_iot_smart_lock", []))
df_users = pd.DataFrame(data.get("data_perilaku_pengguna_perangkat", []))

# Simpan ke CSV
df_files.to_csv("data_files.csv", index=False)
df_logs.to_csv("data_logs.csv", index=False)
df_locks.to_csv("data_locks.csv", index=False)
df_users.to_csv("data_users.csv", index=False)

print("Konversi selesai. Semua CSV sudah dibuat:")
print("- data_files.csv")
print("- data_logs.csv")
print("- data_locks.csv")
print("- data_users.csv")


📌 Penjelasan:

Program membaca file NabilaCheisyaFadhilah_V3925032_Literasiiii3.json.

Data dipisahkan sesuai key JSON (data_file, data_log_aktivitas, data_perangkat_iot_smart_lock, data_perilaku_pengguna_perangkat).

Hasilnya ada 4 file CSV:

data_files.csv

data_logs.csv

data_locks.csv

data_users.csv

Mau saya langsung jalankan program ini ke file JSON-mu biar saya kasih hasil CSV-nya juga?

You said:
boleh
ChatGPT said:

✅ Semua bagian JSON sudah berhasil dikonversi ke CSV.
Silakan unduh hasilnya di sini:

data_files.csv

data_logs.csv

data_locks.csv

data_users.csv 

You said:
buatkan dalam 1 file ke csv itu

ChatGPT said:

📑 Semua data dari JSON sudah digabungkan ke dalam satu file CSV dengan tambahan kolom source untuk menandai asal datanya.

Silakan unduh di sini: Literasi3_AllData.csv 

You said:
NabilaCheisyaFadhilah_V3925032_Literasiiii3[1].json
File
buatkan kode program dari isi file format  json ke csv

ChatGPT said:

Oke 👍
Berikut saya buatkan kode program Python untuk mengubah isi file JSON itu menjadi CSV.

import json
import pandas as pd

# Baca file JSON
with open("NabilaCheisyaFadhilah_V3925032_Literasiiii3[1].json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ubah setiap bagian JSON menjadi DataFrame
df_files = pd.DataFrame(data.get("data_file", []))
df_logs = pd.DataFrame(data.get("data_log_aktivitas", []))
df_locks = pd.DataFrame(data.get("data_perangkat_iot_smart_lock", []))
df_users = pd.DataFrame(data.get("data_perilaku_pengguna_perangkat", []))

# Simpan masing-masing ke file CSV
df_files.to_csv("data_files.csv", index=False)
df_logs.to_csv("data_logs.csv", index=False)
df_locks.to_csv("data_locks.csv", index=False)
df_users.to_csv("data_users.csv", index=False)

# Jika ingin semua data digabungkan dalam satu file CSV:
df_files["source"] = "data_file"
df_logs["source"] = "data_log_aktivitas"
df_locks["source"] = "data_perangkat_iot_smart_lock"
df_users["source"] = "data_perilaku_pengguna_perangkat"

combined = pd.concat([df_files, df_logs, df_locks, df_users], ignore_index=True, sort=False)
combined.to_csv("all_data.csv", index=False)

print("Konversi selesai! File CSV yang dihasilkan:")
print("- data_files.csv")
print("- data_logs.csv")
print("- data_locks.csv")
print("- data_users.csv")
print("- all_data.csv (gabungan)")


📌 Penjelasan:

data_files.csv → dari bagian data_file.

data_logs.csv → dari data_log_aktivitas.

data_locks.csv → dari data_perangkat_iot_smart_lock.

data_users.csv → dari data_perilaku_pengguna_perangkat.

all_data.csv → gabungan semua tabel dalam satu file, dengan kolom tambahan source agar tahu asal datanya.

Mau saya langsung jalankan kode ini untuk file JSON-mu dan kasih hasil CSV-nya?

