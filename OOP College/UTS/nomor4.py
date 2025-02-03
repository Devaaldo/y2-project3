class Siswa: # Class Induk
    def __init__(self, nama, umur, tingkatan):
        self.nama = nama
        self.umur = umur
        self.tingkatan = tingkatan

    #Method get_info()
    def get_info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Tingkatan: {self.tingkatan}"

# Subclass
class SekolahDasar(Siswa):
    def __init__(self, nama, umur):
        super().__init__(nama, umur, "Sekolah Dasar")

    # Override method get_info()
    def get_info(self):
        return f"[Sekolah Dasar] Nama: {self.nama}, Umur: {self.umur}, Tingkatan: {self.tingkatan}"

# Subclass
class SMP(Siswa):
    def __init__(self, nama, umur):
        super().__init__(nama, umur, "SMP")

    # Override method get_info()
    def get_info(self):
        return f"[SMP] Nama: {self.nama}, Umur: {self.umur}, Tingkatan: {self.tingkatan}"

# Subclass
class SMA(Siswa):
    def __init__(self, nama, umur):
        super().__init__(nama, umur, "SMA")

    # Override method get_info()
    def get_info(self):
        return f"[SMA] Nama: {self.nama}, Umur: {self.umur}, Tingkatan: {self.tingkatan}"


siswa_sd = SekolahDasar("Bambang", 10)
siswa_smp = SMP("Yusuf", 13)
siswa_sma = SMA("Suhar", 16)

# Menggunakan polymorphism untuk memanggil get_info() dari berbagai objek
siswa_list = [siswa_sd, siswa_smp, siswa_sma]
for siswa in siswa_list:
    print(siswa.get_info())
