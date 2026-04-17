⍝ APL (A Programming Language) - Rölativistik Kinetik Matris
⍝ --------------------------------------------------------
⍝ Bu betik, CERN'deki rölativistik dinamiklerin vektör tabanlı
⍝ bir simülasyonunu gerçekleştirir. APL'in dizileri birincil
⍝ vatandaş olarak ele alması, proton kümelerini simüle etmek için idealdir.

⍝ 1. Sabitlerin Tanımlanması (Proton durgun kütlesi - GeV)
m ← 0.938

⍝ 2. Hızların Tanımlanması (Işık hızına yakın: 0.9c'den 0.999999991c'ye)
V ← 0.9 0.99 0.999 0.9999 0.99999 0.999999 0.9999999 0.999999991

⍝ 3. Vektörleştirilmiş Lorentz Faktörü: γ = 1 / √(1 - v²)
G ← ÷ (1 - V × V) * 0.5

⍝ 4. Rölativistik Kinetik Enerji: K = (γ - 1)mc²
K ← (G - 1) × m

⍝ 5. Rölativistik Momentum: p = γmv
P ← G × m × V

⍝ 6. Egzotik Görüntüleme Mantığı
⎕ ← '--- CERN VEKTÖRLEŞTİRİLMİŞ KİNETİK MATRİS ---'
⎕ ← 'Hızlar (v/c):      ', ⍕V
⎕ ← 'Lorentz Faktörleri: ', ⍕G
⎕ ← 'Kinetik Enerji(GeV): ', ⍕K
⎕ ← 'Rölativistik Momentum: ', ⍕P

⍝ 7. Durum Kontrolü
⎕ ← 'TANI: ', (G[⍴G] > 7000) ⌽ 'NOMİNAL ENERJİ' 'AŞIRI ÇARPIŞMA ENERJİSİ'
⎕ ← '--- DİZİ SONLANDIRILDI ---'
