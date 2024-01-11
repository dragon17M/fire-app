[app]

# (str) Title of your application
title = FireDetectionApp

# (str) Package name
package.name = fire_detection_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.include_exts = py,png,jpg,kv,atlas
source.include_exts_exclude = README.md, buildozer.spec
source.dir = .

# (list) Application requirements
requirements = python3,kivy,opencv-python,playsound,Pillow

# (str) Supported orientations (for now, just list them here)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = True

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (int) Android NDK version to use
android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your code will need to run.
android.ndk_api = 21

# (bool) Indicate whether the application should be using the android backend
android.arch = armeabi-v7a

# (str) Version of the application
version = 0.1
