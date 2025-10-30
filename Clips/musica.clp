(deftemplate usuario
    (slot nombre)
    (slot id (type INTEGER))
    (slot estadoanimo (allowed-values Normal Ejercicio Concentracion Calma Fiesta))
    (multislot preferencia); Mas de un estilo de musica
);usuario
(deftemplate cancion
    (slot titulo)
    (multislot artista)
    (slot genero)
    (slot bpm)
);cancion