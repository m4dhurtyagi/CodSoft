# To-Do List Application

This repository contains a Kivy-based to-do list application built with Python. The app provides a simple graphical interface for managing tasks, featuring a form for adding new items and a dynamic list view for displaying them.

## Features

* Add New Tasks: Users can enter tasks into a text input field and submit them. The tasks are saved to a data.json file and the input field is cleared after submission.
* View Tasks: Tasks are displayed in a scrollable list that updates every second to reflect the latest data from data.json.
* Navigation: An intuitive menu allows users to switch between the task list view (HomeScreen) and the task entry form (AddScreen).

## Components

* AddNewForm: Handles user input and saves new tasks.
* MyRecycleView: Displays tasks in a scrollable view and refreshes periodically.
* Menu: Provides navigation between different screens.
* HomeScreen: Displays the list of tasks.
* AddScreen: Contains the form for adding new tasks.
* ScreenManagement: Manages the transitions between HomeScreen and AddScreen.

The .kv file defines the application's layout, utilizing Kivy's BoxLayout and RecycleBoxLayout for efficient display and organization. This project demonstrates Kivy’s capabilities for building interactive and dynamic user interfaces.
