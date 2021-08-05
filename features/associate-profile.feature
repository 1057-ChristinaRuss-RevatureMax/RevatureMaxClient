Feature: Associate profile page functionality

 Background:
  Given the user is signed in as an associate

 Scenario: An associate would like to view their profile
  Given the user is on the associate profile page
  Then the associate can view their profile information

 Scenario: An associate would like to edit their name and email address
  Given the user is on the associate profile page
  When the user clicks the edit contact info button
  And the user inputs new contact info
  And the user clicks the submit contact info button
  Then the contact info is updated

 Scenario: An associate would like to edit their bio
  Given the user is on the associate profile page
  When the user clicks the edit bio button
  And the user inputs a new bio
  And the user clicks the submit bio button
  Then the bio is updated

 Scenario: An associate would like to edit their favorite technologies
  Given the user is on the associate profile page
  When the user clicks the edit fav technologies button
  And the user inputs new favorite technologies
  And the user selects a new preference
  And the user clicks the submit fav technologies button
  Then the favorite technologies are updated