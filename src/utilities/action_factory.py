import argparse

class ActionFactory:
    @staticmethod
    def init_class(validator):
        class TemplateAction(argparse.Action):
            def __call__(self, parser, namespace, values, option_string=None):
                if not validator(values):
                    print("Got value:", values)
                    raise ValueError("Invalid Input!")
                setattr(namespace, self.dest, values)
        return TemplateAction