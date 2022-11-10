from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'

    def ready(self):
        print("Starting Scheduler...")
        from .mensage_scheduler import mensage_scheduler
        #mensage_scheduler.start()
