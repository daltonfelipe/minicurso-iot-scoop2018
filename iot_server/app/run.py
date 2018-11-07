from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

app = Flask(
    __name__,
    static_folder='static')

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['MQTT_BROKER_URL'] = 'localhost'

socketio = SocketIO(app)
mqtt = Mqtt(app)

# acesso de um usuario na pagina
@socketio.on("connect")
def on_connect():
    print("Usuario conectado!")

# saida do usuario da pagina
@socketio.on("disconnect")
def on_disconnect():
    print("Usuario desconectado!")
    mqtt.publish('acao',"off")

# conexao mqtt
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('status')

# quando chega uma mudanca de status envia pro socket
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    print("status recebido:", payload)
    socketio.emit('status', payload)

# rota da pagina inicial
@app.route("/")
def home():
    return render_template("index.html")

# acao de ligar ou desligar o led
@socketio.on('acao')
def handle_message(acao):
    mqtt.publish('acao',acao)
    print('acao: ' + str(acao))

socketio.run(app)
