from netmiko import ConnectHandler
import time

# Información de acceso a los routers
routers = [
    {"host": "192.168.10.129", "username": "admin", "password": "inacap2024", "device_type": "cisco_ios"},
    {"host": "192.168.12.2", "username": "admin1", "password": "inacap2025", "device_type": "cisco_ios"},
    {"host": "192.168.23.2", "username": "admin2", "password": "inacap2026", "device_type": "cisco_ios"},
    {"host": "192.168.34.2", "username": "admin3", "password": "inacap2027", "device_type": "cisco_ios"}
]


# Función para conectarse a cada router y obtener el running-config
def backup_running_config(router):
    try:
        # Establecer la conexión SSH con el router
        print(f"Conectando a {router['host']}...")
        connection = ConnectHandler(**router)

        # Obtener el running-config
        print(f"Obteniendo running-config de {router['host']}...")
        running_config = connection.send_command("show running-config")

        # Guardar el running-config en un archivo
        with open(f"backup_{router['host']}_running_config.txt", "w") as file:
            file.write(running_config)

        print(f"Backup completado para {router['host']}")
        connection.disconnect()

    except Exception as e:
        print(f"Error al conectar o hacer backup en {router['host']}: {e}")


# Realizar el backup en cada router
for router in routers:
    backup_running_config(router)

print("Proceso de backup finalizado para todos los routers.")
