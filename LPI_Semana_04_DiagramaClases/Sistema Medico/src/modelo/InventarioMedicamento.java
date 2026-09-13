package modelo;

import java.time.LocalDate;

public class InventarioMedicamento {

    private String idMedicamento;
    private String nombreComercial;
    private int cantidadStock;
    private LocalDate fechaVencimiento;

    public InventarioMedicamento(String idMedicamento,
                                 String nombreComercial,
                                 int cantidadStock,
                                 LocalDate fechaVencimiento) {

        this.idMedicamento = idMedicamento;
        this.nombreComercial = nombreComercial;
        this.cantidadStock = cantidadStock;
        this.fechaVencimiento = fechaVencimiento;
    }

    public void descontarStock(int cantidad) {

        if (cantidad <= 0) {
            System.out.println("La cantidad debe ser mayor que cero.");
            return;
        }

        if (cantidad > cantidadStock) {
            System.out.println("Stock insuficiente.");
            return;
        }

        cantidadStock -= cantidad;

        System.out.println("Stock descontado.");
        System.out.println("Stock actual: " + cantidadStock);
    }

    public void agregarStock(int cantidad) {

        if (cantidad <= 0) {
            System.out.println("La cantidad debe ser mayor que cero.");
            return;
        }

        cantidadStock += cantidad;

        System.out.println("Stock agregado.");
        System.out.println("Stock actual: " + cantidadStock);
    }

    public boolean verificarAlertaVencimiento() {

        LocalDate hoy = LocalDate.now();

        if (!fechaVencimiento.isAfter(hoy)) {
            System.out.println("ALERTA: El medicamento está vencido.");
            return true;
        }

        System.out.println("El medicamento todavía está vigente.");
        return false;
    }

    public String getIdMedicamento() {
        return idMedicamento;
    }

    public String getNombreComercial() {
        return nombreComercial;
    }

    public int getCantidadStock() {
        return cantidadStock;
    }

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }
}
