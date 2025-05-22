from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the Run button was clicked
        if request.form.get('run_mouse') == '1':
            # Run mouse.py in a new process
            subprocess.Popen(['python', 'mouse.py'])
            # Optionally, you can show a message or redirect
            return render_template('index.html', message="Virtual Mouse started!")
        if request.form.get('run_control') == '1':
            # Run mouse.py in a new process
            subprocess.Popen(['python', 'vol_brightness.py'])
            # Optionally, you can show a message or redirect
            return render_template('index.html', message="Virtual Mouse started!")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
