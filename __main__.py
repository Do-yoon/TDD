class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun:
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasSetUp = 1
        self.wasRun = None

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "


class TestCaseTest(TestCase):
    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetUp

    def setUp(self):
        self.test = WasRun("testMethod")


TestCaseTest("testRunning").run()


