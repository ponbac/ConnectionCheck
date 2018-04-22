from flask import Flask, render_template
from threading import Thread
from Main import Main

main_thread = Main()
main_thread.start()

app = Flask(__name__)


@app.route('/')
def index():
    start_time_paragraph = '<p>Start time: ' + '{:.19}'.format(Main.start_time) + '</p>'
    internet_connection_paragraph = '<p>Internet Connection: <b>' + str(Main.internet_status) + '</b></p>'
    current_time_paragraph = '<p>Current time: ' + '{:.19}'.format(Main.current_time) + '</p>'
    last_dc_paragraph = '<p>Last disconnect: ' + Main.last_dc + '</p>'
    total_dc_paragraph = '<p>Total disconnects: <b>' + Main.total_dc + '</b></p>'

    return start_time_paragraph + internet_connection_paragraph + current_time_paragraph + last_dc_paragraph + total_dc_paragraph


@app.route('/test')
def test():
    return render_template('test.html', start_time=Main.start_time, internet_status=Main.internet_status, current_time=Main.current_time, last_dc=Main.last_dc, total_dc=Main.total_dc)


if __name__ == '__main__':
    app.run(host='localhost')
