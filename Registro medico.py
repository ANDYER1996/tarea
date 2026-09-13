from datetime import date, datetime


# ============================================================
# CLASE USUARIO SISTEMA
# ============================================================

class UsuarioSistema:

    def __init__(self, id_usuario, username, password_hash, rol):
        self.id_usuario = id_usuario
        self.username = username
        self.password_hash = password_hash
        self.rol = rol

    def autenticar_usuario(self, username, password_hash):

        return (
            self.username == username
            and self.password_hash == password_hash
        )

    def cerrar_sesion(self):

        print(
            f"Sesión cerrada para el usuario: "
            f"{self.username}"
        )


# ============================================================
# CLASE PERSONAL SALUD
# HEREDA DE USUARIO SISTEMA
# ============================================================

class PersonalSalud(UsuarioSistema):

    def __init__(
        self,
        id_usuario,
        username,
        password_hash,
        rol,
        id_personal,
        numero_colegiatura,
        especialidad
    ):

        # Llamar al constructor de UsuarioSistema
        super().__init__(
            id_usuario,
            username,
            password_hash,
            rol
        )

        self.id_personal = id_personal
        self.numero_colegiatura = numero_colegiatura
        self.especialidad = especialidad

        # Listas para almacenar pacientes y citas
        self.citas = []
        self.pacientes = []

    def programar_cita(self, paciente, fecha):

        # Crear una nueva cita
        numero_cita = len(self.citas) + 1

        cita = CitaMedica(
            f"CITA-{numero_cita}",
            fecha,
            "Consulta médica",
            "Programada",
            paciente
        )

        # Agregar la cita a la lista del personal
        self.citas.append(cita)

        # Agregar la cita al paciente
        paciente.agregar_cita(cita)

        # Agregar paciente a la lista si todavía no existe
        if paciente not in self.pacientes:
            self.pacientes.append(paciente)

        print("\nCita programada correctamente.")
        print(
            f"Paciente: "
            f"{paciente.nombres} {paciente.apellidos}"
        )
        print(f"Fecha: {fecha}")

    def registrar_atencion(self, cita):

        if cita is not None:

            print(
                f"Atención registrada para la cita: "
                f"{cita.id_cita}"
            )

        else:

            print("La cita no existe.")

    def generar_reporte_atenciones(self):

        print("\n====================================")
        print("       REPORTE DE ATENCIONES")
        print("====================================")

        if not self.citas:

            print("No existen citas registradas.")

            return

        for cita in self.citas:

            print(
                f"Cita: {cita.id_cita} | "
                f"Paciente: "
                f"{cita.paciente.nombres} "
                f"{cita.paciente.apellidos} | "
                f"Fecha: {cita.fecha_hora} | "
                f"Estado: {cita.estado}"
            )


# ============================================================
# CLASE PACIENTE
# ============================================================

class Paciente:

    def __init__(
        self,
        id_paciente,
        dni_encriptado,
        nombres,
        apellidos,
        fecha_nacimiento,
        telefono,
        consentimiento_ley29733
    ):

        self.id_paciente = id_paciente
        self.dni_encriptado = dni_encriptado
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.consentimiento_ley29733 = consentimiento_ley29733

        # Listas relacionadas con el paciente
        self.citas = []
        self.historiales = []

    def registrar_paciente(self):

        print(
            f"Paciente registrado: "
            f"{self.nombres} {self.apellidos}"
        )

    def actualizar_contacto(self, nuevo_telefono):

        self.telefono = nuevo_telefono

        print(
            f"Nuevo teléfono: {self.telefono}"
        )

        print(
            "Teléfono actualizado correctamente."
        )

    def anonimizar_datos_personales(self):

        self.nombres = "ANONIMIZADO"
        self.apellidos = "ANONIMIZADO"
        self.telefono = "ANONIMIZADO"

        print(
            "Datos personales anonimizados."
        )

    def agregar_cita(self, cita):

        self.citas.append(cita)

    def agregar_historial(self, historial):

        self.historiales.append(historial)

    def mostrar_datos(self):

        print("\n===== DATOS DEL PACIENTE =====")

        print(
            f"ID paciente: {self.id_paciente}"
        )

        print(
            f"Nombre: {self.nombres} "
            f"{self.apellidos}"
        )

        print(
            f"Fecha de nacimiento: "
            f"{self.fecha_nacimiento}"
        )

        print(
            f"Teléfono: {self.telefono}"
        )

        print(
            f"Consentimiento Ley 29733: "
            f"{self.consentimiento_ley29733}"
        )


# ============================================================
# CLASE CITA MEDICA
# ============================================================

class CitaMedica:

    def __init__(
        self,
        id_cita,
        fecha_hora,
        motivo,
        estado,
        paciente
    ):

        self.id_cita = id_cita
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.estado = estado
        self.paciente = paciente

    def confirmar_cita(self):

        self.estado = "Confirmada"

        print(
            f"Cita {self.id_cita} confirmada."
        )

    def cancelar_cita(self):

        self.estado = "Cancelada"

        print(
            f"Cita {self.id_cita} cancelada."
        )

    def reprogramar_cita(self, nueva_fecha):

        self.fecha_hora = nueva_fecha
        self.estado = "Reprogramada"

        print(
            f"Cita reprogramada para: "
            f"{nueva_fecha}"
        )

    def mostrar_cita(self):

        print("\n===== INFORMACIÓN DE CITA =====")

        print(
            f"ID cita: {self.id_cita}"
        )

        print(
            f"Paciente: "
            f"{self.paciente.nombres} "
            f"{self.paciente.apellidos}"
        )

        print(
            f"Fecha y hora: {self.fecha_hora}"
        )

        print(
            f"Motivo: {self.motivo}"
        )

        print(
            f"Estado: {self.estado}"
        )


# ============================================================
# CLASE HISTORIAL MEDICO
# ============================================================

class HistorialMedico:

    def __init__(
        self,
        diagnostico,
        medicacion,
        numero_cita,
        nombre_paciente
    ):

        self.diagnostico = diagnostico
        self.medicacion = medicacion
        self.numero_cita = numero_cita
        self.nombre_paciente = nombre_paciente

    def mostrar_historial(self):

        print("\n====================================")
        print("          HISTORIAL MÉDICO")
        print("====================================")

        print(
            f"Paciente: {self.nombre_paciente}"
        )

        print(
            f"Número de cita: {self.numero_cita}"
        )

        print(
            f"Diagnóstico: {self.diagnostico}"
        )

        print(
            f"Medicación: {self.medicacion}"
        )


# ============================================================
# CLASE INVENTARIO MEDICAMENTO
# ============================================================

class InventarioMedicamento:

    def __init__(
        self,
        id_medicamento,
        nombre_comercial,
        cantidad_stock,
        fecha_vencimiento
    ):

        self.id_medicamento = id_medicamento
        self.nombre_comercial = nombre_comercial
        self.cantidad_stock = cantidad_stock
        self.fecha_vencimiento = fecha_vencimiento

    def descontar_stock(self, cantidad):

        if cantidad <= 0:

            print(
                "La cantidad debe ser mayor que cero."
            )

            return

        if cantidad > self.cantidad_stock:

            print(
                "Stock insuficiente."
            )

            return

        self.cantidad_stock -= cantidad

        print(
            f"Se descontaron {cantidad} unidades."
        )

        print(
            f"Stock actual: "
            f"{self.cantidad_stock}"
        )

    def agregar_stock(self, cantidad):

        if cantidad <= 0:

            print(
                "La cantidad debe ser mayor que cero."
            )

            return

        self.cantidad_stock += cantidad

        print(
            f"Se agregaron {cantidad} unidades."
        )

        print(
            f"Stock actual: "
            f"{self.cantidad_stock}"
        )

    def verificar_alerta_vencimiento(self):

        hoy = date.today()

        if self.fecha_vencimiento <= hoy:

            print(
                "ALERTA: El medicamento está vencido."
            )

            return True

        else:

            print(
                "El medicamento todavía está vigente."
            )

            return False

    def mostrar_medicamento(self):

        print("\n===== MEDICAMENTO =====")

        print(
            f"ID: {self.id_medicamento}"
        )

        print(
            f"Nombre: {self.nombre_comercial}"
        )

        print(
            f"Stock: {self.cantidad_stock}"
        )

        print(
            f"Fecha de vencimiento: "
            f"{self.fecha_vencimiento}"
        )


# ============================================================
# CLASE REPORTE ATENCION
# ============================================================

class ReporteAtencion:

    def __init__(
        self,
        id_reporte,
        fecha_generacion,
        especialidad,
        citas
    ):

        self.id_reporte = id_reporte
        self.fecha_generacion = fecha_generacion
        self.especialidad = especialidad
        self.citas = citas

    def generar_reporte_semanal(self):

        print("\n====================================")
        print("          REPORTE SEMANAL")
        print("====================================")

        print(
            f"ID reporte: {self.id_reporte}"
        )

        print(
            f"Fecha de generación: "
            f"{self.fecha_generacion}"
        )

        print(
            f"Especialidad: "
            f"{self.especialidad}"
        )

        print("------------------------------------")

        if not self.citas:

            print(
                "No hay citas registradas."
            )

            return

        for cita in self.citas:

            print(
                f"Cita: {cita.id_cita}"
            )

            print(
                f"Paciente: "
                f"{cita.paciente.nombres} "
                f"{cita.paciente.apellidos}"
            )

            print(
                f"Fecha: {cita.fecha_hora}"
            )

            print(
                f"Estado: {cita.estado}"
            )

            print("------------------------------------")

    def exportar_sin_datos_sensibles(self):

        print(
            "\nReporte exportado correctamente."
        )

        print(
            "Los datos sensibles han sido omitidos."
        )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("============================================")
    print("     SISTEMA DE GESTIÓN DE SALUD")
    print("============================================")

    # ========================================================
    # 1. CREAR PERSONAL DE SALUD
    # ========================================================

    print("\n--- CREANDO PERSONAL DE SALUD ---")

    doctor = PersonalSalud(
        "USR001",
        "doctor01",
        "12345",
        "MEDICO",
        "PER001",
        "CMP123456",
        "Cardiología"
    )

    print(
        f"Doctor creado: {doctor.username}"
    )

    print(
        f"Especialidad: {doctor.especialidad}"
    )

    # ========================================================
    # 2. AUTENTICAR USUARIO
    # ========================================================

    print("\n--- AUTENTICACIÓN ---")

    usuario = input(
        "Ingrese usuario (doctor01): "
    )

    password = input(
        "Ingrese contraseña (12345): "
    )

    autenticado = doctor.autenticar_usuario(
        usuario,
        password
    )

    if autenticado:

        print(
            "\nUsuario autenticado correctamente."
        )

    else:

        print(
            "\nUsuario o contraseña incorrectos."
        )

        return

    # ========================================================
    # 3. CREAR PACIENTE
    # ========================================================

    print("\n--- REGISTRANDO PACIENTE ---")

    paciente = Paciente(
        "PAC001",
        "DNI_ENCRIPTADO_123",
        "Juan",
        "Perez",
        date(1995, 5, 20),
        "987654321",
        True
    )

    paciente.registrar_paciente()

    # ========================================================
    # 4. MOSTRAR DATOS DEL PACIENTE
    # ========================================================

    paciente.mostrar_datos()

    # ========================================================
    # 5. ACTUALIZAR CONTACTO
    # ========================================================

    print("\n--- ACTUALIZANDO CONTACTO ---")

    paciente.actualizar_contacto(
        "999888777"
    )

    # ========================================================
    # 6. PROGRAMAR CITA
    # ========================================================

    print("\n--- PROGRAMANDO CITA ---")

    fecha_cita = datetime(
        2026,
        9,
        15,
        10,
        30
    )

    doctor.programar_cita(
        paciente,
        fecha_cita
    )

    # ========================================================
    # 7. OBTENER LA PRIMERA CITA
    # ========================================================

    cita = paciente.citas[0]

    # ========================================================
    # 8. MOSTRAR CITA
    # ========================================================

    cita.mostrar_cita()

    # ========================================================
    # 9. CONFIRMAR CITA
    # ========================================================

    print("\n--- CONFIRMANDO CITA ---")

    cita.confirmar_cita()

    # ========================================================
    # 10. CREAR HISTORIAL MÉDICO
    # ========================================================

    print("\n--- CREANDO HISTORIAL MÉDICO ---")

    historial = HistorialMedico(
        "Hipertensión arterial",
        "Losartán 50mg",
        cita.id_cita,
        paciente.nombres + " " + paciente.apellidos
    )

    paciente.agregar_historial(
        historial
    )

    historial.mostrar_historial()

    # ========================================================
    # 11. REGISTRAR ATENCIÓN
    # ========================================================

    print("\n--- REGISTRANDO ATENCIÓN ---")

    doctor.registrar_atencion(
        cita
    )

    # ========================================================
    # 12. REPROGRAMAR CITA
    # ========================================================

    print("\n--- REPROGRAMANDO CITA ---")

    nueva_fecha = datetime(
        2026,
        9,
        17,
        11,
        0
    )

    cita.reprogramar_cita(
        nueva_fecha
    )

    cita.mostrar_cita()

    # ========================================================
    # 13. INVENTARIO DE MEDICAMENTOS
    # ========================================================

    print("\n--- INVENTARIO DE MEDICAMENTOS ---")

    medicamento = InventarioMedicamento(
        "MED001",
        "Losartán",
        100,
        date(2027, 5, 10)
    )

    medicamento.mostrar_medicamento()

    # ========================================================
    # 14. DESCONTAR STOCK
    # ========================================================

    print("\n--- DESCONTANDO STOCK ---")

    medicamento.descontar_stock(
        10
    )

    # ========================================================
    # 15. AGREGAR STOCK
    # ========================================================

    print("\n--- AGREGANDO STOCK ---")

    medicamento.agregar_stock(
        20
    )

    # ========================================================
    # 16. VERIFICAR VENCIMIENTO
    # ========================================================

    print("\n--- VERIFICANDO VENCIMIENTO ---")

    medicamento.verificar_alerta_vencimiento()

    # ========================================================
    # 17. GENERAR REPORTE
    # ========================================================

    print("\n--- GENERANDO REPORTE ---")

    reporte = ReporteAtencion(
        "REP001",
        datetime.now(),
        doctor.especialidad,
        doctor.citas
    )

    reporte.generar_reporte_semanal()

    # ========================================================
    # 18. EXPORTAR REPORTE
    # ========================================================

    print("\n--- EXPORTANDO REPORTE ---")

    reporte.exportar_sin_datos_sensibles()

    # ========================================================
    # 19. REPORTE DEL PERSONAL DE SALUD
    # ========================================================

    doctor.generar_reporte_atenciones()

    # ========================================================
    # 20. ANONIMIZAR DATOS
    # ========================================================

    print("\n--- ANONIMIZANDO DATOS ---")

    paciente.anonimizar_datos_personales()

    paciente.mostrar_datos()

    # ========================================================
    # 21. CERRAR SESIÓN
    # ========================================================

    print("\n--- CERRANDO SESIÓN ---")

    doctor.cerrar_sesion()

    # ========================================================
    # FIN
    # ========================================================

    print("\n============================================")
    print("          FIN DEL PROGRAMA")
    print("============================================")


# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
