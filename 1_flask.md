# Python Flask alapok

## Mi az a Flask?
A Flask egy webes keretrendszer Pythonban írva.

Előnyei:
* Könnyű beletanulni, ideális kezdőknek
* Könnyen találhatóak hozzá kiegészítők, modulok
* Könnyen olvasható és átlátható a benne írt működés
* "Lightweight", azaz nem fogyaszt sok erőforrást
* Sok leírás található hozzá

Kisebb projektekre ajánlott, API írásához ideális. Kis létszámú fejlesztői csapatoknak ideális.

Hátránya:
* Nagy szabadság, emiatt a tanulási görbe néha meredek
* Kevés a kész megoldás, sokszor kutatni kell a legjobb lehetőséget
* Production környezetben figyelni kell az optimalizálásra, biztonságra 

## Fontos linkek:

Repo link: https://github.com/pallets/flask

Dokumentáció: https://flask.palletsprojects.com/en/1.1.x/

Használt verzió: 1.1.1

Hivatalos 'quickstart': https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

## Előkészítés
1. Python 3.6 letöltés és telepítés

2. Venv létrehozás:
Indítsunk egy terminált a mappában ahol dolgozni fogunk, pl::

`C:\Work\hello_flask`

```
cd C:\Work\hello_flask
python3 -m venv venv
source venv\Scripts\activate
```

így kell kinézzen:

```(venv) c:\tmp>```

Flask telepítés:

```pip install flask==1.1.1```

