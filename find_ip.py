import socket
import qrcode 

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external IP address (Google DNS) to determine the local IP
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip

if __name__ == "__main__":
    ip = get_local_ip()
    print(f"\n🚀 Success! Your local Wi-Fi IP address is: {ip}")
    
    
    target_url = f"http://{ip}:5000/upload"
    print(f"🔗 Target Portal: {target_url}\n")
    
    qr = qrcode.QRCode(
        version=1,
        box_size=1,  
        border=2
    )
    qr.add_data(target_url)
    qr.make(fit=True)
    
    print("👇 SCAN THIS WITH YOUR PHONE CAMERA 👇\n")
    qr.print_tty()  # Prints the QR code directly using terminal text blocks
    
    # Backup PNG for alternate way to Scan
    high_res_qr = qrcode.QRCode(version=1, box_size=10, border=4)
    high_res_qr.add_data(target_url)
    high_res_qr.make(fit=True)
    img = high_res_qr.make_image(fill_color="black", back_color="white")
    img.save("phone_connect_qr.png")
    
    print("\n💾 Backup QR code image saved to your directory as: 'phone_connect_qr.png'\n")