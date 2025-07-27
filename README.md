# **PyQt6_country_picker**
Simple country picker GUI app built with PyQt6 for recruitment exercise.

## Instructions

This exercise is meant to not require more than a few hours of your time. It is ok to come with an incomplete implementation if you get stuck, as long as it provides good foundation for discussion in a potential subsequent interview.

We would like you to write a small Python GUI program following best Python standards and coding practices. You can use any of the following Python packages for Qt (pick the one you’re most comfortable with):

PyQt6
PyQt5
PySide6
This program must display a window when launched. This window must contain a combobox (QComboBox) and a label (QLabel). At the initial stage, both the combobox and the label are empty.

Once the window is shown, a network request should be issued to gather JSON data from the https://www.apicountries.com/countries. JSON should be processed into a list of country names, and the combobox must be popuplated with the list of country names ordered alphabetically.

When the user picks a country from the combobox, the label should change to Selected: <insert country name here>.

As a bonus objective, you can try to download and parse JSON in a background thread, but make sure to always update the UI in the main thread. Use the tools that fit your needs best, e.g. you can choose between either Python or Qt threading primitives.

The program should be a valid Python package or module named country_picker and be runnable with python -m country_picker command.

As another bonus objective, you can add an optional command line argument that will allow to pre-select a given country by default, e.g. python -m country_picker --select Switzerland.

Write a simple test case for your JSON parsing logic using the Python testing framework of your preference. You are not required to test the GUI itself.

Use any appropriate tools from the standard library to help with your implementation (or 3rd party dependencies if required), and write the code such that it is as readable and maintainable as possible, e.g. docstrings, type hints, comments, etc. Organize the code in the file hierarchy that is the most appropriate for such package or module.

Track the source code with git and host it on either Github or Gitlab that is publicly visible. Use appropriate git configuration, such as .gitignore files, to complement the source code. There is no need to set up a CI for this exercise.