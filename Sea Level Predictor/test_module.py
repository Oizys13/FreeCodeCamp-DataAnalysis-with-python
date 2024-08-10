import unittest
import plot_generator
import matplotlib as mpl
import numpy as np

class PlotTests(unittest.TestCase):
    def setUp(self):
        self.ax = plot_generator.generate_sea_level_plot()

    def test_title(self):
        actual_title = self.ax.get_title()
        expected_title = "Sea Level Increase"
        self.assertEqual(actual_title, expected_title, "Title should be 'Sea Level Increase'")
    
    def test_labels(self):
        actual_xlabel = self.ax.get_xlabel()
        expected_xlabel = "Year"
        self.assertEqual(actual_xlabel, expected_xlabel, "X-axis label should be 'Year'")
        actual_ylabel = self.ax.get_ylabel()
        expected_ylabel = "Sea Level (inches)"
        self.assertEqual(actual_ylabel, expected_ylabel, "Y-axis label should be 'Sea Level (inches)'")
        actual_xticks = self.ax.get_xticks().tolist()
        expected_xticks = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(actual_xticks, expected_xticks, "X-axis ticks are not as expected")

    def test_scatter_data(self):
        scatter_offsets = self.ax.get_children()[0].get_offsets().data.tolist()
        expected_offsets = [[1880.0, 0.0], [1881.0, 0.220472441], [1882.0, -0.440944881], [1883.0, -0.232283464], ...]
        np.testing.assert_almost_equal(scatter_offsets, expected_offsets, 7, "Scatter plot data points differ from expected.")

    def test_fit_lines(self):
        first_fit_line = self.ax.get_lines()[0].get_ydata().tolist()
        expected_first_line = [-0.5421240249263661, -0.4790794409142336, ...]
        np.testing.assert_almost_equal(first_fit_line, expected_first_line, 7, "First line of best fit does not match expected.")
        
        second_fit_line = self.ax.get_lines()[1].get_ydata().tolist()
        expected_second_line = [7.06107985777146, 7.227507131103323, ...]
        np.testing.assert_almost_equal(second_fit_line, expected_second_line, 7, "Second line of best fit does not match expected.")

if __name__ == "__main__":
    unittest.main()
