import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills Store", layout="wide")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background-color: #f8f9fb; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 15px 80px; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100; }
        .logo { font-size: 26px; font-weight: 800; color: #1b4697; letter-spacing: -1px; }
        
        .hero { text-align: center; padding: 60px 20px; background: white; border-bottom: 1px solid #eee; }
        .hero h1 { font-size: 42px; margin-bottom: 10px; }
        .blue-text { color: #1b4697; }

        /* Course Grid */
        .course-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; padding: 50px 80px; max-width: 1200px; margin: 0 auto; }
        
        .card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #efefef; transition: transform 0.3s; position: relative; }
        .card:hover { transform: translateY(-5px); }
        .card-img { height: 150px; background: #1b4697; display: flex; align-items: center; justify-content: center; color: white; font-size: 40px; }
        .card-body { padding: 20px; text-align: left; }
        .course-name { font-size: 18px; font-weight: bold; margin: 0 0 10px 0; color: #333; height: 50px; }
        .price-tag { font-size: 20px; font-weight: 700; color: #1b4697; margin-bottom: 15px; }
        .old-price { font-size: 14px; text-decoration: line-through; color: #999; margin-right: 8px; }

        .buy-btn { width: 100%; background: #eb5e28; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; transition: 0.2s; }
        .buy-btn:hover { background: #d45221; }
        .login-btn { background: #1b4697; color: white; border: none; padding: 10px 25px; border-radius: 5px; cursor: pointer; font-weight: 600; }

        /* Navigation Utility */
        .hidden { display: none; }
        .box { max-width: 400px; margin: 80px auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
    </style>
</head>
<body>

    <div id="page-home">
        <nav class="navbar">
            <div class="logo">PW SKILLS</div>
            <button class="login-btn" onclick="showPage('page-login')">Login</button>
        </nav>
        
        <header class="hero">
            <h1>Our <span class="blue-text">Popular</span> Courses</h1>
            <p style="color: #666;">Invest in your future with our industry-ready programs.</p>
        </header>

        <div class="course-container">
            <div class="card" style="border: 2px solid #eb5e28;">
                <div class="card-img" style="background: #eb5e28;">C++</div>
                <div class="card-body">
                    <p class="course-name">Decode C++ with DSA: Programming Powerhouse</p>
                    <div class="price-tag"><span class="old-price">₹19,999</span>₹11,499</div>
                    <button class="buy-btn" onclick="showPage('page-login')">Buy Now</button>
                </div>
            </div>

            <div class="card">
                <div class="card-img">JS</div>
                <div class="card-body">
                    <p class="course-name">Full Stack Web Development (MERN)</p>
                    <div class="price-tag"><span class="old-price">₹12,000</span>₹5,999</div>
                    <button class="buy-btn" onclick="showPage('page-login')">Buy Now</button>
                </div>
            </div>

            <div class="card">
                <div class="card-img" style="background: #2b2b2b;">AI</div>
                <div class="card-body">
                    <p class="course-name">Data Science & Machine Learning Masters</p>
                    <div class="price-tag"><span class="old-price">₹25,000</span>₹16,999</div>
                    <button class="buy-btn" onclick="showPage('page-login')">Buy Now</button>
                </div>
            </div>

            <div class="card">
                <div class="card-img" style="background: #5a32a8;">Java</div>
                <div class="card-body">
                    <p class="course-name">Java Backend Development with Microservices</p>
                    <div class="price-tag"><span class="old-price">₹14,000</span>₹5,999</div>
                    <button class="buy-btn" onclick="showPage('page-login')">Buy Now</button>
                </div>
            </div>
            
            <div class="card">
                <div class="card-img" style="background: #00a8e8;">Cloud</div>
                <div class="card-body">
                    <p class="course-name">DevOps and Cloud Computing (AWS/Azure)</p>
                    <div class="price-tag"><span class="old-price">₹22,000</span>₹16,999</div>
                    <button class="buy-btn" onclick="showPage('page-login')">Buy Now</button>
                </div>
            </div>
        </div>
    </div>

    <div id="page-login" class="hidden">
        <div class="box">
            <h2 style="color: #1b4697;">Account Login</h2>
            <input type="text" id="phone" placeholder="Phone Number">
            <input type="password" id="pass" placeholder="Password">
            <button class="login-btn" style="width: 100%; margin-top: 10px;" onclick="validate()">Login to Purchase</button>
            <p id="error" style="color:red; display:none; margin-top:15px;">Invalid Credentials!</p>
            <p style="margin-top: 20px; font-size: 14px; cursor: pointer; color: #1b4697;" onclick="showPage('page-home')">← Back to Store</p>
        </div>
    </div>

    <div id="page-maint" class="hidden">
        <div class="box">
            <h1>🛠️</h1>
            <h2>Under Maintenance</h2>
            <p>Our payment gateway is being updated.<br>Please buy after <b>12:00 AM</b>.</p>
            <button class="login-btn" style="background: #666;" onclick="window.location.reload()">Back to Store</button>
        </div>
    </div>

    <script>
        function showPage(pageId) {
            document.getElementById('page-home').classList.add('hidden');
            document.getElementById('page-login').classList.add('hidden');
            document.getElementById('page-maint').classList.add('hidden');
            document.getElementById(pageId).classList.remove('hidden');
        }

        function validate() {
            const phone = document.getElementById('phone').value;
            const pass = document.getElementById('pass').value;
            if(phone === "9835871031" && pass === "896972") {
                showPage('page-maint');
            } else {
                document.getElementById('error').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""

components.html(html_content, height=1500, scrolling=True)
