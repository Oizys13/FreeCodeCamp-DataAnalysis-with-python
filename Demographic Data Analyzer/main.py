# Entry point for development. Start by reviewing README.md for setup instructions.
import demographic_data_analyzer
from unittest import main

# Execute the demographic data analysis function
demographic_data_analyzer.analyze_demographic_data()

# Automatically run unit tests
main(module='test_module', exit=False)
