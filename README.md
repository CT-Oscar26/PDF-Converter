## Generador de PDF dinámico con Python y Streamlit

En este proyecto desarrollé una aplicación en **Python** que permite crear archivos **PDF de forma dinámica**, brindando al usuario la posibilidad de construir documentos personalizados página por página. La aplicación facilita la creación de PDFs con títulos, contenido textual e imágenes, todo desde una interfaz web sencilla e intuitiva.

Para la parte visual y de interacción utilicé **Streamlit**, lo que permite mostrar formularios, campos de texto, selectores, botones y controles de manera rápida y eficiente. Gracias a esta librería, el usuario puede definir el título del documento, el número de páginas, el contenido de cada una y subir imágenes opcionales sin necesidad de conocimientos técnicos.

La generación del PDF se realiza con la librería **FPDF**, utilizando una clase personalizada (`PDF`) que hereda de `FPDF`. Esta clase se encarga de definir elementos comunes del documento, como el encabezado (*header*), el pie de página (*footer*) y los estilos de títulos y texto. De esta forma, se mantiene una estructura limpia y reutilizable para todo el documento.

El flujo principal de la aplicación se basa en una función que recibe los datos ingresados por el usuario (título del documento, contenido de cada página, fuente, tamaño de texto e imágenes) y genera automáticamente un PDF con múltiples páginas. Finalmente, el usuario puede **descargar el archivo generado directamente desde la aplicación**.

### Tecnologías utilizadas

- Python  
- Streamlit  
- FPDF  

### Lista de comandos para correr el programa

- pip install streamlit fpdf
- streamlit run (nombre programa)
  
