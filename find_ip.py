import socket

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
    print(f"🔗 Your phone will look for this endpoint: http://{ip}:5000\n")