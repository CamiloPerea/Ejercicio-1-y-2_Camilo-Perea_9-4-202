class Transportadora:
    def __init__(self):
        self.despachos = {}
        self.numero_despacho = 1

    def realizar_despacho(self, placa_vehiculo, descripcion_vehiculo, nombre_conductor, ruta, descripcion_carga):
        self.despachos[self.numero_despacho] = {
            'placa_vehiculo': placa_vehiculo,
            'descripcion_vehiculo': descripcion_vehiculo,
            'nombre_conductor': nombre_conductor,
            'ruta': ruta,
            'descripcion_carga': descripcion_carga
        }
        self.numero_despacho += 1

    def mostrar_despachos(self):
        for numero, despacho in self.despachos.items():
            print(f"Número de Despacho: {numero}")
            print(f"Placa del Vehículo: {despacho['placa_vehiculo']}")
            print(f"Descripción del Vehículo: {despacho['descripcion_vehiculo']}")
            print(f"Nombre del Conductor: {despacho['nombre_conductor']}")
            print(f"Ruta: {despacho['ruta']}")
            print(f"Descripción de la Carga: {despacho['descripcion_carga']}")
            print("-------------------------")


transportadora = Transportadora()


transportadora.realizar_despacho("XTZ125", "HILUX", "Cristiano ronaldo", "Francia-España", "Carga de alimentos")
transportadora.realizar_despacho("YYZ250" "Land cruiser prado, "Messi nazario" "Alemani-Colombia", "Carga de electrónicos")
transportadora.realizar_despacho("CRF250", "CADILACC", "Camilo Pera", " Medellin-Cali", "Carga de mudanzas ")

transportadora.mostrar_despachos()