Feature: To verify the google search
  Scenario: verifying search
    Given I am on search page
    When I searched "Playwright"
    Then Search should be displayed