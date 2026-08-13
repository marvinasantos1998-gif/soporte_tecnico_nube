# Servicio de Soporte Técnico en la Nube

**Institución:** Universidad Tecnológica de Honduras
**Proyecto:** Aplicación Web de Soporte Técnico en la Nube
**Integrantes:** Marvin Josué Santos Rivera (Equipo ##)

## Objetivo del Proyecto
Desarrollar una aplicación web funcional orientada al soporte técnico en la nube que permita a los usuarios reportar incidencias. La aplicación valida los datos ingresados y, mediante automatización, envía un correo electrónico al administrador con los detalles, eliminando la necesidad de persistir información en bases de datos locales o externas.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Framework Web:** Streamlit
* **Librerías Estándar:** `smtplib` (envío de correos), `email.message` (formato del correo), `re` (validación de expresiones regulares).
* **Despliegue:** Streamlit Community Cloud

## Funcionamiento de la Aplicación
1. **Acceso:** El usuario ingresa a la aplicación mediante su navegador.
2. **Formulario:** Completa sus datos (Nombre, Correo, Tipo de problema, Prioridad, Descripción).
3. **Validación:** El sistema evalúa en tiempo real que no haya campos vacíos y que el formato del correo sea válido.
4. **Envío:** Si los datos son correctos, el sistema compila un reporte y lo envía vía SMTP al administrador.
5. **Confirmación:** Se le muestra al usuario una notificación de éxito en la pantalla.

## Gestión Segura de Credenciales (Secrets)
Para cumplir con las normas de seguridad informática, las contraseñas **no** están escritas en el código fuente. Se han utilizado los **Secrets de Streamlit**:
* **Desarrollo Local:** Se configuró un archivo `.streamlit/secrets.toml` (excluido de GitHub vía `.gitignore`) con las variables `EMAIL_USER`, `EMAIL_PASS` y `ADMIN_EMAIL`. Para usar Gmail, se generó una "Contraseña de Aplicación" para evadir el bloqueo de 2FA.
* **Despliegue en la Nube:** Las variables se ingresaron en el panel de control del proyecto dentro de *Streamlit Community Cloud* en la sección *App settings > Secrets*.

## Procedimiento de Ejecución
Para ejecutar este proyecto de forma local:
1. Clonar el repositorio.
2. Crear un entorno virtual e instalar las dependencias: `pip install -r requirements.txt`.
3. Crear un archivo `secrets.toml` dentro de una carpeta oculta `.streamlit` y colocar las credenciales.
4. Ejecutar la aplicación con el comando: `streamlit run app.py`.
