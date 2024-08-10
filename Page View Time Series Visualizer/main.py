# This script is the entry point for development. Start by reading the README.md
import time_series_visualizer as tsv
from unittest import main

# Generate the plots by calling the functions
tsv.draw_line_plot()
tsv.draw_bar_plot()
tsv.draw_box_plot()

# Run the unit tests automatically
main(module='test_module', exit=False)
