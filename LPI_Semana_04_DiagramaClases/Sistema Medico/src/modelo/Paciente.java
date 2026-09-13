package modelo;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Paciente {

    private String idPaciente;
    private String dniEncriptado;
    private String nombres;
    private String apellidos;
    private LocalDate fechaNacimiento;
    private String telefono;
    private boolean consentimientoLey29733;

    private List<CitaMedica> citas;
    private List<HistorialMedico> historiales;

    public Paciente(String idPaciente,
                    String dniEncriptado,
                    String nombres,
                    String apellidos,
                    LocalDate fechaNacimiento,
                    String telefono,
                    boolean consentimientoLey29733) {

        this.idPaciente = idPaciente;
        this.dniEncriptado = dniEncriptado;
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.fechaNacimiento = fechaNacimiento;
        this.telefono = telefono;
        this.consentimientoLey29733 = consentimientoLey29733;

        this.citas = new ArrayList<>();
        this.historiales = new ArrayList<>();
    }

    public void registrarPaciente() {
        System.out.println("Paciente registrado: "
                + nombres + " " + apellidos);
    }

    public void actualizarContacto(String nuevoTelefono) {
        this.telefono = nuevoTelefono;
        System.out.println("Teléfono actualizado correctamente.");
    }

    public void anonimizarDatosPersonales() {
        this.nombres = "ANONIMIZADO";
        this.apellidos = "ANONIMIZADO";
        this.telefono = "ANONIMIZADO";

        System.out.println("Datos personales anonimizados.");
    }

    public void agregarCita(CitaMedica cita) {
        citas.add(cita);
    }

    public void agregarHistorial(HistorialMedico historial) {
        historiales.add(historial);
    }

    public String getIdPaciente() {
        return idPaciente;
    }

    public String getDniEncriptado() {
        return dniEncriptado;
    }

    public String getNombres() {
        return nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public LocalDate getFechaNacimiento() {
        return fechaNacimiento;
    }

    public String getTelefono() {
        return telefono;
    }

    public boolean isConsentimientoLey29733() {
        return consentimientoLey29733;
    }

    public List<CitaMedica> getCitas() {
        return citas;
    }

    public List<HistorialMedico> getHistoriales() {
        return historiales;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}
