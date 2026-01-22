(deftemplate Trenes
    (slot id)
    (slot carga (allowed-values pasajeros mercancias peligrosa))
    (slot velocidad)
    (slot actual (Type INTEGER))
    (slot Estado (allowed-values Parado En_Marcha Frenando Emergencia)(default Parado))
    (slot Peticion (allowed-values Ninguna Acelerar Cambio_Tramo Parada_Solicitada))
)

(deftemplate Tramo
    (slot id (Type INTEGER))
    (slot semaforo (allowed-values Verde Rojo Ambar))
    (slot velmax (Type INTEGER))
    (slot Obstaculo (allowed-values Detectado Limpio))
)

(deftemplate Maquinista
    (slot id_tren)
    (slot Fatiga (Type INTEGER))
    (slot Estado_Con (allowed-values Atento Distraido Incapacitado) (default Atento))
)

(deffunction minutos (?velocidad ?distancia)
    (* 60 (/ ?distancia ?velocidad))
)

(defrule Autorizacion 
    ?tren <- (Trenes (actual ?tramo) (Estado En_Marcha) (Peticion Cambio_Tramo) (velocidad ?vel))
    ?destino <-(Tramo (id ?id_destino) (semaforo Verde) (Obstaculo Limpio) (velmax ?velomax))
    (test (<= ?vel ?velomax))
    (test (= ?id_destino (+ ?tramo 1)))
    =>
    (modify ?tren (actual ?id_destino) (Peticion Ninguna)) 
    (printout t "hora estimada de llegada " (minutos ?vel 50) crlf)
)

(defrule Frenada
    (declare (salience 100))
    ?tren <- (Trenes (actual ?tram) (id ?id))
    ?tramo <- (Tramo (id ?tram) (Obstaculo Detectado))
    =>
    (modify ?tren (Estado Emergencia) (velocidad 0))
    (printout t "Illo alerta" crlf)
)

(defrule Frenada2
    (declare (salience 100))
    ?tren <- (Trenes (id ?id))
    ?maquina <- (Maquinista (id_tren ?id) (Fatiga ?fa))
    (test (< 80 ?fa))
    =>
    (modify ?tren (Estado Emergencia) (velocidad 0))
    (printout t "Illo alerta" crlf)
)

(defrule ajuste 
    ?tren <- (Trenes (actual ?id) (Peticion Acelerar) (velocidad ?vel))
    ?Tramo <- (Tramo (id ?id) (Obstaculo Limpio) (velmax ?maxi))
    (test (<= ?vel (- ?maxi 20 )))
    =>
    (modify ?tren  (velocidad (+ ?vel 20)))
)