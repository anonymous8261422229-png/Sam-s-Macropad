# Sam's Macropad 

A custom 4-key (or more!) macropad designed with flexibility and aesthetics in mind. This project features a **Seeed XIAO RP2040** core and a fully 3D-printed enclosure.

## 🛠 Hardware Specifications

### Core Components
* **Microcontroller:** Seeed XIAO RP2040 (Can be mounted **SMD-style** for a low profile or through-hole). 
    * *Note: SMD soldering is advanced—stick to through-hole if this is your first build!*
* **Switches:** MX-Style mechanical switches (Supports up to 16x).
* **Keycaps:** Blank DSA profile .
* **Diodes:** Through-hole 1N4148 (Supports up to 20x).

### Optional Add-ons
* **Rotary Encoders:** Up to 2x EC11 encoders for scrolling/volume.
* **Display:** 0.91 inch OLED. 
    *  **Warning:** Ensure pin order is **GND-VCC-SCL-SDA**. Incorrect order will damage the display.
* **Lighting:** Up to 16x SK6812 MINI-E RGB LEDs.

### Assembly Hardware
* **Screws:** M3x16mm screws.
* **Inserts:** M3x5mx4mm heatset inserts.
* **Case:** 100% 3D Printed. (This design does not support acrylic layers).

---

##  Repository Structure

* **/CAD**: Contains the single `.STEP`/`.3MF` file for the 3D-printed enclosure.
* **/PCB**: KiCAD design files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`).
* **/Firmware**: KMK source code (`main.py`) for the RP2040.

---

##  Getting Started

1.  **Fabricate the PCB:** Use the files in the `/PCB` folder to order from your preferred manufacturer.
2.  **3D Print the Case:** Export the model from the `/CAD` folder. Ensure you use heatset inserts for the best durability.
3.  **Flash KMK:**
    * Download [CircuitPython for XIAO RP2040](https://circuitpython.org/board/seeeduino_xiao_rp2040/).
    * Drag the `kmk` folder and your `main.py` onto the `CIRCUITPY` drive.

---

## 🔗 Links
* **Project Repo:** [Sam's Macropad](https://github.com/anonymous8261422229-png/Sam-s-Macropad)
* **Built with:** [KMK Firmware](https://github.com/KMKfw/kmk_firmware)
