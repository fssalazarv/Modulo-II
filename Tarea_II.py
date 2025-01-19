ventas = [
    {
        "fecha": "12-01-2023",
        "producto": "Producto_A",
        "cantidad": 50,
        "precio": 45.00,
        "promocion": True
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_AX",
        "cantidad": 160,
        "precio": 12.00,
        "promocion": False
    },
    {
        "fecha": "10-01-2023",
        "producto": "Producto_D",
        "cantidad": 20,
        "precio": 15.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_C",
        "cantidad": 10,
        "precio": 140.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_D",
        "cantidad": 1200,
        "precio": 1.00,
        "promocion": True
    }
]

def menu():
    while True:
        print("\n=== Menú de Ventas ===")
        print("1. Mostrar listado de ventas")
        print("2. Agregar un producto")
        print("3. Calcular suma total de ventas")
        print("4. Calcular promedio de ventas")
        print("5. Mostrar producto más vendido")
        print("6. Mostrar listado de productos")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: ").strip())

            if opcion == 1:
                print("\nListado de Ventas:")
                for venta in ventas:
                    print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {'Sí' if venta['promocion'] else 'No'}")
            elif opcion == 2:
                try:
                    fecha = input("Ingrese la fecha (dd-mm-yyyy): ")
                    producto = input("Ingrese el nombre del producto: ").strip()
                    cantidad = int(input("Ingrese la cantidad: "))
                    precio = float(input("Ingrese el precio: "))
                    promocion = input("¿Está en promoción? (si/no): ").strip().lower() == 'si'

                    nueva_venta = {
                        "fecha": fecha,
                        "producto": producto,
                        "cantidad": cantidad,
                        "precio": precio,
                        "promocion": promocion
                    }
                    ventas.append(nueva_venta)
                    print(f"Producto '{producto}' agregado exitosamente.")
                except ValueError:
                    print("Error: Asegúrese de ingresar valores válidos.")
            elif opcion == 3:
                suma_total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
                print(f"\nLa suma total de las ventas es: {suma_total:.2f}")
            elif opcion == 4:
                if ventas:
                    promedio = sum(venta['cantidad'] * venta['precio'] for venta in ventas) / len(ventas)
                    print(f"\nEl promedio de ventas es: {promedio:.2f}")
                else:
                    print("\nNo hay ventas registradas para calcular el promedio.")
            elif opcion == 5:
                if ventas:
                    mas_vendido = max(ventas, key=lambda venta: venta['cantidad'])
                    print(f"\nEl producto más vendido es: {mas_vendido['producto']} con {mas_vendido['cantidad']} unidades.")
                else:
                    print("\nNo hay ventas registradas para determinar el producto más vendido.")
            elif opcion == 6:
                productos = {venta['producto'] for venta in ventas}
                print("\nListado de Productos:")
                for producto in productos:
                    print(f"- {producto}")
            elif opcion == 7:
                print("\nGracias por usar el sistema de ventas. Hasta luego.")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 7.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 7.")

# Ejecutar el menú
menu()