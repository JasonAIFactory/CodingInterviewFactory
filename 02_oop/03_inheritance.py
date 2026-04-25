"""
03_inheritance.py  —  REFERENCE FILE

Goal: Inheritance, super(), method override, abstract base classes.
This shows up in design questions like:
  "Design a notification system that supports email, SMS, and push."
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. Abstract base class  —  defines the contract
# ============================================================

class Notification(ABC):
    """
    SAY: "ABC means abstract base class.
          You cannot instantiate Notification directly.
          Every subclass MUST implement send()."
    """

    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str) -> None:
        ...

    # Concrete method shared by all subclasses
    def log(self, message: str) -> None:
        # SAY: "I put shared behavior in the base class so I don't repeat it."
        print(f"[LOG] {self.__class__.__name__} -> {self.recipient}: {message}")


# ============================================================
# 2. Subclasses  —  each implements send() its own way
# ============================================================

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        # SAY: "I call self.log to reuse the parent's logging behavior."
        self.log(message)
        print(f"Sending EMAIL to {self.recipient}: {message}")


class SmsNotification(Notification):
    def send(self, message: str) -> None:
        self.log(message)
        print(f"Sending SMS to {self.recipient}: {message}")


# ============================================================
# 3. Subclass that adds state via super().__init__
# ============================================================

class PushNotification(Notification):
    def __init__(self, recipient: str, device_id: str):
        # SAY: "super().__init__ calls the parent constructor.
        #       Then I add my own attribute on top."
        super().__init__(recipient)
        self.device_id = device_id

    def send(self, message: str) -> None:
        self.log(message)
        print(f"Pushing to device {self.device_id}: {message}")


# ============================================================
# 4. Polymorphism  —  treat all subclasses the same way
# ============================================================

def notify_all(notifications, message):
    """
    SAY: "I do not care which subclass each item is.
          As long as it implements send(), the loop works.
          This is polymorphism — same interface, different behavior."
    """
    for n in notifications:
        n.send(message)


# ============================================================
# Run examples
# ============================================================

if __name__ == "__main__":
    targets = [
        EmailNotification("alice@example.com"),
        SmsNotification("+1-555-0100"),
        PushNotification("bob", device_id="abc123"),
    ]
    notify_all(targets, "Your interview is tomorrow")

    # Trying to instantiate the abstract class raises TypeError
    try:
        Notification("x")
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")
