(deftemplate Aeronave
    (slot id)
    (slot compania)
    (slot aerodromo_origen)
    (slot aerodromo_destino)
    (slot velocidad)
    (slot Peticion (allowed-values Ninguna Despegue Aterrizaje Emergencia Rumbo))
    (slot Estado (allowed-values enTierra Ascenso Crucero Descenso) (default enTierra))
)

(deftemplate Aerodromo
    (slot id)
    (slot ciudad_donde_ubica)
    (slot estado_radar (allowed-values ON OFF))
    (slot radio_Visibilidad(type INTEGER))
    (slot velocidad_Viento(type INTEGER))
)

(deftemplate Piloto 
    (slot id)
    (slot aeronave)
    (slot vuelo)
    (slot estado (allowed-values OK SOS Ejecutando Stand-by)(default Stand-by))
)

(deftemplate Vuelo
    (slot id_origen)
    (slot id_destino)
    (slot distancia)
    (slot velocidad_despegue (default 240))
    (slot velocidad_media_crucero (default 700))
)

(deftemplate Meteorologia
    (slot id_aerodromo)
    (slot tiempo (allowed-values Lluvia Niebla Nieve VientoHuracanado Despejado))
    (slot estado (allowed-values Si No))
)

(deffacts hechos_iniciales
    "Hechos iniciales para probar la regla Alerta_Meteorologia"

    ;; --- Aeródromo de origen con mal tiempo ---
    (Aerodromo
        (id XRY)
        (ciudad_donde_ubica Jerez)
        (estado_radar ON)
        (radio_Visibilidad 5)
        (velocidad_Viento 80)
    )

    (Meteorologia
        (id_aerodromo XRY)
        (tiempo Niebla)
        (estado Si)   ;; Condiciones adversas -> dispara la alerta
    )

    ;; --- Aeronave que quiere despegar desde ese aeródromo ---
    (Aeronave
        (id FX001)
        (compania IBERIA)
        (aerodromo_origen XRY)
        (aerodromo_destino MAD)
        (velocidad 0)
        (Peticion Despegue)
        (Estado enTierra)
    )

    ;; --- Piloto asignado a esa aeronave ---
    (Piloto
        (id P001)
        (aeronave FX001)
        (vuelo VUELO1)
        (estado Stand-by)
    )

    ;; --- Vuelo (opcional, no afecta a la regla) ---
    (Vuelo
        (id_origen XRY)
        (id_destino MAD)
        (distancia 600)
    )
)


(defrule Alerta_Meteorologia
    (declare (salience 10))
    ?ae <- (Aeronave (id ?ida)(compania ?comp)(Peticion Despegue)(aerodromo_origen ?ad))
    (Meteorologia (id_aerodromo ?ad)(estado Si))
    ?p <- (Piloto (aeronave ?ida))
    =>
    (modify ?ae (Peticion Ninguna))
    (modify ?p (estado Stand-by))

    (printout t "Alerta: Despegue CANCELADO por condiciones climáticas adversas" crlf)
    (printout t "La aeronave " ?ida " de la compañía "?comp " va a cancelar su vuelo " crlf)
)

(defrule PilotoAsociado 
    (declare (salience 5))
    (Aeronave(id ?ida) (compania ?comp) (aerodromo_origen ?ao)(aerodromo_destino ?ad)(Peticion Despegue))
    (Vuelo (id_origen ?ad))
    (exists (Piloto(aeronave ?ida) (estado OK)))
    =>
    (printout t "La aeronave  " ?ida " de la compañía " ?comp " tiene PILOTO asignado para poder realizar el vuelo desde el aeródromo "?ao 
    " con el destino " ?ad"para realizar in vuelo de los registrados en el aeródromo de origen y la aeronave se encuentra en petición de despegue" crlf)
)