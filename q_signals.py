#!/usr/bin/env python

# pylint: disable=C0103

" Utility functions to use Das Keyboard Q via local server."

import json
import logging
import requests

BACKEND_URL = "http://david:27301/api/1.0/signals"
HEADERS = {"Content-type" : "application/json"}
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

# logging.basicConfig(
#     format='%(asctime)s - %(levelname)s: %(message)s',
#     level=logging.INFO
# )

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def send_signal(color, message, zone_id=DEFAULT_ZONE_ID, effect="BLINK", name="Alert"):

    """
    send_signal(): Send the specified signal to Das Keyboard Q via call to API
    """

    signal["message"] = message
    signal["color"] = color
    signal["effect"] = effect
    signal["name"] = name
    signal["zoneId"] = zone_id
    signal_json = json.dumps(signal)
    logger.debug("Sending signal: %s Color: %s", message, color)
    return requests.post(BACKEND_URL, data=signal_json, headers=HEADERS)

def delete_signal_by_zone(zone_id=DEFAULT_ZONE_ID):
    """
    delete_signal_by_zone(): Delete signal in the zone specified for  Das Keyboard Q via call to API
    """
    logger.debug("Deleting signal by zone %s", zone_id)
    return requests.delete(BACKEND_URL + '/pid/'+ PID + '/zoneId/' + zone_id, headers=HEADERS)

def delete_signal_by_id(signal_id):
    """
    delete_signal_by_idl(): Delete signal pecified by id for  Das Keyboard Q via call to API
    """
    logger.debug("Deleting signal by id %s", signal_id)
    return requests.delete(f'{BACKEND_URL}/{str(signal_id)}', headers=HEADERS)
