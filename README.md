# 📱 LocalDrop: Ad-Hoc Local Network File Pipeline

A high-performance, private utility designed to instantly transfer photos, videos, and files from a mobile phone straight to a PC over a local Wi-Fi network. Because it moves data entirely within your home router gateway, it uses **zero internet bandwidth**, and uses no internet and speed is as fast as wifi hardware.

---

## ✨ Features

* **Dynamic Network Discovery:** Automatically maps out your PC's real network hardware interface card to locate its private IP address, ignoring confusing virtual machines or VPN adapters.
* **On-the-Fly QR Matrices:** Auto-generates scannable network endpoints inside your terminal via text blocks, alongside a high-res fallback PNG image file.
* **AirDrop Mobile Aesthetic:** Mobile First Friendly Design, Dynamic CSS.
* **Zero-Refresh Network Streams:** You can drop file after file rapidly without your mobile browser crashing or forcing a page reload.
* **Color-Shifting Progress Pipeline:** Tracks binary byte streaming over your router in real time, expanding a custom progress bar that shifts colors from a muted neutral gray to an active green on completion.
* **Automatic System Configuration:** Reads your Windows profile paths on startup to automatically generate a designated `Mobile_Files` folder right inside your local **Downloads** directory.
* **Secure File Sanitation:** Cleans Files being uploaded before saving.

---
## 🛠️ Tech Stack

* **Backend Engine:** Python 3
* **Web Server Architecture:** Flask
* **Networking Modules:** Standard `socket` library utilizing connectionless UDP handshakes.
* **Image Processing Engine:** `qrcode` matrix rendering & `pillow` (PIL) for fallback asset compilation.
* **Security Middleware:** `werkzeug.utils.secure_filename` to clean files.
* **Frontend Portal:** HTML5 layouts, responsive CSS3, and raw Asynchronous Vanilla JavaScript utilizing `XMLHttpRequest` lifecycle listeners for precise chunk-by-chunk progress tracking.

---

## 🧠 How the Pipeline Works

```text
[Phone Storage] ──(Native File Picker)──> [Mobile Browser Engine] 
                                                    │
                                           (Wi-Fi Binary Stream)
                                                    │
                                                    ▼
                                            [Router Gateway]
                                                    │
                                                    ▼
                                           [Windows Port 5000]
                                                    │
                                                    ▼
       [Flask Server] ──(secure_filename)──> [Python Disk IO] ──> [Downloads/Mobile_Files/]

## 🚀 Installation & Usage Instructions

---


### Prerequisites
Make sure both your host computer and your mobile device are actively connected to the **exact same Wi-Fi router network** or access point.

### 1. Clone & Organize the Workspace
Clone your repository and verify your file directory layout matches the standard Flask blueprint:

```bash
git clone [https://github.com/AleronVaz/Local-Mobile-Pc-File-Drop.git](https://github.com/AleronVaz/Local-Mobile-Pc-File-Drop.git)
cd Local-Mobile-Pc-File-Drop