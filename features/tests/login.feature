Feature: Login tests

    Scenario: Verify login
      When Click Allow notification button
      When Click Get Started button
      When Put the phone number
      When Click Next button
      When Put the code
      When Click Next button
      Then Verify success login

 