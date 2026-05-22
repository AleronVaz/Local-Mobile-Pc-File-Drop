# 📱 Local Network File Drop

A lightweight utility to transfer photos, videos, and files from a mobile phone straight to a PC over a local Wi-Fi network. Because it transfers data entirely within your home network, it uses zero internet bandwidth and offers maximum transfer speeds.

## 🧭 The Plan
The goal is to run a local backend server on the PC that generates a scannable QR code. When scanned by a phone on the same Wi-Fi network, it will open a simple web page where users can browse their mobile files and drop them straight onto the PC desktop.

## 🛠️ Tech Stack & Progress

### Implemented So Far
- **Core Language:** Python 3
- **Networking:** Python's standard `socket` library (used to dynamically find the PC's real local Wi-Fi IP address).

### Planned / Upcoming Tech
- **Backend Server:** Flask (to host the web server and handle incoming file streams).
- **QR Generation:** `qrcode` & `pillow` (to dynamically convert the local URL into a scannable terminal image).
- **Frontend Portal:** HTML5 & Responsive CSS (to tap into native mobile file managers and handle multi-part file uploads).

## ⚙️ Current Setup & Testing

### Prerequisites
Make sure both your PC and mobile device are connected to the exact same Wi-Fi router.

### Running the Current Build
1. Clone the repository and navigate inside:
   
```bash
   git clone <your-repository-url>
   cd local-file-drop