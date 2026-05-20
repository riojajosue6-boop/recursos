import os
from flask import Flask, render_template_string

app = Flask(__name__)

# BANCO DE DATOS DE RECURSOS PREMIUM (100% Útiles y Reales)
RECURSOS_BASE = [
    {
        "id": "rec_01",
        "categoria": "📊 PLANTILLA EXCEL",
        "titulo": "Control Financiero Pro 2026",
        "descripcion": "Automatiza tus ingresos, gastos mensuales y ahorros con gráficos dinámicos integrados. Ideal para ordenar tus finanzas personales.",
        "icono": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy" # Enlace demo de copia limpia
    },
    {
        "id": "rec_02",
        "categoria": "📚 LIBRO PDF",
        "titulo": "El Hombre Más Rico de Babilonia",
        "descripcion": "El clásico eterno sobre educación financiera y las leyes del oro. Edición digital limpia en PDF lista para leer en tu celular.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://www.gutenberg.org/" # Enlace demo de biblioteca pública
    },
    {
        "id": "rec_03",
        "categoria": "🚀 MARKETING DIGITAL",
        "titulo": "50 Ganchos (Hooks) Virales para TikTok",
        "descripcion": "La lista definitiva de títulos persuasivos para capturar la atención en 3 segundos y reventar el algoritmo vendiendo en Hotmart.",
        "icono": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&auto=format&fit=crop&q=80",
        "enlace_descarga": "https://www.canva.com/" # Enlace demo a Canva
    }
]

# INTERFAZ WEB PREMIUM OPTIMIZADA PARA TELEGRAM MINI APPS (Dark Mode Neón)
HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Flow Recursos Pro</title>
    <style>
        body {
            background-color: #08090c;
            color: #e2e8f0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .app-container {
            width: 100%;
            max-width: 440px; /* Ajuste estricto para pantalla de Telegram */
            background: #11141a;
            border-radius: 16px;
            padding: 16px;
            box-sizing: border-box;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
            border: 1px solid #1e2530;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 22px;
            color: #00ffcc;
            margin: 0 0 4px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .subtitle {
            font-size: 12px;
            color: #718096;
            margin: 0;
        }
        .search-box {
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
        }
        input {
            flex: 1;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #2d3748;
            background: #08090c;
            color: #ffffff;
            font-size: 14px;
            outline: none;
        }
        input:focus {
            border-color: #00ffcc;
        }
        button {
            padding: 12px 18px;
            border-radius: 8px;
            border: none;
            background: #00ffcc;
            color: #08090c;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.2s;
        }
        .card {
            background: #1a1f2c;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 18px;
            border: 1px solid #232a3b;
            display: flex;
            flex-direction: column;
        }
        .card-img {
            width: 100%;
            height: 140px;
            object-fit: cover;
        }
        .card-body {
            padding: 14px;
        }
        .badge {
            font-size: 10px;
            font-weight: bold;
            color: #08090c;
            background: #00ffcc;
            padding: 3px 8px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 8px;
        }
        .card-title {
            font-size: 16px;
            font-weight: bold;
            color: #ffffff;
            margin: 0 0 6px 0;
        }
        .card-text {
            font-size: 13px;
            color: #a0aec0;
            line-height: 1.4;
            margin-bottom: 14px;
        }
        .btn-download {
            display: block;
            text-align: center;
            background: #10b981;
            color: white;
            text-decoration: none;
            padding: 12px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
            transition: background 0.2s;
        }
        .btn-download:hover {
            background: #059669;
        }
    </style>
</head>
<body>

<div class="app-container">
    <div class="header">
        <h1>⚡ FLOW RECURSOS ⚡</h1>
        <p class="subtitle">Herramientas Pro para Emprendedores y Afiliados</p>
    </div>
    
    <div class="search-box">
        <input type="text" id="search-input" placeholder="¿Qué herramienta buscas hoy?">
        <button onclick="buscarRecurso()">Buscar</button>
    </div>

    <div id="resources-list">
        {% for item in recursos %}
        <div class="card">
            <img class="card-img" src="{{ item.icono }}" alt="Recurso">
            <div class="card-body">
                <span class="badge">{{ item.categoria }}</span>
                <div class="card-title">{{ item.titulo }}</div>
                <div class="card-text">{{ item.descripcion }}</div>
                
                <a href="#" class="btn-download" onclick="descargarConMonetizacion('{{ item.enlace_descarga }}'); return false;">
                    📥 DESCARGAR GRATIS
                </a>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
    function descargarConMonetizacion(urlFinal) {
        // 💰 AQUÍ SE INYECTARÁ TU SMARTLINK DE MONETAG EN EL SIGUIENTE PASO
        // Por ahora redirige directo al archivo limpio para verificar que la ruta es estable.
        console.log("Abriendo pasarela de descarga segura...");
        window.open(urlFinal, '_blank');
    }

    function buscarRecurso() {
        alert("Buscador verificado. Listos para activar los filtros en el próximo paso.");
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
