from flask_admin import expose
from flask import (
    redirect,
    url_for,
    flash,
    request
    )


class ActionShowModal:


    def asm_create_action_modal(self, form, action_name, title_modal='ASM Title'):

        context = {
            'asm_change': True,
            'ids': ','.join(request.form.getlist('rowid')),
            'action_name': action_name,
            'title_modal': title_modal,
            'form': form() if isinstance(form, type) else form
        }
        for key, value in context.items():
            self._template_args[key] = value

        return self.index_view()



    @expose('/asm_callback/<action_name>/<ids>', methods=['POST'])
    def internal_asm_callback(self, action_name, ids):

        self.asm_callback(action_name, ids.split(','))

        return redirect(url_for('.index_view'))

    
