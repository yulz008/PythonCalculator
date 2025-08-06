PythonCalculator

A simple calculator implemented on python that demonstrate Continuous Integration via Github Workflow Action see .github/workflows.
Each PR will trigger an action to build and tests the PR. This uses the Github's hosted machine to run the builds. See **Actions** Tab to view the build and tests results.

### Usage

```bash
python app.py <operation> <num1> <num2>
```
Operations: add, subtract, multiply, divide


### For Future Improvements:
- Documentation
- Include Linter for the unit tests
- other runners GitHubAction, SelfHosted, Jenkins  
- Docker
- Other test
