# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from horizon import views
from horizon import forms

from .tables import AvailableRolesTable
from .forms import form_factory
from .forms import get_form_initial
from .forms import AddNewRoleForm
from .api_client import get_roles
from .api_client import get_classes
from .api_client import update_role
from .api_client import get_role


def get_forms(request, classes, with_initial=False, data=None):
    forms = []
    for c in classes:
        name = c['name']
        form = form_factory(c)
        if with_initial:
            initial = get_form_initial(c)
        else:
            initial = None
        forms.append({
            'name': name,
            'form': form(request=request, data=data, initial=initial, prefix=name)
        })
    return forms


class IndexView(views.APIView):
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        data = get_roles()
        context['table'] = AvailableRolesTable(request, data=data)
        return context


class AddNewRoleView(forms.ModalFormView):
    form_class = AddNewRoleForm
    template_name = 'mydashboard/mypanel/add_new_role.html'
    success_url = reverse_lazy('horizon:mydashboard:mypanel:index')
    submit_url = reverse_lazy('horizon:mydashboard:mypanel:add_new_role')


class EditRoleView(views.APIView):
    template_name = 'mydashboard/mypanel/edit_role.html'

    def get_data(self, request, context, role_id, *args, **kwargs):
        classes = get_classes(role_id)
        role = get_role(role_id)
        context['forms'] = get_forms(request, classes, with_initial=True)
        context['role'] = role
        return context

    def post(self, request, role_id):
        classes = get_classes(role_id)
        role = get_role(role_id)
        forms = get_forms(request, classes, data=request.POST)

        update_dct = {}
        valid = True
        for f in forms:
            form = f['form']
            if form.is_valid():
                update_dct[f['name']] = {'fields': form.cleaned_data}
            else:
                valid = False

        if valid:
            update_role(role_id, update_dct)
        else:
            return self.render_to_response({
                'forms': forms,
                'role': role,
            })

        return HttpResponseRedirect(request.path)
