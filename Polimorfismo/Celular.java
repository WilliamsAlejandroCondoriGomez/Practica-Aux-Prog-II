package Polimorfismo;
public class Celular {
    String nroTel, dueño;
    int espacio, ram, nroApp;
    public Celular(String nroTel, String dueño, int espacio, int ram, int nroApp) {
        this.nroTel = nroTel;
        this.dueño = dueño;
        this.espacio = espacio;
        this.ram = ram;
        this.nroApp = nroApp;
    }
    public void instalarApp() {
        this.nroApp += 10;
    }
    public void borrarEspacio() {
        this.espacio -= 5;
        if (this.espacio < 0) this.espacio = 0;
    }
    public void mostrar() {
        System.out.println("Dueño: " + dueño);
        System.out.println("Teléfono: " + nroTel);
        System.out.println("RAM: " + ram + " GB");
        System.out.println("Espacio: " + espacio + " GB");
        System.out.println("Número de Apps: " + nroApp);
        System.out.println("---------------------------");
    }
    public static void main(String[] args) {
        Celular cel = new Celular("77712345", "Luis", 64, 4, 20);
        System.out.println("Antes:");
        cel.mostrar();
        cel.instalarApp();
        cel.borrarEspacio();
        System.out.println("Después:");
        cel.mostrar();
    }
}