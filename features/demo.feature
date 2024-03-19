Feature: User login
  As a registered user
  I want to be able to login to the system

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario Outline: Login with different credentials
    Given the user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user should be logged in successfully

    Examples:
    | username | password |
    | user1    | pass123  |
    | Admin    | admin123  |
    | Admin2    | admin1234  |