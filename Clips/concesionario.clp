(deftemplate coche
    (slot modelo)
    (slot Precio )
    (slot tamano )
    (slot Caballo)
    (slot ABS) 
    (slot Consumo)
)

;deftemplate solo define la estructura del hecho, no crea hechos concretos.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(deffacts base-coches
;   (coche (modelo modelo1) (precio 12000) (tamano pequeño) (caballos 65) (abs no) (consumo 4.7))
;   (coche (modelo modelo2) (precio 12500) (tamano pequeño) (caballos 80) (abs si) (consumo 4.9))
;   (coche (modelo modelo3) (precio 13000) (tamano mediano) (caballos 100) (abs si) (consumo 7.8))
;   (coche (modelo modelo4) (precio 14000) (tamano grande) (caballos 125) (abs si) (consumo 6.0))
;   (coche (modelo modelo5) (precio 15000) (tamano pequeño) (caballos 147) (abs si) (consumo 8.5))
;)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(deffacts iniciales
    ()
)