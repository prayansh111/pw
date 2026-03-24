import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills | Alpha Batch 2026", layout="wide")

# Lecture IDs for the first 8 videos
lectures = {
    "1": "1CIKnETfzAHb23RF5_TAifFbPz70xETeX",
    "2": "1RQCvDJFalDJfIUE1Mmd7R4FSZ-Ggs28H",
    "3": "1fHx2vrNS9lI7bEIMOCHP7-0UZ35s_CY_",
    "4": "1Pl8rLun6oHwgdNB69vPGHb7IkEElP99j",
    "5": "1DzUtG2gB-Vg6dovpPbkEH3YwX6yMbzdT",
    "6": "1kaEvfMg5fXs_BY1f4Q8nN1hltX4OByTs",
    "7": "1Pl8rLun6oHwgdNB69vPGHb7IkEElP99j",
    "8": "1eD3CedWOzslLp6vIWamdWEZqoGIxL2vT"
}

# Generate Sidebar HTML for 100 videos
sidebar_items = ""
for i in range(1, 101):
    num = str(i).zfill(2)
    if i <= 8:
        # Unlocked Videos
        sidebar_items += f"""
        <div id="it{i}" class="lec-item {'active-lec' if i==1 else ''}" onclick="sw('{lectures[str(i)]}', 'Lec {num}: Active Lesson', 'You are watching an unlocked lecture.', 'it{i}', false)">
            <span>{num}. C++ & DSA Video</span> <span style="color:#22c55e;">▶</span>
        </div>"""
    else:
        # Fake Locked Videos (9 to 100)
        sidebar_items += f"""
        <div id="it{i}" class="lec-item locked-item" onclick="sw('', 'Lec {num}: Restricted Content', 'This lecture is currently locked.', 'it{i}', true)">
            <span>{num}. Advanced Module</span> <span>🔒</span>
        </div>"""

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #0b0e11; color: white; overflow: hidden; }}
        .navbar {{ display: flex; justify-content: space-between; padding: 12px 40px; background: #1b4697; border-bottom: 1px solid #2d333b; }}
        .classroom-main {{ display: flex; height: 90vh; }}
        
        /* Video Section */
        .video-section {{ flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; overflow-y: auto; }}
        .video-container {{ width: 100%; position: relative; padding-top: 56.25%; background: #1a1a1a; border-radius: 12px; overflow: hidden; border: 1px solid #333; }}
        iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }}
        
        /* Fake Lock Screen */
        .lock-overlay {{ 
            position: absolute; top:0; left:0; width:100%; height:100%; 
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.9)), url('https://pwskills.com/images/home/banner-1.webp');
            background-size: cover; display: none; flex-direction: column; justify-content: center; align-items: center; text-align: center;
        }}
        .lock-icon {{ font-size: 50px; margin-bottom: 15px; }}

        /* Sidebar */
        .sidebar {{ flex: 1; background: #161b22; border-left: 1px solid #30363d; overflow-y: auto; padding-bottom: 100px; }}
        .sidebar-header {{ padding: 20px; background: #0d1117; font-weight: bold; color: #58a6ff; border-bottom: 1px solid #30363d; position: sticky; top: 0; z-index: 10; }}
        .lec-item {{ padding: 15px 20px; border-bottom: 1px solid #21262d; cursor: pointer; transition: 0.2s; display: flex; justify-content: space-between; font-size: 13px; }}
        .lec-item:hover {{ background: #1b4697; }}
        .active-lec {{ background: #1b4697; border-left: 4px solid #fff; font-weight: bold; }}
        .locked-item {{ opacity: 0.6; }}

        /* Login */
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
            <h2>PW SKILLS</h2>
            <input type="text" id="user" placeholder="Mobile Number">
            <input type="password" id="pw" placeholder="Password">
            <button class="btn" onclick="auth()">ACCESS BATCH</button>
        </div>
    </div>

    <div id="dash-pg" class="hidden">
        <nav class="navbar">
            <div style="font-size:20px; font-weight:800;">PW SKILLS</div>
            <div style="font-size:12px; color:#8b949e;">Student: <b>Pushkar Kumar</b></div>
        </nav>

        <div class="classroom-main">
            <div class="video-section">
                <div class="video-container">
                    <iframe id="main-player" src="https://drive.google.com/file/d/{lectures['1']}/preview"></iframe>
                    <div id="lock-screen" class="lock-overlay">
                        <div class="lock-icon">🔒</div>
                        <h2 style="color: #ffcc00;">LECTURE LOCKED</h2>
                        <p style="padding: 0 20px;">Watch all currently unlocked videos to unlock this lecture.</p>
                        <button class="btn" style="width:auto; padding: 10px 30px; margin-top:10px;">Upgrade Plan</button>
                    </div>
                </div>
                <div style="margin-top:20px;">
                    <h2 id="vid-title">Lec 01: Introduction & Setup</h2>
                    <p id="vid-desc" style="color:#8b949e; font-size:14px;">Welcome to your first lecture.</p>
                </div>
            </div>

            <div class="sidebar">
                <div class="sidebar-header">BATCH CONTENT (100 LESSONS)</div>
                {sidebar_items}
            </div>
        </div>
    </div>

    <script>
        function auth() {{
            if(document.getElementById('user').value === "9835871031" && document.getElementById('pw').value === "896972") {{
                document.getElementById('login-pg').style.display = 'none';
                document.getElementById('dash-pg').classList.remove('hidden');
            }} else {{ alert("Invalid!"); }}
        }}

        function sw(id, title, desc, itemId, isLocked) {{
            const player = document.getElementById('main-player');
            const lock = document.getElementById('lock-screen');
            
            if(isLocked) {{
                player.style.display = 'none';
                lock.style.display = 'flex';
            }} else {{
                player.style.display = 'block';
                lock.style.display = 'none';
                player.src = "https://drive.google.com/file/d/" + id + "/preview";
            }}

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