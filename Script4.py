import subprocess

resultado = subprocess.run(
    ["ps", "-eo", "pid,comm,%mem,rss", "--sort=-%mem"],
    capture_output=True,
    text=True
)

lineas = resultado.stdout.strip().split("\n")

print(f"{'PID':<10} {'PROCESO':<25} {'RAM %':<10} {'RAM MB':<10}")
print("-" * 55)

for linea in lineas[1:4]:
    partes = linea.split()

    pid = partes[0]
    proceso = partes[1]
    ram_porcentaje = partes[2]
    ram_kb = int(partes[3])
    ram_mb = ram_kb / 1024

    print(
        f"{pid:<10} "
        f"{proceso:<25} "
        f"{ram_porcentaje:<10} "
        f"{ram_mb:.2f} MB"
    )