# Razonko: revisión editorial con Unslop

Fecha de referencia: 12 de noviembre de 2026. Rama: `feat/razonko-unslop-redesign`.

## Alcance y seguridad

- Parte de `gh-pages` (el sitio real), no de la antigua rama `main`.
- La web publicada y las ramas originales no se han modificado.
- `styles.css` se conserva. `refine.css` aplica el refinamiento de forma aislada.
- Se mantiene HTML/CSS sin JavaScript, backend, dependencias de compilación ni analíticas.
- Imagen de portada: Fotis Fotopoulos, [Unsplash](https://unsplash.com/photos/6sAl6aQ4OWI), usada como fotografía editorial ilustrativa, **no** como captura del equipo ni del producto.
- El enfoque de revisión sigue [Unslop](https://github.com/heydamir/unslop), creado por Damir Sokolovsky (CC BY 4.0).

## Dirección visual aprobada

- Producto: portfolio profesional de Andrés Valencia y espacio editorial tecnológico Razonko.
- Carácter: directo, técnico, cercano.
- Mundo: trabajo real en ingeniería web, documentación y decisiones arquitectónicas.
- Momentos: portada de alto contraste; diagramas de experiencia real.
- Firma: logo Razonko, acento rojo y numeración editorial.

## Qué cambió

1. Hero con rol explícito, casos profesionales más visibles y dos acciones claras.
2. Banda de contexto: experiencia, especialidad, producción y actividad divulgativa.
3. Casos profesionales conservados sin revelar código privado; etiqueta backend geoespacial corregida a NestJS.
4. PlantOps enlazado como desarrollo con repositorio público. LedgerFlow indicado como desarrollo privado; ninguna demo simulada.
5. Navegación unificada con menú móvil nativo `details` y controles táctiles amplios.
6. Mayor proporción de información visible en las subpáginas, con menor peso de encabezados gigantes.
7. Ajustes de ritmo, contraste de textos pequeños y densidad. Se conserva la identidad Red Impact.
8. Contenido ordenado como experiencia → proyectos → forma de trabajar → Razonko editorial → sobre mí → contacto.

## Verificación

```sh
python3 tests/smoke.py
python3 -m http.server 8765
```

Se realizó también comprobación con Chromium/Playwright en 1440, 768, 390 y 320 píxeles: las 12 rutas respondieron 200, no se observaron imágenes rotas ni scroll horizontal, y se verificó la apertura y navegación del menú móvil. La URL temporal de prueba se sirve desde una copia pública separada del repositorio para no exponer `.git`.

## Pendiente deliberadamente

- No enlazar un CV PDF inexistente: `/cv.pdf` sigue dando 404 hasta que se aporte un PDF aprobado.
- No prometer resultados o métricas confidenciales de proyectos de clientes.
- Sustituir ilustraciones y fotografía editorial por demostraciones reales **solo** cuando puedan publicarse.
- Revisar la exactitud histórica de tecnologías y fechas con evidencias antes de cambiar más campos.
- Revisar visualmente antes de cualquier fusión o despliegue.

