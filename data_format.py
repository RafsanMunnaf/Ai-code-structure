# -----------------------------------------------------------
# data_format.py — AI Function Input Test Cases as Python Data
# -----------------------------------------------------------
# Purpose:
# - Define test cases as Python data structures (lists/dicts)
# - Easily import into local_ai.py or ai_logic.py for testing
# - Avoid JSON parsing overhead and allow direct Python usage
#
# Usage:
# - Define a variable (e.g., test_cases) as a list of dictionaries
# - Each dictionary includes:
#     - 'name': unique test case identifier (string)
#     - 'function': target function name (string)
#     - 'input': dict of arguments to pass to the function
#     - 'expected_keys': list of keys expected in function output (optional)
#
# Example:
# test_cases = [
#     {
#         "name": "summary_test_1",
#         "function": "generate_summary",
#         "input": {"text": "Example input text to summarize."},
#         "expected_keys": ["summary"]
#     },
#     {
#         "name": "classification_test_1",
#         "function": "classify_sentiment",
#         "input": {"text": "I love this product!"},
#         "expected_keys": ["label", "confidence"]
#     },
# ]
#
# Import and Usage in local_ai.py:
# from data_format import test_cases
#
# for case in test_cases:
#     func_name = case['function']
#     args = case['input']
#     # call function dynamically or via if-else and pass args
#
# Notes:
# - Keep data_format.py synced with your actual AI function signatures
# - This approach enables easier debugging and integration
# -----------------------------------------------------------
