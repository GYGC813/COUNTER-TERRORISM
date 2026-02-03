from modules.alert_service import AlertService
import numpy as np

alert_service = AlertService()

# Dummy black image
frame = (np.zeros((480, 640, 3))).astype("uint8")

alert_service.handle_alert(
    {
        "event": "TEST ALERT",
        "confidence": 0.99
    },
    frame
)

print("TEST ALERT TRIGGERED")
