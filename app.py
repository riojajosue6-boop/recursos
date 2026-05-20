import os
from flask import Flask, render_template_string

# 🚨 ESTA ES LA LÍNEA QUE GUNICORN ESTÁ BUSCANDO Y NO ENCONTRABA:
app = Flask(__name__)

# BANCO DE DATOS DE RECURSOS (Formato de Oficina Ejecutivo)
RECURSOS_BASE = [
    {
        "id": "rec_01",
        "categoria": "📌 PLANTILLA EXCEL",
        "titulo": "Control Financiero Pro",
        "descripcion": "Gestión de ingresos, egresos y balances con cuadros dinámicos automatizados.",
        "icono": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy"
    },
    {
        "id": "rec_02",
        "categoria": "📌 AUDIOLIBRO / PDF",
        "titulo": "El Hombre Más Rico de Babilonia",
        "descripcion": "Principios fundamentales de ahorro y leyes del oro. Formato digital de estudio.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://www.gutenberg.org/"
    },
    {
        "id": "rec_03",
        "categoria": "📌 MARKETING DIGITAL",
        "titulo": "50 Ganchos Virales TikTok",
        "descripcion": "Estructuras de copy persuasivo para retener tráfico orgánico en lanzamientos.",
        "icono": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://www.canva.com/"
    }
]

# INTERFAZ PROFESIONAL SERIA (Diseño "Executive Clean")
HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Flow Recursos Pro</title>
    <style>
        body {
            background-color: #f8fafc; /* Gris claro de oficina para descanso visual */
            color: #334155; /* Texto carbón suave */
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .app-container {
            width: 100%;
            max-width: 440px; /* Tamaño optimizado para vista móvil en Telegram */
            background: #ffffff;
            border-radius: 8px;
            padding: 20px;
            box-sizing: border-box;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }
        .header {
            text-align: center;
            margin-bottom: 25px;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 15px;
        }
        h1 {
            font-size: 20px;
            color: #1e293b; /* Azul marino corporativo */
            margin: 0 0 4px 0;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        .subtitle {
            font-size: 12px;
            color: #64748b;
            margin: 0;
        }
        .grid-container {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .card {
            background: #ffffff;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: row; /* Formato horizontal para hacer cuadros más compactos */
            overflow: hidden;
            height: 105px;
        }
        .card-img {
            width: 90px;
            height: 105px;
            object-fit: cover;
            border-right: 1px solid #e2e8f0;
        }
        .card-body {
            padding: 10px 12px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            flex: 1;
        }
        .badge {
            font-size: 9px;
            font-weight: bold;
            color: #475569;
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 3px;
            align-self: flex-start;
            text-transform: uppercase;
        }
        .card-title {
            font-size: 14px;
            font-weight: 600;
            color: #0f172a;
            margin: 3px 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .card-text {
            font-size: 11px;
            color: #627185;
            line-height: 1.3;
            margin-bottom: 4px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .btn-download {
            display: block;
            text-align: center;
            background: #1e293b; /* Botón sobrio azul oscuro */
            color: #ffffff;
            text-decoration: none;
            padding: 6px 0;
            border-radius: 4px;
            font-weight: 600;
            font-size: 11px;
            transition: background 0.2s;
        }
        .btn-download:hover {
            background: #0f172a;
        }
    </style>
</head>
<body>

<div class="app-container">
    <div class="header">
        <h1>Flow Recursos Pro</h1>
        <p class="subtitle">Biblioteca Ejecutiva de Herramientas y Conocimiento</p>
    </div>

    <div class="grid-container" id="resources-list">
        {% for item in recursos %}
        <div class="card">
            <img class="card-img" src="{{ item.icono }}" alt="Recurso">
            <div class="card-body">
                <div>
                    <span class="badge">{{ item.categoria }}</span>
                    <div class="card-title">{{ item.titulo }}</div>
                    <div class="card-text">{{ item.descripcion }}</div>
                </div>
                <a href="#" class="btn-download" onclick="descargarRecurso('{{ item.enlace_descarga }}'); return false;">
                    ACCEDER AL MATERIAL
                </a>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    function descargarRecurso(urlFinal) {
        console.log("Pasarela corporativa segura.");
        window.open(urlFinal, '_blank');
    }
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_FRONTEND, recursos=RECURSOS_BASE)

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto)
