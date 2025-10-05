package Herencia;
class Vehiculo {
    protected int id;
    protected String placa;
    protected String conductor;
    public Vehiculo(int id, String placa, String conductor) {
        this.id = id;
        this.placa = placa;
        this.conductor = conductor;
    }
    public void mostrarDatos() {
        System.out.println("Placa: " + placa);
        System.out.println("Conductor: " + conductor);
    }
    public void cambiarConductor(String nuevoConductor) {
        this.conductor = nuevoConductor;
    }
}
class Bus extends Vehiculo {
    int capacidad;
    String sindicato;
    public Bus(int id, String placa, String conductor, int capacidad, String sindicato) {
        super(id, placa, conductor);
        this.capacidad = capacidad;
        this.sindicato = sindicato;
    }
}
class Auto extends Vehiculo {
    int caballosFuerza;
    boolean descapotable;
    public Auto(int id, String placa, String conductor, int caballosFuerza, boolean descapotable) {
        super(id, placa, conductor);
        this.caballosFuerza = caballosFuerza;
        this.descapotable = descapotable;
    }
}
class Moto extends Vehiculo {
    int cilindrada;
    boolean casco;
    public Moto(int id, String placa, String conductor, int cilindrada, boolean casco) {
        super(id, placa, conductor);
        this.cilindrada = cilindrada;
        this.casco = casco;
    }
}
public class MainVehiculo {
    public static void main(String[] args) {
        Bus bus = new Bus(1, "123-ABC", "Carlos", 50, "Sindicato A");
        Auto auto = new Auto(2, "456-DEF", "Ana", 120, true);
        Moto moto = new Moto(3, "789-GHI", "Luis", 250, true);
        System.out.println("BUS:");
        bus.mostrarDatos();
        System.out.println("\nAUTO:");
        auto.mostrarDatos();
        System.out.println("\nMOTO:");
        moto.mostrarDatos();
        System.out.println("\nCAMBIO DE CONDUCTOR DEL AUTO:");
        auto.cambiarConductor("Pedro");
        auto.mostrarDatos();
    }
}