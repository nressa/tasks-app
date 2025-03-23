class ValidateStatus:

    @classmethod
    def in_list(cls, value):
        if value not in ['to do', 'in progress', 'for review', 'done', 'close']:
            print(f"❌ {value} is not allowed.")
            return False
        
        else:
            return value
