# Parancssoros futtatás

Az alkalmazást futtatni kell a parancssorból, először környezeti változókat állítunk:

## Windows

```
set FLASK_APP=2_main.py
set FLASK_ENV=development
```


## Linux

```
export FLASK_APP=2_main.py
export FLASK_ENV=development
```

## Futtatás

```
python -m flask run
```
vagy

```
python -m 2_main.py
```

Megtekintés:
http://0.0.0.0:5000/ 