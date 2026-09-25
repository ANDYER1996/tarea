from datetime import date, datetime


# ============================================================
# CLASE PERSONA (Clase Base / Padre)
# ============================================================

class Persona:
    """Clase padre que contiene los atributos comunes de Paciente y Médico."""

    def __init__(self, id_persona, dni, nombres, apellidos,
                 fecha_nacimiento, telefono):
        self.id_persona = id_persona
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono

    def get_nombre_completo(self):
        """Concatena el nombre y apellido para devolver el nombre completo."""
        return self.nombres + " " + self.apellidos


# ============================================================
# CLASE PACIENTE (Hereda de Persona)
# ============================================================

class Paciente(Persona):
    """Representa a un paciente registrado en el sistema."""

    def __init__(self, id_persona, dni, nombres, apellidos,
                 fecha_nacimiento, telefono,
                 numero_historia_clinica, tipo_seguro):
        # Llama al constructor de la clase Padre (Persona)
        super().__init__(
            id_persona, dni, nombres, apellidos, fecha_nacimiento, telefono
        )
        self.numero_historia_clinica = numero_historia_clinica
        self.tipo_seguro = tipo_seguro
        self.citas = []  # Lista donde guardaremos las citas de este paciente específico

    def solicitar_cita(self, cita):
        """Agrega una cita a la lista personal del paciente."""
        self.citas.append(cita)
        print("\n[OK] Cita solicitada e ingresada al paciente.")

    def consultar_historial(self):
        """Recorre y muestra en pantalla todas las citas registradas para el paciente."""
        print(f"\n===== HISTORIAL DE CITAS DE {self.get_nombre_completo().upper()} =====")
        if len(self.citas) == 0:
            print("El paciente no tiene citas registradas.")
            return

        for cita in self.citas:
            print(
                f"Cita ID: {cita.id_cita} | "
                f"Fecha/Hora: {cita.fecha_hora.strftime('%Y-%m-%d %H:%M')} | "
                f"Médico: Dr(a). {cita.medico.get_nombre_completo()} | "
                f"Estado: {cita.estado_cita}"
            )


# ============================================================
# CLASE MEDICO (Hereda de Persona)
# ============================================================

class Medico(Persona):
    """Representa a un médico del centro médico."""

    def __init__(self, id_persona, dni, nombres, apellidos,
                 fecha_nacimiento, telefono, cmp, especialidad):
        # Llama al constructor de Persona
        super().__init__(
            id_persona, dni, nombres, apellidos, fecha_nacimiento, telefono
        )
        self.cmp = cmp
        self.especialidad = especialidad

    def atender_cita(self, cita):
        """Cambia el estado de la cita a 'ATENDIDA'."""
        print(
            f"\nEl Dr(a). {self.get_nombre_completo()} "
            f"está atendiendo la cita {cita.id_cita}."
        )
        cita.estado_cita = "ATENDIDA"

    def emitir_receta(self):
        """Simula la emisión formal de la receta."""
        print(f"El Dr(a). {self.get_nombre_completo()} ha emitido una receta.")


# ============================================================
# CLASE CITA MEDICA
# ============================================================

class CitaMedica:
    """Modela el compromiso de cita entre un Paciente y un Médico."""

    def __init__(self, id_cita, fecha_hora, estado_cita, motivo_consulta, paciente, medico):
        self.id_cita = id_cita
        self.fecha_hora = fecha_hora
        self.estado_cita = estado_cita
        self.motivo_consulta = motivo_consulta
        self.paciente = paciente  # Enlace al objeto Paciente
        self.medico = medico      # Enlace al objeto Medico
        self.atencion_medica = None

    def programar_cita(self):
        """Asigna el estado PROGRAMADA."""
        self.estado_cita = "PROGRAMADA"
        print(f"[OK] Cita {self.id_cita} programada correctamente.")

    def cancelar_cita(self):
        """Asigna el estado CANCELADA."""
        self.estado_cita = "CANCELADA"
        print(f"[OK] Cita {self.id_cita} cancelada.")

    def registrar_atencion(self, atencion):
        """Vincula la cita con el registro de atención medica correspondiente."""
        self.atencion_medica = atencion
        self.estado_cita = "ATENDIDA"
        print(f"[OK] Atención registrada para la cita {self.id_cita}.")


# ============================================================
# CLASE MEDICAMENTO
# ============================================================

class Medicamento:
    """Gestiona el inventario de un fármaco."""

    def __init__(self, id_medicamento, nombre, stock_disponible, fecha_vencimiento):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.stock_disponible = stock_disponible
        self.fecha_vencimiento = fecha_vencimiento

    def actualizar_stock(self, cantidad):
        """Aumenta o disminuye el inventario disponible."""
        nuevo_stock = self.stock_disponible + cantidad
        if nuevo_stock < 0:
            print("Error: No hay suficiente stock.")
            return False
        self.stock_disponible = nuevo_stock
        return True

    def esta_vencido(self):
        """Retorna True si el medicamento ya pasó su fecha de vencimiento."""
        return date.today() > self.fecha_vencimiento


# ============================================================
# CLASE DETALLE RECETA
# ============================================================

class DetalleReceta:
    """Representa una línea o ítem recetado dentro de la receta."""

    def __init__(self, cantidad, indicaciones, medicamento):
        self.cantidad = cantidad
        self.indicaciones = indicaciones
        self.medicamento = medicamento  # Enlace al objeto Medicamento

    def validar_stock(self):
        """Verifica si la cantidad pedida está en stock."""
        return self.medicamento.stock_disponible >= self.cantidad

    def descontar_stock(self):
        """Reduce el stock de la farmacia según la cantidad recetada."""
        if self.validar_stock():
            self.medicamento.actualizar_stock(-self.cantidad)
            return True
        print(f"No hay suficiente stock de {self.medicamento.nombre}.")
        return False


# ============================================================
# CLASE ATENCION MEDICA
# ============================================================

class AtencionMedica:
    """Almacena los resultados médicos tras la realización de la cita."""

    def __init__(self, id_atencion, fecha_atencion, diagnostico, tratamiento):
        self.id_atencion = id_atencion
        self.fecha_atencion = fecha_atencion
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.detalles_receta = []  # Lista de DetalleReceta

    def agregar_detalle_receta(self, detalle):
        """Descuenta el stock e incluye el medicamento en la receta médica."""
        if detalle.validar_stock():
            detalle.descontar_stock()
            self.detalles_receta.append(detalle)
            print(f"[OK] Medicamento '{detalle.medicamento.nombre}' agregado a la receta.")
        else:
            print(f"[ERROR] No se pudo agregar {detalle.medicamento.nombre} por falta de stock.")

    def generar_informe(self):
        """Imprime la ficha médica en consola."""
        print("\n================================")
        print("        INFORME MÉDICO")
        print("================================")
        print(f"ID Atención: {self.id_atencion}")
        print(f"Fecha: {self.fecha_atencion.strftime('%Y-%m-%d %H:%M')}")
        print(f"Diagnóstico: {self.diagnostico}")
        print(f"Tratamiento: {self.tratamiento}")
        print("\nMedicamentos Recetados:")
        if len(self.detalles_receta) == 0:
            print("- No se recetaron medicamentos.")
        else:
            for detalle in self.detalles_receta:
                print(
                    f"- {detalle.medicamento.nombre} | "
                    f"Cantidad: {detalle.cantidad} | "
                    f"Indicaciones: {detalle.indicaciones}"
                )
        print("================================")


# ============================================================
# CLASE REGISTRO ATENCION BD
# ============================================================

class RegistroAtencionBD:
    """Simulación de almacenamiento persistente o Base de Datos."""

    def __init__(self):
        self.atenciones = []

    def guardar_atencion(self, atencion):
        """Guarda la atención realizada dentro del historial global."""
        self.atenciones.append(atencion)
        print("[OK] Atención guardada correctamente en la Base de Datos.")
        return True

    def generar_reporte_mensual(self):
        """Genera un reporte consolidado con todas las atenciones registradas."""
        print("\n================================")
        print("     REPORTE DE ATENCIONES")
        print("================================")
        print(f"Total de atenciones: {len(self.atenciones)}")
        for atencion in self.atenciones:
            print(f"\nAtención ID: {atencion.id_atencion}")
            print(f"Diagnóstico: {atencion.diagnostico}")
        print("================================")


# ============================================================
# FUNCIONES AUXILIARES DE BÚSQUEDA
# ============================================================

def buscar_paciente(dni, lista_pacientes):
    # Recorre la lista de pacientes comparando el DNI
    for p in lista_pacientes:
        if p.dni == dni:
            return p  # Retorna el objeto paciente si lo encuentra
    return None       # Retorna None si no existe

def buscar_medico(dni, lista_medicos):
    # Recorre la lista de médicos comparando el DNI
    for m in lista_medicos:
        if m.dni == dni:
            return m  # Retorna el objeto médico
    return None

def buscar_cita(id_cita, lista_citas):
    # Recorre la lista buscando por ID de cita
    for c in lista_citas:
        if c.id_cita == id_cita:
            return c  # Retorna la cita correspondiente
    return None

def buscar_medicamento(id_med, lista_medicamentos):
    # Recorre la lista buscando por ID de medicamento
    for med in lista_medicamentos:
        if med.id_medicamento == id_med:
            return med # Retorna el medicamento
    return None


# ============================================================
# PROGRAMA PRINCIPAL CON EXPLICACIÓN LÍNEA POR LÍNEA
# ============================================================

def main():
    # Inicializamos las listas vacías donde guardaremos la información ingresada
    pacientes = []       # Lista para almacenar objetos de la clase Paciente
    medicos = []         # Lista para almacenar objetos de la clase Medico
    citas = []           # Lista para almacenar objetos de la clase CitaMedica
    medicamentos = []    # Lista para almacenar objetos de la clase Medicamento
    repositorio_bd = RegistroAtencionBD()  # Instanciamos el repositorio simulado de BD

    # Registramos algunos datos iniciales de prueba (opcional) para no empezar en cero
    p_demo = Paciente("P001", "12345678", "Juan", "Perez", date(1995, 5, 10), "999888777", "HC001", "SIS")
    m_demo = Medico("M001", "87654321", "Carlos", "Gomez", date(1980, 3, 15), "988777666", "CMP12345", "General")
    med_demo = Medicamento("MED001", "Paracetamol 500mg", 50, date(2027, 12, 31))
    
    # Agregamos los objetos de prueba a sus respectivas listas
    pacientes.append(p_demo)
    medicos.append(m_demo)
    medicamentos.append(med_demo)

    # Inicia el bucle principal del menú (se repetirá indefinidamente hasta que se elija salir)
    while True:
        # Mostramos las opciones del menú en consola
        print("\n" + "="*35)
        print("   SISTEMA DE GESTIÓN MÉDICA")
        print("="*35)
        print("1. Registrar Paciente")
        print("2. Registrar Médico")
        print("3. Registrar Medicamento")
        print("4. Registrar/Programar Cita")
        print("5. Atender Cita y Generar Receta")
        print("6. Consultar Historial de Paciente")
        print("7. Ver Reporte General de Atenciones")
        print("8. Salir")
        
        # Leemos la opción elegida por el usuario y eliminamos espacios extra
        opcion = input("\nSeleccione una opción (1-8): ").strip()

        # ------------------------------------------------------------
        # OPCIÓN 1: REGISTRAR PACIENTE
        # ------------------------------------------------------------
        if opcion == "1":
            print("\n--- REGISTRO DE PACIENTE ---")
            id_p = f"P00{len(pacientes) + 1}"  # Genera un ID automático (P001, P002, etc.)
            dni = input("DNI: ")               # Pide el número de DNI por consola
            nombres = input("Nombres: ")       # Pide el o los nombres
            apellidos = input("Apellidos: ")   # Pide los apellidos
            f_nac = input("Fecha Nacimiento (AAAA-MM-DD): ") # Pide fecha en texto
            telefono = input("Teléfono: ")     # Pide el número telefónico
            hc = input("Nº Historia Clínica: ")# Pide el código de historia clínica
            seguro = input("Tipo de Seguro: ")  # Pide el tipo de seguro

            try:
                # Convierte la fecha ingresada en texto a un objeto date
                f_date = datetime.strptime(f_nac, "%Y-%m-%d").date()
                # Crea la instancia/objeto Paciente con los datos del usuario
                nuevo_paciente = Paciente(id_p, dni, nombres, apellidos, f_date, telefono, hc, seguro)
                # Agrega el paciente a la lista general de pacientes
                pacientes.append(nuevo_paciente)
                print(f"\n[OK] Paciente {nuevo_paciente.get_nombre_completo()} registrado con ID {id_p}.")
            except ValueError:
                # Muestra un mensaje si el usuario no escribió la fecha en el formato AAAA-MM-DD
                print("\n[ERROR] Formato de fecha incorrecto. Use AAAA-MM-DD.")

        # ------------------------------------------------------------
        # OPCIÓN 2: REGISTRAR MÉDICO
        # ------------------------------------------------------------
        elif opcion == "2":
            print("\n--- REGISTRO DE MÉDICO ---")
            id_m = f"M00{len(medicos) + 1}"    # Genera un ID automático para el médico
            dni = input("DNI: ")               # Pide DNI
            nombres = input("Nombres: ")       # Pide Nombres
            apellidos = input("Apellidos: ")   # Pide Apellidos
            f_nac = input("Fecha Nacimiento (AAAA-MM-DD): ") # Pide fecha de nacimiento
            telefono = input("Teléfono: ")     # Pide teléfono
            cmp = input("Nº CMP: ")             # Pide el código colegiatura médica
            especialidad = input("Especialidad: ") # Pide la especialidad médica

            try:
                # Transforma el texto ingresado en un objeto date
                f_date = datetime.strptime(f_nac, "%Y-%m-%d").date()
                # Instancia la clase Medico con la información leída
                nuevo_medico = Medico(id_m, dni, nombres, apellidos, f_date, telefono, cmp, especialidad)
                # Guarda el objeto médico en la lista general de médicos
                medicos.append(nuevo_medico)
                print(f"\n[OK] Dr(a). {nuevo_medico.get_nombre_completo()} registrado con ID {id_m}.")
            except ValueError:
                print("\n[ERROR] Formato de fecha incorrecto. Use AAAA-MM-DD.")

        # ------------------------------------------------------------
        # OPCIÓN 3: REGISTRAR MEDICAMENTO
        # ------------------------------------------------------------
        elif opcion == "3":
            print("\n--- REGISTRO DE MEDICAMENTO ---")
            id_med = f"MED00{len(medicamentos) + 1}" # Genera ID para el medicamento
            nombre = input("Nombre del medicamento: ")# Pide el nombre comercial
            stock = int(input("Stock inicial: "))     # Pide el stock y lo convierte a entero
            f_venc = input("Fecha Vencimiento (AAAA-MM-DD): ") # Pide fecha de caducidad

            try:
                # Convierte la fecha en un objeto date
                f_date = datetime.strptime(f_venc, "%Y-%m-%d").date()
                # Crea la instancia del medicamento
                nuevo_med = Medicamento(id_med, nombre, stock, f_date)
                # Agrega el medicamento a la lista
                medicamentos.append(nuevo_med)
                print(f"\n[OK] Medicamento '{nombre}' registrado con ID {id_med}.")
            except ValueError:
                print("\n[ERROR] Formato de fecha incorrecto.")

        # ------------------------------------------------------------
        # OPCIÓN 4: REGISTRAR / PROGRAMAR CITA
        # ------------------------------------------------------------
        elif opcion == "4":
            print("\n--- SOLICITAR / REGISTRAR CITA ---")
            dni_p = input("Ingrese DNI del paciente: ") # Pide DNI para buscar al paciente
            paciente = buscar_paciente(dni_p, pacientes) # Busca en la lista de pacientes
            
            # Valida si el paciente fue encontrado
            if not paciente:
                print("\n[ERROR] Paciente no encontrado. Debe registrarlo primero.")
                continue  # Cancela este proceso y regresa al menú principal

            dni_m = input("Ingrese DNI del médico: ")   # Pide DNI para buscar al médico
            medico = buscar_medico(dni_m, medicos)      # Busca en la lista de médicos

            # Valida si el médico fue encontrado
            if not medico:
                print("\n[ERROR] Médico no encontrado. Debe registrarlo primero.")
                continue  # Regresa al menú principal

            id_cita = f"C00{len(citas) + 1}"             # Genera ID automático para la cita
            fecha_str = input("Fecha y hora de la cita (AAAA-MM-DD HH:MM): ") # Pide fecha y hora
            motivo = input("Motivo de la consulta: ")    # Pide el motivo de consulta

            try:
                # Convierte el texto ingresado en un objeto datetime completo (con hora)
                fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
                # Crea el objeto CitaMedica con las referencias al paciente y al médico
                nueva_cita = CitaMedica(id_cita, fecha_hora, "PENDIENTE", motivo, paciente, medico)
                
                # Relaciona la cita con la lista interna del paciente
                paciente.solicitar_cita(nueva_cita)
                # Cambia el estado de la cita a PROGRAMADA
                nueva_cita.programar_cita()
                # Guarda la cita en la lista general de citas
                citas.append(nueva_cita)
            except ValueError:
                print("\n[ERROR] Formato de fecha/hora incorrecto. Use AAAA-MM-DD HH:MM.")

        # ------------------------------------------------------------
        # OPCIÓN 5: ATENDER CITA Y GENERAR RECETA
        # ------------------------------------------------------------
        elif opcion == "5":
            print("\n--- ATENDER CITA MÉDICA ---")
            id_c = input("Ingrese ID de la Cita a atender (ej. C001): ") # Pide el ID de la cita
            cita = buscar_cita(id_c, citas) # Busca la cita en la lista

            # Comprueba si la cita existe
            if not cita:
                print("\n[ERROR] Cita no encontrada.")
                continue

            # Evita atender una cita que ya fue atendida previamente
            if cita.estado_cita == "ATENDIDA":
                print("\n[AVISO] Esta cita ya fue atendida anteriormente.")
                continue

            # El médico atiende formalmente la cita
            cita.medico.atender_cita(cita)

            # Prepara la creación de la Atención Médica asociándole un ID
            id_atencion = f"A00{len(repositorio_bd.atenciones) + 1}"
            diag = input("Diagnóstico: ")   # Recibe el diagnóstico médico
            trat = input("Tratamiento: ")   # Recibe el tratamiento sugerido
            # Crea la instancia de la AtencionMedica
            atencion = AtencionMedica(id_atencion, datetime.now(), diag, trat)

            # Bucle secundario para agregar varios medicamentos a la receta si es necesario
            while True:
                agregar = input("\n¿Desea agregar un medicamento a la receta? (s/n): ").lower()
                if agregar != 's':
                    break  # Rompe el bucle si la respuesta no es 's'

                id_med = input("ID del medicamento (ej. MED001): ")
                med = buscar_medicamento(id_med, medicamentos) # Busca el medicamento

                if not med:
                    print("[ERROR] Medicamento no encontrado.")
                    continue

                cant = int(input(f"Cantidad recetada de '{med.nombre}': ")) # Lee la cantidad
                indicaciones = input("Indicaciones de uso: ")                # Lee la posología

                # Instancia el detalle del ítem de la receta
                detalle = DetalleReceta(cant, indicaciones, med)
                # Intenta descontar el stock e incluirlo en la atención
                atencion.agregar_detalle_receta(detalle)

            # Finalización y vinculación del proceso
            cita.registrar_atencion(atencion)        # Asigna la atención a la cita
            cita.medico.emitir_receta()               # Imprime mensaje de emisión de receta
            atencion.generar_informe()                # Imprime el informe médico detallado
            repositorio_bd.guardar_atencion(atencion) # Almacena el resultado en el repositorio/BD

        # ------------------------------------------------------------
        # OPCIÓN 6: CONSULTAR HISTORIAL DE PACIENTE
        # ------------------------------------------------------------
        elif opcion == "6":
            print("\n--- CONSULTAR HISTORIAL DE PACIENTE ---")
            dni_p = input("Ingrese DNI del paciente: ")   # Pide el DNI del paciente
            paciente = buscar_paciente(dni_p, pacientes) # Busca al paciente

            if paciente:
                paciente.consultar_historial() # Llama al método que imprime sus citas
            else:
                print("\n[ERROR] Paciente no encontrado.")

        # ------------------------------------------------------------
        # OPCIÓN 7: REPORTE GENERAL
        # ------------------------------------------------------------
        elif opcion == "7":
            # Ejecuta la consulta general de atenciones guardadas en el repositorio
            repositorio_bd.generar_reporte_mensual()

        # ------------------------------------------------------------
        # OPCIÓN 8: SALIR
        # ------------------------------------------------------------
        elif opcion == "8":
            print("\nSaliendo del sistema...")
            break  # Detiene la ejecución del ciclo while y finaliza el programa

        # ------------------------------------------------------------
        # OPCIÓN NO VÁLIDA
        # ------------------------------------------------------------
        else:
            print("\nOpción no válida. Intente nuevamente.")


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

# Comprueba si el script se está ejecutando directamente
if __name__ == "__main__":
    main() # Inicia la ejecución llamando a la función principal main()