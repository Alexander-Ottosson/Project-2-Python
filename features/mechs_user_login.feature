Feature: The User Login Feature Works
  Scenario Outline: A Valid User logs in
    Given The User is on the Mechs Home Page
    When The User clicks on Login
    Then The User can view Login Page
    When The User types <word1> in the Username Field
    When The User types <word2> in the Password Field
    When The User clicks the Login Button
    Then The Page Title should be Login

    Examples:
    | word1  | word2    |
    | scari  | password |