Feature: User login
  As a registered user
  I want to be able to login to the system

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard

