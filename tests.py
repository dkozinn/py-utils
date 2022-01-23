#!/usr/bin/env python

from q_signals import *
import time

signal_id = send_signal(Q_YELLOW, "Test message").json()["id"]
print("Signal ID=",signal_id)
time.sleep(5)
res_shadows = delete_signal_by_id(signal_id)

signal_id = send_signal(Q_GREEN, "Green test", zoneId="KEY_I").json()["id"]
print("Signal ID=",signal_id)
time.sleep(5)
res_shadows = delete_signal_by_id(signal_id)

signal_id = send_signal(Q_WHITE, "WHITE test", zoneId="KEY_SPACE", effect="SET_COLOR").json()["id"]
print("Signal ID=",signal_id)