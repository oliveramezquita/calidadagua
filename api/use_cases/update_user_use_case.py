from api.helpers.http_responses import ok
from rest_framework import exceptions
from fcea_monitoreo.utils import update_document
from api.serializers.user_serializer import UserSerializer
import re
import bcrypt


class UpdateUserUseCase:
    def __init__(self, user_raw_data):
        self.user_raw_data = user_raw_data

    def execute(self):
        self.validate_params()
        data = self.update()
        return ok(UserSerializer(data).data)

    def validate_params(self):
        # validate requiere fields
        if 'email' not in self.user_raw_data:
            raise exceptions.ValidationError(
                "El correo electrónico es obligatorio"
            )
        if 'password' not in self.user_raw_data or 'confirm_password' not in self.user_raw_data:
            raise exceptions.ValidationError(
                "La contraseña y la confirmación de la contraseña son obligatorios"
            )
        if 'name' not in self.user_raw_data or 'last_name' not in self.user_raw_data:
            raise exceptions.ValidationError(
                "El nombre y los apellidos son obligatorios"
            )
        if 'phone' not in self.user_raw_data:
            raise exceptions.ValidationError(
                "El télefono es obligatorio"
            )

        # validate email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, self.user_raw_data['email']):
            raise exceptions.ValidationError(
                "El correo electrónico es incorrecto"
            )

    def update(self):
        return update_document(
            'users',
            {'email': self.user_raw_data['email']},
            self.user_raw_data
        )
