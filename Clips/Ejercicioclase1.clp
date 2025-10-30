(deffacts iniciales
    (fiebre (alta))
    (color (organismo, oscuro))
    (color (garganta, rojo))
    (planodivision(unico))
    (morfologia(organismo, coccus))
)

(defrule R1
    Inflamacion(garganta)
    Presencia(estreptococo)
    fiebre(alta) => assert (infeccion(garganta))
)

(defrule R2 
color(garganta, rojo) => assert (Inflamacion (garganta)))

(defrule R3
 morfologia(organismo, coccus) crecimiento(organismo, en_racimo) => assert (presencia(estreptococo)))

(defrule R4
(morfología(organismo, coccus)) (organismo, en_racimo) => assert (presencia(estafilocco)))

