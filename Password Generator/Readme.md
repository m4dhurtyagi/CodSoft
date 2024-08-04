# Password Generator

This repository features a Password Generator application built with Kivy and Python. The application allows users to generate secure passwords of varying lengths and save them to a file. It includes a straightforward graphical interface and essential functionalities for generating and managing passwords.

## Features

* Password Generation: Create passwords with a mix of letters, digits, and special characters. The length of the password can be specified by the user, with validation to ensure the length is between 1 and 30 characters.
* Popup Display: Generated passwords are displayed in a popup window, where users can choose to save the password or close the popup.
 File Saving: Saved passwords are appended to a password.txt file for easy storage and retrieval.

## Components

* MyGrid: The main widget that handles password generation, popup display, and file saving. It includes methods to validate input, generate passwords, and manage the popup for displaying and saving passwords.
* PassGenApp: The main application class that initializes and runs the Kivy application.
* KV File: Defines the user interface layout using Kivy’s language, including a title label, text input for password length, and a generate button.
