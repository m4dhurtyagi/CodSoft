# Simple Calculator Application

This repository contains a simple calculator application built with Kivy and Python. The app features a basic graphical interface for performing arithmetic calculations and supports essential operations.

## Features

* Custom Text Input: The CustomTextInput class ensures only valid mathematical characters are entered and supports real-time validation.
* Real-Time Calculation: Users can input mathematical expressions, which are evaluated and displayed immediately.
* User-Friendly UI: The interface uses Kivy’s GridLayout to arrange buttons for digits, operators, and special functions. The display area is designed to be easily readable.

## Components

* CustomTextInput: A subclass of TextInput that filters input to ensure it only contains valid characters for arithmetic expressions.
* MyGrid: Manages the layout and handles the calculation logic. It updates the display based on user input.
* CalculatorApp: The main application class that initializes and runs the app.

## How It Works

* Input Handling: The CustomTextInput class processes user input and handles text validation and formatting.
* Calculation: The MyGrid class evaluates the input expression using Python’s eval() function and displays the result or an error message.
