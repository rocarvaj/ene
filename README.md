# Scripts para descargar y resumir la ENE

El siguiente repositorio contiene scripts para descargar, re codificar y resumir la encuesta nacional de empleo (ENE).

## `ene-downloader.py`
Éste script escrito en python (y con la ayuda de ChatGPT) descarga la encuesta nacional de empleo (en formato CSV) para los cuatro trimestres disjuntos de cada año en un cierto rango entregado por el usuario. Los archivos csv resultantes deben ser procesados con el notebook `recodificar-y-resumir-ene.Rmd`.


## `recodificar-y-resumir-ene.Rmd`
El notebook usa una serie de archivos CSV descargados desde <https://www.ine.gob.cl/estadisticas/sociales/mercado-laboral/ocupacion-y-desocupacion> (usando el script `ene-downloader.py`), recodifica algunas variables y luego elabora una base de datos con el número de personas, en la población en edad de trabajar, para cada año, trimestre, región, sexo, nivel educacional, rango etario, estado de actividad económica.


## Notas

* El script `ene-downloader.py` descarga los 4 trimestres disjuntos de cada año (EFM, AMJ, JAS, OND).
* En el caso de nivel educacional, rango etario y estado de actividad económica, algunas de las categorías fueron agrupadas para hacer más simple el análisis.
* Los cálculos con factor de expansión son redondeados para evitar confundir a los alumnos con números fraccionarios de personas. Es posible que esto genere incongruencias con cálculos realizados directamente sobre la base de datos original.


[Rodolfo Carvajal](https://github.com/rocarvaj), 2024
