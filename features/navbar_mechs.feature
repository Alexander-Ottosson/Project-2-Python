Feature: Mechs Home Page Nav Supports Mechs Link

  Scenario: Home Page Navbar For Index Works
    Given The User is on the Mechs Home Page
    When The User clicks on Mechs
    Then The User can view Mechs Page

  Scenario: Home Page To Login Page Works
    Given The User is on the Mechs Home Page
    When The User clicks on Login
    Then The User can view Login Page