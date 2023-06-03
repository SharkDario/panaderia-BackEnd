
        nuevoStock = stockActual + cantidad

        stockDatos = (nuevoStock, idMateriaPrima)
        stockAtributos = "stockMateriaPrima = %s"
        bd.actualizar(cone, stockDatos, stockAtributos, "materiaprima", "idMateriaPrim