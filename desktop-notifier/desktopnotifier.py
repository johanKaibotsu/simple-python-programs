from socket import timeout
from plyer import notification
title = 'Alert'
message = 'this is a important notification'
notification.notify(title = title, message = message, app_icon = 'desktop-notifier/icon.ico', timeout = 10)