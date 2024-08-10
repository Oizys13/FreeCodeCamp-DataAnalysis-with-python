import unittest
import medical_data_visualizer
import matplotlib as mpl

# Unit tests for categorical plot
class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_catplot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "variable", "X-axis label for the categorical plot should be 'variable'.")
        self.assertEqual(self.ax.get_ylabel(), "total", "Y-axis label for the categorical plot should be 'total'.")

        expected_labels = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        actual_labels = [label.get_text() for label in self.ax.get_xticklabels()]
        self.assertEqual(actual_labels, expected_labels, "X-axis labels should be ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'].")

    def test_number_of_bars(self):
        bar_count = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        self.assertEqual(bar_count, 13, "There should be 13 bars in the categorical plot.")

# Unit tests for heatmap
class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heatmap_labels(self):
        expected_labels = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        actual_labels = [label.get_text() for label in self.ax.get_xticklabels()]
        self.assertEqual(actual_labels, expected_labels, "X-axis labels in the heatmap should match the expected labels.")

    def test_heatmap_values(self):
        expected_values = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        actual_values = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
        self.assertEqual(actual_values, expected_values, "Heatmap values should match the expected correlation values.")

if __name__ == "__main__":
    unittest.main()
