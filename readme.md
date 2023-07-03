# Cloudflare scan!

> Herramienta para identificar si un sitio está protegido por Cloudflare.

Los mecanismos más comunes para saber si un sitio está protegido por Cloudflare son:

1. Buscar en los Headers que devuelve el sitio la palabra "cloudflare".
2. Buscar dentro de la información de  los DNS del sitio si existe cloudflare en alguna query.



-------

# ¿Cómo ejecutar el programa?

1. Abre una consola en la ruta donde se encuentra el archivo

2. Activa el entorno virtual ejecutando en consola 
	`````powershell
	.\venv\Scripts\activate
	`````
	
3. Para ejecutar la ayuda ejecute:

   ````powershell
   python .\nmapscan -h
   ````
   
4. Para ejecutar en modo header en consola ejecute una de las 2 formas: 
   ````powershell
   python .\nmapscan.py -t [URL_pagina/host]
   ````
   Por defecto esta configurado para escanear los puertos del 1 al 1000
   
      ````powershell
   python .\nmapscan.py -t [URL_pagina/host] -p [puertos]
      ````

5. El programa responde en consola si es que esta protegido o no
