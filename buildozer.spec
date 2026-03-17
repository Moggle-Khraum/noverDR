[app]
title = novelDR
package.name = noveldr
package.domain = org.moggle
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt
version = 0.1

# Using stable kivy version
requirements = python3, kivy, kivymd==2.0.1rc1, requests, beautifulsoup4, charset-normalizer, urllib3, idna, certifi

orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True

# Still keep p4a master as it contains necessary library fixes
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
