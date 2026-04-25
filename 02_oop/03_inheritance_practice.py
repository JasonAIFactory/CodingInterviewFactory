"""
03_inheritance_practice.py  —  TYPE FROM SCRATCH

Build the same Notification hierarchy.
"""

from abc import ABC, abstractmethod


# ============================================================
# Abstract base class
# ============================================================

class Notification(ABC):
    def __init__(self, recipient):
        # TODO: store recipient
        pass

    # TODO: declare @abstractmethod send(self, message)

    # TODO: log(self, message) prints "[LOG] ClassName -> recipient: message"


# ============================================================
# EmailNotification
# ============================================================

class EmailNotification(Notification):
    pass
    # TODO: send(self, message) -> log + print "Sending EMAIL to ..."


# ============================================================
# SmsNotification
# ============================================================

class SmsNotification(Notification):
    pass
    # TODO: send(self, message) -> log + print "Sending SMS to ..."


# ============================================================
# PushNotification  (has extra device_id)
# ============================================================

class PushNotification(Notification):
    def __init__(self, recipient, device_id):
        # TODO: super().__init__(recipient)
        # TODO: store device_id
        pass

    # TODO: send(self, message) -> log + print "Pushing to device ..."


# ============================================================
# Polymorphism helper
# ============================================================

def notify_all(notifications, message):
    # TODO: loop and call .send(message) on each
    pass


# ============================================================
# Run + check
# ============================================================

if __name__ == "__main__":
    targets = [
        EmailNotification("alice@example.com"),
        SmsNotification("+1-555-0100"),
        PushNotification("bob", device_id="abc123"),
    ]
    notify_all(targets, "Your interview is tomorrow")

    # Abstract class cannot be instantiated
    try:
        Notification("x")
        assert False, "should have raised TypeError"
    except TypeError:
        pass

    # PushNotification keeps device_id
    p = PushNotification("bob", "abc123")
    assert p.recipient == "bob"
    assert p.device_id == "abc123"

    print("✅ All tests passed.")
