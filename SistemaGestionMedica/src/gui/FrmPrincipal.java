package gui;

import java.awt.*;
import java.awt.event.*;
import java.beans.PropertyVetoException;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import datos.DatosSistema;

public class FrmPrincipal extends JFrame implements ActionListener {
    private static final long serialVersionUID = 1L;
    private JDesktopPane desktopPane;
    private FormPaciente formPaciente = new FormPaciente();
    private FormMedico formMedico = new FormMedico();
    private FormEspecialidad formEspecialidad = new FormEspecialidad();
    private FormCita formCita = new FormCita();
    private FormReceta formReceta = new FormReceta();
    private FormHistorial formHistorial = new FormHistorial();
    private FormReportes formReportes = new FormReportes();
    private JMenuItem mntmPaciente, mntmEspecialidad, mntmMedico, mntmHistorial, mntmCita, mntmReceta;
    private JMenuItem mntmConsultaHistorial, mntmConsulta02, mntmConsulta03, mntmReporte01, mntmReporte02, mntmReporte03;
    private static JLabel lblPacientesCount, lblMedicosCount, lblCitasCount, lblRecetasCount;

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            DatosSistema.cargarDatosIniciales();
            new FrmPrincipal().setVisible(true);
        });
    }

    public FrmPrincipal() {
        setTitle("Sistema de Gestión de Establecimientos Médicos");
        setExtendedState(Frame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 950, 680);

        JMenuBar menuBar = new JMenuBar(); setJMenuBar(menuBar);
        JMenu mnMantenimiento = new JMenu("Mantenimiento"); menuBar.add(mnMantenimiento);
        mntmPaciente = item("Paciente"); mnMantenimiento.add(mntmPaciente);
        mntmEspecialidad = item("Especialidad"); mnMantenimiento.add(mntmEspecialidad);
        mntmMedico = item("Medico"); mnMantenimiento.add(mntmMedico);

        JMenu mnProcesos = new JMenu("Procesos"); menuBar.add(mnProcesos);
        mntmHistorial = item("Crear Historial Medico"); mnProcesos.add(mntmHistorial);
        mntmCita = item("Cita"); mnProcesos.add(mntmCita);
        mntmReceta = item("Receta"); mnProcesos.add(mntmReceta);

        JMenu mnConsultas = new JMenu("Consultas"); menuBar.add(mnConsultas);
        mntmConsultaHistorial = item("Consultar Historial Medico"); mnConsultas.add(mntmConsultaHistorial);
        mntmConsulta02 = item("Cita por Paciente"); mnConsultas.add(mntmConsulta02);
        mntmConsulta03 = item("Receta por paciente"); mnConsultas.add(mntmConsulta03);

        JMenu mnReportes = new JMenu("Reportes"); menuBar.add(mnReportes);
        mntmReporte01 = item("Reporte de Análisis de Paciente"); mnReportes.add(mntmReporte01);
        mntmReporte02 = item("Reporte de Análisis de Historial Médico"); mnReportes.add(mntmReporte02);
        mntmReporte03 = item("Reporte de Citas"); mnReportes.add(mntmReporte03);

        JPanel contentPane = new JPanel(new BorderLayout()); contentPane.setBorder(new EmptyBorder(5,5,5,5)); setContentPane(contentPane);
        desktopPane = new JDesktopPane(); desktopPane.setBackground(new Color(230,240,250)); contentPane.add(desktopPane, BorderLayout.CENTER);
        desktopPane.add(formPaciente); desktopPane.add(formMedico); desktopPane.add(formEspecialidad); desktopPane.add(formCita); desktopPane.add(formReceta); desktopPane.add(formHistorial); desktopPane.add(formReportes);
        crearPanelBienvenida();
    }

    private JMenuItem item(String text) { JMenuItem i = new JMenuItem(text); i.addActionListener(this); return i; }

    private void crearPanelBienvenida() {
        JPanel pnl = new JPanel(new BorderLayout(15,15)); pnl.setBounds(50,30,800,450); pnl.setOpaque(false);
        JLabel title = new JLabel("Bienvenido al Sistema de Gestión Médica", SwingConstants.CENTER); title.setFont(new Font("Segoe UI",Font.BOLD,22)); title.setForeground(new Color(25,45,80)); pnl.add(title,BorderLayout.NORTH);
        JPanel cards = new JPanel(new GridLayout(2,2,20,20)); cards.setOpaque(false);
        lblPacientesCount = card(cards,"Pacientes Registrados",String.valueOf(DatosSistema.pacientes.size()),new Color(0,123,255),this::abrirPaciente);
        lblMedicosCount = card(cards,"Médicos Disponibles",String.valueOf(DatosSistema.medicos.size()),new Color(40,167,69),this::abrirMedico);
        lblCitasCount = card(cards,"Citas Agendadas",String.valueOf(DatosSistema.citas.size()),new Color(255,193,7),this::abrirCita);
        lblRecetasCount = card(cards,"Recetas Emitidas",String.valueOf(DatosSistema.recetas.size()),new Color(23,162,184),this::abrirReceta);
        pnl.add(cards,BorderLayout.CENTER); desktopPane.add(pnl);
    }

    private JLabel card(JPanel parent,String title,String value,Color color,Runnable action) {
        JPanel c = new JPanel(new BorderLayout()); c.setBackground(Color.WHITE); c.setBorder(BorderFactory.createLineBorder(new Color(200,210,220),1,true));
        JLabel h = new JLabel(title,SwingConstants.CENTER); h.setOpaque(true); h.setBackground(color); h.setForeground(Color.WHITE); h.setFont(new Font("Segoe UI",Font.BOLD,14)); h.setBorder(BorderFactory.createEmptyBorder(8,0,8,0));
        JLabel v = new JLabel(value,SwingConstants.CENTER); v.setFont(new Font("Segoe UI",Font.BOLD,36));
        JButton b = new JButton("Abrir Módulo ->"); b.addActionListener(e->action.run()); c.add(h,BorderLayout.NORTH); c.add(v,BorderLayout.CENTER); c.add(b,BorderLayout.SOUTH); c.addMouseListener(new MouseAdapter(){public void mouseClicked(MouseEvent e){action.run();}}); parent.add(c); return v;
    }

    public static void actualizarContadores() {
        if(lblPacientesCount!=null){lblPacientesCount.setText(String.valueOf(DatosSistema.pacientes.size()));lblMedicosCount.setText(String.valueOf(DatosSistema.medicos.size()));lblCitasCount.setText(String.valueOf(DatosSistema.citas.size()));lblRecetasCount.setText(String.valueOf(DatosSistema.recetas.size()));}
    }
    private void abrirVentanaInterna(JInternalFrame f){ try { if(f.isClosed()) desktopPane.add(f); f.setVisible(true); f.setIcon(false); f.setSelected(true); f.toFront(); } catch(PropertyVetoException e){e.printStackTrace();} }
    private void abrirPaciente(){formPaciente.buscar("");abrirVentanaInterna(formPaciente);} private void abrirMedico(){formMedico.buscar("");abrirVentanaInterna(formMedico);} private void abrirCita(){formCita.actualizarCitas("");abrirVentanaInterna(formCita);} private void abrirReceta(){formReceta.actualizarRecetas("");abrirVentanaInterna(formReceta);}

    @Override public void actionPerformed(ActionEvent e){
        if(e.getSource()==mntmPaciente) abrirPaciente();
        if(e.getSource()==mntmMedico){formMedico.buscar("");abrirVentanaInterna(formMedico);}
        if(e.getSource()==mntmEspecialidad){formEspecialidad.buscar("");abrirVentanaInterna(formEspecialidad);}
        if(e.getSource()==mntmCita||e.getSource()==mntmConsulta02) abrirCita();
        if(e.getSource()==mntmReceta||e.getSource()==mntmConsulta03) abrirReceta();
        if(e.getSource()==mntmHistorial||e.getSource()==mntmConsultaHistorial){formHistorial.actualizar();abrirVentanaInterna(formHistorial);}
        if(e.getSource()==mntmReporte01){formReportes.seleccionarPestana(0);abrirVentanaInterna(formReportes);}
        if(e.getSource()==mntmReporte02){formReportes.seleccionarPestana(1);abrirVentanaInterna(formReportes);}
        if(e.getSource()==mntmReporte03){formReportes.seleccionarPestana(2);abrirVentanaInterna(formReportes);}
    }
}
