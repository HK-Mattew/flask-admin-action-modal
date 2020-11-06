# flask-admin-action-modal

English: Open modal with form when performing action

Pt-BR: Abrir modal com formulário ao realizar a ação


![GIF](asm.gif)


# Example of use
```python
from wtforms import HiddenField, IntegerField, Form
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import InputRequired
from asm_modelview import ActionShowModal
from flask_admin.actions import action


class AddMoney(Form):
    value = IntegerField(validators=[InputRequired()])


class User(ModelView, ActionShowModal):
    list_template = 'admin/model/custom_list.html'

    @action('add_money', 'Adicionar Dinheiro', confirmation=None)
    def add_money(self, ids):

        return self.create_action_modal(
            form=AddMoney,
            action_name='add_money',
            callback=self.callback_add_money,
            title_modal='Adicionar Dinheiro'
            )


    def callback_add_money(self, ids, form):
        """
        Apply the desired action
        """
        display_ids = ','.join(ids)
        flash(f'Callback IDS: {display_ids} | Callback Value: {form.value.data}')


```
