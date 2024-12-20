class BaseTest:

    def setup(self):
        print("Base setting up the test.")

    def run(self):
        print("Base running the test")

    def teardown(self):
        print("Base tearing down after a test.")


class CustomTest(BaseTest):
    def setup(self):
        print("Custom setting up the test.")

    def run(self):
        print("Custom running the test")

    def teardown(self):
        print("Custom down after a test.")


def execute_test(test_case):
    test_case.setup()
    test_case.run()
    test_case.teardown()


base_case = BaseTest()
custom_case = CustomTest()

execute_test(base_case)
print("And with custom set")
execute_test(custom_case)
