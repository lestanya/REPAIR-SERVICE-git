@echo off
chcp 65001 >nul
title Django Project Manager

REM Сохраняем текущую папку
pushd

cd /d repair_app
cls

:menu
color 0D
cls
echo.
echo ========================================
echo    ^| Django Project Manager ^|
echo ========================================
echo.
echo [1] ^| Запустить сервер разработки
echo [2] ^| Создать миграции
echo [3] ^| Применить миграции
echo [4] ^| Django shell
echo [5] ^| Создать суперпользователя
echo [6] ^| Показать все команды Django
echo.
echo [Q] ^| Выход
echo.
set /p "choice=Выберите действие: "

if "%choice%"=="" goto menu

REM Восстанавливаем цвет перед любой командой
color 07

if "%choice%"=="1" (
    cls
    echo [ ^| ЗАПУСК СЕРВЕРА ^| ]
    echo Нажмите Ctrl+C для остановки
    echo.
    python manage.py runserver
    goto menu
)

if "%choice%"=="2" (
    cls
    echo [ ^| СОЗДАНИЕ МИГРАЦИЙ ^| ]
    echo.
    python manage.py makemigrations
    echo.
    pause
    goto menu
)

if "%choice%"=="3" (
    cls
    echo [ ^| ПРИМЕНЕНИЕ МИГРАЦИЙ ^| ]
    echo.
    python manage.py migrate
    echo.
    pause
    goto menu
)

if "%choice%"=="4" (
    cls
    echo [ ^| DJANGO SHELL ^| ]
    echo Используйте exit^(^) для выхода
    echo.
    python manage.py shell
    goto menu
)

if "%choice%"=="5" (
    cls
    echo [ ^| СОЗДАНИЕ СУПЕРПОЛЬЗОВАТЕЛЯ ^| ]
    echo.
    python manage.py createsuperuser
    goto menu
)

if "%choice%"=="6" (
    cls
    echo [ ^| ВСЕ КОМАНДЫ DJANGO ^| ]
    echo.
    python manage.py help
    pause
    goto menu
)

if /i "%choice%"=="q" goto quit

echo Неверный выбор!
pause
goto menu

:quit
color 07
popd
cls
echo До свидания!
timeout /t 2 >nul
cd ..
exit /b
