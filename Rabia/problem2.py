import tkinter as tk #Tkinter kütüphanesini içe aktarıyor.
from tkinter import ttk #Daha modern ve işletim sistemine uyumlu bir arayüz sağlaması için ttk ekleniyor.
import pandas as pd #Pandas kütüphanesi içe aktarılıyor

df = pd.read_csv("saldırılog.csv") # CSV dosyası okutuluyor.
df["Tarih"] = pd.to_datetime(df["Tarih"]) #Sorularda tarihler kullanılacağı için string olan tarih satırı tarihi değere dönüştürülüyor

pencere = tk.Tk() #Ana pencere oluşturuluyor.
pencere.title("Siber Saldırı Analiz Sistemi") #Pencere ismi yazdırılıyor.
pencere.geometry("900x600") #Pencere boyutu belirleniyor.

baslik = tk.Label( #Başlık fontu, yazdırılacak isim, yazı boyutu belirleniyor.
    text="Siber Saldırı Analizi",
    font=("Calibri", 18)
)

baslik.pack(pady=10) #Başlık için altta ve üstte 10 pixel boşluk bırakılması için yazdırılıyor.

problem_yazisi = """ 
A) saldırılog.csv dosyasında bulunan saldırı türlerini en çok gerçekleşenden en aza doğru sıralayarak listeleyiniz.
B) Risk seviyelerine göre saldırı sayılarını listeleyiniz ve en yüksek risk seviyesine sahip saldırı türünü gösteriniz.
C) Engellenen ve engellenemeyen saldırı sayılarını ayrı ayrı hesaplayarak toplam saldırı sayısını yazdırınız.
D) Her saldırının müdahele süresi en uzun olan saldırı tarihini ve süresini yazdırınız.
E) Günlere göre gerçekleşen saldırı sayılarını analiz ederek en yoğundan en aza doğru listeleyiniz.

""" #İlk açılan pencerede problem soruları yazdırılıyor.

problem = tk.Label( #Problem sorularının yazı fontu, yazı boyutu, yazılacak başlığı yazdırılıyor.
    text=problem_yazisi,
    font=("Calibri", 12),
    justify="left"
)

problem.pack(pady=10) #Başlık için altta ve üstte 10 pixel boşluk bırakılması için yazdırılıyor.

tree = ttk.Treeview(pencere) #GUI Uygulamasındaki tablo görüntüsünün sağlanması için yazılıyor.

tree["columns"] = ("Bilgi","Değer") #2 adet sütun tanımlanıyor.

tree.column("#0", width=0, stretch=tk.NO) #Treeview wigdetının kendisi oluşturduğu ilk sütun gizleniyor.

tree.column("Bilgi", width=300, anchor=tk.CENTER)# #0 indexindeki ilk sütun görünür.

tree.column("Değer", width=300, anchor=tk.CENTER)# #1 indexindeki 2. sütun görünür.

tree.pack(fill="both", expand=True) #Tablonun pencerede gözükmesini sağlıyor.


def temizle(): # Sorunun diğer seçeneklerine geçtiğinde tablonun temizlenmesi için fonksiyon yazılıyor.

    for item in tree.get_children(): #Her değerin silinmesi için tablo döngüye alınıyor.
        tree.delete(item) #Değerler sırasıyla siliniyor, tablo temizleniyor.

def iki_sutun(): #Tabloyu 2 sütuna çevirir.

    tree["columns"] = ("Bilgi", "Değer") #2 Adet sütun oluşturuluyor.

    tree.column("Bilgi", width=350, anchor=tk.CENTER) #Sütun genişliği belirleniyor ve ortalaması için fonkisyon tanımlanıyor.
    tree.column("Değer", width=350, anchor=tk.CENTER) #Sütun genişliği belirleniyor ve ortalaması için fonkisyon tanımlanıyor.

def a_sıkkı(): #A şıkkının çözümü için fonksiyon tanımlanıyor.

    temizle() #Önceden seçilen herhangi bir seçenek için tablo temizleniyor.

    iki_sutun() #Tabloyu 2 sütuna çevirir.

    tree.heading("Bilgi", text="Saldırı Türü") #"Bilgi" sütununa onun yerine sorunun cevabı olan "Saldırı Türü" yazılıyor.
    tree.heading("Değer", text="Saldırı Sayısı") #"Değer" sütununa onun yerine sorunun cevabı olan "Saldırı Sayısı" yazılıyor.

    sonuc = df["SaldiriTuru"].value_counts() #CSV dosyasından sorunun cevabı için gerekli olan "SaldırıTuru" sütununu alınır.
                                            #value_counts fonksiyonu işleme alınan aynı verileri tespit eder.

    for saldiri_turu, saldiri_sayisi in sonuc.items(): #"sonuc"un içine atılmış verileri tek tek alır ve döngüye sokar.

        tree.insert(  #Treeview içine yeni satır ekler.
            "", #Tek kategori kullandığımız için boş string veriliyor.
            tk.END, #Yeni satırı en sona ekler.
            values=(saldiri_turu, saldiri_sayisi) #Gelen verilerden ilk veri "Saldırı Türü" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
        )


def b_sıkkı(): #B şıkkının çözümü için fonksiyon tanımlanıyor.

    temizle() #Önceden seçilen herhangi bir seçenek için tablo temizleniyor.

    iki_sutun() #Tabloyu 2 sütuna çevirir.

    tree.heading("Bilgi", text="Risk Seviyesi") #"Bilgi" sütununa onun yerine sorunun cevabı olan "Risk Seviyesi" yazılıyor.
    tree.heading("Değer", text="Saldırı Sayısı") #"Değer" sütununa onun yerine sorunun cevabı olan "Saldırı Sayısı" yazılıyor.

    sonuc = df["RiskSeviyesi"].value_counts()#CSV dosyasından sorunun cevabı için gerekli olan "SaldırıTuru" sütununu alınır.
#value_counts fonksiyonu işleme alınan aynı verileri tespit eder.

    for risk_seviyesi, saldiri_sayisi in sonuc.items(): #"sonuc"un içine atılmış verileri tek tek alır ve döngüye sokar.

        tree.insert(  #Treeview içine yeni satır ekler.
            "", #Tek kategori kullandığımız için boş sting veriliyor.
            tk.END, #Yeni satırı en sona ekler.
            values=(risk_seviyesi, saldiri_sayisi) #Gelen verilerden ilk veri "Risk Seviyesi" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
        )

    risk_sirasi = { #En yüksek riskli saldırıyı bulmak için risk seviyelerine numara atanıyor. Metin risk seviyelerini sayıya çeviriliyor.
        "Dusuk": 1,
        "Orta": 2,
        "Yuksek": 3,
        "Cok Yuksek": 4
    }

    df["RiskPuani"] = df["RiskSeviyesi"].map(risk_sirasi) #Geçici bir sütun oluşuturluyor. 'map' fonksiyonu sözlükte ifadeleri arar.

    en_riskli = df.loc[df["RiskPuani"].idxmax()] #Oluşturulan geçici sütunda 'idmax' fonksiyonu sayesinde en yüksek değerin index numarası bulunur.
#'loc' fonksiyonuyla bu içine yazılan sayısal değerin satırına getirir. Örnek: 1 = 1. Satır. Bu sayede en yüksek riskli satır yani saldırı bulunur.

    tree.insert( #Treeview içine yeni satır ekler.
        "", #Tek kategori kullandığımız için boş sting veriliyor.
        tk.END, #Yeni satırı en sona ekler.
        values=("En Riskli Tür", en_riskli["SaldiriTuru"]) #Gelen verilerden ilk veri "Risk Seviyesi" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
    )


def c_sıkkı(): #C şıkkının çözümü için fonksiyon tanımlanıyor.

    temizle() #Önceden seçilen herhangi bir seçenek için tablo temizleniyor.

    iki_sutun() #Tabloyu 2 sütuna çevirir.

    tree.heading("Bilgi", text="Durum") #"Bilgi" sütununa onun yerine sorunun cevabı olan "Durum" yazılıyor.
    tree.heading("Değer", text="Saldırı Sayısı") #"Değer" sütununa onun yerine sorunun cevabı olan "Saldırıı Sayısı" yazılıyor.

    engellenen = len(df[df["EngellendiMi"] == "Evet"])  #engellenen saldırıları filtreler ve sayısını belirler
    engellenemeyen = len(df[df["EngellendiMi"] == "Hayir"]) #engellenemeyen saldırıları filtreler ve sayısını belirler
    toplam = len(df)

    tree.insert(  #Treeview içine yeni satır ekler.
        "", #Tek kategori kullandığımız için boş string veriliyor.
        tk.END, #Yeni satır en sona ekleniyor.
        values=("Engellenen Saldırılar", engellenen)  #Gelen verilerden ilk veri "Durum" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
    )

    tree.insert( #Treeview içine yeni satır ekler.
        "", #Tek kategori kullandığımız için boş string veriliyor.
        tk.END, #Yeni satır en sona ekleniyor.
        values=("Engellenemeyen Saldırılar", engellenemeyen) #Gelen verilerden ilk veri "Durum" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
    )

    tree.insert( #Treeview içine yeni satır ekler.
        "", #Tek kategori kullandığımız için boş string veriliyor.
        tk.END, #Yeni satır en sona ekleniyor.
        values=("TOPLAM SALDIRI", toplam) #Gelen verilerden ilk veri "Durum" sütununa ikincisi "Saldırı Sayısı" sütununa gider.
    )


def d_sıkkı(): #D şıkkının çözümü için fonksiyon tanımlanıyor.

    temizle() #Önceden seçilen tablo verileri temizleniyor.

    tree["columns"] = ("Bilgi", "Değer", "Süre") #Var olan 2 sütuna ek olarak yeni bir sütun oluşturuluyor.

    tree.heading("Bilgi", text="Saldırı Türü") #"Bilgi" sütununa onun yerine sorunun cevabı olan "Saldırı Türü" yazılıyor.
    tree.heading("Değer", text="En Uzun Müdahale Tarihi") #"Değer" sütununa onun yerine sorunun cevabı olan "En Uzun Müdahele Süresi" yazılıyor.
    tree.heading("Süre", text="Müdahale Süresi") #"Süre" sütununa onun yerine sorunun cevabı olan "Müdahele Süresi" yazılıyor.


    tree.column("Bilgi", width=250, anchor=tk.CENTER) #Sütunun genişliği belirleniyor ve gelecek değerler ortalanıyor.
    tree.column("Değer", width=250, anchor=tk.CENTER) #Sütunun genişliği belirleniyor ve gelecek değerler ortalanıyor.
    tree.column("Süre", width=250, anchor=tk.CENTER) #Sütunun genişliği belirleniyor ve gelecek değerler ortalanıyor.


    for saldiri_turu in df["SaldiriTuru"].unique(): #Her saldırı türü döngüye alınıyor.

        filtre = df[df["SaldiriTuru"] == saldiri_turu] #Sadece ilgili saldırı türü filtreleniyor.
        en_uzun = filtre.loc[filtre["MudahaleSuresi"].idxmax()] #En yüksek müdahale süresine sahip satır bulunuyor.

        tree.insert( #Treeview içine yeni satır ekler.
            "", #Tek kategori kullandığımız için boş string veriliyor.
            tk.END, #Yeni satır en sona ekleniyor.
            values=(saldiri_turu, en_uzun["Tarih"], en_uzun["MudahaleSuresi"])
            #Gelen verilerden ilk veri "Saldırı Sayısı" sütununa ikincisi "En Uzun Müdahele Tarihi" sütununa üçüncüsü "Müdahele Süresi" sütununa gider.
        )


def e_sıkkı(): #E şıkkının çözümü için fonksiyon tanımlanıyor.

    temizle() #Önceden seçilen tablo verileri temizleniyor.

    iki_sutun() #Tabloyu 2 sütuna çevirir.

    tree.heading("Bilgi", text="Tarih") #"Bilgi" sütununa onun yerine sorunun cevabı olan "Tarih" yazılıyor.
    tree.heading("Değer", text="Saldırı Sayısı") #"Değer" sütununa onun yerine sorunun cevabı olan "Saldırı Sayısı" yazılıyor.

    gunluk = df.groupby(df['Tarih'].dt.date).size().sort_values(ascending=False) #Tarihlere göre saldırılar gruplanıyor ve büyükten küçüğe sıralanıyor.
#"groupby" fonksiyonu gruplama yapar. "df['Tarih']" CSV dosyasından "Tarih" sütununu alır. 
    #"dt.date" ifadesi "datetime" fonksiyonu özelliklerini kullanmak içindir ve "date" ifadesi sadece günleri dikkate almak içindir.
    #".size()" Her grubun kaç elemanı olduğunu sayar. "sort_values(ascending=False)" Sonuçları büyükten küçüğe sıralar.

    for tarih, sayi in gunluk.items(): #Tarih ve saldırı sayıları döngüye alınıyor.

        etiket = f"{tarih} (EN YOĞUN)" if tarih == gunluk.index[0] else tarih #İlk tarih en yoğun saldırı tarihi olduğu için yanına etiket ekleniyor.

        tree.insert( #Treeview içine yeni satır ekler.
            "", #Tek kategori kullandığımız için boş string veriliyor.
            tk.END, #Yeni satır en sona ekleniyor.
            values=(etiket, sayi)
        )#Gelen verilerden ilk veri "" sütununa ikincisi "En Uzun Müdahele Tarihi" sütununa


buton_cerceve = tk.Frame(pencere) #Butonları düzenli tutmak için altta açılan alan oluşturuluyor.
buton_cerceve.pack(pady=20) #Butonlar pencereye yerleştirilip altta ve üstte 20 pixel boşluk bırakılıyor.

buton_ayarlar = {"font": ("Calibri", 10, "bold"), "width": 15} #Dictionary oluştuurlarak butonun font, yazı büyüklüğü vb. detaylar ekleniyor.

tk.Button(buton_cerceve, text="A Şıkkı", command=a_sıkkı, **buton_ayarlar).grid(row=0, column=0, padx=5) #Yeni buton oluşturuluyor ve detayları yazılıyor.
tk.Button(buton_cerceve, text="B Şıkkı", command=b_sıkkı, **buton_ayarlar).grid(row=0, column=1, padx=5) #Yeni buton oluşturuluyor ve detayları yazılıyor.
tk.Button(buton_cerceve, text="C Şıkkı", command=c_sıkkı, **buton_ayarlar).grid(row=0, column=2, padx=5) #Yeni buton oluşturuluyor ve detayları yazılıyor.
tk.Button(buton_cerceve, text="D Şıkkı", command=d_sıkkı, **buton_ayarlar).grid(row=0, column=3, padx=5) #Yeni buton oluşturuluyor ve detayları yazılıyor.
tk.Button(buton_cerceve, text="E Şıkkı", command=e_sıkkı, **buton_ayarlar).grid(row=0, column=4, padx=5) #Yeni buton oluşturuluyor ve detayları yazılıyor.

pencere.mainloop() #Pencerenin açılmasını ve programın çalışmasını sağlar