# Leer Texto de PDF con Python

## Conceptos básicos de OCR y Tesseract

### ¿Qué es OCR?

**OCR** proviene del inglés **O***ptical **C**haracter **R**ecognition.
Es una técnica para detectar texto de una imagen. Esto es parte del procesamiento
de imágenes en ciencias de la computación.

El concepto clave es traducir un texto escrito a mano o de manera mecánica desde
una imagen a una cadena de texto. 

Imagen -> Texto

## ¿Qué flujo de trabajo se podría tener?

Las imágenes podrían provenir de diferentes fuentes, por ejemplo:
- Documentos escaneados
- Archivos PDF generados en distintos softwares
- Imágenes tomadas con el móvil u otros dispositivos

Posteriormente se entregaría esto a un software OCR como el ejemplo de el presente
repositorio y este entregaría el texto listo para su persistencia. 

Dependerá del motivo para extraer el texto, el tipo de persistencia, por lo general
será una base de datos de la cual se podrá recuperar la información en el futuro.

![OCR_flow!](readme_files/OCR_flow.jpeg "OCR_flow")

## Nuestro Stack de tecnologías

Para el presente ejemplo ocuparemos:
- python 3.9+ (lenguaje de programación)
- tesseract OCR (Motor de OCR)
- PyPDF2 (Librería para extraer metadatos de un PDF)

## Alcance del ejemplo
Se cubrirán dos casos de uso:
- Obtener la metadata y texto de un archivo PDF
- Obtener lo antes mencionado de muchos PDF dentro de un directorio

## Estructura del ejemplo
Con la finalidad de mantener este ejemplo como una posible semilla para
futuros proyectos, he decidido estructurarlo bajo la siguiente arquitectura:

```
    /src
        | - domain /
        | - use_cases /
        | - infrastructure /
            | - mappers /
            | - persistence /
    /smart_bin
    main.py
```
### domain
Dentro de esta carpeta tendremos los archivos de código que se encarguen
del procesamiento de reglas de negocio específicas del problema que estemos
resolviendo. 
Para el presente ejemplo, tendremos una clase que va a representar un 
documento digitalizado listo para ser usado en nuestro software

### use_cases
Dentro de esta carpeta se encontrará el código que resuelve cada caso de uso.
Para el presente ejemplo son los dos descritos en el alcance.

### infrastructure
Dentro de esta carpeta se encontrará el código que usa librerías y tecnologías
por fuera de nuestro software y de los cuales no tendremos mucho control.

**mappers**
En esta carpeta tendremos las funciones o clases que permitan transformar nuestros
documentos digitales, ya sea desde un PDF a un DigiDoc como en sentido inverso o 
a su persistencia.

**persistence**
En esta carpeta crearemos los repository necesarios para guardar el estado de nuestros
Documentos Digitalizados (DigiDocs)

### smart_bin
Esta funcionará como carpeta que contiene los PDF de los cuales se va a obtener la información

### main.py
Es el punto de arranque(Entry Point) de todo y un ejemplo de como usar los casos de uso 

## ¿Cómo instalar el ejmplo?
1 - Hay que preparar un entorno de python 3.9 o superior, esto se puede hacer con Virtual Env
o instalando directamente la versión de python en el equipo.

2 - Abrir la terminal

3 - Dirigirse a la carpeta del proyecto

4 - Correr Virtual Env(en caso de usar este método)

5 - Ejecutar el comando: 
```
$ pip install -r requirements.txt
```

6 - Esperar a que se terminen de instalar todas las dependencias

7 - Ejecutar el entry point:
 ```
 $ python3 main.py 
 ```
[Conceptos clave referencias](https://nanonets.com/blog/ocr-with-tesseract/#:~:text=Pytesseract%20or%20Python%2Dtesseract%20is,image%20to%20text%20use%20cases.)
    
