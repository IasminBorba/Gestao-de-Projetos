from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Projetos


@receiver(m2m_changed, sender=Projetos.equipe.through)
def atualiza_qtd_membros(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove']:
        instance.qtd_membros = instance.equipe.count()
        instance.save()