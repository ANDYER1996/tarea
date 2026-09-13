package modelo;

public class HistorialMedico {

    private String diagnostico;
    private String medicacion;
    private String numeroCita;
    private String nombrePaciente;

    public HistorialMedico(String diagnostico,
                           String medicacion,
                           String numeroCita,
                           String nombrePaciente) {

        this.diagnostico = diagnostico;
        this.medicacion = medicacion;
        this.numeroCita = numeroCita;
        this.nombrePaciente = nombrePaciente;
    }

    public String getDiagnostico() {
        return diagnostico;
    }

    public String getMedicacion() {
        return medicacion;
    }

    public String getNumeroCita() {
        return numeroCita;
    }

    public String getNombrePaciente() {
        return nombrePaciente;
    }

    public void mostrarHistorial() {

        System.out.println("\n===== HISTORIAL MÉDICO =====");
        System.out.println("Paciente: " + nombrePaciente);
        System.out.println("N° de cita: " + numeroCita);
        System.out.println("Diagnóstico: " + diagnostico);
        System.out.println("Medicación: " + medicacion);
    }
}
