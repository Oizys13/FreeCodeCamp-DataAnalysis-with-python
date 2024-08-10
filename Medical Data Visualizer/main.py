# Entry point for development. Refer to README.md for usage instructions.
import medical_data_visualizer
from unittest import main

# Generate and save plots
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run the test suite
main(module='test_module', exit=False)
