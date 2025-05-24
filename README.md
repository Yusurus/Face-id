
# 🔐 SecureAccess: Sistema de Autenticación Avanzado (Reconocimiento Facial)

**SecureAccess** es un sistema de autenticación dual que combina el clásico inicio de sesión por usuario y contraseña con un sistema moderno de reconocimiento facial. Está diseñado utilizando **Flask** en el backend y **HTML, CSS y JavaScript** en el frontend, con **DeepFace** como motor de reconocimiento facial.

---

## 🚀 Características

- 🔑 **Autenticación Tradicional**: Inicio de sesión con usuario y contraseña.
- 📸 **Reconocimiento Facial**: Verificación mediante cámara web comparando con rostros previamente registrados.
- 🧠 **Tecnología DeepFace**: Precisión mejorada gracias a modelos de aprendizaje profundo.
- 🎨 **Interfaz Intuitiva**: Diseño limpio, amigable y responsivo.
- 📂 **Base de Datos de Rostros Flexible**: Estructura de carpetas fácil de manejar.
- 💬 **Mensajes de Estado**: Retroalimentación clara al usuario.
- 📊 **Dashboard de Éxito**: Pantalla animada tras un login exitoso.

---

## 📁 Estructura del Proyecto

```
.
├── app.py                  # Lógica del backend Flask
├── index.html              # Página principal de inicio de sesión
├── dashboard.html          # Página tras login exitoso
├── script.js               # Funcionalidades del frontend
├── styles.css              # Estilos CSS personalizados
├── rostros_conocidos/      # Base de datos de imágenes faciales
│   ├── Perosna1/
│       ├── fotoCaraPersona.jpg
└── README.md               # Este archivo
```

---

## 🛠️ Requisitos Previos

Asegúrate de tener instalados:

- Python 3.x  
- pip (gestor de paquetes de Python)

---

## ⚙️ Instalación y Configuración

### 1. Clonar el Repositorio o Descargar Archivos

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <nombre_de_tu_carpeta>
```

### 2. Crear un Entorno Virtual (Recomendado)

```bash
python -m venv venv
```

### 3. Activar el Entorno Virtual

- **Windows**:

```bash
.\env\Scripts\activate
```

- **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Instalar Dependencias
esto dentro del directorio del progrma

```bash
pip install -r requirements.txt
```

> ⚠️ **Nota:** En la primera ejecución, DeepFace descargará modelos. Requiere conexión a internet.

### 5. Configurar la Base de Datos de Rostros

1. Crea la carpeta `rostros_conocidos` al nivel de `app.py`.
2. Dentro, crea una subcarpeta por persona (el nombre de la carpeta es el nombre del usuario).
3. Agrega varias imágenes claras del rostro de esa persona.

**Ejemplo**:

```
rostros_conocidos/
├── John_Doe/
│   ├── john_1.jpg
│   └── john_2.png
```

---

## 👤 Usuarios de Prueba

Dentro de `app.py` encontrarás este diccionario de prueba:

```python
USUARIOS_MOCK = {
    'admin': 'password123',
    'usuario': '12345',
    'test': 'test'
}
```

Puedes modificarlo para añadir o cambiar usuarios y contraseñas.

---

## ▶️ Ejecución del Programa

1. Asegúrate de activar el entorno virtual.
2. Ejecuta la aplicación:

```bash
python app.py
```

3. una vez ejecutado el archivo app.py este te lanzara una direcion por la terminal, con esta direcion tu podras acceder a la web

---

## 👨‍💻 Uso del Programa

### 🔐 Inicio de Sesión Tradicional

1. Ingresa usuario y contraseña válidos.
2. Haz clic en **Iniciar Sesión**.
3. Si las credenciales son correctas, accederás al dashboard.

### 🧠 Reconocimiento Facial

1. Haz clic en **Reconocimiento Facial**.
2. Permite el acceso a tu cámara.
3. Asegúrate de estar bien centrado e iluminado.
4. Haz clic en **Capturar y Verificar**.
5. Si tu rostro es reconocido, serás redirigido al dashboard.

---

## 🎨 Personalización

### 👥 Usuarios y Rostros

- Agrega nuevas carpetas a `rostros_conocidos/` con nuevas imágenes para cada usuario.

### 🖌️ Estilo

- Edita `styles.css` para cambiar colores, fuentes y diseño.

### 💻 Lógica del Frontend

- Modifica `script.js` para cambiar cómo se maneja la cámara, animaciones, etc.

### 🧠 Lógica del Backend

- Puedes ajustar el umbral de confianza de DeepFace.
- Agrega logs o mejora el manejo de errores.
- Integra una base de datos real para almacenamiento persistente.

---

## ⚠️ Posibles Problemas y Soluciones

### ❌ `404 Not Found` o `SyntaxError: Unexpected token '<'`

**Causa**: Estás abriendo `index.html` directamente sin ejecutar Flask.  
**Solución**: Ejecuta `python app.py` y accede desde `http://localhost:3000/`.

### 🚫 Permiso de cámara denegado

**Causa**: No diste permiso al navegador o hay problemas con el driver.  
**Solución**: Asegúrate de permitir el acceso y verifica la configuración del sistema.

### 🧠 Error al cargar modelos de DeepFace

**Causa**: Mala conexión o fallo en la descarga.  
**Solución**: Borra la carpeta de caché `~/.deepface/` y vuelve a ejecutar la app.

### 😕 Rostro no detectado

**Causa**: Mala iluminación, baja calidad de imagen o imágenes incorrectas.  
**Solución**: Usa imágenes nítidas y variadas. Mejora la iluminación.

---

## 📃 Licencia

Este proyecto es de uso educativo y libre para personalización. Para uso comercial, asegúrate de revisar las licencias de DeepFace y otras dependencias utilizadas.

---

## 🤝 Contribuciones

¿Tienes ideas para mejorar el proyecto? ¡Sientete libre de enviar un *pull request* o abrir un *issue*!

---

## 📌 Autor

Desarrollado con 💻 y ☕ por **Yusurus**  
📧 Contacto: **yjru_at@hotmail.com**
