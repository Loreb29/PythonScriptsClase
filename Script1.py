import subprocess
import re

# Obtener conexiones y puertos
netstat = subprocess.check_output(
    ["netstat", "-ano"],
    text=True,
    encoding="cp850",
    errors="ignore"
)

# Obtener procesos
tasklist = subprocess.check_output(
    ["tasklist", "/FO", "CSV", "/NH"],
    text=True,
    encoding="cp850",
    errors="ignore"
)

processes = {}

for line in tasklist.splitlines():
    parts = line.split('","')
    if len(parts) >= 2:
        name = parts[0].strip('"')
        pid = parts[1].strip('"')
        processes[pid] = name

print(f"{'PROTO':<6} {'DIRECCIÓN LOCAL':<25} {'DIRECCIÓN REMOTA':<25} {'ESTADO':<15} {'PID':<8} PROCESO")
print("-" * 105)

for line in netstat.splitlines():
    parts = line.split()

    if len(parts) >= 4 and parts[0] in ("TCP", "UDP"):
        protocol = parts[0]
        local = parts[1]
        remote = parts[2]

        if protocol == "TCP":
            state = parts[3]
            pid = parts[4]
        else:
            state = "-"
            pid = parts[3]

        process = processes.get(pid, "Desconocido")

        print(
            f"{protocol:<6} "
            f"{local:<25} "
            f"{remote:<25} "
            f"{state:<15} "
            f"{pid:<8} "
            f"{process}"
        )