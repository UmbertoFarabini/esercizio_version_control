import os
import shutil
import time

os.makedirs("./in", exist_ok=True)
os.makedirs("./processing", exist_ok=True)

while True:
    files = os.listdir("./in")
    if files:
        for file in files:
            src = os.path.join("./in", file)
            dst = os.path.join("./processing", file)
            shutil.move(src, dst)
            print(f"[script2] Moved to processing: {file}")
    else:
        print("[script2] No files in ./in")
    time.sleep(10)