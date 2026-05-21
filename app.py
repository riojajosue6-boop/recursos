import os
from flask import Flask, render_template_string

app = Flask(__name__)

# BANCO DE DATOS MULTIMEDIA EVOLUCIONADO (Soporta archivos únicos y Cursos por Módulos)
RECURSOS_BASE = [
    # 1. CATEGORÍA: EXCEL
    {
        "id": "ex_01",
        "categoria": "excel",
        "badge": "📊 PLANTILLA",
        "titulo": "Control Financiero Pro",
        "descripcion": "Gestión de ingresos, egresos y balances con cuadros dinámicos automatizados.",
        "icono": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&auto=format&fit=crop&q=80",
        # Al tener un solo elemento en la lista, se comporta como archivo único directo
        "archivos": [
            {"titulo": "Plantilla Control Financiero Pro", "tipo": "excel", "url": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy"}
        ]
    },
    # 2. CATEGORÍA: AUDIO
    {
        "id": "au_01",
        "categoria": "audio",
        "badge": "🎧 AUDIOLIBRO",
        "titulo": "El Hombre Más Rico de Babilonia",
        "descripcion": "Audiolibro completo organizado por capítulos para dominar las leyes del oro y la riqueza.",
        "icono": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400&auto=format&fit=crop&q=80",
        # EJEMPLO DE AUDIO MULTI-MÓDULO (Capítulos individuales)
        "archivos": [
            {"titulo": "Capítulo 1: El hombre que deseaba oro", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
            {"titulo": "Capítulo 2: El hombre más rico de Babilonia", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
            {"titulo": "Capítulo 3: Las siete maneras de llenar una bolsa vacía", "tipo": "audio", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"}
        ]
    },
    # 3. CATEGORÍA: VIDEO
    {
        "id": "vi_01",
        "categoria": "video",
        "badge": "🎬 VIDEO CLASE",
        "titulo": "Estrategia de Ventas Hotmart",
        "descripcion": "Masterclass ejecutiva para ajustar embudos de venta orgánica de alta conversión.",
        "icono": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {"titulo": "Clase Única: Embudo Orgánico Pro", "tipo": "video", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"}
        ]
    },
    # 4. CATEGORÍA: PDF (Tu súper curso de 8 módulos o más)
    {
        "id": "pdf_01",
        "categoria": "pdf",
        "badge": "📖 GUÍA TEXTO",
        "titulo": "50 Ganchos Virales TikTok",
        "descripcion": "Manual en PDF con copys persuasivos listos para enganchar tráfico en 3 segundos.",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        "archivos": [
            {"titulo": "Manual de Ganchos Persuasivos", "tipo": "pdf", "url": "https://pdfobject.com/pdf/sample.pdf"}
        ]
    },
    {
        "id": "pdf_02",
        "categoria": "pdf",
        "badge": "🎓 ACADEMIA COMPLETA",
        "titulo": "Programa: Cómo Vender Cuando Nadie Está Comprando",
        "descripcion": "Accede a los módulos oficiales y guías estratégicas de este entrenamiento para hackear mercados difíciles y vender infoproductos con éxito.",
        "icono": "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&auto=format&fit=crop&q=80",
        # 🎯 AQUÍ ESTÁ LA SOLUCIÓN REVOLUCIONARIA PARA TUS MÓDULOS MULTIMEDIA:
        "archivos": [
            {
                "titulo": "Módulo 1: Redireccionar la mente ante la crisis", 
                "tipo": "pdf", 
                "url": "https://f005.backblazeb2.com/file/Material-recursos/Material-PDF/EBOOK_COMO_VENDER_CUANDO_NADIE_ESTA_COMPRANDO_2_.pdf"
            },
            {
                "titulo": "Módulo 2: Encontrando el nuevo ángulo de negocio", 
                "tipo": "pdf", 
                "url": "https://pdfobject.com/pdf/sample.pdf"
            },
            {
                "titulo": "Módulo 3: Video Complementario - Embudo de Rompimiento", 
                "tipo": "video", 
                "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
            },
            {
                "titulo": "Módulo 4: Calculadora de Metas y Comisiones", 
                "tipo": "excel", 
                "url": "https://docs.google.com/spreadsheets/d/1u6Vb2S3XbEEX87RjX647b0H_M8X4X_X8/copy"
            }
        ]
    }
]

HTML_FRONTEND = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Flow Recursos Pro</title>
    <style>
        body {
            background-color: #f8fafc;
            color: #334155;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0; padding: 15px;
            display: flex; flex-direction: column; align-items: center;
        }
        .app-container {
            width: 100%; max-width: 440px;
            background: #ffffff; border-radius: 8px; padding: 20px;
            box-sizing: border-box; box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }
        .header {
            text-align: center; margin-bottom: 20px;
            border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;
        }
        h1 { font-size: 19px; color: #1e293b; margin: 0; font-weight: 700; }
        .subtitle { font-size: 11px; color: #64748b; margin: 4px 0 0 0; }
        
        .tabs-menu {
            display: flex; justify-content: space-between;
            background: #f1f5f9; border-radius: 6px;
            padding: 4px; margin-bottom: 20px; gap: 4px;
        }
        .tab-btn {
            flex: 1; border: none; background: transparent;
            color: #64748b; font-size: 11px; font-weight: 600;
            padding: 8px 0; border-radius: 4px; cursor: pointer;
            text-align: center; transition: all 0.2s;
        }
        .tab-btn.active {
            background: #ffffff; color: #1e293b;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        
        .resources-grid { display: flex; flex-direction: column; gap: 12px; }
        
        .card {
            background: #ffffff; border-radius: 6px; border: 1px solid #e2e8f0;
            display: flex; flex-direction: row; overflow: hidden; min-height: 110px; height: auto;
        }
        .card-img { width: 95px; min-height: 110px; object-fit: cover; border-right: 1px solid #e2e8f0; }
        .card-body { padding: 10px 12px; display: flex; flex-direction: column; justify-content: space-between; flex: 1; min-width: 0; }
        .badge {
            font-size: 9px; font-weight: bold; color: #475569;
            background: #f1f5f9; padding: 2px 6px; border-radius: 3px; align-self: flex-start;
        }
        .card-title { font-size: 13.5px; font-weight: 600; color: #0f172a; margin: 4px 0 4px 0; }
        
        .card-text { 
            font-size: 11px; 
            color: #627185; 
            line-height: 1.4; 
            margin-bottom: 10px; 
            overflow: visible; 
            white-space: normal; 
        }
        
        .btn-action {
            display: block; text-align: center; background: #1e293b;
            color: #ffffff; text-decoration: none; padding: 7px 0;
            border-radius: 4px; font-weight: 600; font-size: 11px; margin-bottom: 2px;
        }

        /* MODAL MULTIMEDIA UNIFICADO INTELIGENTE */
        .global-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: rgba(15, 23, 42, 0.98);
            z-index: 1000;
            box-sizing: border-box;
            padding: 12px;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 10px 12px 10px;
        }
        .modal-header-left {
            display: flex; gap: 8px; align-items: center; max-width: 70%;
        }
        .modal-title {
            color: #ffffff; font-size: 14px; font-weight: 600;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }
        .btn-back-menu {
            display: none; background: #475569; color: white; border: none;
            padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 11px; cursor: pointer;
        }
        .close-btn {
            background: #ef4444; color: white; border: none;
            padding: 6px 14px; border-radius: 4px; font-weight: bold;
            font-size: 12px; cursor: pointer;
        }
        .modal-body-content {
            width: 100%;
            height: calc(100% - 50px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
        }
        
        /* DISEÑO DE LA LISTA DE MÓDULOS (ÍNDICE) */
        .modules-menu-container {
            width: 100%; max-width: 380px; height: 95%;
            display: flex; flex-direction: column; gap: 10px;
            overflow-y: auto; padding: 10px 0;
        }
        .module-list-btn {
            background: #1e293b; border: 1px solid #334155; border-radius: 6px;
            color: #ffffff; padding: 14px 16px; text-align: left; font-size: 12.5px;
            font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;
            transition: background 0.2s;
        }
        .module-list-btn:hover { background: #27374d; }
        .module-list-btn .icon-format { font-size: 14px; background: #334155; padding: 3px 6px; border-radius: 4px; }

        /* REPRODUCTORES */
        .fullscreen-frame { width: 100%; height: 100%; border: none; border-radius: 6px; background: #ffffff; }
        .fullscreen-video { width: 100%; max-height: 85%; border-radius: 6px; outline: none; background: #000000; }
        
        .audio-modal-card {
            background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 30px 20px;
            width: 90%; max-width: 360px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        .audio-modal-card .audio-icon { font-size: 45px; margin-bottom: 15px; }
        .audio-modal-card .audio-title { color: #ffffff; font-size: 15px; font-weight: bold; margin-bottom: 20px; }
        
        .excel-modal-card {
            background: #ffffff; border-radius: 12px; padding: 35px 25px;
            width: 90%; max-width: 360px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }
        .excel-modal-card .excel-icon { font-size: 50px; margin-bottom: 15px; }
        .excel-modal-card .excel-title { color: #1e293b; font-size: 16px; font-weight: 700; margin-bottom: 8px; }
        .excel-modal-card .excel-desc { color: #64748b; font-size: 12px; margin-bottom: 25px; line-height: 1.4; }
        .btn-excel-download {
            display: inline-block; background: #10b981; color: white; text-decoration: none;
            padding: 12px 24px; border-radius: 6px; font-weight: bold; font-size: 13px;
        }
    </style>
</head>
<body>

<div class="app-container">
    <div class="header">
        <h1>Flow Recursos Pro</h1>
        <p class="subtitle">Panel Corporativo de Capacitación Digital</p>
    </div>

    <div class="tabs-menu">
        <button class="tab-btn active" onclick="filtrarCategoria('excel', this)">Excel</button>
        <button class="tab-btn" onclick="filtrarCategoria('audio', this)">Audios</button>
        <button class="tab-btn" onclick="filtrarCategoria('video', this)">Videos</button>
        <button class="tab-btn" onclick="filtrarCategoria('pdf', this)">PDFs</button>
    </div>

    <div class="resources-grid" id="resources-list">
        {% for item in recursos %}
        <div class="card resource-item" data-category="{{ item.categoria }}">
            <img class="card-img" src="{{ item.icono }}" alt="Recurso">
            <div class="card-body">
                <div>
                    <span class="badge">{{ item.badge }}</span>
                    <div class="card-title">{{ item.titulo }}</div>
                    <div class="card-text">{{ item.descripcion }}</div>
                </div>
                
                <div>
                    <a href="#" class="btn-action" onclick="analizarRecurso('{{ item.titulo }}', '{{ item.descripcion }}', {{ item.archivos|tojson|safe }}); return false;">
                        ABRIR CONTENIDO
                    </a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<div id="recurso-modal-global" class="global-modal">
    <div class="modal-header">
        <div class="modal-header-left">
            <button id="btn-modal-back" class="btn-back-menu" onclick="regresarAlIndice()">⬅ MENÚ</button>
            <div id="modal-global-title" class="modal-title">Visualizador</div>
        </div>
        <button class="close-btn" onclick="cerrarRecursoGlobal()">✕ CERRAR</button>
    </div>
    <div id="modal-global-body" class="modal-body-content">
        </div>
</div>

<script>
    // Variables temporales de control para el módulo académico
    let cacheTituloCurso = "";
    let cacheDescripcionCurso = "";
    let cacheArchivosCurso = [];

    function filtrarCategoria(categoria, botonActivo) {
        let botones = document.querySelectorAll('.tab-btn');
        botones.forEach(btn => btn.classList.remove('active'));
        botonActivo.classList.add('active');

        let tarjetas = document.querySelectorAll('.resource-item');
        tarjetas.forEach(tarjeta => {
            if (tarjeta.getAttribute('data-category') === categoria) {
                tarjeta.style.display = 'flex';
            } else {
                tarjeta.style.display = 'none';
            }
        });
    }

    // ANALIZADOR DE RUTA: Detecta si es archivo único o curso multi-módulos
    function analizarRecurso(tituloCurso, descripcionCurso, listaArchivos) {
        cacheTituloCurso = tituloCurso;
        cacheDescripcionCurso = descripcionCurso;
        cacheArchivosCurso = listaArchivos;

        if (listaArchivos.length === 1) {
            // Archivo Único: Abrir directo de golpe como antes
            document.getElementById('btn-modal-back').style.display = 'none';
            renderizarVisualizadorElemento(listaArchivos[0].tipo, listaArchivos[0].url, listaArchivos[0].titulo, descripcionCurso);
        } else {
            // Multi-Módulo: Construir e inyectar el menú de índice interactivo
            document.getElementById('btn-modal-back').style.display = 'none';
            construirIndiceInteractivo();
        }
        document.getElementById('recurso-modal-global').style.display = 'block';
    }

    // CONSTRUCTOR DEL ÍNDICE INTERACTIVO INTERNO
    function construirIndiceInteractivo() {
        document.getElementById('modal-global-title').innerText = cacheTituloCurso;
        var bodyModal = document.getElementById('modal-global-body');
        
        let htmlMenu = `<div class="modules-menu-container">`;
        
        cacheArchivosCurso.forEach((archivo, index) => {
            let prefijoIcono = "📄 PDF";
            if(archivo.tipo === 'video') prefijoIcono = "🎬 VIDEO";
            if(archivo.tipo === 'audio') prefijoIcono = "🎧 AUDIO";
            if(archivo.tipo === 'excel') prefijoIcono = "📊 EXCEL";

            htmlMenu += `
                <button class="module-list-btn" onclick="abrirElementoDesdeIndice(${index})">
                    <span>${archivo.titulo}</span>
                    <span class="icon-format">${prefijoIcono}</span>
                </button>`;
        });
        
        htmlMenu += `</div>`;
        bodyModal.innerHTML = htmlMenu;
    }

    // ACTIVADOR DE LECCIÓN DESDE EL MENÚ INTERNO
    function abrirElementoDesdeIndice(index) {
        let archivoSeleccionado = cacheArchivosCurso[index];
        // Activamos el botón para regresar al índice interno del curso
        document.getElementById('btn-modal-back').style.display = 'block';
        renderizarVisualizadorElemento(archivoSeleccionado.tipo, archivoSeleccionado.url, archivoSeleccionado.titulo, cacheDescripcionCurso);
    }

    function regresarAlIndice() {
        document.getElementById('btn-modal-back').style.display = 'none';
        construirIndiceInteractivo();
    }

    // NÚCLEO RENDERIZADOR MULTIMEDIA
    function renderizarVisualizadorElemento(tipo, url, titulo, descripcion) {
        var bodyModal = document.getElementById('modal-global-body');
        document.getElementById('modal-global-title').innerText = titulo;
        bodyModal.innerHTML = '';
        
        if (tipo === 'pdf') {
            bodyModal.innerHTML = `<iframe class="fullscreen-frame" src="${url}"></iframe>`;
        } else if (tipo === 'video') {
            bodyModal.innerHTML = `<video controls controlsList="nodownload" autoplay class="fullscreen-video"><source src="${url}" type="video/mp4"></video>`;
        } else if (tipo === 'audio') {
            bodyModal.innerHTML = `
                <div class="audio-modal-card">
                    <div class="audio-icon">🎧</div>
                    <div class="audio-title">${titulo}</div>
                    <audio controls controlsList="nodownload" autoplay style="width: 100%; outline: none;"><source src="${url}" type="audio/mpeg"></audio>
                </div>`;
        } else if (tipo === 'excel') {
            bodyModal.innerHTML = `
                <div class="excel-modal-card">
                    <div class="excel-icon">📊</div>
                    <div class="excel-title">${titulo}</div>
                    <div class="excel-desc">${descripcion}</div>
                    <a href="${url}" target="_blank" class="btn-excel-download">📥 DESCARGAR PLANTILLA EXCEL</a>
                </div>`;
        }
    }

    function cerrarRecursoGlobal() {
        document.getElementById('recurso-modal-global').style.display = 'none';
        document.getElementById('modal-global-body').innerHTML = ''; // Limpieza de memoria
        document.getElementById('btn-modal-back').style.display = 'none';
    }

    document.addEventListener("DOMContentLoaded", function() {
        let primerBoton = document.querySelector('.tab-btn');
        filtrarCategoria('excel', primerBoton);
    });
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
