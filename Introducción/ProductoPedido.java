package Introducción;
import java.util.ArrayList;
class Producto {
    String nombre;
    double precio;
    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
    public void mostrar() {
        System.out.println("Producto: " + nombre + ", Precio: Bs " + precio);
    }
}
class Pedido {
    ArrayList<Producto> productos;
    String estado;
    public Pedido() {
        productos = new ArrayList<Producto>();
        estado = "registrado";
    }
    public void agregarProducto(Producto p) {
        productos.add(p);
    }
    public void cambiarEstado(String nuevo) {
        estado = nuevo;
    }
    public void mostrar() {
        System.out.println("Pedido:");
        for (Producto p : productos) {
            p.mostrar();
        }
        System.out.println("Estado actual: " + estado);
    }
    public static void main(String[] args) {
        Producto p1 = new Producto("Café", 10);
        Producto p2 = new Producto("Croissant", 12);
        Pedido pedido = new Pedido();
        pedido.agregarProducto(p1);
        pedido.agregarProducto(p2);
        pedido.mostrar();
        pedido.cambiarEstado("preparado");
        pedido.mostrar();
        pedido.cambiarEstado("entregado");
        pedido.mostrar();
    }
}