class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

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

    def testMethod(self):
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "

    def testBrokenMethod(self):
        raise Exception


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        print(test.log)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return "%d run, %d failed" % self.runCount, self.failureCount


TestCaseTest("testResult").run()


