from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    f = open("files/1.txt", "r")
    return f.readline()

@app.route('/train')
def train_model():
    f = open("files/2.txt", "w")
    f.write(f"Model Finished - {time.time()}")
    return "Model is trained and written to file"

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
