# GEP1316 - İlk Python programı
# Kullanıcıdan adını ve doğum yılını alıp kişisel bir mesaj verir.

from datetime import datetime  # Bilgisayarın geçerli yılını almak için datetime modülünü içe aktarır.


def ad_al():  # Kullanıcının adını güvenli biçimde almak için fonksiyon tanımlar.
    while True:  # Geçerli bir ad girilene kadar döngüyü sürdürür.
        ad = input("Adınız: ").strip()  # Adı alır ve baştaki/sondaki boşlukları temizler.
        if ad:  # Ad alanının boş olup olmadığını kontrol eder.
            return ad  # Boş değilse adı fonksiyonun sonucu olarak döndürür.
        print("Ad alanı boş bırakılamaz. Lütfen tekrar deneyin.")  # Boş girişte uyarı verir.


def dogum_yili_al():  # Kullanıcının doğum yılını doğrulayarak almak için fonksiyon tanımlar.
    su_an_yil = datetime.now().year  # Sistemin geçerli takvim yılını alır.
    while True:  # Geçerli bir doğum yılı girilene kadar döngüyü sürdürür.
        giris = input("Doğum yılınız: ").strip()  # Doğum yılı bilgisini metin olarak alır.
        try:  # Metni tam sayıya dönüştürmeyi dener.
            dogum_yili = int(giris)  # Girilen değeri tam sayıya çevirir.
        except ValueError:  # Giriş sayı değilse bu bölüm çalışır.
            print("Lütfen doğum yılınızı dört haneli bir sayı olarak girin.")  # Hata mesajı gösterir.
            continue  # Programı kapatmadan yeniden doğum yılı ister.

        if dogum_yili < 1900:  # Gerçekçi olmayan çok eski yılları kontrol eder.
            print("Lütfen 1900 veya sonrasında bir yıl girin.")  # Uygun aralık için uyarı verir.
            continue  # Yeni giriş almak için döngünün başına döner.

        if dogum_yili > su_an_yil:  # Ek geliştirme: gelecekteki doğum yılını kontrol eder.
            print(f"Hata: Doğum yılı {su_an_yil} yılından büyük olamaz.")  # Gelecek yıl için uyarı verir.
            continue  # Hatalı girişten sonra programı kapatmadan tekrar sorar.

        return dogum_yili  # Tüm kontrolleri geçen yılı fonksiyonun sonucu olarak döndürür.


def main():  # Programın ana akışını yöneten fonksiyonu tanımlar.
    print("=== Kişisel Karşılama Programı ===")  # Program başlığını ekrana yazdırır.
    ad = ad_al()  # Kullanıcının adını alır.
    dogum_yili = dogum_yili_al()  # Kullanıcının geçerli doğum yılını alır.
    yas = datetime.now().year - dogum_yili  # Yaşı geçerli yıl ile doğum yılı arasındaki farktan hesaplar.
    print(f"\nMerhaba {ad}! {datetime.now().year} yılı itibarıyla {yas} yaşındasınız.")  # Kişiye özel mesajı yazdırır.
    print("GEP1316 portfolyoma hoş geldiniz. İyi çalışmalar!")  # Programı tamamlayan mesajı gösterir.


if __name__ == "__main__":  # Dosyanın doğrudan çalıştırılıp çalıştırılmadığını kontrol eder.
    main()  # Doğrudan çalıştırıldıysa ana fonksiyonu başlatır.
