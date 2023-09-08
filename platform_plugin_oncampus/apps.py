"""
platform_plugin_oncampus Django application initialization.
"""

from django.apps import AppConfig


class PlatformPluginOncampusConfig(AppConfig):
    """
    Configuration for the platform_plugin_oncampus Django application.
    """

    name = 'platform_plugin_oncampus'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'oncampus',
                'regex': r'^oncampus/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'test': {'relative_path': 'settings.test'},
                'common': {'relative_path': 'settings.common'},
                'production': {'relative_path': 'settings.production'},
            },
        },
    }
