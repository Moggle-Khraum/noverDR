[app]
# (str) Title of your application
title = Novel DR

# (str) Package name
package.name = noveldr

# (str) Package domain (needed for android packaging)
package.domain = org.noveldr

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,txt

# (list) Application requirements
# Added requests, bs4, and charset-normalizer for the NovelEngine
requirements = python3, kivy, kivymd==2.0.1rc1, requests, beautifulsoup4, charset-normalizer, urllib3, idna, certifi

# (str) Custom source folders for requirements
# kivymd 2.0.1 is required for the new Material Design 3 components used in your script

# (str) Presplash of the application
presplash.filename = %(source.dir)s/icon.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Required for downloading novels from the web
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
