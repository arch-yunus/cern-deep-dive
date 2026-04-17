import math

class FourVector:
    """Parçacık Kinematiği için (+,-,-,-) metrik imzasını kullanan minimal 4-vektör sınıfı.
    Bu yapı, CERN'in ROOT fizik çerçevelerinde yoğun olarak kullanılmaktadır."""
    def __init__(self, e, px, py, pz):
        self.e = e
        self.px = px
        self.py = py
        self.pz = pz

    def invariant_mass(self):
        """Değişmez kütle karesi formülü: m^2 = E^2 - p^2"""
        p2 = self.px**2 + self.py**2 + self.pz**2
        m2 = self.e**2 - p2
        return math.sqrt(m2) if m2 > 0 else 0

    def __add__(self, other):
        return FourVector(
            self.e + other.e,
            self.px + other.px,
            self.py + other.py,
            self.pz + other.pz
        )

    def print_vector(self, name="Parçacık"):
        print(f"[{name}] E: {self.e:.2f} GeV, Px: {self.px:.2f}, Py: {self.py:.2f}, Pz: {self.pz:.2f} | Değişmez Kütle: {self.invariant_mass():.4f} GeV")


def simulate_lhc_collision():
    print("=" * 60)
    print(" >>> LHC ÇARPIŞMA KİNEMATİĞİ SİMÜLATÖRÜ <<< ".center(60))
    print("=" * 60)

    # Proton kütlesi (GeV/c^2)
    mp = 0.938 
    
    # LHC'de demet enerjisi yaklaşık demet başına 6.8 TeV'dir (Toplam 13.6 TeV)
    beam_energy = 6800.0 # GeV

    # Pz değeri E^2 = P^2 + m^2 => P = sqrt(E^2 - m^2) formülünden türetilir
    p_momentum = math.sqrt(beam_energy**2 - mp**2)

    # Demet 1: Tamamen +Z yönünde ilerliyor
    p1 = FourVector(beam_energy, 0.0, 0.0, p_momentum)
    
    # Demet 2: Tamamen -Z yönünde ilerliyor
    p2 = FourVector(beam_energy, 0.0, 0.0, -p_momentum)

    print("\n--- ÇARPIŞMA ÖNCESİ DURUM ---")
    p1.print_vector("Proton 1 (Demet 1)")
    p2.print_vector("Proton 2 (Demet 2)")

    # Çarpışma! Toplam sistem durumu.
    print("\n--- KÜTLE MERKEZİ SİSTEMİ (ÇARPIŞMA ANI) ---")
    system = p1 + p2
    
    system.print_vector("Çarpışma Sistemi")
    
    print("-" * 60)
    print("Çarpışma sisteminin Değişmez Kütlesine dikkat edin.")
    print("Her biri ~0.938 GeV ağırlığında iki protonla başladık.")
    print(f"Ancak kinetik enerjiden dolayı, şu an {system.invariant_mass():.0f} GeV'lik saf bir enerji mevcut!")
    print("Büyük kütleli parçacıklar (örneğin 125 GeV'deki Higgs Bozonu) tam olarak böyle yaratılır.")
    print("E = mc^2 formülünün saf eylem hali.")


if __name__ == "__main__":
    simulate_lhc_collision()
