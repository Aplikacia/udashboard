
class Role(object):

    def __init__(self, d):
        for k, v in d.items():
            setattr(self, k, v)


def get_roles():
    data = [
        {
            'id': 1,
            'name': 'Role Name 1',
            'created': '123',
            'last_modified': '123',
        },
        {
            'id': 2,
            'name': 'Role Name 2',
            'created': '123',
            'last_modified': '123',
        },
        {
            'id': 3,
            'name': 'Role Name 3',
            'created': '123',
            'last_modified': '123',
        },
        {
            'id': 4,
            'name': 'Role Name 4',
            'created': '123',
            'last_modified': '123',
        },
    ]
    res = []
    for d in data:
        res.append(Role(d))

    return res


def get_classes(role_id):
    apache_class = {
        'name': 'Apache',
        'fields': [
            {
                'name': 'service_ensure',
                'value': 'running_new',
                'type': 'char',
                'options': {
                    'label': 'Service Ensure',
                },
            },
            {
                'name': 'port',
                'value': 80,
                'type': 'char',
                'options': {
                    'label': 'Port',
                    'max_length': 3,
                },
            },
            {
                'name': 'enabled',
                'value': True,
                'type': 'bool',
                'options': {
                    'label': 'Enabled',
                },
            },
            {
                'name': 'enabled',
                'value': False,
                'type': 'bool',
                'options': {
                    'label': 'Enabled 2',
                },
            },
        ],
    }
    ntp_class = {
        'name': 'NTP',
        'fields': [
            {
                'name': 'field1',
                'value': 'Value',
                'type': 'char',
                'options': {
                    'label': 'Some Field 1',
                },
            },
            {
                'name': 'field2',
                'value': 'Value 2',
                'type': 'char',
                'options': {
                    'label': 'Field 2',
                },
            },
            {
                'name': 'enabled',
                'value': False,
                'type': 'bool',
                'options': {
                    'label': 'Enabled',
                },
            },
        ],
    }
    return [
        apache_class,
        ntp_class,
    ]


def update_role(role_id, dct):
    print 'Updating Role: %s with: %s' % (role_id, dct)


def get_role(role_id):
    for r in get_roles():
        if str(r.id) == str(role_id):
            return r
