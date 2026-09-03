<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Calculate Bill</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'Poppins', Arial, sans-serif; margin: 0; background: linear-gradient(135deg, #1b2a4a 0%, #c4841d 100%);
               min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .card { background: white; width: 420px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.25); overflow: hidden; }
        .header { background: linear-gradient(135deg, #1b2a4a, #c4841d); color: white; padding: 26px 30px; }
        .header .icon { font-size: 28px; }
        .header h1 { margin: 6px 0 0; font-size: 19px; }
        .body { padding: 28px 30px; }
        label { display: block; font-size: 13px; font-weight: 600; color: #4a5568; margin: 16px 0 6px; }
        input, select { width: 100%; padding: 11px 12px; border: 1.5px solid #dbe1e8; border-radius: 8px; font-size: 14px; font-family: inherit; background: white; }
        input:focus, select:focus { outline: none; border-color: #c4841d; }
        button { margin-top: 24px; width: 100%; background: #c4841d; color: white; border: none;
                 padding: 13px; border-radius: 8px; font-size: 15px; font-weight: 600; cursor: pointer; font-family: inherit; }
        button:hover { background: #a06e17; }
        .error { background: #fdecea; color: #b3261e; padding: 12px 14px; border-radius: 8px; font-size: 13px; font-weight: 600; }
        .success { background: #fbf1e0; color: #8a5a10; padding: 16px; border-radius: 8px; font-size: 13px; line-height: 1.7; }
        .success strong { display: block; font-size: 14px; margin-bottom: 4px; }
        .success .total { font-size: 20px; font-weight: 700; color: #1b2a4a; margin-top: 6px; }
        .back { display: inline-block; margin-top: 18px; color: #c4841d; text-decoration: none; font-size: 13px; font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header"><span class="icon">💰</span><h1>Calculate Bill</h1></div>
        <div class="body">
            {% if error %}<p class="error">{{ error }}</p>{% endif %}
            {% if success %}
                <div class="success">
                    <strong>✅ Final Bill</strong>
                    Patient Type: {{ success.patient_type }}
                    <div class="total">${{ success.total }}</div>
                </div>
            {% endif %}
            <form method="POST">
                <label>Patient Type</label>
                <select name="patient_type">
                    <option value="Subsidised">Subsidised</option>
                    <option value="Private">Private</option>
                </select>
                <label>Number of Tests Completed</label>
                <input type="text" name="tests">
                <button type="submit">Calculate Bill</button>
            </form>
            <a class="back" href="/">← Back to Menu</a>
        </div>
    </div>
</body>
</html>
