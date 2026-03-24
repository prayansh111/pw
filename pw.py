import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="PW Skills | Student Dashboard", layout="wide")

# 2. Extracting the IDs from your links
LEC_01_ID = "1CIKnETfzAHb23RF5_TAifFbPz70xETeX"
LEC_02_ID = "1RQCvDJFalDJfIUE1Mmd7R4FSZ-Ggs28H"

# 3. Professional Classroom UI
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #0b0e11; color: white; overflow: hidden; }}
        .navbar {{ display: flex; justify-content: space-between; padding: 15px 40px; background: #1b4697; border-bottom: 1px solid #2d333b; }}
        .classroom-main {{ display: flex; height: 90vh; }}
        
        /* Video Section */
        .video-section {{ flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; }}
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

        /* Sidebar Playlist */
        .sidebar {{ flex: 1; background: #161b22; border-left: 1px solid #30363d; overflow-y: auto; }}
        .sidebar-header {{ padding: 20px; background: #0d1117; font-weight: bold; color: #58a6ff; border-bottom: 1px solid #30363d; }}
        .lec-item {{ 
            padding: 15px 20px; 
            border-bottom: 1px solid #21262d; 
            cursor: pointer; 
            transition: 0.2s; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
        }}
        .lec-item:hover {{ background: #1b4697; }}
        .active-lec {{ background: #1b4697; border-left: 4px solid #fff; font-weight: bold; }}
        
        /* Login */
        .login-box {{ position: fixed; top:0; left:0; width:100%; height:100%; background:#0d1117; display:flex; justify-content:center; align-items:center; z-index:9999; }}
        .card {{ background:#161b22; padding:40px; border-radius:15px; border:1px solid #333; text-align:center; width:350px; }}
        input {{ width:90%; padding:12px; margin:10px 0; background:#0b0e11; border:1px solid #333; color:white; border-radius:8px; }}
        .btn {{ background:#1b4697; color:white; border:none; padding:15px; width:100%; border-radius:8px; cursor:pointer; font-weight:bold; }}
        .hidden {{ display: none; }}
    </style>
</head>
<body>

    <div id="login-pg" class="login-box">
        <div class="card">
            <h2 style="margin-top:0; color:#fff;">PW SKILLS</h2>
            <p style="color:#8b949e; font-size:14px;">Access: Decode C++ with DSA</p>
            <input type="text" id="user" placeholder="Mobile Number">
            <input type="password" id="pw" placeholder="Password">
            <button class="btn" onclick="auth()">START LEARNING</button>
        </div>
    </div>

    <div id="dash-pg" class="hidden">
        <nav class="navbar">
            <div style="font-size:22px; font-weight:800;">PW SKILLS</div>
            <div style="font-size:13px; color:#8b949e;">Student: <b>Pushkar Kumar</b></div>
        </nav>

        <div class="classroom-main">
            <div class="video-section">
                <div class="video-container">
                    <iframe id="main-player" src="https://drive.google.com/file/d/{LEC_01_ID}/preview"></iframe>
                </div>
                <div style="margin-top:20px;">
                    <h2 id="vid-title" style="margin:0; font-size:22px;">Lec 01: Introduction & Environment Setup</h2>
                    <p id="vid-desc" style="color:#8b949e; font-size:14px; margin-top:8px;">Getting started with the course roadmap and setting up your compiler.</p>
                </div>
            </div>

            <div class="sidebar">
                <div class="sidebar-header">BATCH CONTENT</div>
                
                <div id="item1" class="lec-item active-lec" onclick="switchVid('{LEC_01_ID}', 'Lec 01: Introduction & Setup', 'Getting started with the course roadmap.', 'item1')">
                    <span>01. C++ Introduction</span>
                    <span style="color:#22c55e;">▶</span>
                </div>

                <div id="item2" class="lec-item" onclick="switchVid('{LEC_02_ID}', 'Lec 02: Flowcharts & Variables', 'Mastering the logic behind programming.', 'item2')">
                    <span>02. Flowcharts & Logic</span>
                    <span style="color:#8b949e;">42:15</span>
                </div>

                <div class="lec-item" style="opacity:0.5; cursor:not-allowed;">
                    <span>03. Arrays & Vectors (Locked)</span>
                    <span>🔒</span>
                </div>
                
                <div style="padding:20px;">
                    <button onclick="window.print()" style="background:#22c55e; color:white; border:none; padding:10px; border-radius:6px; width:100%; cursor:pointer; font-weight:bold;">Download Invoice</button>
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
            }} else {{ alert("Wrong Login Details!"); }}
        }}

        function switchVid(id, title, desc, itemId) {{
            // Change the Iframe Source
            document.getElementById('main-player').src = "https://drive.google.com/file/d/" + id + "/preview";
            
            // Update Title and Description
            document.getElementById('vid-title').innerText = title;
            document.getElementById('vid-desc').innerText = desc;

            // Update UI Sidebar selection
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

# 4. Final Render
components.html(html_content, height=1000, scrolling=False)