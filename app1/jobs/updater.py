from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import printhello
from datetime import datetime

def start():
    scheduler = BackgroundScheduler()
    # Change 'second=1' to 'seconds=1'
    scheduler.add_job(printhello, 'interval', start_date = "2024-2-23 11:00:00")
    scheduler.start()