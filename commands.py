import subprocess
import webbrowser

subprocess.run(["ping", "localhost"])
webbrowser.get("open -a C:\\Program F~\\Mozilla Firefox\\firefox.exe %s")
webbrowser.open('http://google.com')
webbrowser.open(
    'file:///C:/Users/Eduardo/Documents/clases/feb-jun%202021/C.jpg'
    )
subprocess.run(["python", "paint.py"])