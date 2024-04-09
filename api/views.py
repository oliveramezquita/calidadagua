from rest_framework.views import APIView
from api.use_cases.test_data_use_case import TestDataUseCase
from api.use_cases.create_user_use_case import CreateUserUseCase
from api.use_cases.register_user_use_case import RegisterUserUseCase
from api.use_cases.update_user_use_case import UpdateUserUseCase
from api.use_cases.login_use_case import LoginUseCase
from api.use_cases.forgot_password_use_case import ForgotPasswordUseCase
from api.use_cases.reset_password_use_case import ResetPasswordUseCase
from api.use_cases.get_users_use_case import GetUsersUseCase
from api.use_cases.get_user_by_id_use_case import GetUserByIdUseCase
from api.use_cases.get_info_from_users_use_case import GetInfoFromUsersUseCase
from api.use_cases.create_catalog_use_case import CreateCatalogUseCase
from api.use_cases.get_catalogs_use_case import GetCatalogsUseCase
from api.use_cases.get_catalog_by_id_use_case import GetCatalogByIdUseCase
from api.use_cases.update_catalog_use_case import UpdateCatalogUseCase
from api.use_cases.get_projects_use_case import GetProjectsUseCase
from api.use_cases.get_project_by_id_use_case import GetProjectByIdUseCase
from api.use_cases.update_project_use_case import UpdateProjectUseCase
from django.db.transaction import atomic


class UsersView(APIView):
    def get(self, request):
        use_case = GetUsersUseCase(request)
        return use_case.execute()

    def post(self, request):
        use_case = CreateUserUseCase(user_raw_data=request.data)
        return use_case.execute()

    def patch(self, request):
        use_case = RegisterUserUseCase(user_raw_data=request.data)
        return use_case.execute()


class UserViewById(APIView):
    def get(self, request, user_id):
        use_case = GetUserByIdUseCase(request, user_id)
        return use_case.execute()

    def patch(self, request, user_id):
        with atomic():
            user_case = UpdateUserUseCase(
                user_raw_data=request.data,
                user_id=user_id
            )
            return user_case.execute()

    def delete(self, request, user_id):
        use_case = UpdateUserUseCase(
            user_raw_data={'_deleted': True},
            user_id=user_id
        )
        return use_case.delete()


class InstitutionsListView(APIView):
    def get(self, request):
        use_case = GetInfoFromUsersUseCase()
        return use_case.institutions_list()


class CatalogView(APIView):
    def post(self, request):
        catalog_use_case = CreateCatalogUseCase(catalog_raw_data=request.data)
        return catalog_use_case.execute()

    def get(self, request):
        catalog_use_case = GetCatalogsUseCase()
        return catalog_use_case.execute()


class CatalogViewById(APIView):
    def get(self, request, catalog_id):
        use_case = GetCatalogByIdUseCase(
            request=request, catalog_id=catalog_id)
        return use_case.execute()

    def patch(self, request, catalog_id):
        use_case = UpdateCatalogUseCase(
            catalog_raw_data=request.data, catalog_id=catalog_id)
        return use_case.execute()


class ProjectView(APIView):
    def get(self, request):
        use_case = GetProjectsUseCase()
        return use_case.execute()


class ProjectViewById(APIView):
    def get(self, request, project_id):
        use_case = GetProjectByIdUseCase(
            request=request, project_id=project_id)
        return use_case.execute()

    def patch(self, request, project_id):
        use_case = UpdateProjectUseCase(
            project_raw_data=request.data, project_id=project_id)
        return use_case.execute()


class LoginView(APIView):
    def post(self, request):
        login_use_case = LoginUseCase(login_raw_data=request.data)
        return login_use_case.execute()


class ForgotPasswordView(APIView):
    def post(self, request):
        forgot_password_use_case = ForgotPasswordUseCase(raw_data=request.data)
        return forgot_password_use_case.execute()


class ResetPasswordView(APIView):
    def post(self, request):
        reset_password_use_case = ResetPasswordUseCase(raw_data=request.data)
        return reset_password_use_case.execute()


class TestDataView(APIView):
    def post(self, request):
        testdata_use_case = TestDataUseCase(raw_data=request.data)
        return testdata_use_case.test_data()


class EncryptView(APIView):
    def post(self, request):
        test = TestDataUseCase(raw_data=request.data)
        return test.encrypt_test()


class TestEmailFormView(APIView):
    def post(self, request):
        test = TestDataUseCase(raw_data=request.data)
        return test.test_email_form()


class TestEmailRegisterView(APIView):
    def post(self, request):
        test = TestDataUseCase(raw_data=request.data)
        return test.test_email_register()


class TestEmailResetPasswordView(APIView):
    def post(self, request):
        test = TestDataUseCase(raw_data=request.data)
        return test.test_email_reset_password()
