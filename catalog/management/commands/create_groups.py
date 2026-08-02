from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создаёт группы модераторов и контент-менеджеров'

    def handle(self, *args, **options):
        # --- Группа «Модератор продуктов» ---
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа «Модератор продуктов» создана'))
        else:
            self.stdout.write('Группа «Модератор продуктов» уже существует')

        # Право can_unpublish_product
        perm_unpublish = Permission.objects.get(codename='can_unpublish_product')
        moderator_group.permissions.add(perm_unpublish)

        # Право удаления любого продукта
        perm_delete = Permission.objects.get(codename='delete_product')
        moderator_group.permissions.add(perm_delete)

        self.stdout.write(self.style.SUCCESS('Права для модератора назначены'))

        # --- Группа «Контент-менеджер» ---
        content_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа «Контент-менеджер» создана'))
        else:
            self.stdout.write('Группа «Контент-менеджер» уже существует')

        # Права для блога: добавить, изменить, удалить, просматривать
        blog_perms = Permission.objects.filter(
            codename__in=[
                'add_blogentry',
                'change_blogentry',
                'delete_blogentry',
                'view_blogentry',
            ]
        )
        for perm in blog_perms:
            content_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Права для контент-менеджера назначены'))
        self.stdout.write(self.style.SUCCESS('Готово!'))
