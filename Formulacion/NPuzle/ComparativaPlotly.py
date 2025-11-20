# Importe las funciones de búsqueda Voraz y A*. En nuestro caso, en BusquedaHeu
# se permiten ambas junto con las 2 heurísticas: MalColocadas (0) y Manhattan (1)

# Adáptelo a su implementación.
from Busqueda_Alum import Estrella
from Busqueda_Alum import Voraz

# Para poder ejecutar el código de ejemplo, necesitará instalar las bibliotecas de
# pandas y plotly La primera permite trabajar con los datos como una tabla y la segunda
# genera gráficas interactivas. Recuerde, para instalarlas basta con:
#   pip install pandas plotly
import pandas as pd
import plotly.express as px


tabla = []

# Adapte esta llamada a la función de búsqueda que use en su implementación.
#   Ejs: Greedy("MalColocadas") o AStar_Manhattan() en lugar de BusquedaHeu("A*", 0)
# Lo importante es que la función es cuestión devuelva los 4 indicadores que se enumeran en el guión

generados, visitados, coste, maxlon = Estrella("A*", 0)
# Se añaden a la lista los resultados obtenidos.
tabla.append([coste, generados, visitados, maxlon, "Busqueda A*", "Mal Colocadas"])

generados, visitados, coste, maxlon = Estrella("A*", 1)
tabla.append([coste, generados, visitados, maxlon, "Busqueda A*", "Manhattan"])

generados, visitados, coste, maxlon = Voraz("Voraz", 0)
tabla.append([coste, generados, visitados, maxlon, "Busqueda Voraz", "Mal Colocadas"])

generados, visitados, coste, maxlon = Voraz("Voraz", 1)
tabla.append([coste, generados, visitados, maxlon, "Busqueda Voraz", "Manhattan"])

# Se genera la tabla y se le da nombre a las columnas
tabla = pd.DataFrame(
    tabla,
    columns=[
        "Coste",
        "Generados",
        "Visitados",
        "Maxima Longitud",
        "Método",
        "Heuristica",
    ],
)

# A la columna Método se le añade el tipo de heurística
tabla.loc[:, "Método"] = tabla["Método"] + " - " + tabla["Heuristica"]

# Se extiende la tabla para que sea compatible con Plotly y pueda ser interactivo.
tabla = pd.melt(
    tabla,
    id_vars="Método",
    value_vars=["Coste", "Generados", "Visitados", "Maxima Longitud"],
    value_name="Valor",
)

# Se genera una gráfica de barras horizontales y se aumenta el tamaño de la fuente.
# Se agrupan en función de 'variable' que se corresponde con los 4 indicadores mencionados anteriormente
fig = px.bar(
    tabla, x="Valor", y="Método", color="variable", orientation="h", barmode="group"
)
fig.update_layout(font=dict(size=18), hoverlabel=dict(font=dict(size=18)))
fig.show()
