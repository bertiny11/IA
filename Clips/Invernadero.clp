(deftemplate invernadero
    (slot Temperatura (TYPE INTEGER))
    (slot Humedad (TYPE INTEGER))
    (slot Ventana (allowed-values abiertas cerradas))
    (slot Riego (allowed-values encendido apagado))
)

(deffacts iniciales
    (invernadero(Temperatura 35)
                (Humedad 15)
                (Ventana cerradas)
                (Riego apagado))
)

(defrule bajar-temperatura
    ?f <- (invernadero (Temperatura ?tem) (Ventana cerradas))
    (test(> ?tem  30))
    =>
    (printout t "Que calor, abiendo ventana" crlf)
    (modify ?f (Ventana abiertas))
)

(defrule regar-plantas
    ?reg <- (invernadero (Humedad ?hu) (Riego apagado))
    (test(< ?hu 20))
    =>
    (printout t "Suelo seco, encenciendo riesgo" crlf)
    (modify ?reg (Riego encendido))
)

(defrule cerrar-por-lluvia
    (declare (salience 10))
    (lluvia SI)
    ?ventana <- (invernadero (Ventana abiertas))
    =>
    (modify ?ventana (Ventana cerradas))
)