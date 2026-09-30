package entidad;

public class HistorialMedico {
    private String id, diagnostico, alergias, fecha;
    private Paciente paciente;

    public HistorialMedico(String id, Paciente paciente, String diagnostico, String alergias, String fecha) {
        this.id = id; this.paciente = paciente; this.diagnostico = diagnostico; this.alergias = alergias; this.fecha = fecha;
    }
    public String getId() { return id; }
    public Paciente getPaciente() { return paciente; }
    public String getDiagnostico() { return diagnostico; }
    public String getAlergias() { return alergias; }
    public String getFecha() { return fecha; }
}
