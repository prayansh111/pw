import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="PW Skills | Alpha Batch 2026", layout="wide")

# 2. All Lecture IDs
LEC_01_ID = "1CIKnETfzAHb23RF5_TAifFbPz70xETeX"
LEC_02_ID = "1RQCvDJFalDJfIUE1Mmd7R4FSZ-Ggs28H"
LEC_03_ID = "1fHx2vrNS9lI7bEIMOCHP7-0UZ35s_CY_"
LEC_04_ID = "1Pl8rLun6oHwgdNB69vPGHb7IkEElP99j" # Updated
LEC_05_ID = "1DzUtG2gB-Vg6dovpPbkEH3YwX6yMbzdT"
LEC_06_ID = "1kaEvfMg5fXs_BY1f4Q8nN1hltX4OByTs"
LEC_07_ID = "1Pl8rLun6oHwgdNB69vPGHb7IkEElP99j" # New Link 1
LEC_08_ID = "1eD3CedWOzslLp6vIWamdWEZqoGIxL2vT" # New Link 2

# 3. Classroom UI
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #0b0e11; color: white; overflow: hidden; }}
        .navbar {{ display: flex; justify-content: space-between; padding: 12px 40px; background: #1b4697; border-bottom: 1px solid #2d333b; }}
        .classroom-main {{ display: flex; height: 90vh; }}
        
        .video-section {{ flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; overflow-y: auto; }}
        .video-container {{ 
            width: 100%; 
            position: relative; 
            padding-top: 56.25%; 
            background: #000; 
            border-radius: 12px; 
            overflow: hidden; 
            border: 1px solid #333; 
        }}
        iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }}

        .sidebar {{ flex: 1; background: #161b22; border-left: 1px solid #30363d; overflow-y: auto; padding-bottom: 80px; }}
        .sidebar-header {{ padding: 20px; background: #0d1117; font-weight: bold; color: #58a6ff; border-bottom: 1px solid #30363d; position: sticky; top: 0; z-index: 10; }}
        .lec-item {{ 
            padding: 15px 20px; 
            border-bottom: 1px solid #21262d; 
            cursor: pointer; 
            transition: 0.2s; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            font-size: 13px;
        }}
        .lec-item:hover {{ background: #1b4697; }}
        .active-lec {{ background: #1b4697; border-left: 4px solid #fff; font-weight: bold; }}
        
        .login-box {{ position: fixed; top:0; left:0; width:100%; height:100%; background:#0d1117; display:flex; justify-content:center; align-items:center; z-index:9999; }}
        .card {{ background:#161b22; padding:40px; border-radius:15px; border:1px solid #333; text-align:center; width:350px; }}
        input {{ width:95%; padding:12px; margin:10px 0; background:#0b0e11; border:1px solid #333; color:white; border-radius:8px; }}
        .btn {{ background:#1b4697; color:white; border:none; padding:15px; width:100%; border-radius:8px; cursor:pointer; font-weight:bold; }}
        .hidden {{ display: none; }}
    </style>
</head>
<body>

    <div id="login-pg" class="login-box">
        <div class="card">
            <h2 style="margin-top:0;">PW SKILLS</h2>
            <p style="color:#8b949e; font-size:14px;">Decode C++ with DSA: Alpha 2026</p>
            <input type="text" id="user" placeholder="Mobile Number">
            <input type="password" id="pw" placeholder="Password">
            <button class="btn" onclick="auth()">ACCESS BATCH</button>
        </div>
    </div>

    <div id="dash-pg" class="hidden">
        <nav class="navbar">
            <div style="font-size:20px; font-weight:800; letter-spacing:1px;">PW SKILLS</div>
            <div style="font-size:13px; color:#8b949e;">Student: <b>Pushkar Kumar</b></div>
        </nav>

        <div class="classroom-main">
            <div class="video-section">
                <div class="video-container">
                    <iframe id="main-player" src="https://drive.google.com/file/d/{LEC_01_ID}/preview"></iframe>
                </div>
                <div style="margin-top:20px; padding-bottom:40px;">
                    <h2 id="vid-title" style="margin:0; font-size:22px;">Lec 01: Introduction & Environment Setup</h2>
                    <p id="vid-desc" style="color:#8b949e; font-size:15px; margin-top:10px;">Starting your journey with C++ and setting up the environment.</p>
                </div>
            </div>

            <div class="sidebar">
                <div class="sidebar-header">BATCH CONTENT (8 LESSONS)</div>
                
                <div id="it1" class="lec-item active-lec" onclick="sw('{LEC_01_ID}', 'Lec 01: Introduction & Setup', 'Course roadmap and VS Code setup.', 'it1')">
                    <span>01. C++ Introduction</span> <span style="color:#22c55e;">▶</span>
                </div>
                <div id="it2" class="lec-item" onclick="sw('{LEC_02_ID}', 'Lec 02: Flowcharts & Variables', 'Mastering logic and flowcharts.', 'it2')">
                    <span>02. Flowcharts & Logic</span> <span>1:02:15</span>
                </div>
                <div id="it3" class="lec-item" onclick="sw('{LEC_03_ID}', 'Lec 03: Variables & Data Types', 'Data storage in C++.', 'it3')">
                    <span>03. Variables & Types</span> <span>55:20</span>
                </div>
                <div id="it4" class="lec-item" onclick="sw('{LEC_04_ID}', 'Lec_04_ID', 'Loops and conditionals.', 'it4')">
                    <span>04. Control Flow</span> <span>1:10:05</span>
                </div>
                <div id="it5" class="lec-item" onclick="sw('{LEC_05_ID}', 'Lec 05: Patterns Part-1', 'Nested loops logic.', 'it5')">
                    <span>05. Patterns Basics</span> <span>48:30</span>
                </div>
                <div id="it6" class="lec-item" onclick="sw('{LEC_06_ID}', 'Lec 06: Patterns Part-2', 'Advanced nested loops.', 'it6')">
                    <span>06. Patterns Adv</span> <span>52:45</span>
                </div>
                <div id="it7" class="lec-item" onclick="sw('{LEC_07_ID}', 'Lec 07: Functions & Scope', 'Modular programming in C++.', 'it7')">
                    <span>07. Functions</span> <span>1:05:10</span>
                </div>
                <div id="it8" class="lec-item" onclick="sw('{LEC_08_ID}', 'Lec 08: Introduction to Arrays', 'Collection of similar data types.', 'it8')">
                    <span>08. Arrays Intro</span> <span>58:20</span>
                </div>

                <div style="padding:20px;">
                    <button onclick="window.print()" style="background:#22c55e; color:white; border:none; padding:12px; border-radius:6px; width:100%; cursor:pointer; font-weight:bold;">Download Receipt</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        function auth() {{
            const u = document.getElementById('user').value;
            const p = document.getElementById('pw').value;
            if(u === "9835871031" && p === "896972") {{
                document.getElementById('login-pg').style.display = 'none';
                document.getElementById('dash-pg').classList.remove('hidden');
            }} else {{ alert("Incorrect Credentials!"); }}
        }}

        function sw(id, title, desc, itemId) {{
            document.getElementById('main-player').src = "https://drive.google.com/file/d/" + id + "/preview";
            document.getElementById('vid-title').innerText = title;
            document.getElementById('vid-desc').innerText = desc;

            const items = document.getElementsByClassName('lec-item');
            for (let i = 0; i < items.length; i++) {{
                items[i].classList.remove('active-lec');
            }}
            document.getElementById(itemId).classList.add('active-lec');
        }}
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=False)