;;; ============================================================
;;; Sistema Experto de Pricing Dinamico para E-commerce
;;; Workshop 5 - Rule Based Systems
;;; ============================================================

;;; Definicion de templates para los hechos
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
   (slot tipo (allowed-values aumentar-precio disminuir-precio aplicar-descuento no-aplicar-descuento ninguna))
   (slot razon)
   (slot regla-aplicada)
   (slot prioridad (default 0))
)

;;; ============================================================
;;; REGLAS DE NEGOCIO (11 reglas segun el enunciado)
;;; ============================================================

;;; REGLA 1: Si demanda es alta Y inventario es bajo, entonces aumentar precio
(defrule regla-1-demanda-alta-inventario-bajo
   (condiciones (demanda-alta TRUE) (inventario-bajo TRUE))
   =>
   (assert (accion 
      (tipo aumentar-precio)
      (razon "Demanda alta + inventario bajo = escasez")
      (regla-aplicada "Regla 1")
      (prioridad 8)
   ))
   (printout t "REGLA 1 ACTIVADA: Aumentar precio (demanda alta + inventario bajo)" crlf)
)

;;; REGLA 2: Si volumen de ventas es bajo Y margen de ganancia es alto, entonces aplicar descuento
(defrule regla-2-ventas-bajas-margen-alto
   (condiciones (ventas-bajas TRUE) (margen-alto TRUE))
   =>
   (assert (accion 
      (tipo aplicar-descuento)
      (razon "Ventas bajas con margen alto permite promocionar")
      (regla-aplicada "Regla 2")
      (prioridad 5)
   ))
   (printout t "REGLA 2 ACTIVADA: Aplicar descuento (ventas bajas + margen alto)" crlf)
)

;;; REGLA 3: Si (demanda baja O ventas bajas) Y margen NO bajo, entonces aplicar descuento
(defrule regla-3-demanda-o-ventas-bajas-margen-no-bajo
   (or (condiciones (demanda-baja TRUE))
       (condiciones (ventas-bajas TRUE)))
   (condiciones (margen-bajo FALSE))
   =>
   (assert (accion 
      (tipo aplicar-descuento)
      (razon "Baja actividad comercial con margen suficiente")
      (regla-aplicada "Regla 3")
      (prioridad 4)
   ))
   (printout t "REGLA 3 ACTIVADA: Aplicar descuento (baja actividad + margen suficiente)" crlf)
)

;;; REGLA 4: Si margen es bajo, entonces NO aplicar descuento (PRIORIDAD ALTA)
(defrule regla-4-margen-bajo-bloquea-descuento
   (condiciones (margen-bajo TRUE))
   =>
   (assert (accion 
      (tipo no-aplicar-descuento)
      (razon "Margen bajo no permite descuentos")
      (regla-aplicada "Regla 4")
      (prioridad 10)
   ))
   (printout t "REGLA 4 ACTIVADA: NO aplicar descuento (margen bajo - PRIORIDAD MAXIMA)" crlf)
)

;;; REGLA 5: Si tiempo de restock largo Y demanda alta, entonces aumentar precio
(defrule regla-5-restock-largo-demanda-alta
   (condiciones (tiempo-restock-largo TRUE) (demanda-alta TRUE))
   =>
   (assert (accion 
      (tipo aumentar-precio)
      (razon "Restock tardio + demanda alta = mayor valor")
      (regla-aplicada "Regla 5")
      (prioridad 7)
   ))
   (printout t "REGLA 5 ACTIVADA: Aumentar precio (restock largo + demanda alta)" crlf)
)

;;; REGLA 6: Aplicar descuento si (garantia extendida Y ventas bajas) O devolucion restringida
(defrule regla-6-garantia-ventas-o-devolucion
   (or (and (condiciones (garantia-extendida TRUE))
            (condiciones (ventas-bajas TRUE)))
       (condiciones (devolucion-restringida TRUE)))
   =>
   (assert (accion 
      (tipo aplicar-descuento)
      (razon "Incentivo por condiciones de venta restrictivas")
      (regla-aplicada "Regla 6")
      (prioridad 5)
   ))
   (printout t "REGLA 6 ACTIVADA: Aplicar descuento (garantia+ventas bajas O devolucion restringida)" crlf)
)

;;; REGLA 7: Si envio gratis Y solicita financiamiento Y margen NO alto, entonces aumentar precio
(defrule regla-7-envio-financiamiento-margen-no-alto
   (condiciones (envio-gratis TRUE) (solicita-financiamiento TRUE) (margen-alto FALSE))
   =>
   (assert (accion 
      (tipo aumentar-precio)
      (razon "Compensar costos de envio y financiamiento")
      (regla-aplicada "Regla 7")
      (prioridad 6)
   ))
   (printout t "REGLA 7 ACTIVADA: Aumentar precio (envio gratis + financiamiento + margen no alto)" crlf)
)

;;; REGLA 8: Disminuir precio si (ventas bajas Y inventario NO bajo) Y tiempo restock NO largo
(defrule regla-8-ventas-bajas-inventario-ok-restock-ok
   (condiciones (ventas-bajas TRUE) (inventario-bajo FALSE) (tiempo-restock-largo FALSE))
   =>
   (assert (accion 
      (tipo disminuir-precio)
      (razon "Liquidar inventario con ventas lentas")
      (regla-aplicada "Regla 8")
      (prioridad 6)
   ))
   (printout t "REGLA 8 ACTIVADA: Disminuir precio (ventas bajas + inventario suficiente)" crlf)
)

;;; REGLA 9: Si demanda alta PERO ventas NO altas Y NO garantia extendida, entonces aplicar descuento
(defrule regla-9-demanda-alta-ventas-no-altas-sin-garantia
   (condiciones (demanda-alta TRUE) (ventas-altas FALSE) (garantia-extendida FALSE))
   =>
   (assert (accion 
      (tipo aplicar-descuento)
      (razon "Alta demanda sin conversion - impulsar ventas")
      (regla-aplicada "Regla 9")
      (prioridad 7)
   ))
   (printout t "REGLA 9 ACTIVADA: Aplicar descuento (demanda alta pero sin ventas)" crlf)
)

;;; REGLA 10: Si inventario bajo Y (demanda alta O ventas altas), entonces NO aplicar descuento
(defrule regla-10-inventario-bajo-actividad-alta
   (condiciones (inventario-bajo TRUE))
   (or (condiciones (demanda-alta TRUE))
       (condiciones (ventas-altas TRUE)))
   =>
   (assert (accion 
      (tipo no-aplicar-descuento)
      (razon "Inventario limitado con alta demanda")
      (regla-aplicada "Regla 10")
      (prioridad 9)
   ))
   (printout t "REGLA 10 ACTIVADA: NO aplicar descuento (inventario bajo + actividad alta)" crlf)
)

;;; REGLA 11: Disminuir precio si devolucion restringida Y NO garantia extendida Y ventas bajas
(defrule regla-11-devolucion-restringida-sin-garantia-ventas-bajas
   (condiciones (devolucion-restringida TRUE) (garantia-extendida FALSE) (ventas-bajas TRUE))
   =>
   (assert (accion 
      (tipo disminuir-precio)
      (razon "Compensar condiciones poco atractivas")
      (regla-aplicada "Regla 11")
      (prioridad 5)
   ))
   (printout t "REGLA 11 ACTIVADA: Disminuir precio (devolucion restringida + sin garantia)" crlf)
)

;;; ============================================================
;;; REGLA DE RESOLUCION DE CONFLICTOS
;;; ============================================================

(defrule resolver-conflictos
   ?mejor <- (accion (prioridad ?p1))
   (not (accion (prioridad ?p2&:(> ?p2 ?p1))))
   =>
   (printout t crlf "=======================================" crlf)
   (printout t "DECISION FINAL (Mayor prioridad):" crlf)
   (printout t "Accion: " (fact-slot-value ?mejor tipo) crlf)
   (printout t "Razon: " (fact-slot-value ?mejor razon) crlf)
   (printout t "Regla: " (fact-slot-value ?mejor regla-aplicada) crlf)
   (printout t "Prioridad: " (fact-slot-value ?mejor prioridad) crlf)
   (printout t "=======================================" crlf crlf)
)