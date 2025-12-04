import os

# Ruta donde se genera el reporte
REPORT_DIR = "sos_mascota/mutation-test-report"

# El diseño que queremos inyectar (CSS + Botón)
CUSTOM_STYLE = """
<style>
    /* Forzar tipografía y colores de SOS Mascota */
    body { font-family: 'Segoe UI', sans-serif !important; background-color: #f4f4f9 !important; color: #333 !important; }
    
    /* Encabezados */
    h1 { color: #008080 !important; text-align: center; margin-top: 20px; }
    a { color: #008080 !important; text-decoration: none; font-weight: bold; }
    a:hover { text-decoration: underline; }

    /* Tablas mejoradas */
    table { 
        border-collapse: collapse !important; 
        width: 90% !important; 
        margin: 20px auto !important; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); 
        background: white; 
        border-radius: 8px; 
        overflow: hidden; 
    }
    th { background-color: #008080 !important; color: white !important; padding: 12px !important; }
    td { padding: 12px !important; border-bottom: 1px solid #eee !important; }
    tr:hover { background-color: #f1fcfc !important; }

    /* Botón flotante para volver */
    .btn-back {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #005f5f;
        color: white !important;
        padding: 10px 20px;
        border-radius: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        z-index: 1000;
        text-decoration: none !important;
    }
    .btn-back:hover { background-color: #004040; transform: translateY(-2px); }
</style>

<a href="../../index.html" class="btn-back">⬅ Volver al Dashboard</a>
"""

def apply_styles():
    if not os.path.exists(REPORT_DIR):
        print(f"⚠️ No se encontró la carpeta del reporte: {REPORT_DIR}")
        return

    # Buscar todos los archivos HTML en la carpeta (index.html y los detalles)
    count = 0
    for root, dirs, files in os.walk(REPORT_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Inyectar el estilo antes del cierre del body
                if "</body>" in content:
                    new_content = content.replace("</body>", CUSTOM_STYLE + "\n</body>")
                    
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1

    print(f"✅ Estilos aplicados exitosamente a {count} archivos.")

if __name__ == "__main__":
    apply_styles()