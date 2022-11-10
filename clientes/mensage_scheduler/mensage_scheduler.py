from apscheduler.schedulers.background import BackgroundScheduler
from clientes.views import verify_mensage, send_mensage

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(verify_mensage, "interval", days=1, id="verify_mensage", replace_existing=True)
    scheduler.add_job(send_mensage, "cron", hour=22, minute=24, id="send_mensage", replace_existing=True)
    scheduler.start()