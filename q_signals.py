#!/usr/bin/env python

import json
import logging
import requests

BACKEND_URL = "http://david:27301/api/1.0/signals"
HEADERS =  { "Content-type" : "application/json" }
PID = 'DK5QPID'
DEFAULT_ZONE_ID = "KEY_R"
Q_BLUE = "#0000FF"
Q_GREEN = "#00FF00"
Q_CYAN = "#00FFFF"
Q_RED = "#FF0000"
Q_MAGENTA = "#FF00FF"
Q_YELLOW = "#FFFF00"
Q_WHITE = "#FFFFFF"

signal = {
    'pid': PID,
    'clientName': 'DBK Send_signal'
}

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO
)

def send_signal(color, message, zoneId=DEFAULT_ZONE_ID, effect="BLINK", name="Alert"):
    signal["message"] = message
    signal["color"] = color
    signal["effect"] = effect
    signal["name"] = name
    signal["zoneId"] = zoneId
    signal_json = json.dumps(signal)
    logging.debug(f'Sending signal: "{message}" Color: {color}')
    return requests.post(BACKEND_URL, data=signal_json, headers=HEADERS)

def delete_signal_by_zone(zoneId=DEFAULT_ZONE_ID):
    logging.debug("Deleting signal by zone")
    return requests.delete(BACKEND_URL + '/pid/'+ PID + '/zoneId/' + zoneId, headers=HEADERS)
    
def delete_signal_by_id(id):
    logging.debug("Deleting signal by id")
    return requests.delete(f'{BACKEND_URL}/{str(id)}', headers=HEADERS)
    