package Herencia;
interface Persona {
    public void setDatosPersona(String nombre, int edad);
    public String getNombre();
    public int getEdad();
}
interface Empleado {
    public void setDatosEmpleado(String idEmpleado, double sueldo);
    public String getIdEmpleado();
    public double getSueldo();
}
interface Policia {
    public void setDatosPolicia(String grado, String unidad);
    public String getGrado();
    public String getUnidad();
}
public class JefePolicia implements Persona, Empleado, Policia {
    private String nombre;
    private int edad;
    private String idEmpleado;
    private double sueldo;
    private String grado;
    private String unidad;
    public void setDatosPersona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    public String getNombre() {
        return nombre;
    }
    public int getEdad() {
        return edad;
    }
    public void setDatosEmpleado(String idEmpleado, double sueldo) {
        this.idEmpleado = idEmpleado;
        this.sueldo = sueldo;
    }
    public String getIdEmpleado() {
        return idEmpleado;
    }
    public double getSueldo() {
        return sueldo;
    }
    public void setDatosPolicia(String grado, String unidad) {
        this.grado = grado;
        this.unidad = unidad;
    }
    public String getGrado() {
        return grado;
    }
    public String getUnidad() {
        return unidad;
    }
    public void mostrarDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("ID Empleado: " + idEmpleado);
        System.out.println("Sueldo: " + sueldo);
        System.out.println("Grado: " + grado);
        System.out.println("Unidad: " + unidad);
    }
    public void compararSueldo(JefePolicia otro) {
        if (this.sueldo > otro.getSueldo()) {
            System.out.println(this.nombre + " tiene mayor sueldo que " + otro.getNombre());
        } else if (this.sueldo < otro.getSueldo()) {
            System.out.println(otro.getNombre() + " tiene mayor sueldo que " + this.nombre);
        } else {
            System.out.println("Ambos tienen el mismo sueldo.");
        }
    }
    public boolean mismoGrado(JefePolicia otro) {
        return this.grado.equals(otro.getGrado());
    }
    public static void main(String[] args) {
        JefePolicia jefe1 = new JefePolicia();
        jefe1.setDatosPersona("Carlos", 45);
        jefe1.setDatosEmpleado("EMP001", 5000.0);
        jefe1.setDatosPolicia("Capitán", "Antinarcóticos");
        JefePolicia jefe2 = new JefePolicia();
        jefe2.setDatosPersona("Luis", 50);
        jefe2.setDatosEmpleado("EMP002", 5500.0);
        jefe2.setDatosPolicia("Capitán", "Investigación");
        System.out.println("Datos del Jefe 1:");
        jefe1.mostrarDatos();
        System.out.println("\nDatos del Jefe 2:");
        jefe2.mostrarDatos();
        System.out.println("\nComparación de sueldos:");
        jefe1.compararSueldo(jefe2);
        System.out.println("\n¿Tienen el mismo grado?");
        if (jefe1.mismoGrado(jefe2)) {
            System.out.println("Sí, ambos tienen el mismo grado: " + jefe1.getGrado());
        } else {
            System.out.println("No, tienen grados diferentes.");
        }
    }
}