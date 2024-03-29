# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.mypanel import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'/edit_role/(?P<role_id>\d+)$', views.EditRoleView.as_view(), name='edit_role'),
    url(r'/add_new_role/', views.AddNewRoleView.as_view(), name='add_new_role'),
]
