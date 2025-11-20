// App.js - E-Commerce con Pricing Dinamico
let productos = [];
let tiempoVisualizacion = {};
let carrito = [];

// Cargar productos al iniciar
async function cargarProductos() {
    try {
        const response = await fetch('/api/productos');
        productos = await response.json();
        mostrarProductos();
    } catch (error) {
        console.error('Error cargando productos:', error);
    }
}

// Mostrar productos en el grid
function mostrarProductos(categoria = 'todos') {
    const grid = document.getElementById('productos-grid');
    grid.innerHTML = '';
    
    const productosFiltrados = categoria === 'todos' 
        ? productos 
        : productos.filter(p => p.categoria === categoria);
    
    productosFiltrados.forEach(producto => {
        const descuento = producto.descuento > 0;
        const precioAnterior = descuento ? producto.precio_base : null;
        const porcentajeDescuento = descuento 
            ? Math.round((producto.descuento / producto.precio_base) * 100)
            : 0;
        
        const stockBajo = producto.stock < 10;
        
        const card = document.createElement('div');
        card.className = 'producto-card';
        card.setAttribute('data-id', producto.id);
        
        card.innerHTML = `
            <div class="producto-icon">${producto.imagen}</div>
            <div class="producto-info">
                <div class="producto-categoria">${producto.categoria}</div>
                <h3 class="producto-nombre">${producto.nombre}</h3>
                <p class="producto-descripcion">${producto.descripcion}</p>
                
                <div class="producto-footer">
                    <div class="precio-container">
                        <span class="precio-actual">$${producto.precio_actual.toFixed(2)}</span>
                        ${precioAnterior ? `
                            <span class="precio-anterior">$${precioAnterior.toFixed(2)}</span>
                            <span class="descuento-badge">-${porcentajeDescuento}%</span>
                        ` : ''}
                    </div>
                    
                    <div class="badges">
                        ${producto.envio_gratis ? '<span class="badge badge-envio">🚚 Envio Gratis</span>' : ''}
                        ${producto.garantia_extendida ? '<span class="badge badge-garantia">🛡️ Garantia</span>' : ''}
                        ${stockBajo ? `<span class="badge badge-stock stock-bajo">⚠️ Solo ${producto.stock} disponibles</span>` : ''}
                    </div>
                    
                    <button class="btn-comprar" onclick="verDetalle(${producto.id})">
                        Ver Detalles
                    </button>
                </div>
            </div>
        `;
        
        // Tracking de visualizacion
        card.addEventListener('mouseenter', () => trackVisita(producto.id));
        
        grid.appendChild(card);
    });
}

// Track visita a producto
async function trackVisita(productoId) {
    try {
        await fetch(`/api/track/visita/${productoId}`, { method: 'POST' });
        
        // Iniciar timer de visualizacion
        if (!tiempoVisualizacion[productoId]) {
            tiempoVisualizacion[productoId] = {
                inicio: Date.now(),
                enviado: false
            };
        }
    } catch (error) {
        console.error('Error tracking visita:', error);
    }
}

// Track tiempo de visualizacion
async function trackTiempo(productoId) {
    const info = tiempoVisualizacion[productoId];
    if (info && !info.enviado) {
        const tiempo = Math.floor((Date.now() - info.inicio) / 1000);
        
        try {
            await fetch(`/api/track/tiempo/${productoId}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ tiempo })
            });
            info.enviado = true;
        } catch (error) {
            console.error('Error tracking tiempo:', error);
        }
    }
}

// Ver detalle de producto
async function verDetalle(productoId) {
    try {
        const response = await fetch(`/api/producto/${productoId}`);
        const producto = await response.json();
        
        // Track click
        await fetch(`/api/track/click-compra/${productoId}`, { method: 'POST' });
        
        const modal = document.getElementById('modal-producto');
        const modalBody = document.getElementById('modal-body');
        
        const descuento = producto.descuento > 0;
        const porcentajeDescuento = descuento 
            ? Math.round((producto.descuento / producto.precio_base) * 100)
            : 0;
        
        modalBody.innerHTML = `
            <div style="text-align: center;">
                <div style="font-size: 6em; margin: 20px 0;">${producto.imagen}</div>
                <h2>${producto.nombre}</h2>
                <p style="color: #666; margin: 15px 0;">${producto.descripcion}</p>
                
                <div style="margin: 30px 0;">
                    <div style="font-size: 2.5em; color: var(--success); font-weight: 700;">
                        $${producto.precio_actual.toFixed(2)}
                    </div>
                    ${descuento ? `
                        <div style="margin: 10px 0;">
                            <span style="text-decoration: line-through; color: #999; font-size: 1.3em;">
                                $${producto.precio_base.toFixed(2)}
                            </span>
                            <span style="background: var(--danger); color: white; padding: 5px 15px; border-radius: 15px; margin-left: 10px; font-weight: 600;">
                                ${porcentajeDescuento}% OFF
                            </span>
                        </div>
                    ` : ''}
                </div>
                
                <div style="display: flex; gap: 10px; justify-content: center; margin: 20px 0;">
                    ${producto.envio_gratis ? '<span class="badge badge-envio">🚚 Envio Gratis</span>' : ''}
                    ${producto.garantia_extendida ? '<span class="badge badge-garantia">🛡️ Garantia Extendida</span>' : ''}
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <p><strong>Stock disponible:</strong> ${producto.stock} unidades</p>
                    <p><strong>Categoria:</strong> ${producto.categoria}</p>
                    <p><strong>Visitas hoy:</strong> ${producto.visitas}</p>
                </div>
                
                ${producto.decision ? `
                    <div style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 20px; border-radius: 10px; margin: 20px 0;">
                        <h4 style="margin-bottom: 10px;">🤖 Precio Dinamico Activo</h4>
                        <p style="opacity: 0.9; font-size: 0.95em;">${producto.decision.razon}</p>
                        <p style="margin-top: 10px; font-size: 0.85em; opacity: 0.8;">Sistema: ${producto.decision.regla}</p>
                    </div>
                ` : ''}
                
                <button class="btn-primary" style="width: 100%; padding: 15px; font-size: 1.2em; margin-top: 20px;" 
                        onclick="comprarProducto(${producto.id})">
                    🛒 Comprar Ahora
                </button>
            </div>
        `;
        
        modal.style.display = 'block';
        
        // Track tiempo al cerrar modal
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = () => {
            trackTiempo(productoId);
            modal.style.display = 'none';
        };
        
        window.onclick = (event) => {
            if (event.target == modal) {
                trackTiempo(productoId);
                modal.style.display = 'none';
            }
        };
        
    } catch (error) {
        console.error('Error cargando detalle:', error);
    }
}

// Comprar producto
async function comprarProducto(productoId) {
    try {
        const response = await fetch(`/api/comprar/${productoId}`, { method: 'POST' });
        const result = await response.json();
        
        if (result.success) {
            document.getElementById('modal-producto').style.display = 'none';
            
            const modalExito = document.getElementById('modal-exito');
            document.getElementById('mensaje-exito').textContent = 
                `${result.mensaje} Precio pagado: $${result.precio_pagado.toFixed(2)}`;
            modalExito.style.display = 'block';
            
            // Actualizar productos despues de compra
            setTimeout(() => {
                cargarProductos();
            }, 1000);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error en compra:', error);
        alert('Error procesando la compra');
    }
}

function cerrarModalExito() {
    document.getElementById('modal-exito').style.display = 'none';
}

// Filtros
document.addEventListener('DOMContentLoaded', () => {
    cargarProductos();
    
    // Recargar precios cada 30 segundos
    setInterval(cargarProductos, 30000);
    
    // Event listeners para filtros
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const categoria = btn.getAttribute('data-categoria');
            mostrarProductos(categoria);
        });
    });
});