from django.apps import AppConfig


class ProjetosConfig(AppConfig):
    name = 'projetos'

    def ready(self):
        from projetos import signals