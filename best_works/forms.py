from django import forms

from best_works.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "text")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "uk-input",
                "placeholder": "Введите Ваше имя",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "uk-input",
                "placeholder": "Введите адрес электронной почты",
            }
        )
        self.fields["text"].widget.attrs.update(
            {
                "class": "uk-textarea",
                "rows": 5,
                "placeholder": "Введите сообщение",
            }
        )
