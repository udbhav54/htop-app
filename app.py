from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # get the user details
    full_name = "Udbhav Kumar"  
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    # Get top command output
    top_output = subprocess.getoutput("top -bn 1")

    # HTML response
    response = f"""
    <html>
    <head><title>HTOP Output</title></head>
    <body>
        <h2>Name: {full_name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {formatted_time}</h2>
        <h3>TOP Output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
