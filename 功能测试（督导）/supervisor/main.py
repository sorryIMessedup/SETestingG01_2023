import unittest
import HtmlTestRunner

import CheckConsult
import CheckConsultant
import CheckHelp
import CheckSchedule
import CheckVisitor
import ExportConsult
import ExportHelp
import ManageSchedule
import ChangePassword


def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CheckConsult.MyTestCase))
    suite.addTest(unittest.makeSuite(CheckConsultant.MyTestCase))
    suite.addTest(unittest.makeSuite(CheckHelp.MyTestCase))
    suite.addTest(unittest.makeSuite(CheckSchedule.MyTestCase))
    suite.addTest(unittest.makeSuite(CheckVisitor.MyTestCase))
    suite.addTest(unittest.makeSuite(ExportConsult.MyTestCase))
    suite.addTest(unittest.makeSuite(ExportHelp.MyTestCase))
    suite.addTest(unittest.makeSuite(ManageSchedule.MyTestCase))
    suite.addTest(unittest.makeSuite(ChangePassword.MyTestCase))

    return suite


if __name__ == '__main__':
    suite = create_suite()
    runner = HtmlTestRunner.HTMLTestRunner(report_title="测试报告", verbosity=2, descriptions=True)
    runner.run(suite)
