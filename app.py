import streamlit as st

st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="centered")

st.title("💸 Tracker Keuangan")

# Pilihan Bulan
bulan_pilihan = st.selectbox("Pilih Bulan:", ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"])

# 1. Setting Pemasukan & Anggaran Pokok
with st.expander(f"⚙️ Atur Pemasukan & Anggaran {bulan_pilihan}", expanded=False):
    st.write("**💰 Pemasukan:**")
    gaji = st.number_input("Gaji Pokok (Rp)", value=1400000, step=50000)
    pemasukan_tambahan = st.number_input("Pemasukan Tambahan/Bonus (Rp)", value=0, step=50000)
    
    st.divider()
    
    st.write("**💸 Pengeluaran Tetap:**")
    cicilan = st.number_input("Cicilan (Rp)", value=400000, step=50000)
    ortu = st.number_input("Orang Tua (Rp)", value=400000, step=50000)

# Kalkulasi Uang
total_pemasukan = gaji + pemasukan_tambahan
sisa_bulanan = total_pemasukan - cicilan - ortu
jatah_mingguan = sisa_bulanan / 4
batas_harian = jatah_mingguan / 7

st.info(f"**Total Pemasukan:** Rp {total_pemasukan:,.0f} | **Uang Jajan {bulan_pilihan}:** Rp {sisa_bulanan:,.0f}\n\n**Jatah Harian Maksimal:** Rp {batas_harian:,.0f}")

# 2. Catatan Pengeluaran Harian
st.subheader("📝 Evaluasi Harian")
pengeluaran_hari_ini = st.number_input("Berapa yang kamu habiskan hari ini? (Rp)", min_value=0, step=1000)

sisa_hari_ini = batas_harian - pengeluaran_hari_ini

if pengeluaran_hari_ini > 0:
    if sisa_hari_ini > 0:
        st.success(f"**Aman!** Masih ada sisa **Rp {sisa_hari_ini:,.0f}** hari ini.")
    elif sisa_hari_ini == 0:
        st.warning("**Pas!** Jatah hari ini habis tanpa sisa.")
    else:
        st.error(f"**Overbudget!** Kamu tekor **Rp {abs(sisa_hari_ini):,.0f}** hari ini.")

st.divider()

# 3. Akumulasi Bulanan
st.subheader(f"📊 Laporan & Akumulasi {bulan_pilihan}")
st.write(f"Masukkan total semua uang yang sudah kamu habiskan dari awal {bulan_pilihan} sampai hari ini:")

akumulasi_pengeluaran = st.number_input(f"Total Pengeluaran {bulan_pilihan} (Rp)", min_value=0, step=5000)

sisa_uang_bulanan = sisa_bulanan - akumulasi_pengeluaran

# Menampilkan Laporan dengan Desain Kotak (Metric)
col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"Anggaran Jajan {bulan_pilihan}", value=f"Rp {sisa_bulanan:,.0f}")
    st.metric(label="Total Pengeluaran", value=f"Rp {akumulasi_pengeluaran:,.0f}")

with col2:
    if sisa_uang_bulanan > 0:
        st.metric(label="SISA UANG SAAT INI", value=f"Rp {sisa_uang_bulanan:,.0f}")
        st.success("Aman! Uangmu masih sisa.")
    elif sisa_uang_bulanan == 0:
        st.metric(label="SISA UANG SAAT INI", value=f"Rp 0")
        st.warning("Uang jajan habis!")
    else:
        st.metric(label="SISA UANG SAAT INI", value=f"- Rp {abs(sisa_uang_bulanan):,.0f}")
        st.error("Gawat, kamu minus/nombok!")
