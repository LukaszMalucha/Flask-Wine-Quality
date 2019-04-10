Feature: Test navigation between pages


  Scenario: Home can go to Classifier Build
    Given I am on the homepage
    When I click on the "LET'S BUILD CLASSIFIER" link
    Then I am on the classifier build page

  Scenario: Classifier Build can go to Classifier Fit
    Given I am on the classifier build page
    When I click on the "PARAMETERS TUNING" link
    Then I am on the classifier fit page

  Scenario: Classifier Fit can go to Sommeliers
    Given I am on the classifier fit page
    When I click on the "A.I. SOMMELIERS" link
    Then I am on the sommeliers page

  Scenario: Home can go to Login page
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log In" dropdown link
    Then I am on the login page

  Scenario: Home can go to Logout page
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log Out" dropdown link
    Then I am on the login page

  Scenario: Home can go to Signup page
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Sign In" dropdown link
    Then I am on the signup page

  Scenario: Home can go to Sommeliers page
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Rate Wine!" dropdown link
    Then I am on the sommeliers page

  Scenario: Home can go to Manage DB page
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Manage DB" dropdown link
    Then I am on the manage db page

