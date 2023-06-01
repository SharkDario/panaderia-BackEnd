import mysql.connector
# clase estatica
from funciones import funciones as f  # nSToCad


class baseDeDatos():
    @staticmethod
    def abrir():
        conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd="",
                                           database="panaderia")
        return conexion

    @staticmethod
    def alta(cone, dDatos, tabla, nombreA, nA):
        # dDatos = la tupla con todas los datos de los atributos
        # nombreA es la cadena de los nombres de los atributos,
        # nA es la cantidad de atributos, para la cadena de %s
        cursor = cone.cursor()
        sql = f"insert into {tabla}({nombreA}) values ({f.nSToCad(nA)})"
        cursor.execute(sql, dDatos)
        cone.commit()
        cone.close()

    @staticmethod
    def consulta(cone, dDatos, cadenaT, tabla, atributoS):
        # atributoS el atributo en especifico o atributos que se quieren conseguir en formato cadena
        # Por ejemplo: idUsuario  ;  idUsuario, CUIL_CUIT
        # dDatos = tupla con los datos necesarios - en el caso de usuario es solo DNI
        # sacar longitud de la tupla
        cursor = cone.cursor()
        # cadenaT = ("", "")
        if (len(cadenaT) == 1):  # cadenaT - los nombres de atributos (DNI o NFactura and tipoFactura) ; tabla - usuarios ;
            sql = f"select {atributoS} from {tabla} where {cadenaT[0]}=%s"
        else:
            sql = f"select {atributoS} from {tabla} where {cadenaT[0]}=%s AND {cadenaT[1]}=%s"
        cursor.execute(sql, dDatos)
        consulta = cursor.fetchall()
        cone.close()
        return consulta

    @staticmethod
    def recuperarTodos(cone, tabla, nombreA):
        cursor = cone.cursor()
        sql = f"select {nombreA} from {tabla}"
        cursor.execute(sql)
        consulta = cursor.fetchall()
        cone.close()
        return consulta

    @staticmethod
    def recuperarTodosEspecifico(cone, tabla, nombreA, atribN, atriV):
        cursor = cone.cursor()
        sql = f"select {nombreA} from {tabla} where {atribN}=%s"
        cursor.execute(sql, atriV)
        consulta = cursor.fetchall()
        cone.close()
        return consulta

    @staticmethod
    def modificarAtrib(cone, dDatos, tabla, nombreA, nombreId):
        # dDatos = (valorA, valorId)
        # dDatos = (dDatos[0], tuple(dDatos[1]))
        cursor = cone.cursor()
        # print(dDatos)
        sql = f"UPDATE {tabla} SET {nombreA} = %s WHERE {nombreId} = %s;"
        cursor.execute(sql, dDatos)
        cone.commit()
        cone.close()

    @staticmethod
    def baja(cone, dDatos, cadenaT, tabla):
        # dDatos = tupla con los datos necesarios - en el caso de usuario es solo DNI
        # sacar longitud de la tupla
        cursor = cone.cursor()
        # cadenaT = ("", "")
        if (len(cadenaT) == 1):  # cadenaT - tupla de los nombres de atributos (DNI o NFactura and tipoFactura) ; tabla - usuarios ;
            sql = f"DELETE FROM {tabla} WHERE {cadenaT[0]}=%s"
        else:
            sql = f"DELETE FROM {tabla} WHERE {cadenaT[0]}=%s AND {cadenaT[1]}=%s"
        cursor.execute(sql, dDatos)
        cone.commit()
        cone.close()

    @staticmethod
    def join(cone, dDatos, tablas, ides):
        #tuplaDni = (DNI, )
        #idUsuario = Empleado.obtenerId(tuplaDni)
        cursor = cone.cursor()
        #dDatos = (idTipoEmpleado, idUsuario, 2)
        #tablas[0] - usuarios
        #tablas[1] - tipoUsuario
        #ides[0] - idTipoUsuario
        #ides[1] - idTipoEmpleado
        #ides[2] - idUsuario
        sql=f"UPDATE {tablas[0]} AS u JOIN {tablas[1]} AS tu ON u.{ides[0]} = tu.{ides[0]} SET tu.{ides[1]} = %s WHERE u.{ides[2]} = %s AND tu.{ides[0]}=%s;"
        cursor.execute(sql, dDatos)
        cone.commit()
        cone.close()

    @staticmethod
    def consultaJoin(cone, dni):
        cursor = cone.cursor()
        sql=f"SELECT tipoempleado.descripcionTipoEmpleado, tipoempleado.idTipoEmpleado FROM usuarios INNER JOIN tipousuario ON usuarios.idTipoUsuario = tipousuario.idTipoUsuario INNER JOIN tipoempleado ON tipousuario.idTipoEmpleado = tipoempleado.idTipoEmpleado WHERE usuarios.DNI = %s"
        cursor.execute(sql, dni)
        consulta = cursor.fetchall()
        cone.commit()
        cone.close()
        return consulta

    @staticmethod
    def joinContratacion(cone):
        cursor = cone.cursor()
        sql="SELECT * FROM usuarios INNER JOIN contratacion ON usuarios.idUsuario = contratacion.idUsuarioEmpleado;"
        cursor.execute(sql)
        sql2="SELECT * FROM usuarios INNER JOIN contratacion ON usuarios.idUsuario = contratacion.idUsuarioAdmin;"
        cursor.execute(sql2)
        cone.commit()
        cone.close()

    """
    SELECT usuarios.idUsuario, tipoempleado.idTipoEmpleado
    FROM usuarios
    INNER JOIN tipousuario ON usuarios.idTipoUsuario = tipousuario.idTipoUsuario
    INNER JOIN tipoempleado ON tipousuario.idTipoEmpleado = tipoempleado.idTipoEmpleado
    WHERE usuarios.idUsuario = 'nombre_de_usuario'
    """

    #@staticmethod
    #def join(cone, tuplaTablas, tuplaId, dDatos):
    #    cursor = cone.cursor()
        #tuplaTablas = ("tipoEmpleado", "tipoUsuario", "Usuario")
        #tuplaId = ("idTipoEmpleado","idTipoUsuario","idUsuario")
        #dDatos = (valorAtrib, valorId)
    #    sql="UPDATE usuarios AS u JOIN tipoUsuario AS tu ON u.idTipoUsuario = tu.idTipoUsuario SET tu.idTipoEmpleado = %s WHERE u.idUsuario = %s AND tu.idTipoUsuario = 2;"
    #    cursor.execute(sql, dDatos)
    #    cone.commit()
    #    cone.close()

        #SELECT te.atributo
        #FROM usuario u
        #JOIN tipousuario tu ON u.idTipoUsuario = tu.id
        #JOIN tipoempleado te ON tu.idTipoEmpleado = te.id
        #WHERE u.id = ID_USUARIO;

        #UPDATE tipoempleado te
        #JOIN tipousuario tu ON te.id = tu.idTipoEmpleado
        #JOIN usuario u ON tu.id = u.idTipoUsuario
        #SET te.atributo = NUEVO_VALOR
        #WHERE u.id = ID_USUARIO;


    # def fetch_all_users(self):
    #    self.cursor.execute("SELECT * FROM users")
    #    result = self.cursor.fetchall()
    #    return result

    # def insert_user(self, dni, apellido, username):
    #    sql = "INSERT INTO users (dni, apellido, username) VALUES (%s, %s, %s)"
    #    val = (dni, apellido, username)
    #    self.cursor.execute(sql, val)
    #    self.connection.commit()
