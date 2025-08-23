@echo off
call .venv\Scripts\activate
pyinstaller -w -n CFSS_config_maker --onefile --icon icon.ico main.py