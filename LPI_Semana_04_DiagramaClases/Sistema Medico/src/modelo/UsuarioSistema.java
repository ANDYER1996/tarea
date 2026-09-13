package modelo;

public class UsuarioSistema {

    private String idUsuario;
    private String username;
    private String passwordHash;
    private String rol;

    public UsuarioSistema(String idUsuario, String username,
                          String passwordHash, String rol) {
        this.idUsuario = idUsuario;
        this.username = username;
        this.passwordHash = passwordHash;
        this.rol = rol;
    }

    public boolean autenticarUsuario(String username, String passwordHash) {
        return this.username.equals(username)
                && this.passwordHash.equals(passwordHash);
    }

    public void cerrarSesion() {
        System.out.println("Sesión cerrada para el usuario: " + username);
    }

    public String getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(String idUsuario) {
        this.idUsuario = idUsuario;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public String getRol() {
        return rol;
    }

    public void setRol(String rol) {
        this.rol = rol;
    }
}
