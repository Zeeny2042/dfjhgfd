[app]

# Название приложения
title = ClickerApp

# Имя пакета (должно быть уникальным)
package.name = clickerapp

# Домен пакета (например, org.example)
package.domain = org.example

# Путь к исходным файлам
source.dir = .

# Расширения файлов, которые нужно включить (через запятую)
source.include_exts = py, kv, json

# Версия приложения
version = 1.0

# Зависимости (Kivy, библиотеки)
requirements = kivy==2.0.0, pathlib, android

# Ориентация экрана (portrait или landscape)
orientation = portrait

# Разрешения Android (например, INTERNET, VIBRATE)
android.permissions = 

# Уровень API Android (минимальная версия)
android.minapi = 21

# Целевой уровень API Android
android.api = 34

# Версия NDK (используется для сборки нативного кода)
android.ndk = 26b

# Автоматическое скачивание SDK/NDK (оставьте пустым, если Buildozer должен скачать сам)
android.ndk = 23b  # или 26b для Android API 34
android.api = 34

# Иконка приложения (путь к файлу .png)
# icon.filename = %(source.dir)s/assets/icon.png

# Логотип приложения (путь к файлу .png)
# presplash.filename = %(source.dir)s/assets/presplash.png

# Дополнительные настройки
[buildozer]

# Уровень детализации логов (0-2)
log_level = 2

requirements = kivy==2.0.0, pathlib, android
