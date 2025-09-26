# PySchool - Juego de Escape basado en Python

English README: [README-en.md](README-en.md)

PySchool es un juego de escape interactivo basado en la web construido con Python y Quarto. Los jugadores resuelven rompecabezas y desafíos escribiendo y ejecutando código Python directamente en su navegador.

[Demo](https://python-chile.github.io/escape-room-pyschool/)

## Características

- 🎮 Desafíos interactivos de codificación en Python
- 🌐 Se ejecuta completamente en el navegador utilizando Pyodide
- 🎨 Hermosa interfaz de estilo de boceto
- 🔍 Verificación de código en tiempo real
- 📱 Diseño receptivo para todos los dispositivos

## Empezando

### Diseño 

El diseño se basa en el [sketchy theme](https://bootswatch.com/sketchy/) de bootswatch, que depende de las fuentes de Google Neucha y Cabin+Sketch.

### Requisitos

- Python 3.x
- Quarto
- Make (opcional, para usar comandos de Makefile)

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sebastiandres/pyscape.git
   cd pyscape
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Entra a la carpeta principal:
   ```bash
   cd quarto/
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución Local

1. Renderiza el sitio de Quarto:
   ```bash
   make render
   ```
   O manualmente:
   ```bash
   cd quarto && quarto render .
   ```

> [!NOTE]
>
> Quarto se levanta con puerto aleatorio, para ocupar un puerto específico: `quarto preview --port [puerto]`.
> 
> Más detalle `quarto preview --help`.

2. Visualiza el sitio:
   ```bash
   make view
   ```
   O con localhost:
   ````bash
   cd quarto && quarto preview
   ````
   O abre `docs/index.html` en tu navegador.

## Estructura del Proyecto

- `quarto/` - Contiene los archivos principales del sitio de Quarto
- `docs/` - Archivos estáticos generados del sitio
- `verification.py` - Código Python para verificar soluciones
- `Makefile` - Comandos de automatización de construcción

## Contribuyendo

¡Las contribuciones son bienvenidas! Así es como puedes ayudar:

1. Haz un fork del repositorio
2. Crea una rama de características (`git checkout -b feature/AmazingFeature`)
3. Haz tus cambios (`git commit -m 'Agrega alguna AmazingFeature'`)
4. Haz push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Agregar Nuevos Rompecabezas

Para agregar un nuevo rompecabezas:

1. Crea un nuevo documento de Quarto en el directorio `quarto/`
2. Agrega la descripción de tu rompecabezas y el código de verificación en Python
3. Actualiza la navegación en `quarto/_quarto.yml`
4. Prueba tu rompecabezas localmente
5. Envía un pull request

## Detalles Técnicos

- Construido con [Quarto](https://quarto.org/)
- Utiliza [Pyodide](https://pyodide.org/) para la ejecución de Python en el navegador
- Tema personalizado basado en el tema de boceto
- Fuentes: Neucha y Cabin+Sketch

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- Gracias a los equipos de Quarto y Pyodide por sus increíbles herramientas
- Inspirado por la alegría de las salas de escape y la programación en Python