
class PSCommandGenerator:
    @staticmethod
    def save_to_file(code):
        path = "python/test.py"

        code = code.replace('"', '\'')

        return f'\"{code}\" | ' \
            f'Set-Content -Path \"{path}\"'

# napisz kod python, który printuje hello world w funkcji
