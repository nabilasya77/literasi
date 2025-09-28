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

# Simpan ke Excel dengan banyak sheet
with pd.ExcelWriter("literasi3_rapi.xlsx", engine="openpyxl") as writer:
    df_files.to_excel(writer, sheet_name="Data Files", index=False)
    df_logs.to_excel(writer, sheet_name="Log Aktivitas", index=False)
    df_locks.to_excel(writer, sheet_name="IoT Smart Lock", index=False)
    df_users.to_excel(writer, sheet_name="Perilaku Pengguna", index=False)

print("Konversi selesai! Data sudah disimpan ke literasi3_rapi.xlsx")
