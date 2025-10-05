package Introducción;
public class Persona {
    String nombre, paterno, materno, ci;
    int edad;
    public Persona(String nombre, String paterno, String materno, int edad, String ci) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }
    public void mostrarDatos() {
        System.out.println("Nombre completo: " + nombre + " " + paterno + " " + materno);
        System.out.println("Edad: " + edad + " - CI: " + ci);
    }
    public boolean mayorDeEdad() {
        return edad >= 18;
    }
    public void modificarEdad(int nuevaEdad) {
        this.edad = nuevaEdad;
    }
    public boolean mismoApellido(Persona otra) {
        return this.paterno.equals(otra.paterno);
    }
    public static void main(String[] args) {
        Persona p1 = new Persona("Ana", "Lopez", "Perez", 20, "1234567");
        Persona p2 = new Persona("Juan", "Lopez", "Sosa", 17, "7654321");
        p1.mostrarDatos();
        System.out.println("¿Mayor de edad? " + p1.mayorDeEdad());
        p2.modificarEdad(18);
        System.out.println("¿Mismo apellido paterno? " + p1.mismoApellido(p2));
    }
}