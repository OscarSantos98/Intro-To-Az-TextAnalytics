# Intro-To-Az-TextAnalytics

> Taller impartido en [Global AI Back Together](https://www.facebook.com/azuretechfrogs/photos/a.164733232351686/208956561262686/?type=3&source=57&refid=52)

El objetivo principal del taller es compartir una visión general de las capacidades de procesamiento de lenguage natural utilizando Text Analytics API de Microsoft Azure.

A lo largo del taller, se revisarán las distintas funcionalidades como extracción de frases, detección de lenguaje, entidades y particularmente análisis de sentimiento. Con la cual realizaremos ejemplos de aplicación con Python, con Microsoft Excel, Con Microsoft Power BI y dentro de un bot

## Requisitos

### IDE

- [Visual Studio Code](https://code.visualstudio.com/download)

### Suscripción de Azure

- [Prueba gratuita](https://azure.microsoft.com/es-mx/free/search/?&ef_id=EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE:G:s&OCID=AID2100073_SEM_EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE:G:s&gclid=EAIaIQobChMIoo38pqXc8AIVgozICh2Elw7lEAAYASAAEgL7aPD_BwE)

### Python

#### Paquetes

- requests
- pandas

## Pasos

### Pasos para usar Text Analytics desde consola

1. Crear el recurso de Text Analytics dentro del portal de Azure.

2. Copiar clave de acceso.

3. Abrir el siguiente [enlace](https://westus.dev.cognitive.microsoft.com/docs/services?pattern=text) (las llamadas a la API deberán coincidir con la ubicación del recurso creado).

4. Probar las diferentes características.

5. Seleccionar la ubicación correspondiente.

6. Pegar clave de acceso en el campo Ocp-Apim-Subscription-Key.

### Pasos para usar Text Analytics desde Python

1. Clone the repo

```sh
git clone https://github.com/OscarSantos98/Intro-To-Az-TextAnalytics.git
```

2. Abrir el archivo main.py dentro del folder py.

3. Verificar que se tengan todos los paquetes instalados correctamente.

4. Añadir endpoint y api_keys (de preferencia añadir variables de entorno y reiniciar la computadora).

5. Ejecutar código.

### Pasos para usar datos en Microsoft Excel y Microsoft Power BI

1. Abrir Microsoft Excel.

2. Desde la cinta de opciones Datos en el grupo Obtener y transformar datos, importar datos de Texto/CSV y cambiar origen a UTF-8.

3. Abrir Microsoft Power BI.

4. Añadir origen de datos con csv y cambiar origen a UTF-8.

5. Instalar Word Cloud desde el menú de visualizaciones y añadir la columna de sentiments con este tipo de gráfico.