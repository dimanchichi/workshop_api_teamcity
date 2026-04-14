import string
from faker import Faker

faker_instance = Faker()

class DataGenerator:
    """
    Класс для генерации даты с использованием Faker
    """
    @staticmethod
    def generate_project_id():
        first_latter = faker_instance.random.choice(string.ascii_letters)
        rest_characters = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=10))
        project_id = first_latter + rest_characters
        return project_id

    @staticmethod
    def generate_build_config_id():
        first_word = "build_config_"
        rest_characters = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits, k=5))
        build_config_id = first_word + rest_characters
        return build_config_id

    @staticmethod
    def generate_project_name():
        return faker_instance.word()

    @staticmethod
    def generate_build_config_name():
        list_words = faker_instance.words(nb=2)
        return "_".join(list_words)

    @staticmethod
    def generate_user_name():
        return faker_instance.name()

    @staticmethod
    def generate_password():
        return faker_instance.password(length=8)

    @staticmethod
    def generate_email():
        return faker_instance.email(domain="gmail.com")
