from flask_admin import expose
from flask import (
    redirect,
    url_for,
    flash,
    request
    )


class ActionShowModal:

    ASM_ACTIONS = {}

    def create_action_modal(self, form, action_name, callback, title_modal='ASM Title'):
        if not self.ASM_ACTIONS.get(action_name):
            self.ASM_ACTIONS[action_name] = {
                'form': form,
                'action_name': action_name,
                'callback': callback,
                'title_modal': title_modal,
            }

        return redirect(
            url_for('.index_view', action_name=action_name),
            code=307
            )

    @expose('/', methods=['POST'])
    def index(self):
        action_name = request.args.get('action_name')
        if action_name:
            if not self.ASM_ACTIONS.get(action_name):
                return 'Non-existent action'

            context = {
                'asm_change': True,
                'ids': ','.join(request.form.getlist('rowid')),
                **self.ASM_ACTIONS[action_name]
            }
            for key, value in context.items():
                self._template_args[key] = value

            return self.index_view()


    @expose('/asm_callback/<action_name>/<ids>', methods=['POST'])
    def asm_callback(self, action_name, ids):

        if self.ASM_ACTIONS.get(action_name):
            self.ASM_ACTIONS[action_name]['callback'](
                ids=ids.split(','),
                form=self.ASM_ACTIONS[action_name]['form'](request.form)
                )
        else:
            return 'Non-existent action'

        return redirect(url_for('.index_view'))

    