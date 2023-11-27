import atexit
import os
import shutil
from datetime import datetime
from pathlib import Path

def organizar_media():
    try:
        carpeta_origen = input("Por favor, ingresa la ruta de la carpeta de origen: ")
        if not os.path.exists(carpeta_origen):
            raise FileNotFoundError("La carpeta de origen no existe.")
        
        carpeta_destino = Path.cwd() / "almacen"
        carpeta_destino.mkdir(parents=True, exist_ok=True)

        multimedia_extensions = {".jpg", ".jpeg", ".png", ".gif", ".mp4", ".avi", ".mov"}

        for file_path in Path(carpeta_origen).rglob("*"):
            if file_path.suffix.lower() in multimedia_extensions:
                file_time = os.path.getmtime(file_path)
                file_year = datetime.fromtimestamp(file_time).strftime("%Y")
                file_month = datetime.fromtimestamp(file_time).strftime("%m")

                nueva_carpeta_path = carpeta_destino / file_year / file_month
                nueva_carpeta_path.mkdir(parents=True, exist_ok=True)

                destino_file_path = nueva_carpeta_path / file_path.name

                if not destino_file_path.exists():
                    shutil.copy2(file_path, destino_file_path)
                    print(f"Archivo copiado a {nueva_carpeta_path}")
                else:
                    print(f"El archivo ya existe en {nueva_carpeta_path}")

        # Llamamos a la función para eliminar duplicados después de organizar
        carpeta_a_examinar = carpeta_destino
        duplicados_encontrados = encontrar_duplicados(carpeta_a_examinar)

        if duplicados_encontrados:
            print("Archivos duplicados encontrados:")
            for duplicado in duplicados_encontrados:
                print(f"Duplicado 1: {duplicado[0]}\nDuplicado 2: {duplicado[1]}\n")

            respuesta = input("¿Quieres eliminar los archivos duplicados? (s/n): ").lower()

            if respuesta == 's':
                eliminar_duplicados(duplicados_encontrados)
                print("Archivos duplicados eliminados.")
            else:
                print("No se eliminaron archivos duplicados.")
        else:
            print("No se encontraron archivos duplicados.")

    except Exception as e:
        print(f"Error: {e}")

def autoejecutar():
    input("Presiona Enter para organizar los archivos...")
    organizar_media()

def encontrar_duplicados(ruta):
    hash_dict = {}
    duplicados = []
    archivos_examinados = 0

    for carpeta_raiz, carpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_raiz, archivo)
            info_archivo = (os.path.getsize(ruta_completa), os.path.getmtime(ruta_completa))

            if info_archivo in hash_dict:
                duplicados.append((ruta_completa, hash_dict[info_archivo]))
            else:
                hash_dict[info_archivo] = ruta_completa

            archivos_examinados += 1

    print(f"Archivos examinados: {archivos_examinados}")
    return duplicados

def eliminar_duplicados(duplicados):
    for duplicado in duplicados:
        ruta_archivo = duplicado[0]

        if os.path.exists(ruta_archivo):
            print(f"Eliminando duplicado: {ruta_archivo}")
            os.remove(ruta_archivo)
        else:
            print(f"El archivo ya fue eliminado o no se encuentra: {ruta_archivo}")

if __name__ == "__main__":
    atexit.register(autoejecutar)
    organizar_media()
