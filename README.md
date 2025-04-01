# Kayınpederi Mutlu Etme Oyunu

Bu eğlenceli oyun, kayınpederinizle olan ilişkinizi test etmenizi sağlar. Verdiğiniz kararlar, kayınpederinizin sizin hakkınızdaki düşüncelerini etkiler ve sonunda onun mutlu mu yoksa kızgın mı olduğunu görebilirsiniz.

## Özellikler

- 10 farklı senaryo sorusu
- Her seçimin kayınpederiniz üzerinde farklı etkileri var
- Verdiğiniz cevaplara göre farklı sonuçlar
- Mobil uyumlu tasarım

## Kurulum

Bu projeyi yerel olarak çalıştırmak için aşağıdaki adımları izleyin:

1. Repoyu klonlayın:
   ```
   git clone https://github.com/elnidal/kayinpeder.git
   cd kayinpeder
   ```

2. Sanal ortam oluşturun ve aktifleştirin:
   ```
   python -m venv venv
   
   # Windows için
   venv\Scripts\activate
   
   # macOS/Linux için
   source venv/bin/activate
   ```

3. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

4. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

5. Tarayıcınızda `http://127.0.0.1:5000/` adresine gidin

## Resimler Hakkında

Oyun içinde kullanılan görseller için `static/images` klasörüne aşağıdaki dosyaları eklemeniz gerekiyor:
- `happy.jpg`: Mutlu kayınpeder resmi
- `neutral.jpg`: Kararsız kayınpeder resmi
- `angry.jpg`: Kızgın kayınpeder resmi

## Canlı Demo

Oyunun canlı demosu için: [Kayınpederi Mutlu Etme Oyunu](https://kayinpeder.onrender.com)

## Render'a Deployment

Bu projeyi Render'a deploy etmek için:

1. Render hesabınızda yeni bir Web Service oluşturun
2. GitHub repo'nuzu bağlayın
3. Aşağıdaki yapılandırmaları kullanın:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

## Teknolojiler

- Flask
- Bootstrap
- HTML/CSS/JavaScript
- JSON (Sorular ve seçenekler için)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
