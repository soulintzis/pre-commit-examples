# Pre-Commit Hooks - Examples

## The Benefits of Pre-Commit Actions
Pre-commit actions help to enforce consistent coding standards and catch potential issues before they are committed to the codebase. This can improve code quality, reduce bugs and security vulnerabilities, and streamline the development process by catching problems early in the development cycle. Additionally, pre-commit actions can automate repetitive tasks, such as running linting tools, formatting code, or checking for compliance with company policies, freeing up developers to focus on more important tasks.

## How Pre-Commit Actions Work
Pre-commit actions run before code is committed to a repository. 
Once the code is written, the pre-commit actions run to check for any errors or bugs. If any are found, the code can be corrected before it is committed. This helps ensure that the code is up to standards and meets any specific requirements that the company may have.

## PEP 8 (Python Enhancement Proposal)
PEP 8 is a style guide that describes the coding standards for Python. It's the most popular guide within the Python community. 
The most important rules state the following:


#### PEP 8 naming conventions:
- class names should be CamelCase (MyClass)
- variable names should be snake_case and all lowercase (first_name)
- function names should be snake_case and all lowercase (quick_sort())
- constants should be snake_case and all uppercase (PI = 3.14159)
- modules should have short, snake_case names and all lowercase (numpy)
- single quotes and double quotes are treated the same (just pick one and be consistent)

#### PEP 8 line formatting:
- indent using 4 spaces (spaces are preferred over tabs)
- lines should not be longer than 79 characters (we prefer 120 characters)
- avoid multiple statements on the same line
- imports should usually be on separate lines
- top-level function and class definitions are surrounded with two blank lines
- method definitions inside a class are surrounded by a single blank line

#### PEP 8 whitespace:
- avoid trailing whitespace anywhere
- always surround binary operators with a single space on either side
- if operators with different priorities are used, consider adding whitespace around the operators with the lowest priority
- don't use spaces around the = sign when used to indicate a keyword argument

