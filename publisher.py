#!/usr/bin/env python2.7

from paho.mqtt import publish
import datetime, pytz, json, base64

data = []
auth = {'username' : 'atiunov', 'password' : '1234qwer'}
def main():
    # data.append({'data/time': str(datetime.datetime.now(tz=pytz.timezone('EST'))), 'image': base64.b64encode(open('img1.png', 'rb').read()),
    #              'channel': 21, 'free_seller': False, 'free_buyer': True, 'version': '0.0.0.1b','service_type': 'Free seller/Free buyer'})
    # msgs = [("message", (json.dumps(data, ensure_ascii=False)), 0, False)]
    # publish.multiple(msgs, hostname="localhost", port=1883)
    sendMQTTMessage(open('img1.png', 'rb').read(), 21, False, True, 'Free seller/Free buyer', 'message', '0.0.0.1a', '127.0.0.1', '1883', auth)

def sendMQTTMessage(image, channel, freeSeller, freeBuyer, serviceType, topic, version, host, port, auth):
    data = {'data/time': str(datetime.datetime.now(tz=pytz.timezone('EST'))), 'image': base64.b64encode(image),
                 'channel': channel, 'free_seller': freeSeller, 'free_buyer': freeBuyer, 'version': version, 'service_type': serviceType}
    msg = [(topic, (json.dumps(data, ensure_ascii=False)), 0, False)]
    publish.multiple(msgs=msg, hostname=host, port=port, auth=auth)

if __name__ == "__main__":
    main()