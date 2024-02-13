from django.shortcuts import render, redirect
import mysql.connector as sql
import uuid
import bcrypt

em=''
pwd=''

# Create your views here.

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="ankur",passwd="Dearcherry_9",database='newdb')
        cursor=m.cursor()
        d=request.POST

        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())

        if t==():
            return render(request,'error.html')
        else:
            request.session['user_email'] = em
            return redirect('api:product-list')

    return render(request,'login_page.html')

def forget_password(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        reset_token = str(uuid.uuid4())
        
        # Connect to your database
        m = sql.connect(host="localhost", user="ankur", passwd="Dearcherry_9", database='newdb')
        cursor = m.cursor()
        # Insert the reset request into the password_reset_request table
        cursor.execute("INSERT INTO login_passwordresetrequest (email, token, request_time) VALUES (%s, %s, NOW())", (email, reset_token))
        m.commit()
        
        # Generate the reset link with the token
        reset_link = f"http://127.0.0.1:8000/reset-password/?token={reset_token}"
        # print(f"Password reset link (simulate sending via email): {reset_link}")
        
        return render(request, 'reset_link_sent.html', {'link': reset_link})
    return render(request, 'forget_password.html')

def reset_password(request):
    token = request.GET.get('token') or request.POST.get('token')
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        # hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        
        m = sql.connect(host="localhost", user="ankur", passwd="Dearcherry_9", database='newdb')
        cursor = m.cursor()
        cursor.execute("SELECT email FROM login_passwordresetrequest WHERE token=%s", (token,))
        user_email = cursor.fetchone()
        
        if user_email:
            cursor.execute("UPDATE users SET password=%s WHERE email=%s", (new_password, user_email[0]))
            m.commit()
            # Invalidate the token after successful password reset
            cursor.execute("DELETE FROM login_passwordresetrequest WHERE token=%s", (token,))
            m.commit()
            return redirect('login')
        else:
            return render(request, 'reset_password_form.html', {'error': 'Invalid or expired token.'})
            
    return render(request, 'reset_password_form.html', {'token': token})