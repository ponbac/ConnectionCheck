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
    return render_template('connection-history.html', dc_list=list_dc())


def list_dc():
    dc_list_html = ""

    for dc in Main.dc_list:
        dc_list_html += "<p>" + '{:.19}'.format(str(dc.time)) +"</p>"

    return dc_list_html


if __name__ == '__main__':
    app.run(host='localhost')
