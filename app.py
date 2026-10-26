import streamlit as st

st.set_page_config(page_title="Budget Tracker", page_icon="💰", layout="centered")

# Inisialisasi Memori untuk menyimpan total pengeluaran otomatis
if 'total_pengeluaran' not in st.session_state:
    st.session_state.total_pengeluaran = 0

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
    bayar_lainnya = st.number_input("Bayar Lainnya (Rp)", value=0, step=50000)

# Kalkulasi Uang
total_pemasukan = gaji + pemasukan_tambahan
sisa_bulanan = total_pemasukan - cicilan - ortu - bayar_lainnya
jatah_mingguan = sisa_bulanan / 4
batas_harian = jatah_mingguan / 7

st.info(f"**Total Pemasukan:** Rp {total_pemasukan:,.0f} | **Uang Jajan {bulan_pilihan}:** Rp {sisa_bulanan:,.0f}\n\n**Jatah Harian Maksimal:** Rp {batas_harian:,.0f}")

# 2. Catatan Pengeluaran Harian (Otomatis)
st.subheader("📝 Evaluasi Harian")
st.write("Masukkan pengeluaranmu hari ini lalu klik **Simpan** agar otomatis ditambahkan ke total bulanan.")

pengeluaran_hari_ini = st.number_input("Berapa yang kamu habiskan hari ini? (Rp)", min_value=0, step=1000)

# Tombol Simpan
if st.button("💾 Simpan Pengeluaran Hari Ini"):
    if pengeluaran_hari_ini > 0:
        st.session_state.total_pengeluaran += pengeluaran_hari_ini
        st.success(f"Berhasil mencatat Rp {pengeluaran_hari_ini:,.0f} ke laporan bulanan!")
    else:
        st.warning("Masukkan nominal lebih dari 0 untuk disimpan.")

# Evaluasi Harian
sisa_hari_ini = batas_harian - pengeluaran_hari_ini
if pengeluaran_hari_ini > 0:
    if sisa_hari_ini > 0:
        st.info(f"Status Harian: Aman! Masih ada sisa jatah Rp {sisa_hari_ini:,.0f} hari ini.")
    elif sisa_hari_ini == 0:
        st.warning("Status Harian: Pas! Jatah hari ini habis tanpa sisa.")
    else:
        st.error(f"Status Harian: Overbudget! Kamu tekor Rp {abs(sisa_hari_ini):,.0f} hari ini.")

st.divider()

# 3. Akumulasi Bulanan (Otomatis)
st.subheader(f"📊 Laporan & Akumulasi {bulan_pilihan}")

akumulasi_pengeluaran = st.session_state.total_pengeluaran
sisa_uang_bulanan = sisa_bulanan - akumulasi_pengeluaran

# Menampilkan Laporan dengan Desain Kotak (Metric)
col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"Anggaran Jajan {bulan_pilihan}", value=f"Rp {sisa_bulanan:,.0f}")
    st.metric(label="Total Pengeluaran (Otomatis)", value=f"Rp {akumulasi_pengeluaran:,.0f}")

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

st.divider()

# Tombol Reset untuk Bulan Baru
if st.button("🔄 Reset Total Pengeluaran (Mulai Bulan Baru)"):
    st.session_state.total_pengeluaran = 0
    st.rerun()
