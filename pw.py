import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills | Classroom", layout="wide")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #f0f2f5; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 10px 60px; background: #1b4697; color: white; }
        
        /* Video Template Layout */
        .classroom-container { display: flex; height: 90vh; overflow: hidden; }
        
        /* Left Side: Video Player */
        .video-main { flex: 3; padding: 20px; background: #000; display: flex; flex-direction: column; }
        .video-player { flex: 1; border-radius: 8px; overflow: hidden; background: #1a1a1a; position: relative; }
        iframe { width: 100%; height: 100%; border: none; }
        
        /* Right Side: Playlist Sidebar */
        .sidebar-playlist { flex: 1; background: white; border-left: 1px solid #ddd; overflow-y: auto; display: flex; flex-direction: column; }
        .playlist-header { padding: 20px; border-bottom: 2px solid #f0f2f5; background: #fff; position: sticky; top: 0; }
        .module-item { padding: 15px 20px; border-bottom: 1px solid #f0f2f5; cursor: pointer; transition: 0.2s; font-size: 14px; display: flex; align-items: center; gap: 10px; }
        .module-item:hover { background: #eef2ff; }
        .module-item.active { border-left: 4px solid #1b4697; background: #f8f9ff; font-weight: bold; }
        
        .play-icon { width: 20px; height: 20px; opacity: 0.6; }
        .hidden { display: none; }
        
        /* Login UI */
        .login-box { max-width: 400px; margin: 100px auto; background: white; padding: 40px; border-radius: 12px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        input { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 8px; }
        .btn { background: #1b4697; color: white; border: none; padding: 12px; border-radius: 8px; cursor: pointer; width: 100%; font-weight: bold; }
    </style>
</head>
<body>

    <div id="page-login">
        <div class="login-box">
            <h2 style="color:#1b4697">PW Skills Login</h2>
            <input type="text" id="phone" placeholder="Mobile Number">
            <input type="password" id="pass" placeholder="Password">
            <button class="btn" onclick="validate()">LOGIN</button>
        </div>
    </div>

    <div id="page-dashboard" class="hidden">
        <nav class="navbar">
            <div style="font-size:20px; font-weight:bold">PW SKILLS</div>
            <div style="font-size:14px">Pushkar Kumar | Decode C++ with DSA</div>
        </nav>

        <div class="classroom-container">
            <div class="video-main">
                <div class="video-player">
                    <iframe src="https://drive.google.com/embeddedfolderview?id=1RGbhYd87-7iNEzwWc1hIzE5WAMG7Je9f#list"></iframe>
                </div>
                <div style="color: white; padding: 15px 0;">
                    <h3 style="margin:0">Lec 01: Introduction to DSA & Complexity</h3>
                    <p style="font-size:12px; opacity:0.7">Decode C++ Alpha Batch 2026</p>
                </div>
            </div>

            <div class="sidebar-playlist">
                <div class="playlist-header">
                    <h4 style="margin:0">Course Content</h4>
                    <p style="font-size:11px; color:#666">12 / 150 Lessons Completed</p>
                </div>
                
                <div class="module-item active"><span>▶</span> Lec 01: Introduction to DSA</div>
                <div class="module-item"><span>▶</span> Lec 02: Space & Time Complexity</div>
                <div class="module-item"><span>▶</span> Lec 03: Variables and Data Types</div>
                <div class="module-item"><span>▶</span> Lec 04: If-Else & Loops</div>
                <div class="module-item"><span>▶</span> Lec 05: Patterns Part-1</div>
                <div class="module-item"><span>▶</span> Lec 06: Patterns Part-2</div>
                <div class="module-item"><span>▶</span> Lec 07: Functions in C++</div>
                <div class="module-item"><span>▶</span> Lec 08: Arrays Introduction</div>
                <div class="module-item" style="opacity:0.5"><span>🔒</span> Lec 09: Binary Search (Locked)</div>
            </div>
        </div>
    </div>

    <script>
        function validate() {
            if(document.getElementById('phone').value === "9835871031" && document.getElementById('pass').value === "896972") {
                document.getElementById('page-login').classList.add('hidden');
                document.getElementById('page-dashboard').classList.remove('hidden');
            } else { alert("Wrong Credentials"); }
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=False)