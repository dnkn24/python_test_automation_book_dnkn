class BaseTest:
    def setup(self):
        print("BaseTest: Setting up the test")

    def run(self):
        print("BaseTest: Running the test.")

    def teardown(self):
        print("BaseTest: Tearing down the test")

class CustomMixinTest:
    def log(self):
        print("CustomMixinTest: Logging test.")

class MixedTest(BaseTest,CustomMixinTest):
    def setup(self):
        print("MixedTest: setting up the test")


def execute_test(test):
    test.setup()
    test.run()
    test.log()
    test.teardown()

    print("Method Resolution Order for MixedTest:")
    print(MixedTest.mro())

test_case = MixedTest()
execute_test(test_case)
