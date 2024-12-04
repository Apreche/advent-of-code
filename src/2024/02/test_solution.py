#!/usr/bin/env python

import unittest
import solution


class TestSolution(unittest.TestCase):
    report_data = [
        ([7, 6, 4, 2, 1], True, True),
        ([1, 2, 7, 8, 9], False, False),
        ([9, 7, 6, 2, 1], False, False),
        ([1, 3, 2, 4, 5], False, True),
        ([8, 6, 4, 4, 1], False, True),
        ([1, 3, 6, 7, 9], True, True),
    ]
    safe_report_count = 2
    tolerant_safe_report_count = 2

    def test_get_reports(self):
        self.parsed_input = solution.parse_input_file("test_input.txt")
        reports = solution.get_reports(self.parsed_input)
        correct_reports = [report for report, *_ in self.report_data]
        self.assertEqual(reports, correct_reports)

    def test_check_safety(self):
        for report, safety, *_ in self.report_data:
            self.assertEqual(solution.check_safety(report), safety)

    def test_check_safety_tolerance(self):
        for report, _, safety, *_ in self.report_data:
            result = solution.check_safety_tolerant(report)
            self.assertEqual(result, safety)

    def test_count_safe_reports(self):
        reports = [report for report, *_ in self.report_data]
        self.assertEqual(solution.count_safe_reports(reports), self.safe_report_count)

    def test_count_safe_reports_tolerant(self):
        reports = [report for report, *_ in self.report_data]
        self.assertEqual(
            solution.count_safe_reports(reports), self.tolerant_safe_report_count
        )


if __name__ == "__main__":
    unittest.main()
