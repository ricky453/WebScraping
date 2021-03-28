ejecucion=True
while ejecucion==True:
    try:
        import ObtenerDatos
        ejecucion=False
    except Exception as e:
        ejecucion=True