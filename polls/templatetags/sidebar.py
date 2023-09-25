from django import template

register = template.Library()

MENU = [
    {
        'app': 'polls',
        'name': 'Polls Application',
        'icon': 'icon-briefcase',
        'models_render': ['Choice'],
        'models_extend': [
            {'name': 'Custom View', 'perms': {'add': True, 'change': True, 'delete': True, 'view': True}, 'admin_url': '/admin/custom_page/', 'view_only': False}
        ]
    },
    {
        'app': '',
        'name': 'Queues',
        'icon': 'icon-list',
        'models': [
            {'name': 'Job Queues', 'icon': 'icon-list', 'admin_url': '/dadmin/rq/'},
            {'name': 'ADT Queue', 'icon': 'icon-list', 'admin_url': '/dadmin/adt_queue/'},
            {'name': 'Redis Status', 'icon': 'icon-list', 'admin_url': '/dadmin/redis_status/'},
            {'name': 'Job Timings', 'icon': 'icon-list', 'admin_url': '/dadmin/job_timings/'},
        ]
    },
    {
        'app': '',
        'name': 'Client Dashboard',
        'icon': 'icon-list',
        'models': [
            {'name': 'Dashboard App', 'icon': 'icon-list', 'admin_url': 'https://demo.q-reviews.com/', 'blank': True},
        ],
    },
]


@register.simple_tag
def custom_nav_sidebar(app_list):
    new_app_list = []
    app_names = []

    for menu_item in MENU:
        for app_item in app_list:
            if menu_item['app'] == app_item['app_label']:
                new_app_list.append({
                  'name': menu_item['name'],
                  'app_label': app_item['app_label'],
                  'app_url': app_item['app_url'],
                  'icon': menu_item['icon'],
                  'has_module_perms': app_item['has_module_perms'],
                  'models': app_item['models'] + menu_item['models_extend']
                })

            elif not menu_item['app'] and menu_item['name'] not in app_names:
                new_app_list.append({
                    'name': menu_item['name'],
                    'app_label': menu_item['name'],
                    'app_url': '',
                    'icon': menu_item['icon'],
                    'has_module_perms': app_item['has_module_perms'],
                    'models': menu_item['models']
                })
            app_names.append(menu_item['name'])

    return new_app_list