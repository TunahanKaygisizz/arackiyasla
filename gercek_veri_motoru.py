import json
import random
import os

# --- AYARLAR ---
# Bu versiyon "Master Görsel" kullanır. 
# Her yıl için ayrı resim aramaz, modele ait tek ve kaliteli resmi kullanır.

specs_db = {
    "Fiat": {
        "Egea": [
            {"start": 2015, "end": 2020, "engines": [
                {"name": "1.3 Multijet II", "hp": 95, "torque": 200, "fuel_type": "Dizel", "acc": 11.7, "top_speed": 183, "cons": 4.1, "weight": 1270, "baggage": 520},
                {"name": "1.6 Multijet II", "hp": 120, "torque": 320, "fuel_type": "Dizel", "acc": 9.8, "top_speed": 200, "cons": 4.5, "weight": 1300, "baggage": 520},
                {"name": "1.4 Fire", "hp": 95, "torque": 127, "fuel_type": "Benzin", "acc": 11.5, "top_speed": 185, "cons": 5.7, "weight": 1150, "baggage": 520}
            ]},
            {"start": 2021, "end": 2025, "engines": [
                {"name": "1.4 Fire", "hp": 95, "torque": 127, "fuel_type": "Benzin", "acc": 11.8, "top_speed": 186, "cons": 6.4, "weight": 1160, "baggage": 520},
                {"name": "1.0 FireFly", "hp": 100, "torque": 190, "fuel_type": "Benzin", "acc": 10.8, "top_speed": 192, "cons": 5.5, "weight": 1200, "baggage": 520},
                {"name": "1.5 Hibrit", "hp": 130, "torque": 240, "fuel_type": "Hibrit", "acc": 9.0, "top_speed": 205, "cons": 4.9, "weight": 1350, "baggage": 520}
            ]}
        ],
        "Linea": [
            {"start": 2007, "end": 2011, "engines": [
                {"name": "1.3 Multijet", "hp": 90, "torque": 200, "fuel_type": "Dizel", "acc": 13.8, "top_speed": 170, "cons": 4.9, "weight": 1180, "baggage": 500}
            ]},
            {"start": 2012, "end": 2017, "engines": [
                {"name": "1.3 Multijet Euro5", "hp": 95, "torque": 200, "fuel_type": "Dizel", "acc": 13.8, "top_speed": 170, "cons": 4.9, "weight": 1185, "baggage": 500},
                {"name": "1.6 Multijet", "hp": 105, "torque": 290, "fuel_type": "Dizel", "acc": 11.0, "top_speed": 190, "cons": 5.1, "weight": 1250, "baggage": 500}
            ]}
        ]
    },
    "Renault": {
        "Megane": [
            {"start": 2004, "end": 2009, "engines": [
                {"name": "1.5 dCi", "hp": 80, "torque": 185, "fuel_type": "Dizel", "acc": 14.3, "top_speed": 170, "cons": 4.6, "weight": 1205, "baggage": 520},
                {"name": "1.6 16V", "hp": 115, "torque": 152, "fuel_type": "Benzin", "acc": 10.9, "top_speed": 192, "cons": 6.8, "weight": 1175, "baggage": 520}
            ]},
            {"start": 2010, "end": 2015, "engines": [
                {"name": "1.5 dCi", "hp": 105, "torque": 240, "fuel_type": "Dizel", "acc": 10.9, "top_speed": 190, "cons": 4.5, "weight": 1280, "baggage": 405},
                {"name": "1.5 dCi EDC", "hp": 110, "torque": 240, "fuel_type": "Dizel", "acc": 11.9, "top_speed": 190, "cons": 4.4, "weight": 1290, "baggage": 405}
            ]},
            {"start": 2016, "end": 2024, "engines": [
                {"name": "1.5 dCi", "hp": 110, "torque": 260, "fuel_type": "Dizel", "acc": 11.2, "top_speed": 190, "cons": 3.9, "weight": 1380, "baggage": 550},
                {"name": "1.3 TCe", "hp": 140, "torque": 240, "fuel_type": "Benzin", "acc": 9.0, "top_speed": 205, "cons": 5.5, "weight": 1350, "baggage": 550}
            ]}
        ],
        "Fluence": [
            {"start": 2009, "end": 2016, "engines": [
                {"name": "1.5 dCi", "hp": 105, "torque": 240, "fuel_type": "Dizel", "acc": 11.0, "top_speed": 185, "cons": 4.5, "weight": 1280, "baggage": 530},
                {"name": "1.5 dCi EDC", "hp": 110, "torque": 240, "fuel_type": "Dizel", "acc": 11.9, "top_speed": 185, "cons": 4.4, "weight": 1290, "baggage": 530}
            ]}
        ]
    },
    "Volkswagen": {
        "Passat": [
            {"start": 2005, "end": 2010, "engines": [
                {"name": "1.6 FSI", "hp": 115, "torque": 155, "fuel_type": "Benzin", "acc": 11.4, "top_speed": 200, "cons": 7.5, "weight": 1450, "baggage": 565},
                {"name": "2.0 TDI", "hp": 140, "torque": 320, "fuel_type": "Dizel", "acc": 9.8, "top_speed": 209, "cons": 5.9, "weight": 1550, "baggage": 565}
            ]},
            {"start": 2011, "end": 2014, "engines": [
                {"name": "1.6 TDI BlueMotion", "hp": 105, "torque": 250, "fuel_type": "Dizel", "acc": 12.2, "top_speed": 195, "cons": 4.3, "weight": 1490, "baggage": 565},
                {"name": "1.4 TSI", "hp": 122, "torque": 200, "fuel_type": "Benzin", "acc": 10.3, "top_speed": 205, "cons": 6.3, "weight": 1440, "baggage": 565}
            ]},
            {"start": 2015, "end": 2023, "engines": [
                {"name": "1.6 TDI", "hp": 120, "torque": 250, "fuel_type": "Dizel", "acc": 10.8, "top_speed": 206, "cons": 4.1, "weight": 1480, "baggage": 586},
                {"name": "1.5 TSI", "hp": 150, "torque": 250, "fuel_type": "Benzin", "acc": 8.7, "top_speed": 220, "cons": 5.3, "weight": 1420, "baggage": 586}
            ]}
        ]
    },
    "Toyota": {
        "Corolla": [
            {"start": 2007, "end": 2012, "engines": [
                {"name": "1.4 D-4D", "hp": 90, "torque": 190, "fuel_type": "Dizel", "acc": 12.0, "top_speed": 175, "cons": 4.9, "weight": 1270, "baggage": 450},
                {"name": "1.6 Dual VVT-i", "hp": 124, "torque": 157, "fuel_type": "Benzin", "acc": 10.4, "top_speed": 195, "cons": 6.9, "weight": 1250, "baggage": 450}
            ]},
            {"start": 2013, "end": 2018, "engines": [
                {"name": "1.4 D-4D", "hp": 90, "torque": 205, "fuel_type": "Dizel", "acc": 12.5, "top_speed": 180, "cons": 4.1, "weight": 1280, "baggage": 452},
                {"name": "1.6 Valvematic", "hp": 132, "torque": 160, "fuel_type": "Benzin", "acc": 10.0, "top_speed": 200, "cons": 6.0, "weight": 1260, "baggage": 452}
            ]},
            {"start": 2019, "end": 2025, "engines": [
                {"name": "1.8 Hybrid Dream", "hp": 122, "torque": 142, "fuel_type": "Hibrit", "acc": 11.0, "top_speed": 180, "cons": 3.8, "weight": 1380, "baggage": 471},
                {"name": "1.5 Vision", "hp": 123, "torque": 153, "fuel_type": "Benzin", "acc": 12.1, "top_speed": 190, "cons": 5.8, "weight": 1290, "baggage": 471}
            ]}
        ]
    },
    "Honda": {
        "Civic": [
            {"start": 2006, "end": 2011, "engines": [
                {"name": "1.6 i-VTEC", "hp": 125, "torque": 152, "fuel_type": "Benzin", "acc": 10.3, "top_speed": 200, "cons": 7.5, "weight": 1190, "baggage": 389}
            ]},
            {"start": 2012, "end": 2016, "engines": [
                {"name": "1.6 i-VTEC Eco", "hp": 125, "torque": 152, "fuel_type": "Benzin/LPG", "acc": 10.5, "top_speed": 198, "cons": 7.0, "weight": 1240, "baggage": 440}
            ]},
            {"start": 2017, "end": 2021, "engines": [
                {"name": "1.6 i-VTEC", "hp": 125, "torque": 152, "fuel_type": "Benzin/LPG", "acc": 10.6, "top_speed": 200, "cons": 6.7, "weight": 1290, "baggage": 519},
                {"name": "1.5 VTEC Turbo", "hp": 182, "torque": 220, "fuel_type": "Benzin", "acc": 8.1, "top_speed": 210, "cons": 6.0, "weight": 1350, "baggage": 519}
            ]}
        ]
    }
}

def clean_name(text):
    replacements = {'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c', 'İ': 'I', 'Ğ': 'G', 'Ü': 'U', 'Ş': 'S', 'Ö': 'O', 'Ç': 'C', ' ': '_'}
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.lower()

def calculate_score(engine, year):
    acc_score = max(30, (15 - engine['acc']) * 14)
    torque_score = (engine['torque'] / 3.5)
    perf_score = (acc_score * 0.6) + (torque_score * 0.4)
    
    fuel_score = max(20, 150 - (engine['cons'] * 12.5))
    
    base_tech = 40 + ((year - 2000) * 2.5)
    base_comfort = 50 + ((year - 2000) * 1.5)
    
    if engine['weight'] > 1400: base_comfort += 10
    if engine['weight'] < 1100: base_comfort -= 10

    final_score = (perf_score * 0.25) + (fuel_score * 0.30) + (base_comfort * 0.25) + (base_tech * 0.20)
    
    return {
        "score": int(min(99, max(40, final_score))),
        "s_fuel": int(min(100, fuel_score)),
        "s_hp": int(min(100, perf_score)),
        "s_comfort": int(min(100, base_comfort)),
        "s_tech": int(min(100, base_tech))
    }

generated_cars = []

print("Veritabanı oluşturuluyor...")

for brand, models in specs_db.items():
    for model_name, generations in models.items():
        for gen in generations:
            for year in range(gen['start'], gen['end'] + 1, 2): 
                for engine in gen['engines']:
                    scores = calculate_score(engine, year)
                    
                    # --- YENİ RESİM MANTIĞI (MASTER GÖRSEL) ---
                    # Yıl bilgisini kullanmıyoruz. Sadece Marka_Model.jpg
                    # Örn: img/fiat_egea.jpg
                    
                    img_name = f"{clean_name(brand)}_{clean_name(model_name)}.jpg"
                    img_path = f"img/{img_name}"
                    
                    # Eğer dosya yoksa placeholder koy (Hata önleyici)
                    if not os.path.exists(img_path):
                        # print(f"Uyarı: {img_name} bulunamadı!") # Konsolu kirletmeyelim
                        img_path = "https://via.placeholder.com/320x240?text=Resim+Yok"

                    car_obj = {
                        "brand": brand,
                        "model": model_name,
                        "year": year,
                        "engine_name": engine['name'],
                        "hp": engine['hp'],
                        "torque": engine['torque'],
                        "fuel": engine['fuel_type'],
                        "acc": engine['acc'],
                        "top_speed": engine['top_speed'],
                        "cons": engine['cons'],
                        "weight": engine['weight'],
                        "baggage": engine['baggage'],
                        "image": img_path, 
                        
                        "score": scores['score'],
                        "s_fuel": scores['s_fuel'],
                        "s_hp": scores['s_hp'],
                        "s_comfort": scores['s_comfort'],
                        "s_tech": scores['s_tech']
                    }
                    generated_cars.append(car_obj)

random.shuffle(generated_cars)

with open("gercek_arac_verileri.js", "w", encoding="utf-8") as f:
    f.write(f"const carData = {json.dumps(generated_cars, indent=4)};")

print(f"Bitti! Toplam {len(generated_cars)} araç verisi 'gercek_arac_verileri.js' dosyasına yazıldı.")