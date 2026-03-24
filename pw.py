import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode for a better classroom experience
st.set_page_config(page_title="PW Skills | My Learning Dashboard", layout="wide", initial_sidebar_state="collapsed")

# The Single-Page Application (SPA) Logic
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PW Skills Classroom</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #f4f7fe; color: #333; }
        
        /* Navbar Styling */
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 12px 60px; background: #1b4697; color: white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        .logo { font-size: 24px; font-weight: 800; letter-spacing: 1px; }
        .user-profile { font-size: 14px; opacity: 0.9; }

        /* Login Container */
        .login-wrapper { display: flex; justify-content: center; align-items: center; height: 90vh; }
        .login-box { background: white; padding: 40px; border-radius: 15px; width: 100%; max-width: 400px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid #eef2ff; }
        .login-box img { width: 140px; margin-bottom: 20px; }
        .login-box h2 { color: #1b4697; margin-bottom: 5px; font-size: 22px; }
        .login-box p { color: #888; font-size: 14px; margin-bottom: 30px; }

        /* Input Styling - Blank by default */
        input { width: 90%; padding: 14px; margin: 10px 0; border: 1px solid #dcdcdc; border-radius: 8px; font-size: 16px; transition: 0.3s; }
        input:focus { border-color: #1b4697; outline: none; box-shadow: 0 0 8px rgba(27, 70, 151, 0.2); }
        
        .btn-login { background: #1b4697; color: white; border: none; padding: 15px; border-radius: 8px; cursor: pointer; width: 100%; font-weight: bold; font-size: 16px; margin-top: 15px; transition: 0.3s; }
        .btn-login:hover { background: #133475; transform: translateY(-1px); }

        /* Dashboard Styling */
        .main-content { padding: 30px 60px; max-width: 1400px; margin: 0 auto; }
        .course-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; background: white; padding: 20px; border-radius: 12px; border-left: 6px solid #1b4697; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        
        .video-container { background: white; padding: 10px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); height: 750px; overflow: hidden; border: 1px solid #eee; }
        iframe { width: 100%; height: 100%; border: none; }

        .btn-invoice { background: #22c55e; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14px; cursor: pointer; border: none; transition: 0.3s; }
        .btn-invoice:hover { background: #16a34a; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.3); }

        .hidden { display: none; }
        
        @media (max-width: 768px) {
            .navbar, .main-content { padding: 15px 20px; }
            .course-header { flex-direction: column; text-align: center; gap: 15px; }
        }
    </style>
</head>
<body>

    <div id="page-login">
        <div class="login-wrapper">
            <div class="login-box">
                <img src="https://pwskills.com/images/PWSkills-main.png" alt="PW Skills Logo">
                <h2>Student Login</h2>
                <p>Login to access <b>Decode C++ with DSA</b></p>
                
                <input type="text" id="phone_input" placeholder="Registered Mobile Number" autocomplete="off">
                <input type="password" id="pass_input" placeholder="Password" autocomplete="off">
                
                <button class="btn-login" onclick="handleLogin()">LOGIN TO CLASSROOM</button>
                <div style="margin-top: 20px; font-size: 12px; color: #bbb;">Powered by Physics Wallah Ecosystem</div>
            </div>
        </div>
    </div>

    <div id="page-dashboard" class="hidden">
        <nav class="navbar">
            <div class="logo">PW SKILLS</div>
            <div class="user-profile">Welcome, <b id="display_name">Pushkar Kumar</b></div>
        </nav>

        <div class="main-content">
            <div class="course-header">
                <div>
                    <h1 style="margin: 0; font-size: 24px; color: #1b4697;">Decode C++ with DSA (Alpha 2026)</h1>
                    <p style="margin: 5px 0 0 0; color: #666;">Course Status: <span style="color: #22c55e; font-weight: bold;">Active</span> | Batch ID: PWS-C++-2026</p>
                </div>
                <button class="btn-invoice" onclick="window.print()">Download Invoice</button>
            </div>
            
            <div class="video-container">
                <iframe src="https://drive.google.com/embeddedfolderview?id=1RGbhYd87-7iNEzwWc1hIzE5WAMG7Je9f#list"></iframe>
            </div>
            
            <div style="margin-top: 20px; text-align: center; color: #888; font-size: 13px;">
                Tip: Click on any file above to start playing the lecture directly in this window.
            </div>
        </div>
    </div>

    <script>
        function handleLogin() {
            const u_correct = "9835871031";
            const p_correct = "896972";
            
            const u_typed = document.getElementById('phone_input').value;
            const p_typed = document.getElementById('pass_input').value;

            if (u_typed === u_correct && p_typed === p_correct) {
                document.getElementById('page-login').classList.add('hidden');
                document.getElementById('page-dashboard').classList.remove('hidden');
                // Smooth scroll to top
                window.scrollTo(0, 0);
            } else {
                alert("❌ Authentication Failed: Please check your credentials.");
            }
        }

        // Allow 'Enter' key to trigger login
        document.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                handleLogin();
            }
        });
    </script>
</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_content, height=1000, scrolling=True)