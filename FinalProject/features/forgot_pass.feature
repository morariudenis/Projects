Feature: Jules forgot password tests

    # se ruleaza inainte de orice test(in general givenuri)
    Background:
      Given sign_in: I am a user on jules sing in page

    @jules
    Scenario: Wrong email validation message
      When sing_in: I click forgot password link
      When forgot_pass: I set my email "abcd"
      Then forgot_pass: I verify that email validation message is correct

    @jules
    Scenario Outline: Wrong email validation message with table data
      When sing_in: I click forgot password link
      When forgot_pass: I set my email "abcd"
      Then forgot_pass: I verify that email validation message is correct

      Examples:

        | email        |
        | sdcas@il.com |
        | asda@ail.com |







