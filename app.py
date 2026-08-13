import streamlit as st
import smtplib
from email.message import EmailMessage
import re

# Configuración de la página
st.set_page_config(page_title="Soporte Técnico en la Nube", page_icon="🛠️", layout="centered")

# Encabezado
st.title("🛠️ Sistema de Reporte de Soporte Técnico")
st.write("Por favor, complete el siguiente formulario para reportar su incidencia. Nuestro equipo lo revisará a la brevedad.")

# Función para validar el formato del correo
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, correo):
        return True
    return False

# Función para enviar el correo utilizando Streamlit Secrets
def enviar_correo(nombre, correo_usuario, tipo, prioridad, descripcion):
    try:
        # Credenciales seguras desde los Secrets de Streamlit
        remitente = st.secrets["EMAIL_USER"]
        password = st.secrets["EMAIL_PASS"]
        destinatario = st.secrets["ADMIN_EMAIL"] 

        # Preparar el mensaje
        msg = EmailMessage()
        msg['Subject'] = f"Nuevo Reporte de Soporte [{prioridad}] - {tipo}"
        msg['From'] = remitente
        msg['To'] = destinatario

        contenido = f"""
        Se ha recibido un nuevo reporte de soporte técnico.

        DATOS DEL USUARIO:
        -------------------
        Nombre: {nombre}
        Correo: {correo_usuario}

        DETALLES DE LA INCIDENCIA:
        ---------------------------
        Tipo de Problema: {tipo}
        Prioridad: {prioridad}
        
        Descripción:
        {descripcion}
        """
        msg.set_content(contenido)

        # Conexión al servidor SMTP (Ejemplo con Gmail)
        # Si usas otro proveedor (Outlook, Yahoo), cambia el host y el puerto.
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error interno al enviar el correo. Verifique la configuración. Detalles: {e}")
        return False

# Contenedor del Formulario
with st.form("formulario_soporte", clear_on_submit=False):
    st.subheader("Datos del Reporte")
    
    nombre = st.text_input("Nombre del usuario *")
    correo = st.text_input("Correo electrónico *")
    tipo_problema = st.selectbox("Tipo de problema *", ["", "Hardware", "Software", "Redes", "Cuentas/Accesos", "Otro"])
    prioridad = st.selectbox("Nivel de prioridad *", ["", "Baja", "Media", "Alta", "Crítica"])
    descripcion = st.text_area("Descripción detallada del problema *")
    
    submit_btn = st.form_submit_button("Enviar reporte")

# Lógica de Validación y Envío al presionar el botón
if submit_btn:
    # 1. Validar campos obligatorios
    if not nombre or not correo or tipo_problema == "" or prioridad == "" or not descripcion:
        st.warning("⚠️ Por favor, complete todos los campos obligatorios.")
    # 2. Validar formato de correo
    elif not validar_correo(correo):
        st.warning("⚠️ Por favor, ingrese un formato de correo electrónico válido.")
    # 3. Procesar si todo es correcto
    else:
        with st.spinner("Enviando reporte al administrador..."):
            exito = enviar_correo(nombre, correo, tipo_problema, prioridad, descripcion)
            if exito:
                st.success("¡Reporte enviado correctamente! Su reporte ha sido enviado al administrador.")
