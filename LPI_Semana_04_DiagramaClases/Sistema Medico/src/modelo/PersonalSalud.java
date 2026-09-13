package modelo;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class PersonalSalud extends UsuarioSistema {

    private String idPersonal;
    private String numeroColegiatura;
    private String especialidad;

    private List<CitaMedica> citas;
    private List<Paciente> pacientes;

    public PersonalSalud(String idUsuario, String username,
                          String passwordHash, String rol,
                          String idPersonal, String numeroColegiatura,
                          String especialidad) {

        super(idUsuario, username, passwordHash, rol);

        this.idPersonal = idPersonal;
        this.numeroColegiatura = numeroColegiatura;
        this.especialidad = especialidad;

        this.citas = new ArrayList<>();
        this.pacientes = new ArrayList<>();
    }

    public void programarCita(Paciente paciente, LocalDateTime fecha) {

        CitaMedica cita = new CitaMedica(
                "CITA-" + (citas.size() + 1),
                fecha,
                "Consulta médica",
                "Programada",
                paciente
        );

        citas.add(cita);
        paciente.agregarCita(cita);

        System.out.println("Cita programada correctamente.");
        System.out.println("Paciente: " + paciente.getNombres()
                + " " + paciente.getApellidos());
        System.out.println("Fecha: " + fecha);
    }

    public void registrarAtencion(CitaMedica cita) {

        if (cita != null) {
            System.out.println("Atención registrada para la cita: "
                    + cita.getIdCita());
        } else {
            System.out.println("La cita no existe.");
        }
    }

    public void generarReporteAtenciones() {
        System.out.println("\n===== REPORTE DE ATENCIONES =====");

        if (citas.isEmpty()) {
            System.out.println("No existen citas registradas.");
            return;
        }

        for (CitaMedica cita : citas) {
            System.out.println(
                    "Cita: " + cita.getIdCita()
                    + " | Fecha: " + cita.getFechaHora()
                    + " | Estado: " + cita.getEstado()
            );
        }
    }

    public String getIdPersonal() {
        return idPersonal;
    }

    public void setIdPersonal(String idPersonal) {
        this.idPersonal = idPersonal;
    }

    public String getNumeroColegiatura() {
        return numeroColegiatura;
    }

    public void setNumeroColegiatura(String numeroColegiatura) {
        this.numeroColegiatura = numeroColegiatura;
    }

    public String getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }

    public List<CitaMedica> getCitas() {
        return citas;
    }

    public List<Paciente> getPacientes() {
        return pacientes;
    }
}
