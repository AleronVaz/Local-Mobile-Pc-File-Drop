import socket
import qrcode 
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import sys
import ctypes 

if sys.platform == "win32":
    try:
        kernel32 = ctypes.windll.kernel32
        stdout_handle = kernel32.GetStdHandle(-11) 
        mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(stdout_handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(stdout_handle, mode.value | 0x0004)
    except Exception:
        os.system('')

if getattr(sys, 'frozen', False):
    # App is running bundled inside an executable container
    template_dir = os.path.join(sys._MEIPASS, 'templates')
    static_dir = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
else:
    app = Flask(__name__)

#Storing in Downloads/Mobile_Files
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
UPLOAD_FOLDER = os.path.join(DOWNLOADS_PATH, "Mobile_Files")

# Create the Mobile_Files folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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

@app.route('/')
@app.route('/upload', methods=['GET', 'POST'])
def upload_portal():
    if request.method == 'POST':
        if 'dropped_file' not in request.files:
            return "Error: No file container received. Check your HTML form input name.", 400
            
        file = request.files['dropped_file']
        
        if file.filename == '':
            return "Error: No file chosen. Go back and select an object.", 400
            
        if file:
            #Clean the filename
            filename = secure_filename(file.filename)        
            final_destination = os.path.join(UPLOAD_FOLDER, filename)
            file.save(final_destination)
            
            print(f"\n📥 SUCCESS: Wrote '{filename}' straight into Downloads/Mobile_Files/")
            return f"🎉 File '{filename}' successfully dropped to your PC!"
        
    elif request.method == 'GET':
        print("\n📱 Phone requested the page (GET)!")
        return render_template('upload.html')


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
    
    print("SCAN THIS WITH YOUR PHONE CAMERA\n")
    qr.print_tty()  # Prints the QR code directly using terminal text blocks
    
    # Backup PNG for alternate way to Scan
    high_res_qr = qrcode.QRCode(version=1, box_size=10, border=4)
    high_res_qr.add_data(target_url)
    high_res_qr.make(fit=True)
    img = high_res_qr.make_image(fill_color="black", back_color="white")
    img.save("phone_connect_qr.png")
    print("\n💾 Backup QR code image saved to your directory as: 'phone_connect_qr.png'\n")

    print("Starting Server\n")
    # host='0.0.0.0' tells the OS to listen to incoming signals from the local Wi-Fi network
    app.run(host='0.0.0.0', port=5000)