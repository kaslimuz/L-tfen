[app]

title Oyunum

package.name oyunum

source.dir

package.domain= org.seninadın

source.include exts py,png,jpg,jpeg,kv,atlas,ogg, wav

version 0.1

requirements python3, pygame

orientation landscape

fullscreen=1

icon.filename=%(source.dir)s/icon.png

presplash.filename=%(source.dir)s/icon.png

[app:android]

android.permissions INTERNET

android.ap1 = 33

android.minap1 = 21

android.ndk = 25b

android.archs arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
