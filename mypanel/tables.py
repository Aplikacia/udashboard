from horizon.tables import DataTable
from horizon.tables import Column
from horizon.tables import LinkAction


class AddNewRoleAction(LinkAction):
    name = 'add_new_role_action'
    verbose_name = 'New Role'
    classes = ('ajax-modal',)
    url = 'horizon:mydashboard:mypanel:add_new_role'

    def handle(self):
        pass


class EditRoleAction(LinkAction):
    name = 'edit_role_action'
    verbose_name = 'Edit'

    def get_link_url(self, datum=None):
        return 'mydashboard/edit_role/%s' % datum.id


class AvailableRolesTable(DataTable):
    id = Column('id', hidden=True)
    name = Column('name')
    created = Column('created')
    last_modified = Column('last_modified')

    class Meta:
        name = 'available_roles_table'
        table_actions = (AddNewRoleAction,)
        row_actions = (EditRoleAction,)
