import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills | My Learning", layout="wide")

# This is the updated code with your Google Drive Folder embedded
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background-color: #f0f2f5; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 10px 60px; background: #1b4697; color: white; }
        .logo { font-size: 22px; font-weight: 800; }
        
        .dashboard { display: flex; flex-direction: column; gap: 20px; padding: 20px 60px; max-width: 1400px; margin: 0 auto; }
        .video-container { background: white; padding: 15px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: 700px; }
        
        iframe { width: 100%; height: 100%; border: none; border-radius: 8px; }
        
        .hidden { display: none; }
        .btn { background: #1b4697; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; }
        .login-box { max-width: 400px; margin: 100px auto; background: white; padding: 40px; border-radius: 10px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        input { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        
        .course-card { background: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; max-width: 350px; margin: 50px auto; text-align: center; }
        .badge { background: #eef2ff; color: #1b4697; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    </style>
</head>
<body>

    <div id="page-home">
        <nav class="navbar"><div class="logo">PW SKILLS</div></nav>
        <div class="course-card">
            <span class="badge">MY BATCHES</span>
            <h2 style="margin: 15px 0;">Decode C++ with DSA</h2>
            <p style="color: #666; font-size: 14px;">Master DSA with Pushkar Kumar</p>
            <button class="btn" onclick="showPage('page-login')">GO TO DASHBOARD</button>
        </div>
    </div>

    <div id="page-login" class="hidden">
        <nav class="navbar"><div class="logo">PW SKILLS</div></nav>
        <div class="login-box">
            <h2 style="color: #1b4697;">Student Login</h2>
            <p style="color: #666; font-size: 14px;">Enter your registered details</p>
            <input type="text" id="phone" placeholder="Phone Number (9835871031)">
            <input type="password" id="pass" placeholder="Password (896972)">
            <button class="btn" onclick="validate()">LOGIN TO STUDY</button>
        </div>
    </div>

    <div id="page-dashboard" class="hidden">
        <nav class="navbar">
            <div class="logo">PW SKILLS | Classroom</div>
            <div style="font-size: 14px;">Welcome, <b>Pushkar Kumar</b></div>
        </nav>

        <div class="dashboard">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2 style="color: #333;">Lectures & Resources</h2>
                <span style="color: #1b4697; font-weight: bold;">Batch: Alpha 2026</span>
            </div>
            
            <div class="video-container">
                <iframe src="https://drive.google.com/embeddedfolderview?id=1RGbhYd87-7iNEzwWc1hIzE5WAMG7Je9f#list"></iframe>
            </div>
            
            <p style="color: #666; font-size: 13px; text-align: center;">
                Select a video from the list above to start watching inside the player.
            </p>
        </div>
    </div>

    <script>
        function showPage(p) {
            document.getElementById('page-home').classList.add('hidden');
            document.getElementById('page-login').classList.add('hidden');
            document.getElementById('page-dashboard').classList.add('hidden');
            document.getElementById(p).classList.remove('hidden');
        }

        function validate() {
            const ph = document.getElementById('phone').value;
            const ps = document.getElementById('pass').value;
            if(ph === "9835871031" && ps === "896972") {
                showPage('page-dashboard');
            } else {
                alert("Incorrect Credentials. Please try again.");
            }
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=900, scrolling=True)