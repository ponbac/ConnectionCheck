from flask import Flask, render_template
from threading import Thread
from Main import Main

main_thread = Main()
main_thread.start()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', start_time=Main.start_time, internet_status=Main.internet_status, current_time=Main.current_time, last_dc=Main.last_dc, total_dc=Main.total_dc)


if __name__ == '__main__':
    app.run(host='localhost')
