from BuscarPeli import Buscar_Peli
from datetime import datetime

buscar_dept='San Salvador'
buscar_id_peli='getTicket_3176'
buscar_nombre_cine='Cinépolis Galerías'
buscar_tipo_doblaje='Tradicional - 2D DOB'
buscar_hora='18:30'
fecha=datetime.now()
fecha=fecha.date()
metodo= Buscar_Peli()
metodo.contarAsientos(buscar_id_peli, buscar_dept, buscar_nombre_cine, buscar_tipo_doblaje, fecha, buscar_hora)