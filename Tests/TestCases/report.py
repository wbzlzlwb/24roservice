#-*- coding: UTF-8 -*-
import unittest
import HtmlTestRunner
from Tests.TestCases.CheckElements import Testing



testcase = unittest.TestLoader().loadTestsFromTestCase(Testing)


testsuite = unittest.TestSuite([testcase])

#print(testsuite)
HtmlTestRunner.HTMLTestRunner(
                            output="Reports",  # 보고서 생성할 폴더 이름
                            report_name="이사로_자동화테스트",  # HTML 파일 이름
                            report_title="Test Results",  # HTML 파일 타이틀
                            combine_reports=True,  # True : 테스트 케이스가 여러개 일 때 보고서 하나로 합치기
                            template="tep.html"
                            ).run(testsuite)