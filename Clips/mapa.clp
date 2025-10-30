(deffacts iniciales
    (ubicacion A Norte D)
    (ubicacion A oeste B)
    (ubicacion B Norte E)
    (ubicacion B oeste C)
    (ubicacion D Norte G)
    (ubicacion D oeste E)
    (ubicacion E Norte H)
    (ubicacion E oeste F)
)

(defrule sur
    (ubicacion ?x Norte ?y) => (assert(ubicacion ?y sur ?x))
)

(defrule este
    (ubicacion ?x oeste ?y) => (assert(ubicacion ?y este ?x))
)

(defrule nortex2
    (ubicacion ?x Norte ?y)(ubicacion ?y Norte ?z) => (assert(ubicacion ?x Norte ?z))
)

;(defrule polivalente
;   (ubicacion ?x ?u ?y)(ubicacion ?y ?u ?z) => (assert(ubicacion ?x ?u ?z))
;)
(defrule oestex2
    (ubicacion ?x oeste ?y)(ubicacion ?y oeste ?z) => (assert(ubicacion ?x oeste ?z))
)

(defrule estex2
    (ubicacion ?x este ?y)(ubicacion ?y este ?z) => (assert(ubicacion ?x este ?z))
)

(defrule surx2
    (ubicacion ?x sur ?y)(ubicacion ?y sur ?z) => (assert(ubicacion ?x sur ?z))
)

(defrule noroeste
    (ubicacion ?x norte ?y)(ubicacion ?y oeste ?z) => (assert(ubicacion ?x noroeste ?z))
)

(defrule noreste
    (ubicacion ?x norte ?y)(ubicacion ?y este ?z) => (assert(ubicacion ?x noreste ?z))
)

(defrule suroeste
    (ubicacion ?x sur ?y)(ubicacion ?y oeste ?z) => (assert(ubicacion ?x suroeste ?z))
)

(defrule sureste
    (ubicacion ?x sur ?y)(ubicacion ?y este ?z) => (assert(ubicacion ?x sureste ?z))
)

(defrule noroestex2
    (ubicacion ?x norte ?y)(ubicacion ?y oeste ?z)(ubicacion ?z norte ?j)(ubicacion ?j oeste ?k) => (assert(ubicacion ?x noroeste ?k))
)

(defrule norestex2
    (ubicacion ?x norte ?y)(ubicacion ?y este ?z)(ubicacion ?z norte ?j)(ubicacion ?j este ?k) => (assert(ubicacion ?x noreste ?k))
)

(defrule suroestex2
    (ubicacion ?x sur ?y)(ubicacion ?y oeste ?z)(ubicacion ?z norte ?j)(ubicacion ?j oeste ?k) => (assert(ubicacion ?x suroeste ?k))
)

(defrule surestex2
    (ubicacion ?x sur ?y)(ubicacion ?y este ?z)(ubicacion ?z norte ?j)(ubicacion ?j este ?k) => (assert(ubicacion ?x sureste ?k))
)

(defrule inicio
    ?f1 <-(situacion ?x ?y)
    (ubicacion ?x ?u ?y)
    =>
    (println ?x " esta al " ?u " de " ?y)
    (retract ?f1)
); inicio