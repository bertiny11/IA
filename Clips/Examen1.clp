; --- 1. TEMPLATES ---

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
    (slot radio_Visibilidad (type INTEGER))
    (slot velocidad_Viento (type INTEGER))
)

(deftemplate Piloto 
    (slot id)
    (slot aeronave)
    (slot vuelo)
    (slot estado (allowed-values OK SOS Ejecutando Stand-by) (default Stand-by))
)

(deftemplate Vuelo
    (slot id_origen)
    (slot id_destino)
    (slot distancia)
    (slot velocidad_despegue (default 240))
    (slot velocidad_media_crucero (default 700))
)

; --- 2. FUNCIONES (Deben ir antes de las reglas) ---

(deffunction calcular-horas (?distancia ?velocidad)
    (div ?distancia ?velocidad)
)

(deffunction calcular-minutos (?distancia ?velocidad)
    (div (* (mod ?distancia ?velocidad) 60) ?velocidad)
)

; --- 3. REGLAS ---

(defrule despegar
    ?Desp <- (Aeronave (id ?idA) (aerodromo_origen ?id-origen) (aerodromo_destino ?id-dest) (velocidad ?veloinicial) (Peticion Despegue) (Estado enTierra))
    ?piloto <- (Piloto (aeronave ?idA) (estado OK))
    ?Aero <- (Aerodromo (id ?id-origen) (estado_radar ON) (radio_Visibilidad ?vis&:(> ?vis 5)) (velocidad_Viento ?velo&:(< ?velo 75)))
    ?vuelo <- (Vuelo (id_origen ?id-origen) (id_destino ?id-dest) (velocidad_despegue ?vel-desp))   
    =>
    (modify ?piloto (estado Ejecutando))
    (modify ?Desp (Estado Ascenso) (velocidad ?vel-desp) (Peticion Ninguna))        
    (printout t "La aeronave " ?idA " despega desde " ?id-origen " hacia " ?id-dest crlf)
)

(defrule excepcion
    ?av <- (Aeronave (id ?idA) (aerodromo_origen ?origen) (aerodromo_destino ?dest) (Peticion Despegue))
    (Vuelo (id_origen ?origen) (id_destino ?dest))      
    (not (Piloto (aeronave ?idA)))                      
    =>
    (modify ?av (Peticion Ninguna))
    (printout t "ALERTA: La aeronave " ?idA " intenta despegar sin piloto asignado." crlf)
)

(defrule Crucero
    ?aerona <- (Aeronave (id ?idA) (aerodromo_origen ?id-origen) (aerodromo_destino ?id-dest) (Estado Ascenso))
    
    ?vuel <- (Vuelo (id_origen ?id-origen) (id_destino ?id-dest) (velocidad_media_crucero ?vel-crucero) (distancia ?dist))
    
    ?piloto <- (Piloto (aeronave ?idA) (estado Ejecutando))
    =>
    ; Acciones de cambio de estado
    (modify ?piloto (estado Stand-by))
    (modify ?aerona (Estado Crucero) (velocidad ?vel-crucero))

    ; Cálculos
    (bind ?horas (calcular-horas ?dist ?vel-crucero))
    (bind ?minutos (calcular-minutos ?dist ?vel-crucero))
    
    ; Mensaje obligatorio del ejercicio
    (printout t "--- MENSAJE A PASAJEROS ---" crlf)
    (printout t "El despegue ha sido correcto. Entrando en velocidad de crucero." crlf)
    (printout t "Tiempo estimado de vuelo: " ?horas " horas y " ?minutos " minutos." crlf)
    (printout t "---------------------------" crlf)
)