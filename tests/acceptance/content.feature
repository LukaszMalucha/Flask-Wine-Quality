Feature: Test that page have correct content


  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "A.I. Sommelier"

  Scenario: Homepage has a quality chart
    Given I am on the homepage
    Given I wait for the quality chart to load
    Then I can see there is a quality chart on the page

  Scenario: Signup page loads the form
   Given I am on the signup page
   Then I can see there is a signup form on the page

  Scenario: Login page loads the form
   Given I am on the login page
   Then I can see there is a login form on the page

  Scenario: Manage DB page has the add template form
    Given I am on the manage db page
    Then I can see there is the add template form displayed on the page


  Scenario: Classifier Build page has six charts
    Given I am on the classifier build page
    Then I can see there are six charts displayed on the page

  Scenario: Sommeliers page loads the rate form
    Given I am on the sommeliers page
    Then I can see there is the rate form displayed on the page







