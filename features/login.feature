Feature: Login form

  Scenario: For login page

  Given login page

  Scenario: For Login success page

	Given an anonymous user
	When I submit a valid login page
	Then I am redirected to the login success page

  Scenario: For login failure page

	Given an anonymous user
	When I submit an invalid login page
	Then I am redirected to the login fail page
