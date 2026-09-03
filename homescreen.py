<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CareBridge Hospital</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Poppins', Arial, sans-serif;
            margin: 0;
            background: linear-gradient(135deg, #1b2a4a 0%, #2e7d6e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: white;
            width: 480px;
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.25);
            overflow: hidden;
        }
        .hero {
            background: linear-gradient(135deg, #1b2a4a, #2e7d6e);
            color: white;
            padding: 36px 30px;
            text-align: center;
        }
        .hero .logo { font-size: 40px; margin-bottom: 8px; }
        .hero h1 { margin: 0; font-size: 22px; font-weight: 700; }
        .hero p { margin: 6px 0 0; font-size: 13px; opacity: 0.85; }
        .menu { padding: 24px; }
        .menu-item {
            display: flex;
            align-items: center;
            gap: 14px;
            background: #f6f8fa;
            text-decoration: none;
            color: #1b2a4a;
            padding: 16px 18px;
            border-radius: 12px;
            margin-bottom: 12px;
            font-weight: 600;
            font-size: 15px;
            transition: 0.2s;
            border: 1px solid #eceff2;
        }
        .menu-item:hover { background: #eaf3f0; border-color: #2e7d6e; transform: translateX(4px); }
        .menu-item .icon { font-size: 22px; }
        .menu-item .arrow { margin-left: auto; color: #9aa5b1; }
    </style>
</head>
<body>
    <div class="card">
        <div class="hero">
            <div class="logo">🏥</div>
            <h1>CareBridge Hospital</h1>
            <p>Hospital Management System</p>
        </div>
        <div class="menu">
            <a class="menu-item" href="/register"><span class="icon">🧑‍⚕️</span> Register Patient <span class="arrow">›</span></a>
            <a class="menu-item" href="/appointment"><span class="icon">📅</span> Book Appointment <span class="arrow">›</span></a>
            <a class="menu-item" href="/bill"><span class="icon">💰</span> Calculate Bill <span class="arrow">›</span></a>
            <a class="menu-item" href="/triage"><span class="icon">🚑</span> Assign Triage Room <span class="arrow">›</span></a>
        </div>
    </div>
</body>
</html>
