package modelo;

import java.time.LocalDateTime;

public class CitaMedica {

    private String idCita;
    private LocalDateTime fechaHora;
    private String motivo;
    private String estado;

    private Paciente paciente;

    public CitaMedica(String idCita,
                      LocalDateTime fechaHora,
                      String motivo,
                      String estado,
                      Paciente paciente) {

        this.idCita = idCita;
        this.fechaHora = fechaHora;
        this.motivo = motivo;
        this.estado = estado;
        this.paciente = paciente;
    }

    public void confirmarCita() {
        this.estado = "Confirmada";
        System.out.println("Cita " + idCita + " confirmada.");
    }

    public void cancelarCita() {
        this.estado = "Cancelada";
        System.out.println("Cita " + idCita + " cancelada.");
    }

    public void reprogramarCita(LocalDateTime nuevaFecha) {
        this.fechaHora = nuevaFecha;
        this.estado = "Reprogramada";

        System.out.println("Cita reprogramada para: " + nuevaFecha);
    }

    public String getIdCita() {
        return idCita;
    }

    public LocalDateTime getFechaHora() {
        return fechaHora;
    }

    public String getMotivo() {
        return motivo;
    }

    public String getEstado() {
        return estado;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setFechaHora(LocalDateTime fechaHora) {
        this.fechaHora = fechaHora;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
}
