from django.forms import Form, ModelForm


class BootstrapForm(Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(args, kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(args, kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
