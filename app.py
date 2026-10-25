import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="centered")

st.title("💸 Tracker Keuangan Bulanan")

# Bagian Pengaturan Anggaran
with st.expander("⚙️ Atur Anggaran Bulan Ini", expanded=False):
    gaji = st.number_input("Total Gaji (Rp)", value=1400000, step=50000)
    cicilan = st.number_input("Cicilan (Rp)", value=400000, step=50000)
    ortu = st.number_input("Orang Tua (Rp)", value=400000, step=50000)

# Kalkulasi Otomatis
sisa = gaji - cicilan - ortu
mingguan = sisa / 4
harian = mingguan / 7

# Menampilkan Ringkasan
st.info(f"""
**Sisa Uang Bulanan:** Rp {sisa:,.0f}  
**Jatah Mingguan:** Rp {mingguan:,.0f}  
**Batas Harian Maksimal:** Rp {harian:,.0f}
""")

# Bagian Checklist
st.subheader("📝 Checklist Harian")
minggu_aktif = st.selectbox("Pilih Minggu:", ["Minggu 1", "Minggu 2", "Minggu 3", "Minggu 4"])

hari_dalam_seminggu = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

st.write(f"**Target pengeluaran {minggu_aktif}:**")
for hari in hari_dalam_seminggu:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"📅 {hari} (Maks Rp {harian:,.0f})")
    with col2:
        # Checkbox unik menggunakan kombinasi minggu dan hari
        st.checkbox("Aman", key=f"{minggu_aktif}_{hari}")

st.success("Gunakan fitur ini setiap malam untuk mengevaluasi pengeluaran harianmu!")
