import time
import random

# ---------------------------------
# --- SETTINGS (Ayarlar) ---
# ---------------------------------

# If light level is BELOW this value, we consider it "dark"
# Eğer ışık seviyesi bu değerin ALTINDAYSA, "karanlık" sayarız.
LIGHT_THRESHOLD = 400

# How many seconds to wait between checks
# Kontroller arasında kaç saniye beklenecek
LOOP_DELAY_SECONDS = 3

# ---------------------------------
# --- SIMULATOR FUNCTIONS (Simülatör Fonksiyonları) ---
# ---------------------------------

def check_simulated_motion():
    """
    Simulates a PIR motion sensor.
    Returns True (motion) or False (no motion) randomly.
    Bir PIR hareket sensörünü simüle eder.
    Rastgele True (hareket var) veya False (hareket yok) döndürür.
    """
    # 50/50 chance to return True or False
    return random.choice([True, False])

def get_simulated_light_level():
    """
    Simulates a light (LDR) sensor.
    Returns a random light value between 0 (pitch black) and 1000 (very bright).
    Bir ışık (LDR) sensörünü simüle eder.
    0 (zifiri karanlık) ile 1000 (çok parlak) arasında rastgele bir değer döndürür.
    """
    return random.randint(0, 1000)

# ---------------------------------
# --- MAIN PROGRAM (Ana Program) ---
# ---------------------------------
def main():
    print("--- Smart Light Simulator ---")
    print(f"Running... Light threshold is set to: {LIGHT_THRESHOLD}")
    print("Press Ctrl+C to stop.")

    try:
        # Infinite loop to keep checking
        # Sürekli kontrol etmek için sonsuz döngü
        while True:
            # 1. Get data from (simulated) sensors
            # (Simüle edilen) sensörlerden verileri al
            motion_detected = check_simulated_motion()
            current_light_level = get_simulated_light_level()

            # 2. Decision Logic (Karar Mekanizması)
            # This is the "brain" of the program
            # Bu, programın "beyni"
            
            if motion_detected == True and current_light_level < LIGHT_THRESHOLD:
                # --- CONDITION MET: Turn light ON ---
                # --- ŞART SAĞLANDI: Işığı AÇ ---
                print(f"[MOTION: {motion_detected}, LIGHT: {current_light_level}] -> Motion detected AND it's dark. Turning light ON.")
            
            else:
                # --- CONDITION NOT MET: Turn light OFF ---
                # --- ŞART SAĞLANMADI: Işığı KAPAT ---
                if motion_detected == False:
                    print(f"[MOTION: {motion_detected}, LIGHT: {current_light_level}] -> No motion detected. Turning light OFF.")
                elif current_light_level >= LIGHT_THRESHOLD:
                    print(f"[MOTION: {motion_detected}, LIGHT: {current_light_level}] -> Motion detected, but it's bright enough. Turning light OFF.")

            # 3. Wait for the next check
            # Bir sonraki kontrol için bekle
            time.sleep(LOOP_DELAY_SECONDS)
    
    except KeyboardInterrupt:
        print("\nSimulator stopped. Goodbye!")

# ---------------------------------
# --- START THE PROGRAM (Programı Başlat) ---
# ---------------------------------
if __name__ == "__main__":
    main()