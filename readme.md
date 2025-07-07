# AI Logic Testing Repo

## Overview

This repository provides a clean and modular structure for developing, testing, and integrating AI-related functions in Python. The core AI logic is written and tested locally in `local_ai.py`, using test cases defined in `data_format.py`.


## Project Structure

- `local_ai.py`  
  Contains raw AI functions written as pure Python functions. No Django or web dependencies here. Used for local development and testing.

- `data_format.py`  
  Defines test cases as Python variables (`test_cases` list). Each test case specifies input arguments and expected outputs for AI functions.

- `ai_logic.py` *(optional)*  
  Contains reusable AI logic functions to be imported by Django views or other services.

---


## Best Practices

- Keep AI functions pure
- Use data_format.py to maintain test coverage and quickly verify changes.
- Pin package versions in requirements.txt for consistent deployments.