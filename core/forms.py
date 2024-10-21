from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "phone_number", "email", "text")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "uk-input",
                "placeholder": "Введите Ваше имя",
            }
        )
        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "uk-input",
                "placeholder": "Введите Ваш номер телефона",
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
