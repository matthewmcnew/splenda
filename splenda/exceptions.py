class SplendaException(Exception):
    def __init__(self, method_name, fake_class, spec_class):
        self.fake_class = fake_class
        self.spec_class = spec_class
        self.method_name = method_name

    def __str__(self):
        spec_name = self.spec_class.__name__
        fake_name = self.fake_class.__name__
        return self.message.format(
            fake_name=fake_name,
            method_name=self.method_name,
            spec_name=spec_name)
