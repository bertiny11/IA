(deftemplate coche
(slot modelo (type INTEGER)(allowed-values 1 2 3 4 5))
(slot precio (type INTEGER))
(slot maletero (allowed-values pequeno mediano grande))
(slot caballos (type INTEGER))
(slot ABS (allowed-values Si No))
(slot consumo (type FLOAT))
);coche

(deftemplate formulario
(slot precio(type INTEGER)(default 13000))
(slot maletero (allowed-values pequeno mediano grande) (default grande))
(slot caballos (type INTEGER) (default 80))
(slot ABS (allowed-values Si No) (default Si))
(slot consumo (type FLOAT) (default 8.0))
)


(deffacts iniciales
(coche      (modelo 1)
            (precio 12000)
            (maletero pequeno)
            (caballos 65)
            (ABS No)
            (consumo 4.7))

(coche      (modelo 2)
            (precio 12500)
            (maletero pequeno)
            (caballos 80)
            (ABS Si)
            (consumo 4.9))


(coche      (modelo 3)
            (precio 13000)
            (maletero mediano)
            (caballos 100)
            (ABS Si)
            (consumo 7.8))


(coche      (modelo 4)
            (precio 14000)
            (maletero grande)
            (caballos 125)
            (ABS Si)
            (consumo 6.0))


(coche      (modelo 5)
            (precio 15000)
            (maletero pequeno)
            (caballos 147)
            (ABS Si)
            (consumo 8.5))

)

(defrule recomendar
(coche (modelo ?model) (precio ?precio) (maletero ?maletero) (caballos ?caballos) (ABS ?ABS) (consumo ?consumo))
(formulario (precio ?precio2) (maletero ?maletero2) (caballos ?caballos2) (ABS ?ABS2) (consumo ?consumo2))
(test (eq ?ABS ?ABS2))
(test (eq ?maletero ?maletero2))
(test (<= ?precio ?precio2))
(test (>= ?caballos ?caballos2))
(test (<= ?consumo ?consumo2))
=>
(printout t "El modelo recomendado es el " ?model crlf)
)
