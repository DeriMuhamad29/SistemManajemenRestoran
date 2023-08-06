# Creational Patterns


# Singleton Pattern
class NotifikasiKoki:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotifikasiKoki, cls).__new__(cls)
            cls._instance._pesanan = []
        return cls._instance

    def tambahPesanan(self, menu):
        self._pesanan.append(menu)

    def getPesanan(self):
        return self._pesanan


# Factory Method Pattern
from abc import ABC, abstractmethod


class Menu(ABC):
    @abstractmethod
    def tampilkanMenu(self):
        pass


class Makanan(Menu):
    def tampilkanMenu(self):
        print("Menu Makanan: Nasi Goreng, Ayam Goreng")


class Minuman(Menu):
    def tampilkanMenu(self):
        print("Menu Minuman: Es Teh, Es Jeruk")


class Factory:
    def buatMenu(self, jenis):
        if jenis.lower() == "makanan":
            return Makanan()
        elif jenis.lower() == "minuman":
            return Minuman()
        else:
            return None


# Builder Pattern
class Pesanan:
    def __init__(self):
        self._menu = []
        self._metode_bayar = None

    def tambahMenu(self, menu):
        self._menu.append(menu)

    def setMetodeBayar(self, metode_bayar):
        self._metode_bayar = metode_bayar

    def getTotalHarga(self):
        total_harga = 0
        for menu in self._menu:
            total_harga += menu.getHarga()
        return total_harga


# Structural Patterns


# Adapter Pattern
class AdapterPembayaran(Menu):
    def __init__(self, pembayaran):
        self._pembayaran = pembayaran

    def tampilkanMenu(self):
        self._pembayaran.bayar()


# Decorator Pattern
class Decorator:
    def tambahMenu(self, pesanan, jenis_menu):
        if jenis_menu.lower() == "makanan":
            pesanan.tambahMenu(Makanan())
        elif jenis_menu.lower() == "minuman":
            pesanan.tambahMenu(Minuman())


# Composite Pattern
class Restoran:
    def __init__(self):
        self._pesanan = []

    def tambahPesanan(self, pesanan):
        self._pesanan.append(pesanan)

    def terimaPesanan(self):
        print("Koki menerima pesanan baru:")
        for pesanan in self._pesanan:
            for menu in pesanan._menu:
                menu.tampilkanMenu()


# Behavioral Patterns


# Observer Pattern
class Pelanggan:
    def pesanMenu(self, menu):
        print("Pelanggan memesan:")
        menu.tampilkanMenu()
        NotifikasiKoki().tambahPesanan(menu)


class Koki:
    def terimaPesanan(self):
        pesanan = NotifikasiKoki().getPesanan()
        print("Koki menerima pesanan baru:")
        for menu in pesanan:
            menu.tampilkanMenu()


# Strategy Pattern
class PembayaranStrategy:
    def bayar(self):
        pass


class KartuKredit(PembayaranStrategy):
    def bayar(self):
        print("Pembayaran dengan Kartu Kredit")


class DompetDigital(PembayaranStrategy):
    def bayar(self):
        print("Pembayaran dengan Dompet Digital")


class Tunai(PembayaranStrategy):
    def bayar(self):
        print("Pembayaran dengan Tunai")


if __name__ == "__main__":
    # Creational Patterns
    notifikasi_koki = NotifikasiKoki()
    factory = Factory()
    builder = Builder()

    # Structural Patterns
    adapter_kartu_kredit = AdapterPembayaran(KartuKredit())
    adapter_dompet_digital = AdapterPembayaran(DompetDigital())
    adapter_tunai = AdapterPembayaran(Tunai())
    decorator = Decorator()
    restoran = Restoran()

    # Behavioral Patterns
    pelanggan = Pelanggan()
    koki = Koki()

    # Testing Creational Patterns
    print("Creational Patterns:")
    factory = Factory()
    menu1 = factory.buatMenu("makanan")
    menu2 = factory.buatMenu("minuman")
    menu1.tampilkanMenu()
    menu2.tampilkanMenu()

    print("\nBuilder Pattern:")
    pesanan_builder = Pesanan()
    builder.tambahMenu(pesanan_builder, "makanan")
    builder.tambahMenu(pesanan_builder, "minuman")
    builder.setMetodeBayar(pesanan_builder, "kartu kredit")

    print("Pesanan:")
    for menu in pesanan_builder._menu:
        menu.tampilkanMenu()
    print(f"Total Harga: {pesanan_builder.getTotalHarga()}")
    print(f"Metode Bayar: {pesanan_builder._metode_bayar}")

    # Testing Structural Patterns
    print("\nStructural Patterns:")
    decorator = Decorator()
    pesanan = Pesanan()

    decorator.tambahMenu(pesanan, "makanan")
    decorator.tambahMenu(pesanan, "minuman")

    print("Pesanan:")
    for menu in pesanan._menu:
        menu.tampilkanMenu()
    print(f"Total Harga: {pesanan.getTotalHarga()}")

    restoran.tambahPesanan(pesanan)
    restoran.terimaPesanan()

    print("\nAdapter Pattern:")
    adapter_kartu_kredit.tampilkanMenu()
    adapter_dompet_digital.tampilkanMenu()
    adapter_tunai.tampilkanMenu()

    # Testing Behavioral Patterns
    print("\nBehavioral Patterns:")
    menu1 = Makanan()
    menu2 = Minuman()

    pelanggan.pesanMenu(menu1)
    pelanggan.pesanMenu(menu2)

    koki.terimaPesanan()
