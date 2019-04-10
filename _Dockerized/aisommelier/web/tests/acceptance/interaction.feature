Feature: Test that forms work correctly


  Scenario: Signup page registers user
    Given I am on the signup page
    When I enter "tester4" in the "username" field
    And I enter "tester4@gmail.com" in the "email" field
    And I enter "12341234" in the "password" field
    And I press the submit button


  Scenario: Login page logins user
    Given I am on the login page
    When I enter "tester1" in the "username" login field
    And I enter "12341234" in the "password" login field
    And I press the submit button
    Then I am on the library page

  Scenario: Rate Wine form applies default value to blank fields
    Given I am on the sommeliers page
    When I click on the "RATE IT" link
    When I scroll to the bottom of the page
    Given I wait for the sommeliers page to load
    Then There three sommelier scores are displayed


  Scenario: Homepage allows code download
    Given I am on the homepage
    When I press the download button
    Given I wait for the download code template to finish
    Then I downloaded the code template
