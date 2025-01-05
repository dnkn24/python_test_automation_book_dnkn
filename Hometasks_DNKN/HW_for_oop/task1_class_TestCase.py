class TestCase:

    def setup(self):
        print("Setting up the test.")

    def run(self):
        print("Running the test")

    def teardown(self):
        print("Tearing down after a test.")

tc_1 = TestCase()
tc_2 = TestCase()
tc_3 = TestCase()

tc_1.setup()
tc_1.run()
tc_1.teardown()

tc_2.teardown()
tc_3.setup()