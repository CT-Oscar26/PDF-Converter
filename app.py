import streamlit as st
from fpdf import FPDF
import os


# ---------- CLASE PDF ----------
class PDF(FPDF):

    def header(self):
        # Se ejecuta automáticamente al crear cada página
        if hasattr(self, "document_title"):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, self.document_title, 0, 1, "C")
            self.ln(5)

    def footer(self):
        # Se ejecuta automáticamente al final de cada página
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def page_title(self, title, font="Arial", size=12):
        # Título de cada página
        self.set_font(font, "B", size)
        self.cell(0, 10, title, 0, 1)
        self.ln(5)

    def page_body(self, text, font="Arial", size=12):
        # Texto principal de la página
        self.set_font(font, "", size)
        self.multi_cell(0, 8, text)
        self.ln(5)


# ---------- FUNCIÓN QUE CREA EL PDF ----------
def create_pdf(filename, document_title, pages):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.document_title = document_title  # Usado por el header

    for title, text, font, size, image_path, image_size in pages:
        pdf.add_page()  # 👉 Cada iteración crea UNA página nueva

        if title.strip():
            pdf.page_title(title, font, size)

        if image_path:
            # Calcula el ancho de la imagen según el % elegido
            width = pdf.w * (image_size / 100)

            # Centra la imagen horizontalmente
            pdf.image(
                image_path,
                x=(pdf.w - width) / 2,
                w=width
            )
            pdf.ln(5)

        pdf.page_body(text, font, size)

    pdf.output(filename)


# ---------- STREAMLIT APP ----------
def main():
    st.title("Generador de PDF por páginas")

    document_title = st.text_input("Título del documento")

    st.header("Páginas del documento")

    pages = []
    page_count = st.number_input("Número de páginas", 1, 10, 1)

    for i in range(page_count):
        st.subheader(f"Página {i + 1}")

        title = st.text_input(f"Título página {i + 1}", key=f"title{i}")
        content = st.text_area(f"Contenido página {i + 1}", key=f"content{i}")

        uploaded_image = st.file_uploader(
            f"Imagen página {i + 1} (opcional)",
            type=["jpg", "png"],
            key=f"image{i}"
        )

        image_size = st.slider(
            f"Tamaño de imagen (%) página {i + 1}",
            20, 100, 50,
            key=f"img_size{i}"
        )

        font = st.selectbox(
            f"Fuente página {i + 1}",
            ["Arial", "Courier", "Times"],
            key=f"font{i}"
        )

        size = st.slider(
            f"Tamaño fuente página {i + 1}",
            8, 24, 12,
            key=f"size{i}"
        )

        image_path = None
        if uploaded_image:
            # Guarda la imagen temporalmente para que FPDF pueda usarla
            image_path = f"page_image_{i}_{uploaded_image.name}"
            with open(image_path, "wb") as f:
                f.write(uploaded_image.getbuffer())

        # Guardamos toda la info de la página en una tupla
        pages.append((title, content, font, size, image_path, image_size))

    # ---------- FORMULARIO FINAL ----------
    with st.form("form_pdf"):
        nombre_pdf = st.text_input("Nombre del PDF")
        generar = st.form_submit_button("Generar PDF")

    if generar:
        if not nombre_pdf:
            st.error("Ingrese un nombre para el PDF")
            return

        if not nombre_pdf.lower().endswith(".pdf"):
            nombre_pdf += ".pdf"

        create_pdf(nombre_pdf, document_title, pages)

        with open(nombre_pdf, "rb") as pdf_file:
            st.download_button(
                "Descargar PDF",
                pdf_file,
                file_name=nombre_pdf,
                mime="application/pdf"
            )

        st.success("PDF generado correctamente")

        # Evita archivos basura
        if os.path.exists(nombre_pdf):
            os.remove(nombre_pdf)


if __name__ == "__main__":
    main()
