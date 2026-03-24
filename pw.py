import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills | Student Portal", layout="wide", initial_sidebar_state="collapsed")

# Your converted Direct Stream Link
DIRECT_VIDEO_URL = "https://drive.google.com/uc?export=download&id=1RWNlrRKh2Qef52zOsAPnvzutFXd4vlyX"

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #0b0e11; color: white; overflow: hidden; }}
        .navbar {{ display: flex; justify-content: space-between; padding: 15px 60px; background: #1b4697; border-bottom: 1px solid #2d333b; }}
        
        .classroom-container {{ display: flex; height: 90vh; }}
        
        /* THE CUSTOM VIDEO PLAYER */
        .video-section {{ flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; overflow-y: auto; }}
        .player-wrapper {{ width: 100%; position: relative; background: #000; border-radius: 12px; overflow: hidden; box-shadow: 0 0 50px rgba(0,0,0,0.8); border: 1px solid #333; }}
        video {{ width: 100%; height: auto; max-height: 70vh; outline: none; }}
        
        /* PLAYLIST SIDEBAR */
        .sidebar {{ flex: 1; background: #161b22; border-left: 1px solid #30363d; overflow-y: auto; }}
        .sidebar-header {{ padding: 20px; background: #0d1117; font-weight: bold; color: #58a6ff; border-bottom: 1px solid #30363d; }}
        .lecture-item {{ padding: 15px 20px; border-bottom: 1px solid #21262d; cursor: pointer; transition: 0.2s; font-size: 14px; display: flex; justify-content: space-between; }}
        .lecture-item:hover {{ background: #1b4697; color: white; }}
        .active-lec {{ background: #1b4697; border-left: 4px solid #fff; font-weight: bold; }}
        
        /* CUSTOM CONTROLS */
        .controls {{ margin-top: 15px; display: flex; gap: 15px; align-items: center; background: #161b22; padding: 10px; border-radius: 8px; border: 1px solid #333; }}
        .btn-speed {{ background: #30363d; color: white; border: 1px solid #444; padding: 6px 15px; border-radius: 6px; cursor: pointer; font-size: 12px; }}
        .btn-speed:hover {{ background: #1b4697; }}

        /* LOGIN UI */
        .hidden {{ display: none; }}
        .login-box {{ max-width: 380px; margin: 120px auto; background: #161b22; padding: 40px; border-radius: 15px; text-align: center; border: 1px solid #30363d; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }}
        input {{ width: 90%; padding: 12px; margin: 10px 0; background: #0d1117; border: 1px solid #30363d; color: white; border-radius: 8px; font-size: 16px; }}
        .btn-login {{ background: #1b4697; color: white; border: none; padding: 15px; border-radius: 8px; width: 100%; cursor: pointer; font-weight: bold; font-size: 16px; margin-top: 10px; }}
    </style>
</head>
<body>

    <div id="page-login">
        <div class="login-box">
            <h2 style="margin-bottom:5px;">PW SKILLS</h2>
            <p style="color:#8b949e; font-size:14px; margin-bottom:25px;">Classroom Access</p>
            <input type="text" id="phone" placeholder="Mobile Number">
            <input type="password" id="pass" placeholder="Password">
            <button class="btn-login" onclick="login()">START LEARNING</button>
        </div>
    </div>

    <div id="page-dash" class="hidden">
        <nav class="navbar">
            <div style="font-weight:800; font-size:22px; letter-spacing:1px;">PW SKILLS</div>
            <div style="font-size:13px; color:#8b949e;">Student: <b>Pushkar Kumar</b></div>
        </nav>

        <div class="classroom-container">
            <div class="video-section">
                <div class="player-wrapper">
                    <video id="mainPlayer" controls controlsList="nodownload" poster="https://pwskills.com/images/home/banner-1.webp">
                        <source id="videoSource" src="{DIRECT_VIDEO_URL}" type="video/mp4">
                        Your browser does not support HTML5 video.
                    </video>
                </div>
                
                <div class="controls">
                    <span style="font-size:12px; color:#8b949e;">STUDY SPEED:</span>
                    <button class="btn-speed" onclick="setSpeed(1)">1x</button>
                    <button class="btn-speed" onclick="setSpeed(1.25)">1.25x</button>
                    <button class="btn-speed" onclick="setSpeed(1.5)">1.5x</button>
                    <button class="btn-speed" onclick="setSpeed(2)">2x</button>
                </div>

                <div style="margin-top:20px; padding-bottom:40px;">
                    <h2 id="currentTitle" style="margin:0;">Lec 01: Introduction to C++ and DSA</h2>
                    <p style="color:#8b949e; font-size:14px; margin-top:8px;">Batch: Alpha 2026 | Study Material Verified</p>
                    <hr style="border:0; border-top:1px solid #333; margin:20px 0;">
                    <button onclick="window.print()" style="background:#22c55e; color:white; border:none; padding:12px 25px; border-radius:6px; cursor:pointer; font-weight:bold;">Download Batch Invoice</button>
                </div>
            </div>

            <div class="sidebar">
                <div class="sidebar-header">COURSE CONTENT</div>
                <div class="lecture-item active-lec">
                    <span>01. Master Class: C++ Basics</span>
                    <span style="color:#22c55e;">✔</span>
                </div>
                <div class="lecture-item">
                    <span>02. Variables & Data Types</span>
                    <span>🔒</span>
                </div>
                <div class="lecture-item">
                    <span>03. Operators & Logic</span>
                    <span>🔒</span>
                </div>
                <div style="padding:20px; font-size:12px; color:#8b949e;">
                    Upcoming: Lec 04 (Next Week)
                </div>
            </div>
        </div>
    </div>

    <script>
        function login() {{
            if(document.getElementById('phone').value === "9835871031" && document.getElementById('pass').value === "896972") {{
                document.getElementById('page-login').classList.add('hidden');
                document.getElementById('page-dash').classList.remove('hidden');
            }} else {{ alert("Invalid login!"); }}
        }}

        function setSpeed(s) {{
            document.getElementById('mainPlayer').playbackRate = s;
        }}
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=False)