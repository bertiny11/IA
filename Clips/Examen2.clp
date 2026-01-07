(deftemplate Productos
    (slot idP)
    (slot nombre)
    (slot Npasillo (type INTEGER))
    (slot stock (type INTEGER))
    (slot precio(type FLOAT))
)

(deftemplate Pedidos
    (slot idC)
    (slot producto)
    (slot unidades-Compra)
)

(deftemplate Carrito
    (slot cliente)
    (slot N_AC (default 0))
    (slot importe (default 0))
    (slot Ubipasillo (default 1))
)

(deffunction sumaTotal (?precio ?importeAct ?cantidad)
    (+ importeAct (* ?precio ?cantidad))
    ;sumar el importe 
)

(defrule Asignar
    ?peticion <- (nuevo-cliente ?id)
    =>
    assert(Carrito (cliente ?id))

    (retract ?peticion)
)

(defrule Comprar
    (declare (salience 20))
    ?carro <- (Carrito (cliente ?idcl) (N_AC ?nproducto) (importe ?dinero) (Ubipasillo ?donde))
    ?pedido <- (Pedidos (idC ?idcl) (producto ?id) (unidades-Compra ?cant))
    ?producto <- (Productos (idP ?id) (Npasillo ?donde) (stock ?stock&:(>= ?stock ?cant)) (precio ?precio) (nombre ?n))
    =>
    (retract ?pedido)
    (bind ?total (sumaTotal ?precio ?cant ?dinero))
    (modify ?carro (importe ?total) (N_AC (+ ?nproducto ?cant)))
    (modify ?producto (stock (- ?stock ?cant))) 
)

(defrule Existencias
    (declare(salience 20))
    ?pedido <- (Pedidos (idC ?idcl) (producto ?id) (unidades-Compra ?cant))
    ?producto <- (Productos (idP ?id) (Npasillo ?donde) (stock ?stock&:(< ?stock ?cant)) (precio ?precio) (nombre ?n))
    =>
    (retract ?pedido)
    (printout t "--- ALERTA: Stock insuficiente de " ?n " (Stock: " ?stock "). Pedido cancelado. ---" crlf)
)

(defrule Mover-Carro
    (declare (salience 0)) ; PRIORIDAD BAJA
    
    ?carro <- (Carrito (cliente ?idC) (Ubipasillo ?p))
    ; Solo se mueve si quedan pedidos pendientes para este cliente
    (exists (Pedidos (idC ?idC)))
    =>
    (if (< ?p 12) 
        then 
            (bind ?nuevo-pasillo (+ ?p 1))
        else 
            (bind ?nuevo-pasillo 1)
    )
    
    (modify ?carro (Ubipasillo ?nuevo-pasillo))
    (printout t "--- Moviendo carro al pasillo " ?nuevo-pasillo " ---" crlf)
)