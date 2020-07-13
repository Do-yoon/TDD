class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def tearDown(self):
        pass


class WasRun:
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

    def testMethod(self):
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        print(test.log)
        assert "setUp testMethod tearDown " == test.log


test = TestCaseTest("testTemplateMethod")
test.run()
# print(test.test.log)


