(defglobal ?*intentos* = 3)
(defglobal ?*dinerolimite* = 1000)
(defglobal ?*annio* = 2027)




(deftemplate Usuario
    (slot DNI)
    (slot Pin)  ; Pin que pone el usuario(hay que compararlo con el pin de la tarjeta)
    (slot Dinerob (default 0)) ; Dinero que quiere sacar el usuario
    )

(deftemplate Tarjeta
    (slot Pin)
    (slot Nintentos (default 0))
    (slot Limite (default dinerolimite))
    (slot Expiracion (default annio))
    (slot Validada (allowed-values Si No)(default No))
)

(deftemplate Cuenta
    (slot DNI)
    (slot Saldo)
    (slot estado (allowed-values enPantalla dineroEntregado Inicial SuperaLimite SinSaldo) default(Inicial))
)

(defrule Supera_Intentos
    (declare (salience 10))
    ?t <-Tarjeta(DNI ?dni)(Pin ?pin2)(Nintentos ?n)(Validada No) 
    test (>= ?n *?intentos*)
    =>
    printout "Tarjeta bloqueada"
    (retract ?t)
)

(defrule Pin_invalido
    (declare (salience5))
    ?u <- Usuario(DNI ?dni)(Pin ?pin1)
    ?t <- Tarjeta(DNI ?dni)(Pin ?pin2)(Nintentos ?n)(Validada No)
    test(neq pin1 pin2)
    =>
    (bind ?nuevo (+ ?n 1))
    (modify ?t (Nintentos ?nuevo))
)