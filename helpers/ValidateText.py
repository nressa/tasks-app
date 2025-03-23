class ValidateText:

    @classmethod
    def required_string(cls, prompt, field_name):
        while True:
            value = input(prompt).strip()

            if not value:
                print(f"❌ {field_name} is required.")
                return False

            elif len(value) > 255:
                print(f"❌ {field_name} must not exceed 255 characters.")
                return False

            else:
                return value
