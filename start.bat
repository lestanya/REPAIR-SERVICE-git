chcp 65001 >nul


@echo off
echo Активация venv...
call venv\Scripts\activate

echo Установка зависимостей...
call pip install -r requirements.txt

echo Проверка пакетов:
call pip list

@REM echo.
@REM echo ✅ Настройка окончена! Запуск Django? (Y/N)
@REM set /p choice= 

@REM if /i "%choice%"=="Y" (
@REM     echo Запуск сервера...
@REM     python manage.py runserver
@REM ) else (
@REM     echo Готово! manage.py готов к работе.
@REM )

cmd /k
