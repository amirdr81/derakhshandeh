from notif_box import NotifBox
from notificationBox import NotificationBox

class User:
    def __init__(self, name, lastname, phone, id, email, username, password, role):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.role = role,
        self.notifications = []

        def make_notification(title, description, submit_date):
            return NotificationBox.add_notification(title, description, submit_date, 0.4)
            
        def add_notification(notification):
            self.notifications.append(make_notification)
        
    