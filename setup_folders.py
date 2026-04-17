import os

directories = {
    "01_Accelerator_and_RF_Systems": "Hızlandırıcı Zinciri ve Radyo Frekans (RF) Sistemleri üzerine araştırmalar, notlar ve simülasyonlar.",
    "02_Cryogenics_and_Superconducting_Magnets": "Kriyojenik teknolojiler, 1.9 Kelvin'e soğutma sistemleri ve devasa süperiletken dipol mıknatıslar.",
    "03_DAQ_and_Trigger_Systems": "Saniyede 40 milyon çarpışmayı işleyen FPGA tabanlı tetikleyiciler ve Veri Toplama (DAQ) donanımları.",
    "04_Control_and_Safety_Systems": "Security by Design, Interlock, SCADA mimarileri ve yüksek enerji güvenliği sistemleri.",
    "05_WLCG_and_Distributed_Computing": "Worldwide LHC Computing Grid, küresel dağıtık hesaplama ve Petabayt seviyesi veri yönetimi.",
    "06_Open_Source_Technologies": "ROOT, Geant4, KiCad, White Rabbit gibi CERN kökenli teknolojiler ve pratik uygulamaları.",
    "assets": "Görseller, pdf dokümanları, paper ve medya dosyaları."
}

for d, desc in directories.items():
    os.makedirs(d, exist_ok=True)
    if d != "assets":
        readme_path = os.path.join(d, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                title = d.replace("_", " ")
                f.write(f"# {title}\n\n{desc}\n\nEklemeler ve dökümantasyonlar buraya yapılacaktır.\n")
    else:
        keep_path = os.path.join(d, ".gitkeep")
        if not os.path.exists(keep_path):
            with open(keep_path, "w", encoding="utf-8") as f:
                f.write("")

print("Directory structure created successfully.")
