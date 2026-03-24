import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Streamlit page
st.set_page_config(page_title="PW Skills Clone", layout="wide")

# 2. Define the Single Page Application (SPA) HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; margin: 0; background-color: #f3f7ff; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .logo { font-size: 24px; font-weight: bold; color: #1b4697; }
        .hero { text-align: center; padding: 100px 20px; background: white; }
        .hero h1 { font-size: 50px; }
        .blue-text { color: #1b4697; }
        .course-container { display: flex; justify-content: center; gap: 20px; padding: 50px; flex-wrap: wrap; }
        .card { background: white; padding: 30px; border-radius: 10px; width: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee; text-align: center; }
        .login-btn { background: #1b4697; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; transition: 0.3s; }
        .box { max-width: 400px; margin: 80px auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div id="page-home">
        <nav class="navbar">
            <div class="logo">PW SKILLS</div>
            <button class="login-btn" onclick="showPage('page-login')">Login / Register</button>
        </nav>
        <header class="hero">
            <h1>Upskilling Made <span class="blue-text">Affordable</span></h1>
            <button class="login-btn" style="background:#eb5e28; margin-top:20px; font-weight:bold;" onclick="showPage('page-login')">View C++ Course</button>
        </header>
        <div class="course-container">
            <div class="card"><h3>Full Stack Web Dev</h3><p>MERN Stack</p></div>
            <div class="card"><h3>Data Science</h3><p>Python & AI</p></div>
            <div class="card"><h3>Java Masters</h3><p>Backend Dev</p></div>
        </div>
    </div>
    <div id="page-login" class="hidden">
        <div class="box">
            <h2 style="color: #1b4697;">Course Login</h2>
            <input type="text" id="phone" placeholder="Enter Phone Number">
            <input type="password" id="pass" placeholder="Enter Password">
            <button class="login-btn" style="width: 100%; margin-top: 10px;" onclick="validate()">Login</button>
            <p id="error" style="color:red; display:none; margin-top:15px;">Incorrect details.</p>
            <p style="margin-top: 20px; cursor: pointer; color: #1b4697;" onclick="showPage('page-home')">← Back</p>
        </div>
    </div>
    <div id="page-maint" class="hidden">
        <div class="box">
            <h1>🛠️</h1>
            <h2>Under Maintenance</h2>
            <p>Please view after 12:00 AM.</p>
            <button class="login-btn" onclick="window.location.reload()">Refresh</button>
        </div>
    </div>
    <script>
        function showPage(p) {
            document.getElementById('page-home').classList.add('hidden');
            document.getElementById('page-login').classList.add('hidden');
            document.getElementById('page-maint').classList.add('hidden');
            document.getElementById(p).classList.remove('hidden');
        }
        function validate() {
            const phone = document.getElementById('phone').value;
            const pass = document.getElementById('pass').value;
            if(phone === "9835871031" && pass === "896972") { showPage('page-maint'); }
            else { document.getElementById('error').style.display = 'block'; }
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=True)