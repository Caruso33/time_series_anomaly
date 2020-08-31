# time_series_anomaly

## Aufgaben

- Webanwendung in React
- Erstellung des/der Chart(s) in D3
- Speicherung der Daten in einer Datenbank Ihrer Wahl
- Kommunikation mit dem Backend zur Datenbankabfrage über REST
- Weitere Module (z.B. für ein Backend) in Python

## Verwendete Komponenten

- [Sqlite3](https://sqlite.org/) dient als database ([InfluxDB](https://www.influxdata.com/products/influxdb-overview/) war geplant, war zeitlich leider nicht machbar)
- [Django](https://www.djangoproject.com/) + [Django Rest Framework](https://www.django-rest-framework.org/)
- [ReactJS](https://reactjs.org/) frontend
- [C3JS](https://c3js.org/) Chart library (basiert auf D3)

## Programm Starten

### Backend

[python](https://www.python.org/) in der version 3 muss installiert sein (am besten mit [Conda](https://anaconda.org/anaconda/conda) eine virtuelle Umgebung erstellen)

`pip install -r requirements.txt`

um die Komponenten zu installieren

`python app.py`

um die app zu starten - was als erstes die Datenbank, dann Django migrationen erstellen sollte, und daraufhin die app started

REST endpoint ist `localhost:8000/time_series/`

### Frontend

[NodeJS](https://nodejs.org/en/) muss installiert sein.
In den Ordner `frontend` navigieren und die Dependencies installieren

`cd frontend && npm install`

mit `npm run start` den Entwicklungsserver starten

`localhost:3000` mit dem Browser besuchen, um die Webseite zu sehen

## TODO:

- influxDB anstatt sqlite3 verwenden
- Django served das Produktionsbuild von React mit, was unter `localhost:8000` zu erreichen ist
