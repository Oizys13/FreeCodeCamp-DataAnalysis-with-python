import unittest
import time_series_visualizer as tsv
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        # Check if the cleaned data has the correct number of entries
        actual = int(tsv.df.count(numeric_only=True))
        expected = 1238
        self.assertEqual(actual, expected, "Expected DataFrame count to be 1238 after cleaning.")

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        # Generate the line plot figure
        self.fig = tsv.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        # Verify the title of the line plot
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views (5/2016 - 12/2019)"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Daily freeCodeCamp Forum Page Views (5/2016 - 12/2019)'")
    
    def test_line_plot_labels(self):
        # Verify the x and y labels of the line plot
        self.assertEqual(self.ax.get_xlabel(), "Date", "Expected xlabel to be 'Date'")
        self.assertEqual(self.ax.get_ylabel(), "Page Views", "Expected ylabel to be 'Page Views'")

    def test_line_plot_data_quantity(self):
        # Check the number of data points in the plot
        actual = len(self.ax.lines[0].get_ydata())
        expected = 1238
        self.assertEqual(actual, expected, "Expected 1238 data points in the line plot.")

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        # Generate the bar plot figure
        self.fig = tsv.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_legend_labels(self):
        # Verify the labels in the bar plot legend
        actual = [label.get_text() for label in self.ax.get_legend().get_texts()]
        expected = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                    'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, expected, "Expected bar plot legend labels to match months of the year.")
    
    def test_bar_plot_labels(self):
        # Verify the x and y labels of the bar plot
        self.assertEqual(self.ax.get_xlabel(), "Year", "Expected xlabel to be 'Year'")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views", "Expected ylabel to be 'Average Page Views'")

    def test_bar_plot_number_of_bars(self):
        # Check the number of bars in the bar plot
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 49
        self.assertEqual(actual, expected, "Expected 49 bars in the bar plot.")

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        # Generate the box plot figure
        self.fig = tsv.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_number(self):
        # Verify that the figure contains two box plots
        self.assertEqual(len(self.fig.get_axes()), 2, "Expected two box plots in the figure.")
    
    def test_box_plot_labels(self):
        # Verify the labels for both box plots
        self.assertEqual(self.ax1.get_xlabel(), "Year", "Expected xlabel for the first box plot to be 'Year'")
        self.assertEqual(self.ax1.get_ylabel(), "Page Views", "Expected ylabel for the first box plot to be 'Page Views'")
        self.assertEqual(self.ax2.get_xlabel(), "Month", "Expected xlabel for the second box plot to be 'Month'")
        self.assertEqual(self.ax2.get_ylabel(), "Page Views", "Expected ylabel for the second box plot to be 'Page Views'")

    def test_box_plot_titles(self):
        # Verify the titles for both box plots
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)", "Expected title for the first box plot to be 'Year-wise Box Plot (Trend)'")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)", "Expected title for the second box plot to be 'Month-wise Box Plot (Seasonality)'")

    def test_box_plot_number_of_boxes(self):
        # Verify the number of boxes in each plot
        self.assertEqual(len(self.ax1.lines) / 6, 4, "Expected four boxes in the first box plot.")
        self.assertEqual(len(self.ax2.lines) / 6, 12, "Expected twelve boxes in the second box plot.")

if __name__ == "__main__":
    unittest.main()
