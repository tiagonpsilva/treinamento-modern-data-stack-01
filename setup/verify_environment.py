#!/usr/bin/env python3
"""
Script para verificar se o ambiente está configurado corretamente
para o treinamento Modern Data Stack.
"""

import os
import sys
import subprocess
import pkg_resources
import platform
from typing import Dict, List, Tuple
import json
from datetime import datetime

def print_header(message: str) -> None:
    """Imprime um cabeçalho formatado."""
    print("\n" + "="*80)
    print(f" {message}")
    print("="*80)

def check_python_version() -> Tuple[bool, str]:
    """Verifica se a versão do Python é compatível."""
    current_version = sys.version_info
    required_version = (3, 8)
    
    is_compatible = current_version >= required_version
    message = f"Python {current_version.major}.{current_version.minor}.{current_version.micro}"
    
    return is_compatible, message

def check_pip_packages() -> List[Tuple[str, bool, str]]:
    """Verifica se os pacotes pip requeridos estão instalados."""
    required_packages = {
        'apache-airflow': '2.7.1',
        'dbt-core': '1.6.0',
        'dbt-bigquery': '1.6.0',
        'google-cloud-bigquery': '3.11.4',
        'pyspark': '3.4.1',
        'requests': '2.31.0',
        'python-dotenv': '1.0.0',
        'pytest': '7.4.2',
        'jupyter': '1.0.0'
    }
    
    results = []
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    for package, required_version in required_packages.items():
        installed_version = installed_packages.get(package)
        is_installed = installed_version is not None
        message = f"{package}: {installed_version if is_installed else 'não instalado'} (requerido: {required_version})"
        results.append((package, is_installed, message))
    
    return results

def check_docker() -> Tuple[bool, str]:
    """Verifica se o Docker está instalado e rodando."""
    try:
        docker_version = subprocess.check_output(['docker', '--version']).decode().strip()
        # Tenta rodar um container de teste
        subprocess.check_output(['docker', 'run', '--rm', 'hello-world'])
        return True, docker_version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, "Docker não encontrado ou não está rodando"

def check_environment_variables() -> List[Tuple[str, bool]]:
    """Verifica variáveis de ambiente necessárias."""
    required_vars = [
        'GOOGLE_APPLICATION_CREDENTIALS',
        'AIRFLOW_HOME'
    ]
    
    results = []
    for var in required_vars:
        exists = var in os.environ
        results.append((var, exists))
    
    return results

def check_disk_space(min_gb: int = 20) -> Tuple[bool, str]:
    """Verifica se há espaço em disco suficiente."""
    if platform.system() == 'Windows':
        import ctypes
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p("."), None, None, ctypes.pointer(free_bytes))
        free_gb = free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs('.')
        free_gb = (st.f_bavail * st.f_frsize) / (1024 * 1024 * 1024)
    
    has_space = free_gb >= min_gb
    message = f"{free_gb:.1f}GB livre (mínimo: {min_gb}GB)"
    
    return has_space, message

def generate_report(all_checks: Dict) -> str:
    """Gera um relatório em formato JSON com os resultados."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "system": {
            "platform": platform.system(),
            "release": platform.release(),
            "machine": platform.machine()
        },
        "checks": all_checks
    }
    
    return json.dumps(report, indent=2)

def main():
    all_checks = {}
    
    # Verifica Python
    print_header("Verificando versão do Python")
    python_ok, python_message = check_python_version()
    print(f"✓ {python_message}" if python_ok else f"✗ {python_message}")
    all_checks["python"] = {"ok": python_ok, "message": python_message}
    
    # Verifica pacotes pip
    print_header("Verificando pacotes Python")
    pip_results = check_pip_packages()
    for package, is_installed, message in pip_results:
        print(f"{'✓' if is_installed else '✗'} {message}")
    all_checks["pip_packages"] = [{"package": p, "installed": i, "message": m} for p, i, m in pip_results]
    
    # Verifica Docker
    print_header("Verificando Docker")
    docker_ok, docker_message = check_docker()
    print(f"✓ {docker_message}" if docker_ok else f"✗ {docker_message}")
    all_checks["docker"] = {"ok": docker_ok, "message": docker_message}
    
    # Verifica variáveis de ambiente
    print_header("Verificando variáveis de ambiente")
    env_results = check_environment_variables()
    for var, exists in env_results:
        print(f"{'✓' if exists else '✗'} {var}")
    all_checks["environment_variables"] = [{"variable": v, "exists": e} for v, e in env_results]
    
    # Verifica espaço em disco
    print_header("Verificando espaço em disco")
    space_ok, space_message = check_disk_space()
    print(f"✓ {space_message}" if space_ok else f"✗ {space_message}")
    all_checks["disk_space"] = {"ok": space_ok, "message": space_message}
    
    # Gera relatório
    print_header("Gerando relatório")
    report = generate_report(all_checks)
    report_path = "environment_check_report.json"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Relatório completo salvo em: {report_path}")
    
    # Verifica se há problemas críticos
    critical_issues = not all([
        python_ok,
        docker_ok,
        space_ok,
        any(installed for _, installed, _ in pip_results)
    ])
    
    if critical_issues:
        print("\n⚠️  ATENÇÃO: Foram encontrados problemas críticos que precisam ser resolvidos.")
        sys.exit(1)
    else:
        print("\n✅ Ambiente configurado corretamente!")
        sys.exit(0)

if __name__ == "__main__":
    main() 