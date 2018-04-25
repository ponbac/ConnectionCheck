from flask import Flask, render_template
from threading import Thread
from Main import Main
from ConError import ConError

main_thread = Main()
main_thread.start()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', start_time=Main.start_time, internet_status=Main.internet_status, current_time=Main.current_time, last_dc=Main.last_dc, total_dc=Main.total_dc)


@app.route('/connection-history/')
def connection_history():
    list_dc()
    print("history")
    return render_template('connection-history.html')


def list_dc():
    for dc in Main.dc_list:
        print(str(dc.time))


if __name__ == '__main__':
    app.run(host='localhost')
