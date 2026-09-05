import sys
from core.overlay import Overlay
from core.recoil_compensator import RecoilCompensator
from utils.config_loader import load_config

def main():
    print("CS2 Aim Toolkit (Educational)")
    config = load_config("configs/default.json")
    overlay = Overlay()
    comp = RecoilCompensator(config.get("sensitivity", 1.0))
    # В реальности здесь запускается цикл, но мы просто выводим сообщение
    print("Overlay started. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()