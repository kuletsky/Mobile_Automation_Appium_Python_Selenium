Feature: Login tests

    Scenario: Verify login
      When Click Allow notification button
      And Click Get Started button
      And Put the phone number
      And Click Next button
      And Put the code
      And Click Next button
      Then Verify success login

 