# Razonko — Portfolio orientado a entrevistas

Estado: prototipo en rama aislada `feat/razonko-recruiter-ready`. Referencia: 12 de noviembre de 2026.

## Motivo

Una revisión del portfolio de [Paula Reixach](https://paulareixach.github.io/) y su [publicación en LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7526575047990476800/) mostró una práctica útil: explicar la especialidad y el trabajo real, con fichas individuales, en vez de depender de una landing visual.

La identidad de Razonko se conserva; no se traslada el estilo visual de la referencia.

## Decisiones aplicadas

- Partir del commit `4f5b937` del rediseño previamente aprobado, **anterior a la iteración de diagramas rechazada**.
- Mantener portada Red Impact, navegación, tipografía y fotografía editorial que ya gustaban.
- Sustituir las ilustraciones decorativas de los dos casos profesionales por texto estructurado y enlaces a páginas de detalle. No se añaden diagramas especulativos.
- Incorporar cuatro fichas: formación B2B, coordinación de emergencias, PlantOps y LedgerFlow.
- Presentar el problema, responsabilidades concretas, decisiones de ingeniería y evidencia posible, con transparencia cuando el código es privado.
- PlantOps: fuente pública verificada en [GitHub](https://github.com/andresvalencia72/plantops); proyecto **en desarrollo**, no una demo acabada.
- LedgerFlow: repositorio privado y trabajo en desarrollo; no anunciar una demo o código público inexistente.
- Ninguna cifra de rendimiento, testimonios de cliente ni capturas ficticias. La experiencia laboral declarada permanece cercana a dos años, sin inflar periodos.

## Lo que NO se ha publicado

- Un PDF de CV existente en Descargas. Encontrar un archivo no implica permiso para exponerlo públicamente.
- Datos de clientes, capturas internas, código privado o información sensible.
- Una demo de PlantOps o LedgerFlow sin verificar su estado real.
- Cambios sobre `main`, `gh-pages` o `razonko.com`; no hay fusión ni despliegue permanente.

## Pruebas

```sh
python3 tests/smoke.py
python3 -m http.server 8766
```

Comprobación navegador con Chromium/Playwright en 1440, 1024, 390 y 320 px: rutas, menú responsive, `h1`, enlaces hacia las fichas, imágenes, hojas de estilo y ausencia de desbordamiento horizontal.

## Pendiente para una candidatura competitiva

1. Validar públicamente el CV definitivo y autorizar expresamente si debe descargarse desde la web.
2. Revisar fechas laborales y tecnologías con el CV aprobado y LinkedIn; evitar mostrar periodos contradictorios.
3. Revisar `README.md` y estado visible de `main` en PlantOps antes de promocionar el repositorio a reclutadores, porque hay PRs todavía sin fusionar.
4. Generar capturas **reales** de la aplicación PlantOps cuando existan flujos demostrables; no sustituirlas por UI inventada.
5. Evaluar en entrevistas si las fichas permiten explicar cada decisión técnica sin recurrir a métricas privadas.
6. Tras la aprobación visual, revisar accesibilidad y rendimiento con auditoría especializada y publicar mediante PR, no con un push directo sobre la rama desplegada.

## Recomendación sobre LinkedIn

La futura publicación de lanzamiento debería explicar por qué el portfolio representa mejor las responsabilidades reales, con un ejemplo verificable y un enlace. No presentar el trabajo como un lanzamiento de producto terminado.

