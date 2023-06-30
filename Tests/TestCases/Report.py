#-*- coding: UTF-8 -*-
import unittest
import HtmlTestRunner
from Tests.TestCases.CheckElements import Testing


#테스트 케이스 로드
testcase = unittest.TestLoader().loadTestsFromTestCase(Testing)

#testsuite에 리스트형으로 전달
testsuite = unittest.TestSuite([testcase])

#print(testsuite) / 어떤 테스트 케이스 불러왔는지 확인
HtmlTestRunner.HTMLTestRunner(
                            output="Reports",  # 보고서 생성할 폴더 이름
                            report_name="이사로_자동화테스트",  # HTML 파일 이름
                            report_title="Test Results",  # HTML 파일 타이틀
                            combine_reports=True,  # True : 테스트 케이스가 여러개 일 때 보고서 하나로 합치기
                            template="tep.html"
                            ).run(testsuite)

## 파이썬 3.X버전에서 HtmlTestRunner 에러 뜰 경우
# Inside the HtmlTestRunner folder of the package you have installed, look for result.py
#
# Find the "_exc_info_to_string" method of the "HtmlTestResult" class.
#
# Replace these lines:
#
# if exctype is test.failureException:
#      # Skip assert*() traceback levels
#      length = self._count_relevant_tb_levels(tb)
#      msg_lines = traceback.format_exception(exctype, value, tb, length)
# if exctype is test.failureException:
#     # Skip assert*() traceback levels
#     msg_lines = traceback.format_exception(exctype, value, tb)