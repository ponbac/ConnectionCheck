from flask import Flask
from threading import Thread
from main import Main

main_thread = Main()
main_thread.start()

app = Flask(__name__)


@app.route('/')
def index():
    internet_connection_paragraph = '<p>Internet Connection: ' + str(Main.internet_status) + '</p>'
    current_time_paragraph = '<p>Current time: ' + Main.current_time + '</p>'
    last_dc_paragraph = '<p>Last DC: ' + Main.last_dc + '</p>'
    total_dc_paragraph = '<p>Total disconnects since ' + Main.start_time + ': ' + Main.total_dc + '</p>'

    return internet_connection_paragraph + current_time_paragraph + last_dc_paragraph + total_dc_paragraph


if __name__ == '__main__':
    app.run()
