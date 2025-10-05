package Polimorfismo;
import java.util.ArrayList;
class Pasajero {
    String nombre;
    int habitacion;
    double costoPasaje;
    String genero;
    public Pasajero(String nombre, int habitacion, double costoPasaje, String genero) {
        this.nombre = nombre;
        this.habitacion = habitacion;
        this.costoPasaje = costoPasaje;
        this.genero = genero;
    }
    public void mostrar() {
        System.out.println(nombre + " - Habitación: " + habitacion + " - Costo: " + costoPasaje + " - Género: " + genero);
    }
}
class Crucero {
    String nombre;
    ArrayList<Pasajero> pasajeros;
    public Crucero(String nombre) {
        this.nombre = nombre;
        pasajeros = new ArrayList<>();
    }
    public void agregarPasajero(Pasajero p) {
        pasajeros.add(p);
    }
    public void mostrarPasajeros() {
        System.out.println("--- Crucero: " + nombre + " ---");
        for (Pasajero p : pasajeros) {
            p.mostrar();
        }
    }
    public double totalPasajes() {
        double total = 0;
        for (Pasajero p : pasajeros) {
            total += p.costoPasaje;
        }
        return total;
    }
    public boolean compararPasajeros(Crucero otro) {
        return this.pasajeros.size() == otro.pasajeros.size();
    }
    public void contarGeneros() {
        int h = 0, m = 0;
        for (Pasajero p : pasajeros) {
            if (p.genero.equals("M")) h++;
            else if (p.genero.equals("F")) m++;
        }
        System.out.println("Hombres: " + h + ", Mujeres: " + m);
    }
    public static void main(String[] args) {
        Crucero c1 = new Crucero("Titanic");
        Crucero c2 = new Crucero("Olympic");
        Pasajero p1 = new Pasajero("Juan Vargas", 502, 500, "M");
        Pasajero p2 = new Pasajero("Martina Vasques", 603, 1000, "F");
        Pasajero p3 = new Pasajero("Wilmer Montero", 401, 925, "M");
        Pasajero p4 = new Pasajero("Lina Perez", 101, 800, "F");
        Pasajero p5 = new Pasajero("Carlos Gomez", 202, 950, "M");
        c1.agregarPasajero(p1);
        c1.agregarPasajero(p2);
        c2.agregarPasajero(p3);
        c2.agregarPasajero(p4);
        c2.agregarPasajero(p5);
        c1.mostrarPasajeros();
        c2.mostrarPasajeros();
        System.out.println("Total pasajes C1: " + c1.totalPasajes());
        System.out.println("Total pasajes C2: " + c2.totalPasajes());
        System.out.println("¿Misma cantidad de pasajeros? " + c1.compararPasajeros(c2));
        System.out.print("Géneros en C2: ");
        c2.contarGeneros();
    }
}