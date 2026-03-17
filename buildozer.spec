[app]
title = novelDR
package.name = noveldr
package.domain = org.moggle
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt
version = 0.1

# Requirements for your script
requirements = python3, kivy==master, kivymd==2.0.1rc1, requests, beautifulsoup4, charset-normalizer, urllib3, idna, certifi

orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.enable_androidx = True

# Critical fix for cross-compilation header issues
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
