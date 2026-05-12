# PROJE ÖDEVİ 1. SORUNUN CEVABI

import tkinter as tk  #Arayüz oluşturmak için tkinter kütüphanesini çağırdık
import pandas as pd   ## Veri analizi için pandas kütüphanesini çağırdık

def hesapla():
    # csv dosyasındaki verileri pandas DataFrame yapısına aktardık
    df = pd.read_csv('yardım.csv')
    
    # a) Para birimine göre gruplayıp miktarları topluyoruz (Çoktan aza sıralama)
    
    # 'Birim' sütununa göre gruplama 'Miktar' sütununa göre topla işlemi yapıyoruz ve indeksi sıfırlıyoruz
    birim_toplam = df.groupby('Birim')['Miktar'].sum().reset_index()
    # Paranın 'Miktarına' göre büyükten küçüğe doğru sıralıyoruz
    birim_sirali = birim_toplam.sort_values(by='Miktar', ascending=False)
    
    # b) Aynı verileri bu sefer azdan çoğa doğru sıralıyoruz
    
    ulke_sirali = birim_toplam.sort_values(by='Miktar', ascending=True)
    # Listedeki tüm bağış miktarlarının genel toplamını hesaplıyoruz
    genel_toplam = df['Miktar'].sum()

    # Sonuçları ekrana yazdırmadan önce metin kutusundaki eski verileri temizledik
    cikti_metni.delete('1.0', tk.END)


    # A şıkkı sonuçlarını (Çoktan Aza) döngü kullanarak metin kutusuna ekliyoruz
    cikti_metni.insert(tk.END, "--- A ŞIKKI: Para Miktarına Göre (Çoktan Aza) ---\n")
    for i, satir in birim_sirali.iterrows():
        cikti_metni.insert(tk.END, f"{satir['Birim']}: {satir['Miktar']}\n")


    # B şıkkı sonuçlarını (Azdan Çoğa) metin kutusuna ekliyoruz
    cikti_metni.insert(tk.END, "\n--- B ŞIKKI: Para Birimine Göre (Azdan Çoğa) ---\n")
    for i, satir in ulke_sirali.iterrows():
        cikti_metni.insert(tk.END, f"{satir['Birim']}: {satir['Miktar']}\n")

        
    # En alta 'genel toplam' bilgisini yazdırıyoruz
    cikti_metni.insert(tk.END, f"\nGENEL TOPLANAN YARDIM: {genel_toplam}")


    
# --- Biraz da uygulamamızın görünüşünü düzenleyelimm ---

pencere = tk.Tk()  # Ana uygulama penceresini oluşturuyoruz
pencere.title("YBS Yardım Organizasyonu")  # Pencere başlığını belirliyoruz
pencere.geometry("900x700")  #Açılan pencerimizin boyutunu ayarlıyoruz

baslik = tk.Label(pencere, text="Yardım Kayıt Analizi", font=("Arial", 25,"bold" ))
baslik.pack(pady=25)
#Uygulama başlığını oluşturup düzenliyoruz ve pencereye ekliyoruz

buton = tk.Button(pencere, text="Verileri Oku ve Listele", command=hesapla, bg="pink")
buton.pack(pady=20)
# Hesaplama işlemini tetikleyecek olan buttonu oluşturuyoruz ve rengini ayarlıyıp penceremize ekliyotuz

cikti_metni = tk.Text(pencere, height=40, width=90)
cikti_metni.pack(pady=100)
# Sonuçların görüneceği metin kutusunu da düzenliyoruz

pencere.mainloop() 
# ve kodumuz çalışmaya hazır