import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Streamlit page configuration
st.set_page_config(page_title="PW Skills Store", layout="wide")

# 2. The entire website logic (HTML, CSS, JS) in one string
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background-color: #f8f9fb; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 15px 80px; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100; }
        .logo { font-size: 26px; font-weight: 800; color: #1b4697; }
        .hero { text-align: center; padding: 40px 20px; background: white; border-bottom: 1px solid #eee; }
        
        /* Grid for 10 Courses */
        .course-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; padding: 40px 80px; max-width: 1400px; margin: 0 auto; }
        
        .card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #efefef; display: flex; flex-direction: column; transition: 0.3s; }
        .card:hover { transform: translateY(-5px); }
        .card-header { height: 100px; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; font-weight: bold; }
        
        /* Category Colors */
        .cpp { background: #eb5e28; } .web { background: #22c55e; } .data { background: #1b4697; }
        .java { background: #8b5cf6; } .cloud { background: #0ea5e9; } .ui { background: #f43f5e; }
        
        .card-body { padding: 15px; flex-grow: 1; }
        .course-name { font-size: 16px; font-weight: bold; color: #333; height: 45px; margin-bottom: 5px; }
        .price { font-size: 18px; font-weight: 700; color: #1b4697; }
        .old-price { font-size: 12px; text-decoration: line-through; color: #999; margin-right: 5px; }
        
        .buy-btn { width: 100%; background: #1b4697; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 10px; transition: 0.2s; }
        .buy-btn:hover { background: #14336d; }
        
        .hidden { display: none; }
        .box { max-width: 400px; margin: 80px auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
    </style>
</head>
<body>
    <div id="page-home">
        <nav class="navbar"><div class="logo">PW SKILLS</div><button class="buy-btn" style="width:auto; margin:0;" onclick="showPage('page-login')">Login</button></nav>
        <header class="hero"><h1>Explore Our <span style="color:#1b4697;">Top 10</span> Programs</h1></header>
        
        <div class="course-container">
            <div class="card"><div class="card-header cpp">C++</div><div class="card-body">
                <p class="course-name">Decode C++ with DSA: Programming Powerhouse</p>
                <div class="price"><span class="old-price">₹19,999</span>₹11,499</div>
                <button class="buy-btn" style="background:#eb5e28;" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header web">MERN</div><div class="card-body">
                <p class="course-name">Full Stack Web Development</p>
                <div class="price"><span class="old-price">₹15,000</span>₹6,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header data">AI/ML</div><div class="card-body">
                <p class="course-name">Data Science Masters</p>
                <div class="price"><span class="old-price">₹20,000</span>₹14,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header java">JAVA</div><div class="card-body">
                <p class="course-name">Java Backend Bootcamp</p>
                <div class="price"><span class="old-price">₹12,000</span>₹5,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header cloud">AWS</div><div class="card-body">
                <p class="course-name">DevOps & Cloud Masters</p>
                <div class="price"><span class="old-price">₹18,000</span>₹9,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header ui">UX</div><div class="card-body">
                <p class="course-name">User Experience Design Pro</p>
                <div class="price"><span class="old-price">₹10,000</span>₹4,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header data">WEB3</div><div class="card-body">
                <p class="course-name">Advanced Blockchain Tech</p>
                <div class="price"><span class="old-price">₹22,000</span>₹12,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header web">PY</div><div class="card-body">
                <p class="course-name">Python for Automation & Data</p>
                <div class="price"><span class="old-price">₹8,000</span>₹3,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header cpp">SEC</div><div class="card-body">
                <p class="course-name">Cyber Security Analyst</p>
                <div class="price"><span class="old-price">₹25,000</span>₹15,999</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>

            <div class="card"><div class="card-header java">MKT</div><div class="card-body">
                <p class="course-name">Digital Marketing Expert</p>
                <div class="price"><span class="old-price">₹9,000</span>₹4,499</div>
                <button class="buy-btn" onclick="showPage('page-login')">Purchase Course</button>
            </div></div>
        </div>
    </div>

    <div id="page-login" class="hidden">
        <div class="box">
            <h2 style="color:#1b4697;">Account Login</h2>
            <input type="text" id="phone" placeholder="Enter Phone Number (9835871031)">
            <input type="password" id="pass" placeholder="Enter Password (896972)">
            <button class="buy-btn" style="background:#eb5e28" onclick="validate()">Login to Purchase</button>
            <p onclick="showPage('page-home')" style="cursor:pointer; color:#1b4697; margin-top:15px; font-size:14px;">← Back to Courses</p>
        </div>
    </div>

    <div id="page-maint" class="hidden">
        <div class="box">
            <h1 style="font-size:60px;">🛠️</h1>
            <h2>Under Maintenance</h2>
            <p style="color:#666;">Our payment gateway is being updated.<br><b>Please purchase after 12:00 AM.</b></p>
            <button class="buy-btn" onclick="location.reload()">Return to Store</button>
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
            const ph = document.getElementById('phone').value;
            const ps = document.getElementById('pass').value;
            if(ph === "9835871031" && ps === "896972") {
                showPage('page-maint');
            } else {
                alert("Incorrect Login Details!");
            }
        }
    </script>
</body>
</html>
"""

# 3. Display in Streamlit
components.html(html_content, height=1800, scrolling=True)