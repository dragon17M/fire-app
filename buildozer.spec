[app]

# (str) Title of your application
title = FireDetectionApp

# (str) Package name
package.name = fire_detection_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas
source.include_exts_exclude = README.md, buildozer.spec

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,opencv-python,playsound,Pillow

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy
# requirements.source.sdl2_faucet = ../../sdl2_faucet

# (str) Supported orientations (for now, just list them here)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) The entry point to launch, for Kivy it should be the name of your app
#rootpath = /path/to/your/app

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,opencv-python,playsound,Pillow

# (str) The entry point to launch, for Kivy it should be the name of your app
#rootpath = /path/to/your/app

# (list) Garden requirements
#garden_requirements = 

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
# android.permissions = INTERNET

# (list) Application needs a fullscreen mode
fullscreen = True

# (list) Services to declare
# android.services =


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
#android.blacklist = pygame
android.arch = armeabi-v7a

# (bool) Indicate whether the version of SDL2 should be forced
# blacklisted sdl2 version
#android.sdl2_version = ''

# (str) Android Gradle plugin to use, one of 'default', 'readable' or 'pov'
#android.gradle =  '2.3.0'
