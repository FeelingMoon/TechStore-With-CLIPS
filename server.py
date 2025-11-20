"""
E-Commerce con Sistema Experto de Pricing Dinamico
Workshop 5 - Rule Based Systems
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import clips
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__, static_folder='static')
CORS(app)

# Colores para consola
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Base de datos expandida de productos
productos_db = {
    1: {
        'id': 1, 'nombre': 'iPhone 15 Pro', 'descripcion': 'Smartphone de ultima generacion',
        'precio_base': 999.99, 'categoria': 'Smartphones', 'imagen': '📱', 'stock': 8,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    2: {
        'id': 2, 'nombre': 'MacBook Pro 14', 'descripcion': 'Laptop profesional con M3 Pro',
        'precio_base': 1999.99, 'categoria': 'Laptops', 'imagen': '💻', 'stock': 15,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    3: {
        'id': 3, 'nombre': 'Smart TV 55 4K', 'descripcion': 'Televisor inteligente 4K',
        'precio_base': 599.99, 'categoria': 'TV', 'imagen': '📺', 'stock': 45,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': True
    },
    4: {
        'id': 4, 'nombre': 'AirPods Pro', 'descripcion': 'Auriculares con cancelacion de ruido',
        'precio_base': 249.99, 'categoria': 'Audio', 'imagen': '🎧', 'stock': 120,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': False
    },
    5: {
        'id': 5, 'nombre': 'PlayStation 5', 'descripcion': 'Consola de videojuegos next-gen',
        'precio_base': 499.99, 'categoria': 'Gaming', 'imagen': '🎮', 'stock': 3,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': True
    },
    6: {
        'id': 6, 'nombre': 'Mouse Inalambrico', 'descripcion': 'Mouse ergonomico para oficina',
        'precio_base': 29.99, 'categoria': 'Accesorios', 'imagen': '🖱️', 'stock': 200,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': False
    },
    7: {
        'id': 7, 'nombre': 'Samsung Galaxy S24', 'descripcion': 'Smartphone Android premium',
        'precio_base': 899.99, 'categoria': 'Smartphones', 'imagen': '📱', 'stock': 25,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    8: {
        'id': 8, 'nombre': 'iPad Air', 'descripcion': 'Tablet versatil para trabajo y ocio',
        'precio_base': 649.99, 'categoria': 'Tablets', 'imagen': '📱', 'stock': 30,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    9: {
        'id': 9, 'nombre': 'Nintendo Switch', 'descripcion': 'Consola hibrida portatil',
        'precio_base': 299.99, 'categoria': 'Gaming', 'imagen': '🎮', 'stock': 50,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': True
    },
    10: {
        'id': 10, 'nombre': 'Bose QuietComfort', 'descripcion': 'Audifonos premium noise-cancelling',
        'precio_base': 349.99, 'categoria': 'Audio', 'imagen': '🎧', 'stock': 18,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    11: {
        'id': 11, 'nombre': 'Teclado Mecanico RGB', 'descripcion': 'Teclado gaming con switches Cherry MX',
        'precio_base': 149.99, 'categoria': 'Accesorios', 'imagen': '⌨️', 'stock': 75,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': False
    },
    12: {
        'id': 12, 'nombre': 'Webcam 4K', 'descripcion': 'Camara web profesional para streaming',
        'precio_base': 99.99, 'categoria': 'Accesorios', 'imagen': '📷', 'stock': 60,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': False
    },
    13: {
        'id': 13, 'nombre': 'Disco SSD 1TB', 'descripcion': 'Almacenamiento solido de alta velocidad',
        'precio_base': 89.99, 'categoria': 'Componentes', 'imagen': '💾', 'stock': 100,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': False
    },
    14: {
        'id': 14, 'nombre': 'Monitor 27 QHD', 'descripcion': 'Monitor para productividad 2560x1440',
        'precio_base': 329.99, 'categoria': 'Monitores', 'imagen': '🖥️', 'stock': 22,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    15: {
        'id': 15, 'nombre': 'Lenovo ThinkPad', 'descripcion': 'Laptop empresarial confiable',
        'precio_base': 1299.99, 'categoria': 'Laptops', 'imagen': '💻', 'stock': 12,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    16: {
        'id': 16, 'nombre': 'Razer DeathAdder', 'descripcion': 'Mouse gaming de precision',
        'precio_base': 69.99, 'categoria': 'Accesorios', 'imagen': '🖱️', 'stock': 85,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': False
    },
    17: {
        'id': 17, 'nombre': 'Echo Dot Alexa', 'descripcion': 'Asistente virtual inteligente',
        'precio_base': 49.99, 'categoria': 'Smart Home', 'imagen': '🔊', 'stock': 150,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': True
    },
    18: {
        'id': 18, 'nombre': 'Ring Doorbell', 'descripcion': 'Timbre inteligente con camara',
        'precio_base': 129.99, 'categoria': 'Smart Home', 'imagen': '🚪', 'stock': 40,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    },
    19: {
        'id': 19, 'nombre': 'Kindle Paperwhite', 'descripcion': 'E-reader con luz ajustable',
        'precio_base': 139.99, 'categoria': 'Lectores', 'imagen': '📚', 'stock': 65,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': False, 'envio_gratis': True
    },
    20: {
        'id': 20, 'nombre': 'GoPro Hero 12', 'descripcion': 'Camara de accion 5.3K',
        'precio_base': 399.99, 'categoria': 'Camaras', 'imagen': '📹', 'stock': 15,
        'visitas': 0, 'tiempo_visualizacion': 0, 'ventas_hoy': 0, 'clicks_compra': 0,
        'garantia_extendida': True, 'envio_gratis': True
    }
}

# Metricas globales
metricas_globales = {
    'total_visitas_hoy': 0,
    'productos_mas_vistos': [],
    'hora_inicio': datetime.now()
}

def print_banner():
    print(f"\n{Colors.CYAN}{'='*80}")
    print(f"{Colors.BOLD}    🛒 E-COMMERCE CON PRICING DINAMICO INTELIGENTE")
    print(f"    Sistema Experto CLIPS + Tracking en Tiempo Real")
    print(f"    Workshop 5: Rule-Based Systems")
    print(f"{'='*80}{Colors.ENDC}\n")

def log_event(tipo, mensaje, indent=False):
    """Logging mejorado con indentación"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    colores = {
        'VISITA': Colors.BLUE,
        'CLICK': Colors.CYAN,
        'ANALISIS': Colors.YELLOW,
        'REGLA': Colors.CYAN,
        'DECISION': Colors.GREEN,
        'PRECIO': Colors.GREEN,
        'VENTA': Colors.GREEN,
        'SISTEMA': Colors.BOLD
    }
    color = colores.get(tipo, Colors.ENDC)
    
    prefijo = "   " if indent else ""
    
    if tipo == 'SISTEMA' or tipo == 'VENTA':
        print(f"{color}[{timestamp}] {tipo}: {mensaje}{Colors.ENDC}")
    elif tipo in ['ANALISIS', 'REGLA', 'DECISION', 'PRECIO']:
        print(f"{color}{prefijo}{mensaje}{Colors.ENDC}")


class PricingExpertSystem:
    def __init__(self):
        self.env = clips.Environment()
        self.env.load('pricing_rules.clp')
        log_event('SISTEMA', '✓ Motor CLIPS inicializado con 11 reglas de negocio')
    
    def analizar_producto(self, producto):
        """Analiza un producto y ajusta su precio dinamicamente"""
        self.env.reset()
        
        # Calcular metricas en tiempo real
        total_productos = len(productos_db)
        promedio_visitas = sum(p['visitas'] for p in productos_db.values()) / total_productos
        promedio_ventas = sum(p['ventas_hoy'] for p in productos_db.values()) / total_productos
        
        # Determinar condiciones dinamicamente
        condiciones = {
            'demanda_alta': producto['visitas'] > promedio_visitas * 1.5,
            'demanda_baja': producto['visitas'] < promedio_visitas * 0.5,
            'inventario_bajo': producto['stock'] < 10,
            'ventas_altas': producto['ventas_hoy'] > promedio_ventas * 1.5,
            'ventas_bajas': producto['ventas_hoy'] < promedio_ventas * 0.5,
            'margen_alto': producto['precio_base'] > 500,
            'margen_bajo': producto['precio_base'] < 50,
            'tiempo_restock_largo': producto['stock'] < 5,
            'solicita_financiamiento': producto['precio_base'] > 1000,
            'envio_gratis': producto['envio_gratis'],
            'devolucion_restringida': not producto.get('envio_gratis', True),
            'garantia_extendida': producto['garantia_extendida']
        }
        
        # Crear hechos en CLIPS
        producto_fact = f"""(producto 
            (id {producto['id']})
            (precio-base {producto['precio_base']})
        )"""
        
        condiciones_fact = f"""(condiciones
            (demanda-alta {str(condiciones['demanda_alta']).upper()})
            (demanda-baja {str(condiciones['demanda_baja']).upper()})
            (inventario-bajo {str(condiciones['inventario_bajo']).upper()})
            (ventas-altas {str(condiciones['ventas_altas']).upper()})
            (ventas-bajas {str(condiciones['ventas_bajas']).upper()})
            (margen-alto {str(condiciones['margen_alto']).upper()})
            (margen-bajo {str(condiciones['margen_bajo']).upper()})
            (tiempo-restock-largo {str(condiciones['tiempo_restock_largo']).upper()})
            (solicita-financiamiento {str(condiciones['solicita_financiamiento']).upper()})
            (envio-gratis {str(condiciones['envio_gratis']).upper()})
            (devolucion-restringida {str(condiciones['devolucion_restringida']).upper()})
            (garantia-extendida {str(condiciones['garantia_extendida']).upper()})
        )"""
        
        self.env.assert_string(producto_fact)
        self.env.assert_string(condiciones_fact)
        
        # Mostrar inicio de análisis
        print(f"\n{Colors.YELLOW}{'─' * 80}")
        log_event('ANALISIS', f"🔍 Analizando: {producto['nombre']} (${producto['precio_base']:.2f})", indent=False)
        log_event('ANALISIS', f"Stock: {producto['stock']} | Visitas: {producto['visitas']} | Ventas: {producto['ventas_hoy']}", indent=True)
        
        # Mostrar condiciones activas
        condiciones_activas = [k.replace('_', ' ').title() for k, v in condiciones.items() if v]
        if condiciones_activas:
            log_event('ANALISIS', f"Condiciones: {', '.join(condiciones_activas)}", indent=True)
        
        # Ejecutar motor CLIPS
        self.env.run()
        
        # Obtener acciones y mostrar reglas aplicadas
        acciones = []
        reglas_aplicadas = []
        
        for fact in self.env.facts():
            if fact.template.name == 'accion':
                accion = {
                    'tipo': str(fact['tipo']),
                    'razon': str(fact['razon']),
                    'regla': str(fact['regla-aplicada']),
                    'prioridad': int(fact['prioridad'])
                }
                acciones.append(accion)
                
                # Mostrar cada regla aplicada
                tipo_emoji = {
                    'aumentar-precio': '📈',
                    'disminuir-precio': '📉',
                    'aplicar-descuento': '🏷️',
                    'no-aplicar-descuento': '🚫'
                }
                emoji = tipo_emoji.get(accion['tipo'], '⚙️')
                log_event('REGLA', f"{emoji} {accion['regla']}: {accion['tipo'].replace('-', ' ').title()}", indent=True)
        
        acciones.sort(key=lambda x: x['prioridad'], reverse=True)
        
        # Calcular precio final
        if acciones:
            decision = acciones[0]
            precio_final = self.calcular_precio_final(producto['precio_base'], decision['tipo'])
            cambio = ((precio_final - producto['precio_base']) / producto['precio_base']) * 100
            
            # Mostrar decisión final
            log_event('DECISION', f"✨ Decisión Final: {decision['regla']} (Prioridad: {decision['prioridad']})", indent=True)
            log_event('PRECIO', f"💰 Precio: ${producto['precio_base']:.2f} → ${precio_final:.2f} ({cambio:+.1f}%)", indent=True)
            log_event('PRECIO', f"📝 Razón: {decision['razon']}", indent=True)
        else:
            precio_final = producto['precio_base']
            cambio = 0
            log_event('PRECIO', f"✓ Mantener precio base: ${precio_final:.2f}", indent=True)
        
        print(f"{Colors.YELLOW}{'─' * 80}{Colors.ENDC}\n")
        
        return {
            'precio_final': precio_final,
            'precio_base': producto['precio_base'],
            'cambio_porcentual': cambio,
            'decision': acciones[0] if acciones else None,
            'condiciones': [k for k, v in condiciones.items() if v]
        }
    
    def calcular_precio_final(self, precio_base, tipo_accion):
        if tipo_accion == 'aumentar-precio':
            return precio_base * 1.10
        elif tipo_accion == 'disminuir-precio':
            return precio_base * 0.90
        elif tipo_accion == 'aplicar-descuento':
            return precio_base * 0.95
        else:
            return precio_base

expert_system = None

# ==================== ENDPOINTS ====================

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/productos', methods=['GET'])
def get_productos():
    """Obtiene todos los productos con precios dinamicos"""
    productos_con_precios = []
    
    for producto in productos_db.values():
        analisis = expert_system.analizar_producto(producto)
        
        productos_con_precios.append({
            'id': producto['id'],
            'nombre': producto['nombre'],
            'descripcion': producto['descripcion'],
            'precio_base': producto['precio_base'],
            'precio_actual': analisis['precio_final'],
            'descuento': max(0, analisis['precio_base'] - analisis['precio_final']),
            'cambio_porcentual': analisis['cambio_porcentual'],
            'categoria': producto['categoria'],
            'imagen': producto['imagen'],
            'stock': producto['stock'],
            'visitas': producto['visitas'],
            'garantia_extendida': producto['garantia_extendida'],
            'envio_gratis': producto['envio_gratis']
        })
    
    return jsonify(productos_con_precios)

@app.route('/api/producto/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    """Obtiene un producto especifico"""
    if producto_id not in productos_db:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    producto = productos_db[producto_id]
    analisis = expert_system.analizar_producto(producto)
    
    return jsonify({
        'id': producto['id'],
        'nombre': producto['nombre'],
        'descripcion': producto['descripcion'],
        'precio_base': producto['precio_base'],
        'precio_actual': analisis['precio_final'],
        'descuento': max(0, analisis['precio_base'] - analisis['precio_final']),
        'cambio_porcentual': analisis['cambio_porcentual'],
        'categoria': producto['categoria'],
        'imagen': producto['imagen'],
        'stock': producto['stock'],
        'visitas': producto['visitas'],
        'garantia_extendida': producto['garantia_extendida'],
        'envio_gratis': producto['envio_gratis'],
        'decision': analisis['decision']
    })

@app.route('/api/track/visita/<int:producto_id>', methods=['POST'])
def track_visita(producto_id):
    """Registra una visita a un producto"""
    if producto_id not in productos_db:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    productos_db[producto_id]['visitas'] += 1
    metricas_globales['total_visitas_hoy'] += 1
    
    return jsonify({'success': True})

@app.route('/api/track/tiempo/<int:producto_id>', methods=['POST'])
def track_tiempo(producto_id):
    """Registra tiempo de visualizacion"""
    if producto_id not in productos_db:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    data = request.json
    tiempo = data.get('tiempo', 0)
    productos_db[producto_id]['tiempo_visualizacion'] += tiempo
    
    return jsonify({'success': True})

@app.route('/api/track/click-compra/<int:producto_id>', methods=['POST'])
def track_click_compra(producto_id):
    """Registra click en boton de compra"""
    if producto_id not in productos_db:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    productos_db[producto_id]['clicks_compra'] += 1
    
    return jsonify({'success': True})

@app.route('/api/comprar/<int:producto_id>', methods=['POST'])
def comprar_producto(producto_id):
    """Procesa una compra"""
    if producto_id not in productos_db:
        return jsonify({'error': 'Producto no encontrado'}), 404
    
    producto = productos_db[producto_id]
    
    if producto['stock'] <= 0:
        return jsonify({'error': 'Producto sin stock'}), 400
    
    # Procesar compra
    producto['stock'] -= 1
    producto['ventas_hoy'] += 1
    
    analisis = expert_system.analizar_producto(producto)
    
    log_event('VENTA', f"✅ {producto['nombre']} - ${analisis['precio_final']:.2f} (Stock: {producto['stock']})")
    
    return jsonify({
        'success': True,
        'mensaje': f'¡Compra exitosa de {producto["nombre"]}!',
        'precio_pagado': analisis['precio_final']
    })

@app.route('/api/metricas', methods=['GET'])
def get_metricas():
    """Obtiene metricas globales"""
    return jsonify({
        'total_visitas': metricas_globales['total_visitas_hoy'],
        'productos': [{
            'id': p['id'],
            'nombre': p['nombre'],
            'visitas': p['visitas'],
            'ventas': p['ventas_hoy'],
            'stock': p['stock']
        } for p in productos_db.values()]
    })

if __name__ == '__main__':
    print_banner()
    log_event('SISTEMA', 'Inicializando sistema experto...')
    expert_system = PricingExpertSystem()
    
    print(f"\n{Colors.GREEN}{'='*80}")
    print(f"{Colors.BOLD}  🌐 Tienda online: http://localhost:5000")
    print(f"  📦 {len(productos_db)} productos disponibles")
    print(f"  🤖 Sistema experto activo con logging organizado")
    print(f"{'='*80}{Colors.ENDC}\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)