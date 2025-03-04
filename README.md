🔐 Password Manager - Basit ve Etkili Şifre Yöneticisi

Python ile geliştirilmiş, kullanımı son derece basit ve hızlı bir şifre yöneticisi. Bu uygulama, kullanıcıların şifrelerini güvenli bir şekilde saklamasına, güncellemesine, aramasına ve yönetmesine yardımcı olur.

📌 Özellikler

✅ Şifreleri güvenli bir şekilde saklama✅ Şifreleri listeleme ve görüntüleme✅ Şifreleri güncelleme ve değiştirme✅ Kayıtlı şifreler arasında arama yapma✅ Kullanılmayan veya eski şifreleri silme✅ Kullanıcı dostu ve basit bir arayüz (CLI tabanlı)✅ Python ile modüler yapı kullanılarak geliştirilmiş

🛠️ Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları takip edebilirsin.

1️⃣ Gerekli Bağımlılıkları Kur

Python yüklü değilse Python'un resmi web sitesinden yükleyebilirsin.

Bağımlılıkları yüklemek için terminalde aşağıdaki komutu çalıştır:

pip install -r requirements.txt

(Eğer requirements.txt kullanmıyorsan, projenin gerektirdiği bağımlılıkları manuel olarak yükleyebilirsin.)

2️⃣ Projeyi Klonla

git clone https://github.com/kullanici-adi/password-manager.git
cd password-manager

3️⃣ Programı Çalıştır

python main.py

📂 Dosya Yapısı

/password-manager
│── main.py                # Ana program dosyası
│── requirements.txt        # Gerekli bağımlılıkları içeren dosya
│── /Modul                  # Modüllerin bulunduğu klasör
│   │── __init__.py         # Paket tanımlayıcı dosya
│   │── ekleme.py           # Şifre ekleme fonksiyonları
│   │── listeleme.py        # Şifre listeleme fonksiyonları
│   │── silme.py            # Şifre silme fonksiyonları
│   │── guncelleme.py       # Şifre güncelleme fonksiyonları
│   │── arama.py            # Şifre arama fonksiyonları

🚀 Kullanım

Yeni bir şifre eklemek için:

python main.py

Ardından, menüden "Yeni Şifre Ekle" seçeneğini seç.

Kayıtlı şifreleri listelemek için:

python main.py

Menüden "Şifreleri Listele" seçeneğini seç.

Bir şifreyi güncellemek için:

python main.py

Menüden "Şifre Güncelle" seçeneğini seç.

Bir şifreyi silmek için:

python main.py

Menüden "Şifre Sil" seçeneğini seç.

Kayıtlı şifreler arasında arama yapmak için:

python main.py

Menüden "Şifre Ara" seçeneğini seç.

🛡️ Güvenlik Önlemleri

🔒 Şifrelerinizin güvenliği için:

Şifrelerin güvenli bir şekilde saklanması için hashing yöntemi uygulanabilir.

Dosya bazlı veri saklama yerine veritabanı kullanımı düşünülebilir.

Daha güçlü şifreleme algoritmaları entegre edilebilir.

🏗️ Geliştirme Planları

🚀 Gelecekte eklenebilecek özellikler:

Şifrelerin hash ile saklanması

Grafiksel kullanıcı arayüzü (GUI)

2FA (İki faktörlü kimlik doğrulama) entegrasyonu

🤝 Katkıda Bulunma

Projeye katkıda bulunmak için:

Fork'la 🚀

Yeni bir branch oluştur 🛠️

Değişiklikleri yap ve commit et ✅

PR (Pull Request) aç 🎯

📄 Lisans...

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına bakabilirsin.

