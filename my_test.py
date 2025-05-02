from test_case import TestCase, TestCaseTest
from test_result import TestResult

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


if __name__ == "__main__":
    result = TestResult()

    test = TestCaseTest('test_result_success_run')
    test.run(result)

    test = TestCaseTest('test_result_failure_run')
    test.run(result)

    test = TestCaseTest('test_result_error_run')
    test.run(result)

    test = TestCaseTest('test_result_multiple_run')
    test.run(result)

    test = TestCaseTest('test_was_set_up')
    test.run(result)

    test = TestCaseTest('test_was_run')
    test.run(result)

    test = TestCaseTest('test_was_tear_down')
    test.run(result)

    test = TestCaseTest('test_template_method')
    test.run(result)

    print(result.summary())