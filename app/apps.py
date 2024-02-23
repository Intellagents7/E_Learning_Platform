from django.apps import AppConfig

class ELearningPlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_learning_platform'

    def ready(self):
        # Import signal handlers
        import e_learning_platform.signals
