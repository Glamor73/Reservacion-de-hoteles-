from graphviz import Digraph  # type: ignore # ¡IMPORTANTE! No olvides esta línea

sequence_diagram = Digraph(format="png")
sequence_diagram.attr(rankdir="LR", splines="ortho", fontsize="12")

# Configuración general de nodos
sequence_diagram.attr("node", shape="rect", fontname="Helvetica", style="filled", fillcolor="lightgrey")

# Participantes
sequence_diagram.node("Jugador", "Jugador")
sequence_diagram.node("Sistema", "Sistema")
sequence_diagram.node("Mundo", "Mundo")
sequence_diagram.node("Ranking", "Ranking")

# Mensajes
sequence_diagram.edge("Jugador", "Sistema", label="Crear Partida", arrowhead="vee")
sequence_diagram.edge("Sistema", "Mundo", label="Verificar Equipos", arrowhead="vee")
sequence_diagram.edge("Sistema", "Mundo", label="Crear Mapa (Grafo)", arrowhead="vee")
sequence_diagram.edge("Sistema", "Jugador", label="Seleccionar Ubicaciones", arrowhead="vee")
sequence_diagram.edge("Sistema", "Ranking", label="Registrar Resultado", arrowhead="vee")
sequence_diagram.edge("Ranking", "Sistema", label="Actualizar Ranking", arrowhead="vee")

# Generar la imagen
output_sequence_path = "diagrama_secuencias"  # Usa una ruta relativa para que no falle
sequence_diagram.render(output_sequence_path, format="png", cleanup=True)
