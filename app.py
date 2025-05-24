from flask import Flask, render_template, request, jsonify
import cv2
import os
import base64
import numpy as np
from PIL import Image
import io
from deepface import DeepFace

app = Flask(__name__)

# Configuración
DIRECTORIO_ROSTROS = "rostros_conocidos"
USUARIOS_MOCK = {
    'admin': 'password123',
    'usuario': '12345',
    'test': 'test'
}

def verificar_base_datos_rostros():
    """Verifica que la base de datos de rostros existe"""
    if not os.path.isdir(DIRECTORIO_ROSTROS):
        print(f"Error: El directorio '{DIRECTORIO_ROSTROS}' no existe.")
        return False
    print(f"Base de datos de rostros lista: {DIRECTORIO_ROSTROS}")
    return True

def procesar_imagen_base64(imagen_base64):
    """Convierte imagen base64 a formato OpenCV"""
    try:
        # Remover el prefijo data:image/jpeg;base64,
        if ',' in imagen_base64:
            imagen_base64 = imagen_base64.split(',')[1]
        
        # Decodificar base64
        imagen_bytes = base64.b64decode(imagen_base64)
        imagen_pil = Image.open(io.BytesIO(imagen_bytes))
        
        # Convertir a array numpy para OpenCV
        imagen_np = np.array(imagen_pil)
        
        # Convertir RGB a BGR (OpenCV usa BGR)
        if len(imagen_np.shape) == 3:
            imagen_cv = cv2.cvtColor(imagen_np, cv2.COLOR_RGB2BGR)
        else:
            imagen_cv = imagen_np
            
        return imagen_cv
    except Exception as e:
        print(f"Error procesando imagen: {e}")
        return None

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login_tradicional():
    """Endpoint para login tradicional"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if username in USUARIOS_MOCK and USUARIOS_MOCK[username] == password:
            return jsonify({
                'success': True,
                'message': f'Bienvenido, {username}!',
                'user': username
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Usuario o contraseña incorrectos'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error del servidor: {str(e)}'
        })

@app.route('/api/verify-face', methods=['POST'])
def verificar_rostro():
    """Endpoint para verificación facial"""
    try:
        data = request.get_json()
        imagen_base64 = data.get('image')
        
        if not imagen_base64:
            return jsonify({
                'success': False,
                'message': 'No se recibió imagen'
            })
        
        # Procesar imagen
        imagen_cv = procesar_imagen_base64(imagen_base64)
        if imagen_cv is None:
            return jsonify({
                'success': False,
                'message': 'Error procesando la imagen'
            })
        
        # Detectar rostros primero
        detector_rostros = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        gray = cv2.cvtColor(imagen_cv, cv2.COLOR_BGR2GRAY)
        rostros_detectados = detector_rostros.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )
        
        if len(rostros_detectados) == 0:
            return jsonify({
                'success': False,
                'message': 'No se detectó ningún rostro en la imagen'
            })
        
        # Usar DeepFace para reconocimiento
        try:
            resultados_df = DeepFace.find(
                img_path=imagen_cv,
                db_path=DIRECTORIO_ROSTROS,
                model_name="VGG-Face",
                detector_backend="opencv",
                distance_metric="cosine",
                enforce_detection=True
            )
            
            if len(resultados_df) > 0 and not resultados_df[0].empty:
                # Rostro reconocido
                ruta_identidad = resultados_df[0].iloc[0]['identity']
                nombre_usuario = os.path.basename(os.path.dirname(ruta_identidad))
                distancia = resultados_df[0].iloc[0]['distance']
                
                return jsonify({
                    'success': True,
                    'message': f'¡Bienvenido, {nombre_usuario}!',
                    'user': nombre_usuario,
                    'confidence': round((1 - distancia) * 100, 2)
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Rostro no reconocido'
                })
                
        except ValueError as e:
            return jsonify({
                'success': False,
                'message': 'No se pudo procesar el rostro'
            })
        except Exception as e:
            print(f"Error con DeepFace: {e}")
            return jsonify({
                'success': False,
                'message': 'Error en el reconocimiento facial'
            })
            
    except Exception as e:
        print(f"Error general: {e}")
        return jsonify({
            'success': False,
            'message': f'Error del servidor: {str(e)}'
        })

@app.route('/dashboard')
def dashboard():
    """Página de dashboard tras login exitoso"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Verificar base de datos de rostros al iniciar
    if verificar_base_datos_rostros():
        print("Iniciando servidor Flask...")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("No se puede iniciar el servidor sin la base de datos de rostros.")