import paho.mqtt.client as mqtt

DOMAIN = "recorder_service"

WAV_ATTR_NAME = "wav"
URL_ATTR_NAME = "target

server=""
port=""
username=""
password=""

def setup(hass, config):
    def handle_recorder(call):
        wav = call.data.get(WAV_ATTR_NAME, '')
        target = call.data.get(URL_ATTR_NAME, '')

        # send wav to server
        url = target
        payload = bytearray(wav)
        headers = {'content-type': 'audio/wav', 'Accept': 'application/json'}
        request = mqtt.single(test, payload=None, qos=2, retain=False, hostname=server, port=port, auth={‘username’:username, ‘password’:password})

    hass.services.register(DOMAIN, "process", handle_recorder)

    return True
