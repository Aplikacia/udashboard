from horizon import forms


FORM_TYPE_MAP = {
    'text': forms.Textarea,
    'char': forms.CharField,
    'bool': forms.BooleanField,
}


class BaseForm(forms.SelfHandlingForm):

    def handle(self):
        pass


class AddNewRoleForm(forms.SelfHandlingForm):
    name = forms.CharField(label='Name')

    def handle(self, request, data):
        print 'AddNewRoleForm handle data:', data
        return data


def form_field_factory(type_, options):
    cls = FORM_TYPE_MAP[type_]
    return cls(**options)


def form_factory(dct):
    name = '%sForm' % dct['name']

    d = {}
    for f in dct['fields']:
        d[f['name']] = form_field_factory(f['type'], f['options'])
    cls = type(name, (BaseForm,), d)
    return cls


def get_form_initial(dct):
    res = {}
    for f in dct['fields']:
        res[f['name']] = f['value']
    return res
