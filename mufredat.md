Bu eğitim bir görev kontrol ünitesinde çalışan bir Dronekit Scripti aracılığı ile ardupilot/ px4 üzerine bina edilmiş bir insansız hava aracı otonom uçuşu nasıl gerçekleştirilir bunu kapsar. 

11 dersten oluşan bir müfredata sahiptir. Bu dersler video olarak youtube üzerinden izlenmeli ve adım adım uygulanmalıdır.

Youtube eğitim linki: https://www.youtube.com/watch?v=hKjJbWBXjbA&list=PLfnjV8SeD2_dpVGki_pdTd6ZdiHg7qM6i&ab_channel=%C4%B0mamDe%C4%9Filim

--Müfredat--

Ders1. Gazebo simulasyon ortamı ile Sitl bağlantısı nasıl yapılır?

Ders2. Dronekit ile ardupilot(sitl ile çalışan ya da bir pixhawk içinde çalışan) arasındaki bağlantı nasıl yapılır?

Ders3. Drone'u arm etme, Mod değiştirme, auto takeoff yaptırma.

Ders4. Dronekit attributeleri

Ders5. Parametreleri çekme ve onlara değer atama

Ders6. Simple goto fonksiyonu ile drone'un dünya üzerindeki herhangi bir konuma gitmesini sağlama

Ders7. Mavlink komutları, Hız komutu, frameler

Ders8. Konum komutu

Ders9. Mavlink Mesajı Dinleme, Gps zamanı.

Ders 10. Görev Bilgisayarı ile Otopilot arası bağlantıyı Dronekit ile kurmak

Ders 11. Dronekit ile Telemetri Bağlantısı ve Minik bir YKİ arayüzü geliştirme.

--Ödevler-- 

Bu ödevler eğitimin ardından yapılmalıdır.
(İlk iki ödev sizin yazacağınız fonksiyondur, dronekitle alakası yoktur.)


1-Girilen iki konum arası uzaklığı ekrana bastıran bir kod yazınız.

2-Girilen iki konum arasında çizilecek vektörün kuzeyle yaptığı açıyı hesaplayan bir kod yazınız.

3-Drone’u kaldırın 2 metreye kaldırın. 5 metre kuzeye götürün. İndirin tekrar bu sefer 10 metreye kaldırın. 4 metre kuzey batıya götürün indirin. Tekrar kaldırın Return to Launch modunu aktive edin. Drone modu tamamlayınca disarm edin.

4-Velocity ya da pozisyon komutlarını kullanarak havada çember çizen bir kod yazınız. Bu hareketi gazebo üzerinde gözlemleyiniz.(çember x ve z ekseni üzerinde olmalı. Çemberin merkezi yerden 5 metre yükseklikte olsun ve çemberin yarıçapı 3 metre olsun) (Sinüs, kosinüs karekök gibi hesaplamalar yapmak için math kütüphanesini kullanabilirsiniz)

5-Benzer bir hareketi 360 derece kendi etrafında döndürerek yaptırınız.

Kaynak olarak dronekitin sitesi kullanılmıştır. Siz de bu eğitimin ardından ödevleri yaparken ileri okuma olarak bu sitedeki dökümanları okumalısınız. https://dronekit-python.readthedocs.io/en/latest/about/index.html
