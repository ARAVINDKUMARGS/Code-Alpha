import os, shutil

source = "/storage/emulated/0/Download"
destination = "/storage/emulated/0/Pictures/JPG_Files"

if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))

print("✅ All JPG files moved successfully!")
