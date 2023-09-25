from django import template

register = template.Library()

MENU_CONFIG = [
    {
        'app': 'core',
        'name': 'Client Management',
        'icon': 'fa-solid fa-gears',
        'models_ignore': ['Sauce'],
        'models_extend': [
            {'name': 'Volume info for renewal', 'permissions': 'is_superuser', 'admin_url': '/dadmin/client_db/recipient/volume_info'}
        ]
    },
    {
        'app': 'polls',
        'name': 'Polls Application',
        'icon': 'fa-solid fa-list',
        'models_ignore': [],
        'models_extend': [
            {'name': 'Custom View', 'permissions': 'is_superuser', 'admin_url': '/admin/polls/custom_page/'}
        ]
    },
    {
        'app': '',
        'name': 'Queues',
        'icon': 'fa-solid fa-file-lines',
        'models_ignore': [],
        'models': [
            {'name': 'Job Queues', 'permissions': '', 'admin_url': '/dadmin/rq/'},
            {'name': 'ADT Queue', 'permissions': '', 'admin_url': '/dadmin/adt_queue/'},
            {'name': 'Redis Status', 'permissions': '', 'admin_url': '/dadmin/redis_status/'},
            {'name': 'Job Timings', 'permissions': '', 'admin_url': '/dadmin/job_timings/'},
        ]
    },
    {
        'app': '',
        'name': 'Client Dashboard',
        'icon': 'fa-solid fa-sitemap',
        'models_ignore': [],
        'models': [
            {'name': 'Dashboard App', 'permissions': '', 'admin_url': 'https://demo.q-reviews.com/', 'blank': True},
        ],
    },
]


@register.simple_tag
def custom_nav_sidebar(app_list):
    new_app_list = []
    app_names = []

    # TODO: check permissions for each models.
    for menu in MENU_CONFIG:
        for app in app_list:
            if menu['app'] == app['app_label']:
                app['models'] = [model for model in app['models'] if model['object_name'] not in menu['models_ignore']]

                new_app_list.append({
                  'name': menu['name'],
                  'app_label': app['app_label'],
                  'icon': menu['icon'],
                  'has_module_perms': app['has_module_perms'],
                  'models': app['models'] + menu['models_extend']
                })

            elif not menu['app'] and menu['name'] not in app_names:
                new_app_list.append({
                    'name': menu['name'],
                    'app_label': menu['name'],
                    'icon': menu['icon'],
                    'has_module_perms': app['has_module_perms'],
                    'models': menu['models']
                })
            app_names.append(menu['name'])
    [print(item) for item in new_app_list]
    return new_app_list