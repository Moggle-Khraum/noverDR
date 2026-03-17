[app]
# (str) Title of your application
title = novelDR

# (str) Package name
package.name = noveldr

# (str) Package domain (needed for android packaging)
package.domain = org.moggle

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,txt

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Note: kivy==master is used to ensure compatibility with modern Android NDKs
requirements = python3, kivy==master, kivymd==2.0.1rc1, requests, beautifulsoup4, charset-normalizer, urllib3, idna, certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support (Required for KivyMD 2.0+)
android.enable_androidx = True

# (str) python-for-android branch to use
# This is critical for fixing the header errors we saw earlier
p4a.branch = master

# (list) List of service to declare
services = 

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
