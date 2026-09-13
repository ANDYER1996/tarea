package modelo;

import java.time.LocalDateTime;
import java.util.List;

public class ReporteAtencion {

    private String idReporte;
    private LocalDateTime fechaGeneracion;
    private String especialidad;

    private List<CitaMedica> citas;

    public ReporteAtencion(String idReporte,
                           LocalDateTime fechaGeneracion,
                           String especialidad,
                           List<CitaMedica> citas) {

        this.idReporte = idReporte;
        this.fechaGeneracion = fechaGeneracion;
        this.especialidad = especialidad;
        this.citas = citas;
    }

    public void generarReporteSemanal() {

        System.out.println("\n===== REPORTE SEMANAL =====");
        System.out.println("ID reporte: " + idReporte);
        System.out.println("Fecha generación: " + fechaGeneracion);
        System.out.println("Especialidad: " + especialidad);

        if (citas == null || citas.isEmpty()) {
            System.out.println("No hay citas registradas.");
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

    public void exportarSinDatosSensibles() {

        System.out.println("\nReporte exportado.");
        System.out.println("Los datos sensibles han sido omitidos.");
    }

    public String getIdReporte() {
        return idReporte;
    }

    public LocalDateTime getFechaGeneracion() {
        return fechaGeneracion;
    }

    public String getEspecialidad() {
        return especialidad;
    }
}
