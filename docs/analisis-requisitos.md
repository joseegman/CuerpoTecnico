# Análisis de Requisitos — Cuerpo Técnico de Selección Olímpica (Judo y Artes Marciales)

> Documento vivo. Generado al inicio del proyecto para fundamentar el diseño de agentes del Cuerpo Técnico.
> Última revisión: 2026-09-09.

## 1. Contexto y objetivo

Construir desde cero un **Cuerpo Técnico de agentes** que dé soporte integral a una selección olímpica
de Judo (y, por extensión, de artes marciales), replicando la estructura real de los programas de alto
rendimiento (véase §3). Los agentes:

- Actúan **solo en su dominio** y no pueden modificar el dominio de los demás.
- **Delegan entre sí** según expertise (el Entrenador principal coordina).
- Generan **formularios y encuestas** para conocer el tono, la forma y las condiciones de cada deportista.
- Trabajan sobre una **carpeta de temporada en curso**, que contiene **varios equipos**, y dentro de
  cada equipo los documentos y subcarpetas que cada dominio necesite.
- Cuentan con un agente **documentador** que organiza y genera los formularios que piden los demás,
  usando las herramientas del harness que los aloja (opencode, Claude, ChatGPT, Hermes, AnythingLLM o
  una colección de MCPs).

## 2. Alcance y supuestos

- **Harness objetivo:** opencode (entorno donde se materializa este proyecto). El diseño es portable a
  otros harnesses (véase §12).
- **Idioma de trabajo:** español (cuerpo técnico hispanohablante).
- **Deportes:** Judo como disciplina principal; el diseño es extensible a otras artes marciales
  (taekwondo, karate, etc.) añadiendo equipos o dominios.
- **Datos de deportistas:** los agentes no sustituyen el juicio clínico/profesional humano; son
  asistentes que estructuran información. Las decisiones médicas y psicológicas críticas requieren
  revisión humana.
- **Almacenamiento:** sistema de archivos en el repositorio (markdown estructurado), no base de datos.
  Elegido por simplicidad, auditabilidad y portabilidad entre harnesses.

## 3. Fuentes y fundamentos (actualizadas)

Estructura de cuerpo técnico real y evidencia de preparación física en judo de élite:

| Fuente | Aporte al diseño |
|---|---|
| Weldon et al. (2024). *Strength and Conditioning (S&C) Practices of Judo Athletes and S&C Coaches*. J Strength Cond Res 38(4). https://pubmed.ncbi.nlm.nih.gov/38513184/ | El S&C se considera crítico para randori, velocidad/potencia y reducción de lesiones. Justifica el rol de **preparador físico** y la batería de tests. |
| Kons et al. (2024). *Strength and conditioning practices of judo coaches*. Int J Sports Sci Coach 19(2). https://journals.sagepub.com/doi/abs/10.1177/17479541231206910 | Ejercicios más prescritos: sentadillas/variantes (fuerza), derivados de halterofilia (potencia), movimientos específicos de judo (agilidad), estiramientos/movilidad (prevención). |
| Ouergui et al. (2022). *Effects of intensified training and tapering periods... judo-specific physical test performances*. Biol Sport. https://pubmed.ncbi.nlm.nih.gov/36247945/ | Tests específicos: SJFT, JPFT, CMJ, chin-ups con judogi, UST; HIIT específico (kumi-kata, uchi-komi) como modalidad de acondicionamiento. |
| Wang et al. (2023), citado en arXiv 2505.20859 (2025), sobre taper | Taper efectivo: ≤ 21 días, reducción de volumen 41–60 % sin bajar intensidad ni frecuencia. Base para los protocolos del entrenador principal y preparador. |
| Franchini et al. (2019). *HIIT on Olympic combat sports athletes*. J Strength Cond Res 33(1) | HIIT específico de combate como estrategia de acondicionamiento. |
| British Judo WCPP Coaching Team (2022–2026). https://www.britishjudo.org.uk/british-judo-wcpp-coaching-team | Organigrama real: head coach por programa, performance analyst técnico, equipo médico, fisioterapia, desarrollo. Valida los roles elegidos. |
| Judo Canada Staff / Integrated Support Team (2024–2026). https://judocanada.org/staff | Estructura: HP Director/Head Coach, preparador físico, therapist/medical lead IST. Valida división de dominios y el canal médico/psico como «integrated support». |
| Documentación oficial opencode (2026). https://opencode.ai/docs/agents/ , https://opencode.ai/docs/permissions/ | Mecanismo de agentes, permisos granulares por agente, patrones last-match-wins, permisos de tarea para delegación. |

### 3.1 Revisión con documentación federativa española y gallega

Fuentes federativas consultadas:

| Fuente | Aporte |
|---|---|
| RFEJYDA — Portal de transparencia y organización. https://www.rfejudo.com/portal-de-transparencia-indice | Estructura federativa nacional: Junta Directiva, Comisión Delegada, departamentos (Actividades Deportivas, Escuela Federativa, Colegio Nacional de Árbitros). Valida el modelo de roles por dominio. |
| RFEJYDA — Normativas. https://www.rfejudo.com/documentos-normativas | Normativa de Equipos Nacionales, Actividades Nacionales, competición internacional y protocolo de prevención en el deporte. |
| RFEJYDA — Normativa Categoría Junior 2026 (criterios de participación del equipo nacional). https://www.rfejudo.com/documentos/normativas/nacionales/ | Existen criterios oficiales de selección/convocatoria por categoría que el sistema debe poder reflejar. |
| RFEJYDA — Rankings Nacionales y Calendario. https://www.rfejudo.com/rankings-nacionales | Competiciones nacionales por fases (Fase Sector → final), Copas/Super Copas de España, ranking nacional por categorías, kata, edad escolar, concentraciones/stages. |
| Convenio Xunta de Galicia (Secretaría Xeral para o Deporte) — Federación Gallega de Judo (2014-2016 + adenda) | Programas reales: «Tecnificación e Rendemento», «Grupo Especial de Alto Rendimiento» y «Actividad deportiva en edad escolar»; personal técnico deportivo (director técnico, entrenadores y profesionales de apoyo). Valida el organigrama del Cuerpo Técnico. |
| Convenio Xunta — RFEJYDA, Centro Gallego de Tecnificación Deportiva (CGTD) | Modelo de concentraciones y seguimiento de deportistas de categorías inferiores tutelado por la federación nacional. |
| Decreto 165/2020 (Xunta de Galicia) | Categorías de deportista (alto nivel, alto rendimiento, rendimiento de base), requisito de licencia federativa gallega y beneficios académicos. |

**Hallazgos y decisiones derivadas**

1. **Categorías y edades:** la competición federativa usa alevín, infantil, cadete, junior y senior (más
   edad escolar). Las fichas de equipo y deportista modelan **categoría de edad + categoría de peso**,
   no solo peso. → Aplicado en la ficha de equipo.
2. **Selección y convocatorias:** existen normativas oficiales de criterios de participación por categoría.
   El entrenador-principal mantiene el **calendario de convocatorias** (plazos, criterios, convocados).
   → Nuevo `calendario/convocatorias.md`.
3. **Concentraciones y stages:** el calendario distingue **competición / concentración / stage**
   (modelo CGTD y training camps RFEJYDA). → Campo `tipo` en `competiciones.md`.
4. **Kata:** el kata es modalidad de competición oficial (Campeonatos de España de Kata, IJF Kata World
   Series). → Responsabilidad del entrenador-tecnica.
5. **Ranking nacional:** además del ranking IJF, el analista sigue el **Ranking Nacional RFEJYDA** por
   categoría como soporte de selección.
6. **Entornos seguros y prevención:** la RFEJYDA tiene protocolo de prevención en el deporte y líneas de
   igualdad y prevención de violencia de género; la Federación Gallega colabora en prevención del acoso
   (A-Judo). → Responsabilidad añadida a psicólogo y médico.
7. **Antidopaje:** el programa antidopaje de la RFEJYDA coincide con la responsabilidad ya asignada al
   médico (WADA). Sin cambios.
8. **Base/tecnificación (edad escolar):** el modelo gallego articula base y alto rendimiento. La selección
   olímpica es el nivel superior; se documenta la vía de escalado (nuevo equipo por disciplina/categoría)
   sin crear un agente de base por ahora.

## 4. Roles y organigrama del Cuerpo Técnico

| Agente | Modo | Dominio de escritura (exclusivo) | Función principal |
|---|---|---|---|
| **entrenador-principal** | primary (coordinador) | `planificacion/`, `calendario/`, `compartido/` | Coordina al staff, planifica y calendariza la temporada según objetivos y competiciones, decide cuándo pedir información de los deportistas y delega. |
| **entrenador-tecnica** | subagent | `tecnica/` | Técnica y táctica de judo (uchikomi, nage-komi, randori, kumi-kata, ne-waza), progresiones y correcciones. |
| **preparador-fisico** | subagent | `preparacion-fisica/` | Fuerza, potencia, acondicionamiento específico (HIIT kumi-kata/uchi-komi), tests (SJFT, JPFT, CMJ, judogi chin-ups), monitoreo de carga (RPE, Hooper, TQR). |
| **entrenador-estiramientos** | subagent | `estiramientos/` | Flexibilidad y movilidad específicas, estiramiento dinámico/pre-post, prevención, trabajo con fisio y preparador. |
| **psicologo-deportivo** | subagent | `psicologia/` (**privado**) | Preparación mental, ansiedad/activación, rutinas pre-competición, cohesión, psicometría, apoyo en gestión de peso. |
| **medico-deportivo** | subagent | `medicina/` (**privado**) | Reconocimientos, aptitud médica, gestión de lesiones (con fisio), corte de peso seguro, antidopaje/WADA, salud general. |
| **fisioterapeuta** | subagent | `fisioterapia/` | Rehabilitación, criterios objetivos de vuelta al tatami, vendajes, prevención. |
| **nutricionista** | subagent | `nutricion/` | Planes nutricionales, gestión de peso/categorías, hidratación, suplementación (listas WADA), recuperación. |
| **analista-rendimiento** | subagent | `rendimiento/` | Datos de competición y ranking IJF, análisis de combates propios y de rivales (scouting), informes para técnica y preparación. |
| **documentador** | subagent | `formularios/`, `encuestas/`, índices y READMEs de temporada | Genera y organiza formularios/encuestas que solicitan los demás agentes; mantiene la estructura de la temporada; usa las herramientas del harness (MCPs, plugins, web). |

## 5. Requisitos funcionales

**RF-01** — El Entrenador principal debe poder crear el plan de temporada (macro → meso → microciclos) a partir de los objetivos que le envíe el usuario y del calendario de competiciones facilitado.

**RF-02** — El Entrenador principal debe calendarizar los entrenamientos en base a la temporada y a las competiciones (fechas de pico, taper).

**RF-03** — El Entrenador principal decide cuándo es necesario recoger información de los deportistas y lo canaliza como solicitud de formulario/encuesta.

**RF-04** — Cualquier agente del staff puede solicitar un formulario/encuesta; solo el **documentador** genera y despliega los formularios.

**RF-05** — Los agentes pueden delegar tareas entre sí (vía tool `task`), cada uno en su expertise.

**RF-06** — Cada agente solo escribe en su dominio (y en `compartido/`); no puede modificar dominios ajenos (enforced por permisos del harness, no solo por prompt).

**RF-07** — Los datos clínicos (médico) y psicológicos son de acceso restringido (solo su agente propietario). La información sale de esos dominios como resúmenes anonimizados publicados en `compartido/`.

**RF-08** — El documentador mantiene la estructura de la temporada (índices, READMEs) y un registro de formularios.

**RF-09** — Los agentes trabajan sobre una carpeta de temporada (`temporadas/<año>/`) que puede contener varios equipos; cada equipo contiene sus subcarpetas de dominio.

**RF-10** — El sistema debe permitir crear nuevas temporadas y nuevos equipos sin cambiar la configuración de agentes.

**RF-11** — El documentador debe usar los plugins/MCPs disponibles en el harness para optimizar la generación de formularios (p. ej. Google Forms, Notion) y caer a markdown autocontenido si no hay herramientas especializadas.

**RF-12** — Los agentes crean en su dominio las subcarpetas y documentos que necesiten; el usuario **no
sube documentos** a las carpetas: usa los formularios/documentos generados, los rellena/edita y los deja
en las mismas carpetas.

**RF-13** — Los formularios y encuestas son **nominales** (por competidor, equipo, torneo o temporada) y
**nunca se sobrescriben**: las versiones nuevas usan sufijo numérico (`-v2`, `-v3`, ...). El usuario es
el único responsable de eliminar documentos.

## 6. Requisitos no funcionales

- **RNF-01 (Aislamiento de dominio):** la contención se garantiza por permisos del harness (edición), no solo por instrucciones del prompt.
- **RNF-02 (Privacidad/RGPD):** datos médicos y psicológicos tratados como categoría especial; acceso mínimo y registro de publicación vía `compartido/`.
- **RNF-03 (Portabilidad):** prompts autocontenidos; los formularios son markdown con frontmatter, reutilizables en cualquier harness.
- **RNF-04 (Auditabilidad):** ficheros versionables en git, nombres con fecha ISO, estados explícitos en frontmatter.
- **RNF-05 (Coste/control):** límite de pasos (`steps`) por agente; sin loops infinitos; `bash` denegado al staff.
- **RNF-06 (Rendimiento):** estructura plana y predecible; los agentes leen solo lo necesario de su dominio.

## 7. Modelo de datos: estructura de carpetas

```
temporadas/
└── 2026/
    ├── README.md                  # Índice de la temporada (mantenido por documentador)
    ├── calendario/                # RF-02 — Entrenador principal
    │   └── competiciones.md       # Fechas, sedes, categorías, peso, prioridad
    ├── planificacion/             # RF-01 — Entrenador principal
    │   └── plan-temporada.md      # Macro/meso/microciclos, picos y tapers
    ├── formularios/               # Plantillas de formularios — Documentador
    │   └── <nombre-formulario>.md
    └── equipos/
        ├── README.md              # Lista de equipos de la temporada
        └── <equipo>/              # p. ej. seleccion-judo
            ├── README.md          # Ficha del equipo (categorías, deportistas)
            ├── compartido/        # Resúmenes y actas visibles a todo el staff
            ├── tecnica/
            ├── preparacion-fisica/
            ├── estiramientos/
            ├── psicologia/        # PRIVADO
            ├── medicina/          # PRIVADO
            ├── fisioterapia/
            ├── nutricion/
            ├── rendimiento/
            └── encuestas/         # Instancias y respuestas — Documentador
                └── <dominio>/<formulario-id>/<equipo>/<deportista>.md
```

**Convenciones de ficheros**

- Nombres: `YYYY-MM-DD-<slug>.md` para registros con fecha; slugs descriptivos.
- Frontmatter mínimo: `equipo`, `deportista` (si aplica), `dominio`, `estado` (`borrador|activo|archivado`), `autor` (agente), `fecha`.
- Fichas de deportista dentro de cada dominio: `<dominio>/fichas/<apellido>-<nombre>.md`.
- **Carpetas y documentos creados por los agentes:** cada agente crea en su dominio las subcarpetas y
  documentos que precisen; el usuario no sube documentos a las carpetas.
- **Formularios nominales:** un fichero por competidor, o por equipo/torneo/temporada, según lo que se mida.
- **Versionado:** nunca sobrescribir documentos previos; si se rehace algo, versión nueva (`-v2`, `-v3`, ...).
- **Borrado:** responsabilidad exclusiva del usuario; los agentes no eliminan archivos.

## 8. Modelo de aislamiento de dominios

Se aplica en `permission` de cada agente (opencode). Regla: última regla que casa gana; `"*": deny`
primero y excepciones `allow` después.

| Área | Quién puede escribir | Quién puede leer |
|---|---|---|
| `planificacion/`, `calendario/` | Entrenador principal | Todo el staff |
| `compartido/**` (por equipo) | Todo el staff | Todo el staff |
| `<dominio>/**` (técnica, preparación, estiramientos, fisioterapia, nutrición, rendimiento) | Agente propietario | Todo el staff |
| `psicologia/**` | Psicólogo | Solo psicólogo |
| `medicina/**` | Médico | Solo médico |
| `formularios/**`, `encuestas/**`, READMEs de temporada | Documentador | Todo el staff (salvo psicología/medicina) |

La **privacidad** se implementa con patrones de denegación de lectura del tipo
`temporadas/**/medicina/**` y `temporadas/**/psicologia/**` para cualquier agente que no sea el
propietario. La escritura se implementa con allowlists de rutas por agente.

## 9. Flujo de trabajo operativo

1. El usuario envía **objetivos** y **calendario de competiciones** al Entrenador principal.
2. El Entrenador principal elabora el plan y calendario (RF-01/02) y **decide qué información necesita**.
3. Solicita al **documentador** los formularios/encuestas necesarios (RF-03/04).
4. El documentador genera, despliega y organiza las encuestas; recoge/archiva respuestas.
5. Cada agente de dominio interpreta las respuestas de su dominio y publica un **resumen** en `compartido/`.
6. El Entrenador principal consolida y ajusta el plan; delega tareas específicas (RF-05).

## 10. Ciclo de vida de un formulario/encuesta

`Solicitud` → `Borrador` → `Validación` → `Instancia (despliegue por equipo)` → `Respuestas`
→ `Análisis (agente de dominio)` → `Resumen en compartido/` → `Archivo`.

- **Solicitud:** el agente de dominio pide el formulario (qué quiere medir, a quién, cuándo).
- **Generación:** solo el documentador. Usa plantillas de `formularios/` y herramientas del harness.
- **Despliegue:** instancia por equipo en `encuestas/<dominio>/<formulario-id>/<equipo>/`.
- **Respuestas (nominales):** fichero por deportista (o por equipo/torneo/temporada); las rellena el
  usuario y las deja en la misma carpeta. Nunca se sobrescriben (versión `-v2`, `-v3`, ...).
- **Análisis:** el agente propietario del dominio lee las respuestas (las encuestas de psicología/
  medicina son privadas) y sintetiza.
- **Publicación:** resumen anonimizado en `compartido/`.

## 11. Privacidad y protección de datos (RGPD)

- Datos de salud (`medicina/`) y psicológicos (`psicologia/`) = categorías especiales (art. 9 RGPD).
- Solo el propietario del dominio los lee; el resto del staff recibe resúmenes.
- Los formularios solicitan solo datos mínimos necesarios.
- Los agentes no publican información clínica bruta en `compartido/`.
- El repositorio puede alojar datos personales: el usuario debe decidir el control de versiones y
  acceso (privado) de las carpetas de temporada.

## 12. Portabilidad entre harnesses

| Harness | Mecanismo equivalente |
|---|---|
| **opencode** (actual) | `.opencode/agents/*.md` + `permission` + `task` |
| **Claude Desktop** | Proyecto por temporada + instrucciones personalizadas + tarjetas de rol (`claude-desktop/`); MCP para Gmail/Drive/M365. Aislamiento por convención, no por permisos |
| Claude Code | `.claude/agents/*.md` (frontmatter: name/description/tools) — sin permisos por ruta; usar prompts y herramientas restringidas |
| ChatGPT (GPTs) | Instrucciones del GPT + acciones (OpenAPI); misma estructura de carpetas como «knowledge» |
| **AnythingLLM** | Workspace por temporada con RAG (`anythingllm/`) + Custom Agent con prompt maestro (cambio de rol) o un agente por rol; MCP compatible (Gmail/Drive/M365); aislamiento por convención o por workspaces restringidos en Docker multiusuario |
| Hermes / otros | Agentes personalizados con system prompt; herramientas limitadas |
| MCPs | El documentador puede invocar MCPs de formularios/docs si el harness los expone (p. ej. Google Forms, Notion); el prompt ya lo contempla |

## 13. Decisiones de diseño y alternativas descartadas

- **Datos en sistema de archivos vs BD:** elegido FS+markdown por auditabilidad, git y portabilidad;
  descartada BD para no acoplar el harness.
- **Aislamiento por permisos vs solo prompt:** elegido permisos del harness (defensa en profundidad);
  el prompt refuerza la norma, no la sustituye.
- **Un único agente documentador centralizado vs cada agente con sus plantillas:** centralizado para
  evitar colisiones de nombres y mantener un único canon de formularios.
- **Carpetas privadas dentro de cada equipo vs un buzón central:** elegido dentro del equipo para
  mantener el dato cerca del contexto del equipo; los resúmenes viajan por `compartido/`.

## 14. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Un agente escribe fuera de su dominio | Permisos de edición por ruta (harness), revisables en git |
| Fuga de datos médicos/psicológicos | Denegación de lectura por ruta + resúmenes anonimizados |
| Loops / consumo excesivo | `steps` por agente; `bash` denegado; prompts que ordenan detenerse y devolver control |
| Formularios inconsistentes | Plantillas canónicas del documentador + skill `ciclo-formulario` |
| Modelos sin experiencia en judo | Prompts con conocimiento de dominio y baterías de tests específicas; posibilidad de asignar modelos distintos por agente |
| Dependencia de MCPs que no existen | El documentador degrada a markdown autocontenido si el harness no ofrece herramientas |

## 15. Roadmap sugerido

1. **(Actual)** Esqueleto del Cuerpo Técnico + estructura de temporada + primer formulario de ejemplo.
2. Importador de calendario de competiciones (IJF + Ranking Nacional RFEJYDA) y de criterios de
   convocatoria por el analista de rendimiento.
3. Plantillas de encuestas validadas por dominio (técnica, S&C, estiramientos, psico, médico, nutrición).
4. Integración opcional con MCP de formularios (Google Forms/Notion) para despliegue externo.
5. Pipelines de datos (ranking IJF, resultados) en `rendimiento/` con scripts opcionales.