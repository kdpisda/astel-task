import os

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    help = "Create a new resource with a predefined directory structure"

    def add_arguments(self, parser):
        parser.add_argument(
            "app", type=str, help="App name where the resource will be created"
        )
        parser.add_argument("resource", type=str, help="Name of the new resource")

    def handle(self, *args, **options):
        app_name = options["app"]
        resource_name = options["resource"]

        # Base and subdirectory paths
        base_path = os.path.join(app_name, resource_name)
        sub_dirs = ["admins", "models", "serializers", "views", "tasks"]

        try:
            # Create base directory and __init__.py
            os.makedirs(base_path, exist_ok=True)
            open(os.path.join(base_path, "__init__.py"), "a").close()

            # Create subdirectories and __init__.py
            for dir_name in sub_dirs:
                dir_path = os.path.join(base_path, dir_name)
                os.makedirs(dir_path, exist_ok=True)
                open(os.path.join(dir_path, "__init__.py"), "a").close()

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created resource "{resource_name}" in app "{app_name}"'
                )
            )
        except Exception as e:
            raise CommandError(f"Error creating resource: {e}")
