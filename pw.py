from flask import Flask, render_template, redirect, request, session, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "pw_skills_clone_2024"

# Data for Home Page (with given prices)
HOME_COURSES = [
    {"id": 1, "name": "C++ with Data Structures and Algorithms", "price": 11499, "tag": "HIGH-DEMAND"},
    {"id": 2, "name": "Full Stack Web Development (MERN)", "price": 1499, "tag": "TRENDING"}
]

# Data for Detailed Grid
DETAILED_COURSES = [
    {"id": 101, "name": "C++ & DSA Mastery", "duration": "6 months", "type": "Selfpaced", "price": 11499},
    {"id": 102, "name": "DSA Problem Solving", "duration": "4 months", "type": "Selfpaced", "price": 1499},
    {"id": 103, "name": "Full Stack Web Development (MERN)", "duration": "7 months", "type": "Selfpaced", "price": 1499},
    {"id": 104, "name": "Python for Interviews", "duration": "3 months", "type": "Selfpaced", "price": 1499},
    {"id": 105, "name": "Java Core + Advanced", "duration": "5 months", "type": "Selfpaced", "price": 1499},
]

@app.route('/')
def index():
    return render_template('pw.html', courses=HOME_COURSES)

@app.route('/course-details')
def course_details():
    categories = ["Software Development Courses", "Data Science & Analytics", "DSA Courses", "Career Growth"]
    return render_template('detail.html', courses=DETAILED_COURSES, categories=categories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        if phone == "9835871031" and password == "896972":
            session['user'] = phone
            return redirect(url_for('index'))
        else:
            return "<script>alert('Invalid Credentials'); window.location='/login';</script>"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

def is_maintenance_time():
    now = datetime.now()
    return now.hour == 0 and now.minute == 0

@app.route('/pay/<int:id>', methods=['GET', 'POST'])
def pay(id):
    if is_maintenance_time():
        return "<h1 style='text-align:center; font-family:sans-serif; margin-top:100px;'>Website Under Maintenance</h1><p style='text-align:center;'>Please try again after 12:01 AM.</p>"

    course = next((c for c in DETAILED_COURSES if c['id'] == id), None)
    if not course:
        return "<h1>Course not found</h1>", 404

    if request.method == 'POST':
        return redirect(url_for('payment_result', id=id))

    return render_template('pay.html', course=course)

@app.route('/payment-result/<int:id>')
def payment_result(id):
    if is_maintenance_time():
        return "<h1 style='text-align:center; font-family:sans-serif; margin-top:100px;'>Website Under Maintenance</h1><p style='text-align:center;'>Please try again after 12:01 AM.</p>"

    course = next((c for c in DETAILED_COURSES if c['id'] == id), None)
    if not course:
        return "<h1>Course not found</h1>", 404

    return render_template('confirmation.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)
