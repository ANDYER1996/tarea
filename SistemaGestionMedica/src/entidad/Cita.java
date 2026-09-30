package entidad;

public class Cita {
    private String id, fecha, hora, estado;
    private Paciente paciente;
    private Medico medico;

    public Cita(String id, String fecha, String hora, Paciente paciente, Medico medico, String estado) {
        this.id = id; this.fecha = fecha; this.hora = hora; this.paciente = paciente; this.medico = medico; this.estado = estado;
    }
    public String getId() { return id; }
    public String getFecha() { return fecha; }
    public String getHora() { return hora; }
    public Paciente getPaciente() { return paciente; }
    public Medico getMedico() { return medico; }
    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }
}
