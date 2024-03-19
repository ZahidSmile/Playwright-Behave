# Playwright Behave Framework

Welcome to the Playwright Behave framework! This framework combines the power of Playwright for browser automation with Behave for behavior-driven development (BDD) testing. With Playwright Behave, you can write test scenarios in a human-readable format using Gherkin syntax and automate browser interactions using Playwright.

## Features

- **Behavior-Driven Development (BDD)**: Write test scenarios in a human-readable format using Gherkin syntax, allowing collaboration between technical and non-technical stakeholders.
- **Powerful Browser Automation**: Utilize the capabilities of Playwright to automate browser interactions across different browsers (Chromium, WebKit, and Firefox).
- **Flexible Fixture Support**: Define fixtures for setting up and tearing down browser environments, making it easy to organize and manage test setup and cleanup tasks.
- **Integration with Behave**: Seamlessly integrate Playwright with Behave to leverage the rich ecosystem of Behave for test execution, reporting, and management.

## Getting Started

To get started with the Playwright Behave framework, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```
    git clone https://github.com/ZahidSmile/Playwright-Behave.git
    ```

2. **Install Dependencies**: Install the required Python dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. **Write Test Scenarios**: Write your test scenarios using Gherkin syntax in feature files located in the `features` directory.

4. **Define Step Definitions**: Implement step definitions for your test scenarios in Python files located in the `features/steps` directory. Use Playwright to automate browser interactions within your step definitions.

5. **Execute Tests**: Run your tests using Behave:

    ```
    behave
    ```

6. **View Test Results**: View the test results and generated reports in the `reports` directory.

## Project Structure

The project structure for the Playwright Behave framework is organized as follows:

```
playwright-behave-framework/
│
├── features/           # Directory containing feature files and step definitions
│   ├── steps/          # Step definitions written in Python
│   └── *.feature       # Feature files written in Gherkin syntax
│
├── reports/            # Directory containing test reports (e.g., Allure reports)
│
├── requirements.txt    # List of Python dependencies
└── README.md           # Project README file
```

## Contributing

Contributions to the Playwright Behave framework are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
