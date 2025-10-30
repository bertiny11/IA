(deftemplate comecocos (slot PosX(default 0))(slot PosY(default 0))(slot contador (default 0))(slot vida (default 10)))

(deftemplate fantasma (slot PosX)(slot PosY))

(deftemplate fruta (slot PosX) (slot PosY))


(defrule Comer
    ?co <-(comecocos(PosX ?x) (PosY ?y) (contador ?c))
    ?fr <- (fruta(PosX ?x)  (PosY ?y))
    => (modify ?co (contador(+ ?c 1)))
        (retract ?fr)
)

(deffacts iniciales 
    (comecocos)
    (fantasma (PosX 3) (PosY 4))

)

(defrule Ganar
    (declare (salience 10))
    (comecocos (contador ?c))
    (test (>= ?c 10))
)