import unittest
import demographic_data_analyzer

class DemographicDataTest(unittest.TestCase):
    def setUp(self):
        self.results = demographic_data_analyzer.analyze_demographic_data(display_output=False)

    def test_race_distribution(self):
        obtained = self.results['race_distribution'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in race distribution count. Expected [27816, 3124, 1039, 311, 271].")

    def test_avg_age_males(self):
        obtained = self.results['avg_age_males']
        expected = 39.4
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the average age of males.")

    def test_bachelors_percentage(self):
        obtained = self.results['bachelors_percentage']
        expected = 16.4
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the percentage of Bachelor's degree holders.")

    def test_higher_education_earning_50k(self):
        obtained = self.results['higher_education_earning_50k']
        expected = 46.5
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the percentage of higher education individuals earning >50K.")

    def test_lower_education_earning_50k(self):
        obtained = self.results['lower_education_earning_50k']
        expected = 17.4
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the percentage of lower education individuals earning >50K.")

    def test_minimum_working_hours(self):
        obtained = self.results['minimum_working_hours']
        expected = 1
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in minimum working hours.")

    def test_rich_min_hour_workers(self):
        obtained = self.results['rich_min_hour_workers']
        expected = 10
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the percentage of high earners among those working the least.")

    def test_top_earning_country(self):
        obtained = self.results['top_earning_country']
        expected = 'Iran'
        self.assertEqual(obtained, expected, msg="Mismatch in the country with the highest percentage of high earners.")

    def test_top_country_percentage(self):
        obtained = self.results['top_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(obtained, expected, msg="Mismatch in the highest percentage of high earners by country.")

    def test_top_occupation_india(self):
        obtained = self.results['top_occupation_india']
        expected = 'Prof-specialty'
        self.assertEqual(obtained, expected, msg="Mismatch in the top occupation for high earners in India.")

if __name__ == "__main__":
    unittest.main()
