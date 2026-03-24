import streamlit as st
import streamlit.components.v1 as components

# 1. Setup the Page
st.set_page_config(page_title="PW Skills | Alpha 2026", layout="wide")

# 2. Your Video ID (Extracted from your link)
# Original: https://drive.google.com/file/d/1RWNlrRKh2Qef52zOsAPnvzutFXd4vlyX/view
VIDEO_ID = "1RWNlrRKh2Qef52zOsAPnvzutFXd4vlyX"

# 3. The Professional HTML/CSS Code
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #0b0e11; color: white; }}
        .navbar {{ display: flex; justify-content: space-between; align-items: center; padding: 15px 40px; background: #1b4697; border-bottom: 1px solid #2d333b; }}
        .logo {{ font-size: 24px; font-weight: 800; letter-spacing: 1px; }}
        
        .classroom-main {{ display: flex; height: 88vh; }}
        
        /* Video Container */
        .video-player-section {{ flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; }}
        .iframe-wrapper {{ 
            width: 100%; 
            position: relative; 
            padding-top: 56.25%; /* 16:9 Aspect Ratio */
            background: #000;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #333;
        }}
        iframe {{
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            width: 100%; height: 100%;
            border: none;
        }}

        /* Sidebar Playlist */
        .playlist-sidebar {{ flex: 1; background: #161b22; border-left: 1px solid #30363d; overflow-y: auto; }}
        .sidebar-title {{ padding: 20px; font-size: 14px; font-weight: bold; color: #58a6ff; border-bottom: 1px solid #30363d; background: #0d1117; }}
        .lecture-card {{ padding: 15px 20px; border-bottom: 1px solid #21262d; cursor: pointer; display: flex; justify-content: space-between; align-items: center; transition: 0.3s; }}
        .lecture-card:hover {{ background: #1b4697; }}
        .active-lecture {{ background: #1b4697; border-left: 4px solid #fff; }}

        /* Login Styling */
        .login-overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #0d1117; display: flex; justify-content: center; align-items: center; z-index: 1000; }}
        .login-card {{ background: #161b22; padding: 40px; border-radius: 15px; border: 1px solid #30363d; text-align: center; width: 350px; }}
        input {{ width: 90%; padding: 12px; margin: 10px 0; background: #0b0e11; border: 1px solid #30363d; color: white; border-radius: 6px; }}
        .btn-blue {{ background: #1b4697; color: white; border: none; padding: 14px; width: 100%; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 10px; }}
        .hidden {{ display: none; }}
    </style>
</head>
<body>

    <div id="auth-screen" class="login-overlay">
        <div class="login-card">
            <h2 style="margin-top:0;">PW SKILLS</h2>
            <p style="color:#8b949e; font-size:14px;">Enter credentials to unlock Alpha Batch</p>
            <input type="text" id="mob" placeholder="Mobile Number">
            <input type="password" id="pin" placeholder="Password">
            <button class="btn-blue" onclick="validate()">LOGIN</button>
        </div>
    </div>

    <div id="classroom-ui" class="hidden">
        <div class="navbar">
            <div class="logo">PW SKILLS</div>
            <div style="font-size:13px; color:#c9d1d9;">User: <b>Pushkar Kumar</b> | Batch 2026</div>
        </div>

        <div class="classroom-main">
            <div class="video-player-section">
                <div class="iframe-wrapper">
                    <iframe src="https://drive.google.com/file/d/{VIDEO_ID}/preview" allow="autoplay"></iframe>
                </div>
                <div style="margin-top:20px;">
                    <h2 style="margin:0;">Lec 01: Getting Started with C++ & DSA</h2>
                    <p style="color:#8b949e; font-size:14px; margin-top:10px;">Welcome to the first lecture. Ensure you have your compiler ready.</p>
                </div>
            </div>

            <div class="playlist-sidebar">
                <div class="sidebar-title">LECTURE LIST</div>
                <div class="lecture-card active-lecture">
                    <div>1. Introduction & Setup</div>
                    <span style="color:#22c55e;">▶ Playing</span>
                </div>
                <div class="lecture-card">
                    <div>2. Flowcharts (Locked)</div>
                    <span>🔒</span>
                </div>
                <div class="lecture-card">
                    <div>3. Pseudocode (Locked)</div>
                    <span>🔒</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        function validate() {{
            const u = document.getElementById('mob').value;
            const p = document.getElementById('pin').value;
            if(u === "9835871031" && p === "896972") {{
                document.getElementById('auth-screen').style.display = 'none';
                document.getElementById('classroom-ui').classList.remove('hidden');
            }} else {{
                alert("Incorrect Details");
            }}
        }}
    </script>
</body>
</html>
"""

# 4. Render in Streamlit
components.html(html_content, height=900, scrolling=False)