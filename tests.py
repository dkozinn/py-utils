#!/usr/bin/env python
# pylint: disable=C0103

" This contains simple tests for the q_signals() modules"
import time
from q_signals import * # pylint: disable=unused-wildcard-import, wildcard-import

signal_id = send_signal(Q_YELLOW, "Test message").json()["id"]
print("Signal ID=", signal_id)
time.sleep(5)
res_shadows = delete_signal_by_id(signal_id)

signal_id = send_signal(Q_GREEN, "Green test", zone_id="KEY_I").json()["id"]
print("Signal ID=", signal_id)
time.sleep(5)
res_shadows = delete_signal_by_id(signal_id)

signal_id = send_signal(Q_WHITE, "White test", zone_id="KEY_SPACE",
                        effect="SET_COLOR").json()["id"]
print("Signal ID=", signal_id)
time.sleep(5)
delete_signal_by_zone("KEY_SPACE")
