# Reemplaza el bloque CSS dentro de <style> en tu app.py con este:
"""
    <style>
        body {
            background-color: #f1f5f9; /* Gris muy claro de oficina */
            color: #334155;
            font-family: 'Inter', -apple-system, sans-serif;
            margin: 0; padding: 20px;
            display: flex; flex-direction: column; align-items: center;
        }
        .app-container {
            width: 100%; max-width: 800px; /* Más ancho para permitir rejilla */
            background: #ffffff;
            border-radius: 8px; padding: 30px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #e2e8f0;
        }
        h1 {
            font-size: 24px; color: #1e293b; /* Azul marino serio */
            text-align: center; margin-bottom: 8px;
        }
        .subtitle {
            text-align: center; font-size: 14px; color: #64748b; margin-bottom: 30px;
        }
        #resources-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Cuadros más pequeños */
            gap: 20px;
        }
        .card {
            background: #ffffff; border: 1px solid #e2e8f0;
            border-radius: 6px; overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .card-img { width: 100%; height: 120px; object-fit: cover; filter: grayscale(20%); }
        .card-body { padding: 15px; }
        .badge {
            font-size: 10px; background: #f1f5f9; color: #475569;
            padding: 2px 6px; border-radius: 4px; margin-bottom: 10px; display: inline-block;
        }
        .card-title { font-size: 16px; font-weight: 600; color: #1e293b; margin-bottom: 8px; }
        .card-text { font-size: 12px; color: #64748b; line-height: 1.5; margin-bottom: 15px; }
        .btn-download {
            display: block; text-align: center; background: #2563eb; /* Azul corporativo */
            color: white; text-decoration: none; padding: 10px;
            border-radius: 4px; font-weight: 500; font-size: 13px;
        }
    </style>
"""
