from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play(x=3, color = 'aqua'):
    return render_template('index.html', x=x, color=color)

@app.route('/play/<int:x>')
def display_x_boxes(x, color = 'aqua'):
    return render_template('index.html', x=x, color=color)

@app.route('/play/<int:x>/<color>')
def display_color(x, color):
    return render_template('index.html', x=x, color=color)

if __name__ == '__main__':
    app.run(debug = True)
