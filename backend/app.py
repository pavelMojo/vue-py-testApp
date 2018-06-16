from flask import Flask

app = Flask(__name__)


class JSONEncoder(app.json_encoder):
    def default(self, o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        else:
            return super().default(o)


app.json_encoder = JSONEncoder
