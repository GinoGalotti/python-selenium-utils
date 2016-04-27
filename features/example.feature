Feature: Basic Scenarios

  Scenario: post 2nd of april account redirects to dash after login
    Given I am the user called "ui-functional"
    When I login via web
    Then I should be redirected to somewhere

  Scenario: new account redirects to dash after signup
    Given I am a new user
    When I signup via web
    Then I should be redirected to somewhere
    Then I delete the user