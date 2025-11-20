# 🛒 TechStore - Sistema Experto de Pricing Dinámico

> E-Commerce inteligente con ajuste automático de precios basado en reglas de negocio usando CLIPS

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![CLIPS](https://img.shields.io/badge/CLIPS-6.4-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Sistema Experto CLIPS](#-sistema-experto-clips)
- [API Endpoints](#-api-endpoints)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Autores](#-autores)
- [Licencia](#-licencia)

---

## 📖 Descripción

**TechStore** es una plataforma de e-commerce inteligente que utiliza un **sistema experto basado en reglas (CLIPS)** para ajustar dinámicamente los precios de los productos en tiempo real. El sistema analiza múltiples factores como demanda, inventario, comportamiento del usuario y condiciones de venta para tomar decisiones de pricing óptimas.

### 🎯 Objetivo

Demostrar la aplicación práctica de sistemas basados en reglas (Rule-Based Systems) en un contexto empresarial real, optimizando estrategias de pricing mediante inteligencia artificial simbólica.

### 🏆 Workshop 5: Rule-Based Systems

Este proyecto es parte del **Workshop 5** sobre sistemas basados en reglas, desarrollado como material educativo para entender:
- Sistemas expertos
- Motor de inferencia CLIPS
- Razonamiento forward-chaining
- Resolución de conflictos por prioridad
- Aplicaciones empresariales de IA

---

## ✨ Características

### 🤖 Sistema Experto Inteligente

- ✅ **11 reglas de negocio** implementadas en CLIPS
- ✅ **Ajuste dinámico de precios** basado en múltiples condiciones
- ✅ **Resolución de conflictos** por prioridad de reglas
- ✅ **Motor de inferencia** con forward-chaining
- ✅ **Logging detallado** de decisiones en tiempo real

### 📊 Análisis en Tiempo Real

- ✅ Tracking de visitas por producto
- ✅ Registro de tiempo de visualización
- ✅ Clicks en botón de compra
- ✅ Métricas de conversión
- ✅ Análisis de demanda

### 🛍️ Funcionalidades de E-Commerce

- ✅ Catálogo de **30 productos** en diversas categorías
- ✅ Sistema de **carrito de compras** persistente
- ✅ Filtrado por **categorías**
- ✅ Sección de **ofertas especiales**
- ✅ Proceso de **checkout completo**
- ✅ Badges de envío gratis y garantía

### 💻 Interfaz de Usuario

- ✅ Diseño moderno y responsive
- ✅ Gradientes y animaciones suaves
- ✅ Modal de detalles de producto
- ✅ Confirmación visual de acciones
- ✅ Estadísticas en tiempo real

---

## 🛠️ Tecnologías

### Backend

| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| **Python** | 3.8+ | Lenguaje principal |
| **Flask** | 3.0+ | Framework web |
| **CLIPS** | 6.4 | Motor de inferencia |
| **clipspy** | 1.0+ | Python bindings para CLIPS |
| **Flask-CORS** | 4.0+ | Manejo de CORS |

### Frontend

| Tecnología | Descripción |
|------------|-------------|
| **HTML5** | Estructura semántica |
| **CSS3** | Estilos y animaciones |
| **JavaScript (Vanilla)** | Lógica del cliente |
| **LocalStorage** | Persistencia del carrito |

---

## 🏗️ Arquitectura del Sistema
```
┌─────────────────────────────────────────────────────────────┐
│                    NAVEGADOR (Cliente)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   HTML/CSS   │  │  JavaScript  │  │ LocalStorage │     │
│  └──────┬───────┘  └──────┬───────┘  └──────────────┘     │
│         │                  │                                 │
└─────────┼──────────────────┼─────────────────────────────────┘
          │                  │
          │  HTTP REST API   │
          │                  │
┌─────────▼──────────────────▼─────────────────────────────────┐
│                    SERVIDOR FLASK                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              API Endpoints (server.py)                │   │
│  │  • GET  /api/productos                               │   │
│  │  • GET  /api/producto/<id>                           │   │
│  │  • POST /api/track/visita/<id>                       │   │
│  │  • POST /api/comprar/<id>                            │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │                                         │
│  ┌──────────────────▼───────────────────────────────────┐   │
│  │         Sistema Experto (PricingExpertSystem)        │   │
│  │                                                       │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │        Motor CLIPS (clipspy)                │    │   │
│  │  │  • Forward Chaining                         │    │   │
│  │  │  • Pattern Matching                         │    │   │
│  │  │  • Conflict Resolution                      │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  │                                                       │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │    Base de Reglas (pricing_rules.clp)      │    │   │
│  │  │  • 11 Reglas de Negocio                    │    │   │
│  │  │  • Templates de Hechos                     │    │   │
│  │  │  • Prioridades                              │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐   │
│  │         Base de Datos en Memoria (productos_db)       │   │
│  │  • 30 Productos                                       │   │
│  │  • Métricas en tiempo real                           │   │
│  │  • Estado de inventario                              │   │
│  └───────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────┘
```

---

## 📋 Requisitos Previos

### Software Necesario

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

### Librerías Python
```bash
Flask>=3.0.0
Flask-CORS>=4.0.0
clipspy>=1.0.0
```

---

## 🚀 Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/techstore-expert-system.git
cd techstore-expert-system
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install Flask Flask-CORS clipspy
```

### 4. Verificar Instalación
```bash
python --version  # Debe mostrar Python 3.8+
pip list          # Debe mostrar Flask, Flask-CORS, clipspy
```

---

## 💻 Uso

### Iniciar el Servidor
```bash
python server.py
```

### Acceder a la Aplicación

Abre tu navegador y visita:
```
http://localhost:5000
```

### Consola de Logs

El servidor mostrará en tiempo real:
```
================================================================================
    🛒 E-COMMERCE CON PRICING DINAMICO INTELIGENTE
    Sistema Experto CLIPS + Tracking en Tiempo Real
    Workshop 5: Rule-Based Systems
================================================================================

[09:30:45] SISTEMA: Inicializando sistema experto...
[09:30:45] SISTEMA: ✓ Motor CLIPS inicializado con 11 reglas de negocio

================================================================================
  🌐 Tienda online: http://localhost:5000
  📦 30 productos disponibles
  🤖 Sistema experto activo con logging organizado
================================================================================

────────────────────────────────────────────────────────────────────────────────
🔍 Analizando: iPhone 15 Pro ($999.99)
   📅 Fecha y Hora: 20/11/2025 09:30:45
   Stock: 8 | Visitas: 5 | Ventas: 1
   Condiciones: Demanda Alta, Inventario Bajo, Ventas Altas, Margen Alto
   📈 Regla 1: Aumentar Precio
   🚫 Regla 10: No Aplicar Descuento
   ✨ Decisión Final: Regla 10 (Prioridad: 9)
   💰 Precio: $999.99 → $999.99 (+0.0%)
   📝 Razón: Inventario limitado con alta demanda
────────────────────────────────────────────────────────────────────────────────

[09:31:15] VENTA: ✅ MacBook Pro 14 - $1799.99 (Stock: 14)
```

---

## 🧠 Sistema Experto CLIPS

### Arquitectura del Motor de Inferencia

El sistema utiliza **CLIPS (C Language Integrated Production System)**, un motor de inferencia que implementa:

- **Forward Chaining**: Razonamiento desde los hechos hacia las conclusiones
- **Pattern Matching**: Coincidencia eficiente de patrones
- **Conflict Resolution**: Resolución por prioridad de reglas

### Templates de Hechos
```clips
(deftemplate producto
   (slot id)
   (slot precio-base)
)

(deftemplate condiciones
   (slot demanda-alta (default FALSE))
   (slot demanda-baja (default FALSE))
   (slot inventario-bajo (default FALSE))
   (slot ventas-altas (default FALSE))
   (slot ventas-bajas (default FALSE))
   (slot margen-alto (default FALSE))
   (slot margen-bajo (default FALSE))
   (slot tiempo-restock-largo (default FALSE))
   (slot solicita-financiamiento (default FALSE))
   (slot envio-gratis (default FALSE))
   (slot devolucion-restringida (default FALSE))
   (slot garantia-extendida (default FALSE))
)

(deftemplate accion
   (slot tipo)
   (slot razon)
   (slot regla-aplicada)
   (slot prioridad)
)
```

### 11 Reglas de Negocio

#### **Regla 1: Escasez con Alta Demanda** (Prioridad: 8)
```clips
Si demanda alta Y inventario bajo
→ Aumentar precio
Razón: Demanda alta + inventario bajo = escasez
```

#### **Regla 2: Promoción con Margen** (Prioridad: 5)
```clips
Si ventas bajas Y margen alto
→ Aplicar descuento
Razón: Ventas bajas con margen alto permite promocionar
```

#### **Regla 3: Reactivar Ventas** (Prioridad: 4)
```clips
Si (demanda baja O ventas bajas) Y margen NO bajo
→ Aplicar descuento
Razón: Baja actividad comercial con margen suficiente
```

#### **Regla 4: Protección de Margen** (Prioridad: 10) ⚠️ MÁXIMA
```clips
Si margen bajo
→ NO aplicar descuento
Razón: Margen bajo no permite descuentos
```

#### **Regla 5: Valor por Escasez Temporal** (Prioridad: 7)
```clips
Si tiempo restock largo Y demanda alta
→ Aumentar precio
Razón: Restock tardío + demanda alta = mayor valor
```

#### **Regla 6: Compensación por Restricciones** (Prioridad: 5)
```clips
Si (garantía extendida Y ventas bajas) O devolución restringida
→ Aplicar descuento
Razón: Incentivo por condiciones de venta restrictivas
```

#### **Regla 7: Costos de Servicios** (Prioridad: 6)
```clips
Si envío gratis Y solicita financiamiento Y margen NO alto
→ Aumentar precio
Razón: Compensar costos de envío y financiamiento
```

#### **Regla 8: Liquidación Inteligente** (Prioridad: 6)
```clips
Si ventas bajas Y inventario NO bajo Y tiempo restock NO largo
→ Disminuir precio
Razón: Liquidar inventario con ventas lentas
```

#### **Regla 9: Conversión de Demanda** (Prioridad: 7)
```clips
Si demanda alta PERO ventas NO altas Y NO garantía extendida
→ Aplicar descuento
Razón: Alta demanda sin conversión - impulsar ventas
```

#### **Regla 10: Reservar Inventario Crítico** (Prioridad: 9)
```clips
Si inventario bajo Y (demanda alta O ventas altas)
→ NO aplicar descuento
Razón: Inventario limitado con alta demanda
```

#### **Regla 11: Compensar Condiciones Desfavorables** (Prioridad: 5)
```clips
Si devolución restringida Y NO garantía extendida Y ventas bajas
→ Disminuir precio
Razón: Compensar condiciones poco atractivas
```

### Estrategias de Pricing

| Acción | Ajuste | Casos de Uso |
|--------|--------|--------------|
| `aumentar-precio` | +10% | Escasez, alta demanda, valor temporal |
| `disminuir-precio` | -10% | Liquidación, baja conversión |
| `aplicar-descuento` | -5% | Promoción, incentivos |
| `no-aplicar-descuento` | 0% | Protección de margen, reserva de inventario |

### Condiciones Dinámicas

El sistema calcula en tiempo real:
```python
demanda_alta = visitas > promedio_visitas * 1.5
inventario_bajo = stock < 10
ventas_altas = ventas_hoy > promedio_ventas * 1.5
margen_alto = precio_base > $500
margen_bajo = precio_base < $50
tiempo_restock_largo = stock < 5
```

---

## 🌐 API Endpoints

### Productos

#### `GET /api/productos`
Obtiene todos los productos con precios dinámicos

**Response:**
```json
[
  {
    "id": 1,
    "nombre": "iPhone 15 Pro",
    "descripcion": "Smartphone de ultima generacion",
    "precio_base": 999.99,
    "precio_actual": 999.99,
    "descuento": 0,
    "cambio_porcentual": 0,
    "categoria": "Smartphones",
    "imagen": "📱",
    "stock": 8,
    "visitas": 5,
    "garantia_extendida": true,
    "envio_gratis": true
  }
]
```

#### `GET /api/producto/<id>`
Obtiene un producto específico con análisis detallado

**Response:**
```json
{
  "id": 1,
  "nombre": "iPhone 15 Pro",
  "precio_actual": 999.99,
  "decision": {
    "tipo": "no-aplicar-descuento",
    "razon": "Inventario limitado con alta demanda",
    "regla": "Regla 10",
    "prioridad": 9
  }
}
```

### Tracking

#### `POST /api/track/visita/<id>`
Registra una visita al producto

#### `POST /api/track/tiempo/<id>`
Registra tiempo de visualización

**Body:**
```json
{
  "tiempo": 5
}
```

#### `POST /api/track/click-compra/<id>`
Registra click en botón de compra

### Compras

#### `POST /api/comprar/<id>`
Procesa una compra

**Response:**
```json
{
  "success": true,
  "mensaje": "¡Compra exitosa de iPhone 15 Pro!",
  "precio_pagado": 999.99
}
```

### Métricas

#### `GET /api/metricas`
Obtiene métricas globales del sistema

**Response:**
```json
{
  "total_visitas": 150,
  "productos": [
    {
      "id": 1,
      "nombre": "iPhone 15 Pro",
      "visitas": 25,
      "ventas": 3,
      "stock": 5
    }
  ]
}
```

---

## 📁 Estructura del Proyecto
```
Workshop_8_Rules_Business_Engine/
│
├── server.py                      # Servidor Flask y lógica del sistema experto
├── pricing_rules.clp             # Base de reglas CLIPS (11 reglas)
├── README.md                     # Este archivo
├── requirements.txt              # Dependencias Python
│
├── static/                       # Archivos estáticos del frontend
│   ├── index.html               # Estructura HTML
│   ├── styles.css               # Estilos CSS
│   └── app.js                   # Lógica JavaScript
│
└── docs/                         # Documentación adicional (opcional)
    ├── arquitectura.md
    ├── reglas_negocio.md
    └── manual_usuario.md
```

### Descripción de Archivos Clave

#### `server.py`
- **Backend principal** del sistema
- Implementación de la clase `PricingExpertSystem`
- API REST con Flask
- Logging detallado en consola
- Base de datos en memoria con 30 productos

#### `pricing_rules.clp`
- **Base de conocimiento** del sistema experto
- 11 reglas de negocio en sintaxis CLIPS
- Templates de hechos
- Resolución de conflictos por prioridad

#### `static/index.html`
- Estructura de la **interfaz de usuario**
- Navegación entre secciones
- Modales de producto y confirmación

#### `static/app.js`
- **Lógica del cliente**
- Gestión del carrito de compras
- Llamadas a la API
- Tracking de comportamiento del usuario

#### `static/styles.css`
- **Diseño visual** moderno
- Gradientes y animaciones
- Responsive design

---

## 📸 Capturas de Pantalla

### 🏠 Página Principal
![Inicio](docs/screenshots/inicio.png)
*Vista principal con todos los productos y estadísticas en tiempo real*

### 📂 Categorías
![Categorías](docs/screenshots/categorias.png)
*Navegación por categorías de productos*

### 🏷️ Ofertas Especiales
![Ofertas](docs/screenshots/ofertas.png)
*Productos con descuentos aplicados por el sistema experto*

### 🛒 Carrito de Compras
![Carrito](docs/screenshots/carrito.png)
*Gestión completa del carrito con cálculo de totales*

### 🤖 Análisis del Sistema Experto
![Consola](docs/screenshots/consola.png)
*Logs en tiempo real mostrando decisiones de pricing*

### 📱 Modal de Producto
![Modal](docs/screenshots/modal.png)
*Detalles del producto con información de la IA*

---

## 🧪 Ejemplos de Uso

### Ejemplo 1: Producto con Alta Demanda y Stock Bajo

**Entrada:**
- Producto: PlayStation 5
- Stock: 3 unidades
- Visitas: 15
- Ventas hoy: 2

**Análisis del Sistema:**
```
Condiciones detectadas:
- demanda_alta: TRUE
- inventario_bajo: TRUE
- ventas_altas: TRUE

Reglas activadas:
- Regla 1: Aumentar precio (Prioridad: 8)
- Regla 10: NO aplicar descuento (Prioridad: 9)

Decisión Final: Regla 10 (NO aplicar descuento)
Razón: Inventario limitado con alta demanda
Precio: $499.99 → $499.99 (sin cambio)
```

### Ejemplo 2: Producto con Ventas Bajas y Alto Margen

**Entrada:**
- Producto: MacBook Pro 14
- Stock: 15 unidades
- Visitas: 3
- Ventas hoy: 0

**Análisis del Sistema:**
```
Condiciones detectadas:
- ventas_bajas: TRUE
- margen_alto: TRUE

Reglas activadas:
- Regla 2: Aplicar descuento (Prioridad: 5)
- Regla 8: Disminuir precio (Prioridad: 6)

Decisión Final: Regla 8 (Disminuir precio)
Razón: Liquidar inventario con ventas lentas
Precio: $1999.99 → $1799.99 (-10%)
```

### Ejemplo 3: Producto con Margen Bajo

**Entrada:**
- Producto: Mouse Inalámbrico
- Stock: 200 unidades
- Precio base: $29.99
- Ventas hoy: 5

**Análisis del Sistema:**
```
Condiciones detectadas:
- margen_bajo: TRUE
- ventas_altas: TRUE

Reglas activadas:
- Regla 4: NO aplicar descuento (Prioridad: 10)

Decisión Final: Regla 4 (NO aplicar descuento)
Razón: Margen bajo no permite descuentos
Precio: $29.99 → $29.99 (sin cambio)
```

---

## 🎓 Conceptos Aprendidos

### Sistemas Expertos
- ✅ Representación del conocimiento mediante reglas
- ✅ Separación entre motor de inferencia y base de conocimiento
- ✅ Forward chaining (encadenamiento hacia adelante)
- ✅ Resolución de conflictos por prioridad

### CLIPS
- ✅ Sintaxis de reglas y templates
- ✅ Pattern matching
- ✅ Assert y retract de hechos
- ✅ Integración con Python via clipspy

### Aplicaciones Empresariales
- ✅ Dynamic pricing
- ✅ Revenue management
- ✅ Inventory optimization
- ✅ Behavioral analytics

### Desarrollo Full Stack
- ✅ API REST con Flask
- ✅ Frontend moderno con Vanilla JS
- ✅ Gestión de estado del cliente
- ✅ Persistencia con LocalStorage

---

## 🔧 Configuración Avanzada

### Modificar Umbrales de Condiciones

Edita en `server.py`, método `analizar_producto`:
```python
condiciones = {
    'demanda_alta': producto['visitas'] > promedio_visitas * 1.5,  # Cambiar 1.5
    'inventario_bajo': producto['stock'] < 10,                      # Cambiar 10
    'margen_alto': producto['precio_base'] > 500,                   # Cambiar 500
    # ...
}
```

### Ajustar Porcentajes de Pricing

Edita en `server.py`, método `calcular_precio_final`:
```python
if tipo_accion == 'aumentar-precio':
    return precio_base * 1.10  # Cambiar 1.10 (10%)
elif tipo_accion == 'disminuir-precio':
    return precio_base * 0.90  # Cambiar 0.90 (-10%)
elif tipo_accion == 'aplicar-descuento':
    return precio_base * 0.95  # Cambiar 0.95 (-5%)
```

### Agregar Nuevas Reglas

1. Edita `pricing_rules.clp`
2. Define la nueva regla con su prioridad
3. Reinicia el servidor
```clips
(defrule regla-12-nueva-estrategia
   (condiciones (nueva-condicion TRUE))
   =>
   (assert (accion 
      (tipo nueva-accion)
      (razon "Descripción de la estrategia")
      (regla-aplicada "Regla 12")
      (prioridad 7)
   ))
)
```

---

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'clips'`

**Solución:**
```bash
pip install clipspy
```

### Error: `Address already in use`

**Solución:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Los precios no cambian

**Verificar:**
1. El sistema experto está inicializado
2. Los productos tienen métricas de visitas/ventas
3. Las condiciones se están evaluando correctamente
4. Revisar logs en consola

### El carrito se vacía al recargar

**Verificar:**
- LocalStorage está habilitado en el navegador
- No hay errores en la consola del navegador
- `localStorage.setItem()` se está ejecutando

---

## 📊 Métricas y Análisis

### Estadísticas del Sistema
```python
# Ver métricas en tiempo real
GET http://localhost:5000/api/metricas
```

### Productos Más Visitados

Los productos con más visitas influyen en el cálculo de `demanda_alta`

### Tasa de Conversión
```
Tasa = (Ventas / Clicks en Comprar) * 100
```

### Efectividad de Descuentos

Comparar ventas antes y después de aplicar descuentos

---

## 🚀 Mejoras Futuras

### Funcionalidades Propuestas

- [ ] **Persistencia en base de datos** (PostgreSQL/MongoDB)
- [ ] **Sistema de usuarios y autenticación**
- [ ] **Historial de precios** por producto
- [ ] **Dashboard de analytics** para administradores
- [ ] **Machine Learning** para predecir demanda
- [ ] **A/B Testing** de estrategias de pricing
- [ ] **Integración con pasarelas de pago**
- [ ] **Sistema de recomendaciones**
- [ ] **Notificaciones de ofertas** por email/push
- [ ] **Análisis de competencia** con web scraping

### Mejoras Técnicas

- [ ] Dockerización del proyecto
- [ ] Tests unitarios y de integración
- [ ] CI/CD con GitHub Actions
- [ ] Documentación de API con Swagger
- [ ] Rate limiting en endpoints
- [ ] Caching con Redis
- [ ] Monitoreo con Prometheus/Grafana

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guía de Estilo

- Código en **español** (variables, comentarios, mensajes)
- Seguir **PEP 8** para Python
- Documentar funciones complejas
- Agregar tests para nuevas features

---

## 👨‍💻 Autores

- **Johan [Tu Apellido]** - *Desarrollo completo* - [GitHub](https://github.com/tu-usuario)

### Workshop 5: Rule-Based Systems
- **Curso:** Sistemas Inteligentes / Inteligencia Artificial
- **Institución:** [Tu Universidad]
- **Fecha:** Noviembre 2025

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
```
MIT License

Copyright (c) 2025 Johan [Tu Apellido]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Agradecimientos

- **CLIPS Development Team** por el motor de inferencia
- **Flask Team** por el framework web
- **Comunidad de Python** por las librerías utilizadas
- **Profesores y compañeros** del Workshop 5

---

## 📚 Referencias

### Documentación

- [CLIPS Official Documentation](https://clipsrules.net/)
- [clipspy Documentation](https://clipspy.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Artículos Relevantes

1. *Expert Systems: Principles and Programming* - Giarratano & Riley
2. *Production Systems and Expert Systems* - Brownston et al.
3. *Dynamic Pricing Strategies in E-Commerce* - Journal of Revenue Management

### Tutoriales

- [Introduction to CLIPS](https://clipsrules.net/Documentation.html)
- [Building Expert Systems with CLIPS](https://www.youtube.com/watch?v=example)
- [Flask REST API Tutorial](https://flask.palletsprojects.com/en/latest/tutorial/)

---

## 📞 Contacto

**Johan [Tu Apellido]**

- 📧 Email: tu-email@ejemplo.com
- 💼 LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)
- 🐙 GitHub: [@tu-usuario](https://github.com/tu-usuario)

---

## 🌟 ¡Dale una estrella al proyecto!

Si este proyecto te fue útil, considera darle una ⭐ en GitHub.

---

<div align="center">

**Desarrollado con ❤️ para el Workshop 5: Rule-Based Systems**

</div>
