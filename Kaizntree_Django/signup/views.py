from django.shortcuts import render, redirect
import mysql.connector as sql

fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.

def signaction(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="ankur", passwd="Dearcherry_9", database='newdb')
        cursor = m.cursor()
        d = request.POST
        fn = d.get('first_name')
        ln = d.get('last_name')
        s = d.get('sex')
        em = d.get('email')
        pwd = d.get('password')
        
        # Use parameterized queries for security
        c = "INSERT INTO users (first_name, last_name, sex, email, password) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(c, (fn, ln, s, em, pwd))
        m.commit()
        return redirect('login')

    return render(request, 'signup_page.html')