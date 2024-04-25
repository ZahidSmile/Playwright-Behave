Feature: I want to test the Profile Picture functionality

  Scenario: Uploading profile picture with valid data
    Given I am on profile page
    When I click on profile picture
    Then I should landed on change profile picture page
    When I select the file from system
    And I click on save button
    Then file should be up loaded successfully