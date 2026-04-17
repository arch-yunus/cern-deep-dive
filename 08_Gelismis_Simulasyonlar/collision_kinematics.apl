⍝ APL - Rölativistik 4-Vektör Çarpışma Kinematiği
⍝ --------------------------------------------------
⍝ Bu betik, 'collision_kinematics.py' mantığını APL'in
⍝ yerel dizi işleme yetenekleriyle yeniden üretir.
⍝ Kütle merkezi çarpışma sisteminin değişmez kütlesini hesaplar.

⍝ 1. Fiziksel Sabitlerin Tanımlanması
MP ← 0.938              ⍝ Proton Kütlesi (GeV)
E  ← 6800               ⍝ Demet Enerjisi (GeV)

⍝ 2. Momentum Pz Hesabı (E² = P² + M² => P = √(E² - M²))
Pz ← ( (E*2) - (MP*2) ) * 0.5

⍝ 3. 4-Vektörlerin Tanımlanması [E, Px, Py, Pz]
P1 ← E, 0, 0, Pz        ⍝ Demet 1 (+Z Yönünde)
P2 ← E, 0, 0, (-Pz)     ⍝ Demet 2 (-Z Yönünde)

⍝ 4. 4-Vektörlerin Toplamı (Çarpışma Sistemi)
S ← P1 + P2

⍝ 5. Değişmez Kütle Fonksiyonu: M = √(E² - Σ(Pi²))
InvMass ← { ( (⍵[1]*2) - ( +/ (1 ↓ ⍵)*2 ) ) * 0.5 }

⍝ 6. Egzotik Ekran Çıktısı
⎕ ← '===[ LHC ÇARPIŞMA SİSTEMİ: APL TANI İŞLEMİ ]==='
⎕ ← 'Parçacık 1 (4-Vektör): ', ⍕P1
⎕ ← 'Parçacık 2 (4-Vektör): ', ⍕P2
⎕ ← 'Sistem Toplam Enerjisi: ', ⍕S[1]
⎕ ← 'Mevcut KM Enerjisi:    ', ⍕InvMass S
⎕ ← '------------------------------------------------'
⎕ ← 'SONUÇ: ', ( (InvMass S) > 125 ) ⌽ 'HİGGS YOK' 'HİGGS OLUŞUMU MÜMKÜN'
⎕ ← '================================================'
