Feature: User login With positive & negative test cases

  Scenario: Performing Logout if User is Already Logged In
  When User is Already Logged In Performed Logout

  Scenario Outline: Login with different credentials
    Given the user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user should be logged in successfully

    Examples:
    | username | password |
    | user1    | pass123  |
    | Admin    | admin123  |
    | Admin2    | admin1234  |