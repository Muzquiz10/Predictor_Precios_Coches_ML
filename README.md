# Predictor_Precios_Coches_ML
## Proyecto de Machine Learning para el Bootcamp de Data Science de The Bridge School

El objetivo de este proyecto es crear un modelo de Machine Learning funcional y preparado para ponerlo en producción, capaz rápidamente de a través de diferentes parámetros, poder saber el precio al que se debe vender un vehículo.

Para ello he trabajado con un dataset de más de 40000 registros con una gran variedad de tipo de coches, desde precios muy bajos a precios muy altos, desde marcas básicas a marcas de alta gama.

Tras analizar los datos de los que disponía (En el EDA se puede ver con detalle todo este análisis) Tras este análisis pude ser capaz de implementar una lógica para que mis variables tuvieran una correlación interesante con mi target (el precio). 

Por último antes de empezar a probar los diferentes modelos de Machine Learning, limpie los registros que no iban a ser útiles y procedí a eliminar las filas con valores vacíos. 

Para poder encontrar el mejor modelo que mejor se adapatara a este caso, decidí empezar a hacer pruebas desde el modelo más básico, desde una Liner Regresion, hasta los modelos más complejos. En total probé 9 modelos. En el documento llamado modelos, se puede ver con detalle todas las pruebas que hice. El modelo elegido se llama my_model y es a través de un Gradient  Boosting.

Por último para poder probar el modelo de una manera más práctica he creado una pequeña interfaz (interfaz_datos.py) que se encuentra en la carpeta "interfaz_pruebaModelo". Con esta podemos meter los datos del vehículo para que nos imprimar el precio predicho.
