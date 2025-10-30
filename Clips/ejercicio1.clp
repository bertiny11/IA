(deffacts iniciales

(Robi Animal)
(Animal Robi) ;Se puede utilizar las dos
(Animal susi)
(Tiene pelo Robi)
(Tiene susi plumas)

)

;Los templates se aconsejan cunado haya mucha informacion

(defrule R1
    (caracteristica(nombre ?x)(atributo pelo)(calor si))
    =>
    (assert(mamifero ?x)))

(defrule R2
    (caracteristica(nomber ?x)(atributo da-leche)(valor si))
    =>
    (assert(mamifero ?x)))

(defrule R3
    (caracteristica(nomber ?x)(atributo plumas)(valor si))
    =>
    (assert(ave ?x)))

(defrule R4
    (caracteristica(nomber ?x)(atributo vuela)(valor si))
    (caracteristica(nomber ?x)(atributo pone-huevos)(valor si))
    =>
    (assert(ave ?x)))

(defrule R7
    (mamifero ?x)
    (caracteristica(nomber ?x)(atributo pezuñas)(valor si))
    =>
    (assert(ungulado ?x)))

(defrule R9
    (mamifero ?x) (carnivoro ?x)
    (caracteristica(nomber ?x)(atributo color)(valor leonardo))
    (caracteristica(nomber ?x)(atributo manchas)(valor oscuras))
    =>
    (assert(ungulado ?x)))

    ; Primero hacemos un clear(limpia todo), cargo las reglas templates, deffacts, luegp reset para incluir los hechos iniciales en la memoria y por último un run 