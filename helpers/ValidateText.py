class ValidateText:

    @classmethod
    def required_string(cls, prompt, field_name):
        while True:
            value = input(prompt).strip()

            if not value:
                print(f"❌ {field_name} is required.")
            elif len(value) > 255:
                print(f"❌ {field_name} must not exceed 255 characters.")
            else:
                return value
