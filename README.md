# Razonko — portfolio + espacio editorial estático

Primera versión extendida del sitio de Andrés Valencia, con identidad **Razonko**.
**Stack: HTML semántico + CSS. Sin React, Next.js, JavaScript, backend ni herramientas de compilación.**

## Ver en local

```bash
python3 -m http.server 8080
# abre http://localhost:8080
```

## Estructura

```text
index.html             Inicio / experiencia y proyectos
styles.css             Estilos globales y responsive
explorar/index.html    Índice editorial
blog/index.html        Blog
blog/por-que-razonko/  Primer artículo editorial
cursos/                Temarios de cursos
cursos/sistemas-digitales/
cursos/typescript/
rutas/                 Rutas de aprendizaje
rutas/fundamentos/
rutas/ingenieria/
youtube/               Canal y series
 diario/                Diario de proyectos (propuestas, no avances falsos)
assets/                Marca y hero
.nojekyll              Publicación GitHub Pages sin Jekyll
404.html               Página 404
```

## Añadir una entrada al blog (sin CMS)

1. Duplica `blog/por-que-razonko/index.html` en `blog/mi-nuevo-articulo/index.html`.
2. Actualiza título, metadatos, fecha, contenido e índice lateral.
3. Añade una tarjeta con enlace `./mi-nuevo-articulo/` a `blog/index.html`.
4. Comprueba enlaces, ortografía y móviles; publica los cambios con Git.

Un futuro migrado a React puede transformar estas páginas en componentes y usar Markdown/MDX con un generador estático. No hemos añadido un CMS ni un editor visual que no exista.

## GitHub Pages

Sube esta carpeta a un repositorio público. En GitHub, entra en **Settings → Pages → Build and deployment → Deploy from a branch**, y selecciona la rama de publicación y `/(root)`. El archivo `.nojekyll` hace que Pages sirva los archivos tal cual. Los enlaces son relativos y funcionan en dominios raíz y URLs de proyecto (`usuario.github.io/repositorio/`).

El dominio personalizado de Razonko requiere una decisión y configuración DNS posterior. No supongas que `razonko.com` está configurado ni agregues CNAME sin comprobarlo.

## Contenidos y transparencia

- Los casos profesionales son descritos de forma anónima, sin código de clientes.
- PlantOps, LedgerFlow y Shipyard siguen como propuestas **no aprobadas ni publicadas**.
- Los cursos y posibles playlists están etiquetados como **planificados** cuando no hay vídeos reales enlazables.
- El primer artículo editorial de bienvenida es el único artículo completo incluido en esta entrega.
- No hay cookies, formularios ni analíticas añadidas.

## Componentes futuros en React

`SiteHeader`, `SiteFooter`, `Hero`, `ExperienceCases`, `EditorialCard`, `ResourceCard`, `ArticleLayout`, `CurriculumSteps`, `CoursePage`, `LearningPathPage`.

## Verificar

Usa un servidor estático local (evita rutas `file://` con prefijos complejos), revisa anclas, enlaces internos, mobile y accesibilidad. No llames «publicado» a ninguna funcionalidad que solo exista como contenido planificado.
