import streamlit as st

st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="centered")

st.title("💸 Tracker Keuangan Harian")

# 1. Setting Anggaran Pokok
with st.expander("⚙️ Atur Anggaran Bulan Ini", expanded=False):
    gaji = st.number_input("Total Gaji (Rp)", value=1400000, step=50000)
    cicilan = st.number_input("Cicilan (Rp)", value=400000, step=50000)
    ortu = st.number_input("Orang Tua (Rp)", value=400000, step=50000)

sisa_bulanan = gaji - cicilan - ortu
jatah_mingguan = sisa_bulanan / 4
batas_harian = jatah_mingguan / 7

st.info(f"**Jatah Maksimal Harianmu:** Rp {batas_harian:,.0f}")

# 2. Catatan Pengeluaran Harian
st.subheader("📝 Catat Pengeluaran Hari Ini")
hari_ini = st.selectbox("Hari apa ini?", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
pengeluaran = st.number_input(f"Berapa yang kamu habiskan di hari {hari_ini}? (Rp)", min_value=0, step=1000)

sisa_hari_ini = batas_harian - pengeluaran

# 3. Evaluasi Otomatis
if pengeluaran > 0:
    st.divider()
    if sisa_hari_ini > 0:
        st.success(f"**Hebat!** Masih ada sisa **Rp {sisa_hari_ini:,.0f}**. Uang ini bisa disimpan atau ditambahkan ke jatah besok.")
    elif sisa_hari_ini == 0:
        st.warning("**Pas!** Jatah hari ini habis tanpa sisa. Hati-hati besok ya.")
    else:
        st.error(f"**Waduh Overbudget!** Kamu tekor **Rp {abs(sisa_hari_ini):,.0f}**. Besok harus kurangi pengeluaran untuk menutupi minus ini!")
