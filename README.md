# 🖱️ AI Virtual Mouse & Gesture Controller

OpenCV, MediaPipe ve PyAutoGUI kullanılarak geliştirilmiş, web kamerası üzerinden el hareketlerini algılayarak fare imlecini, tıklama ve sayfa kaydırma (scroll) işlemlerini temassız kontrol eden bilgisayarlı görü projesi.

---

## 🚀 Özellikler

- **Hassas İmleç Kontrolü:** Avuç içi merkezli konumlandırma ve ani titreşimleri önleyen pürüzsüzleştirme (smoothing) algoritması.
- **Sol Tık (Left Click):** Baş parmak ve işaret parmağının birbirine temas etmesiyle tetiklenir (Sürükle-bırak destekler).
- **Sağ Tık (Right Click):** Baş parmak ve orta parmağın temas etmesiyle tetiklenir.
- **Sayfa Kaydırma Modu (Scroll):** İşaret, orta ve yüzük parmakları bir araya getirildiğinde kaydırma modu aktifleşir; elinizi yukarı/aşağı hareket ettirerek sayfayı akıcı şekilde kaydırabilirsiniz.

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **OpenCV (`cv2`):** Kamera akışı, renk uzayı dönüşümü ve görsel çizimler.
- **MediaPipe:** Gerçek zamanlı 21 el eklem noktası (landmark) takibi.
- **PyAutoGUI:** İşletim sistemi seviyesinde fare kontrolü ve event tetikleme.
- **NumPy:** Koordinat haritalama ve enterpolasyon işlemleri.

---

## 📁 Proje Yapısı

```text
├── hand_detector.py    # MediaPipe el tespiti ve koordinat çıkarımı yapan modül
├── main.py             # Fare kontrolleri ve mantıksal eşiklerin yönetildiği ana script
├── requirements.txt    # Gerekli bağımlılıklar listesi
├── .gitignore          # Git tarafından takip edilmeyecek geçici dosyalar
└── README.md           # Proje dokümantasyonu
