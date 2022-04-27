from django.contrib.auth import forms as auth_forms

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        # profile = Profile(
        #     **self.cleaned_data,
        #     user=user,
        # )
        # if commit:
        #     profile.save()

        return user
