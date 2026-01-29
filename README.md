# AraçKıyasla 🚗

**AraçKıyas**, araçların teknik verilerini (HP, Tork, Tüketim, 0-100) analiz ederek kullanıcıya en mantıklı aracı öneren, yapay zeka destekli bir karşılaştırma platformu prototipidir.

🔗 **Canlı Demo:** [https://tunahankaygisizz.github.io/arackiyasla/](https://tunahankaygisizz.github.io/arackiyasla/)

![Project Screenshot](https://tunahankaygisizz.github.io/arackiyasla/img/fiat_egea.jpg)

---

## 🛠️ Proje Hakkında Dürüst Notlar (Development Philosophy)

Bu proje benim için bir **"Prompt Engineering" (İstem Mühendisliği) ve Algoritma Tasarımı** deneyidir. 

Bir Bilgisayar Mühendisliği öğrencisi olarak bu projede odaklandığım nokta "kod hamallığı" değil, **Yazılım Mimarisi (Software Architecture)** ve **Ürün Yönetimi** olmuştur.

* **Benim Rolüm:** Projenin mantıksal çerçevesini, puanlama algoritmasını (hangi verinin ne kadar ağırlığı olacağını), veri yapısını ve kullanıcı deneyimini (UX) ben kurguladım.
* **AI Rolü:** Kurguladığım mantık çerçevesinde; HTML yapısı, CSS stilleri ve JavaScript fonksiyonlarının yazımında **LLM (Large Language Model)** araçlarından asistan olarak faydalandım.
* **Veri Seti:** Binlerce satırlık veriyi elle girmek yerine, araçların teknik verilerini simüle eden ve bunları JSON formatına dönüştüren bir **Python otomasyon scripti** tasarladım.

---

## 🚀 Temel Özellikler

* **⚖️ Akıllı Puanlama Algoritması:** Araçlara sadece beygir gücüne göre değil; Performans (%25), Yakıt (%30), Konfor (%25) ve Teknoloji (%20) kriterlerine göre ağırlıklı puan verir.
* **🔍 Dinamik Filtreleme:** Marka, Yıl, Yakıt Tipi ve Motor Gücüne göre anlık (istemci taraflı) filtreleme yapar.
* **VS Karşılaştırma Modu:** Seçilen araçları yan yana getirir ve her kategoride (Hız, Bagaj, Tüketim) kazananı yeşil ile vurgular.
* **⚡ Statik Mimari:** Backend gerektirmeden, tarayıcı üzerinde çalışan (Client-Side) hafif ve hızlı yapı.

---

## 🧮 Puanlama Mantığı (Algorithm Logic)

Araçların "Puanı" rastgele değildir. Python tarafında kurduğum şu mantığa göre hesaplanır:

```python
# Örnek Puanlama Formülü (Basitleştirilmiş)
Performance = (0_100_Hızlanma * 0.6) + (Tork * 0.4)
Fuel_Score  = (Reel_Tüketim * Katsayı)
Comfort     = (Model_Yılı * 1.5) + (Ağırlık_Etkisi)

Final_Score = (Performance * 0.25) + (Fuel_Score * 0.30) + (Comfort * 0.25) + (Tech * 0.20)
