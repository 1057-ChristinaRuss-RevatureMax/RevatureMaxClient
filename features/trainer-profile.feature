Feature: Trainer profile page functionality

 Background:
  Given the user is signed in as a trainer

 Scenario: A trainer would like to view their profile
  Given the user is on the trainer profile page
   And the trainers info is reset
  Then the trainer can view their profile information

 Scenario: A trainer would like to edit their name and email address
  Given the user is on the trainer profile page
  When the user clicks the edit contact info button
  And the trainer inputs new contact info
  And the user clicks the submit contact info button
  Then the contact info is updated

 Scenario: A trainer would like to edit their bio
  Given the user is on the trainer profile page
  When the user clicks the edit bio button
  And the user inputs a new bio
  And the user clicks the submit bio button
  Then the bio is updated

 Scenario: A trainer would like to edit their specialization and location
  Given the user is on the trainer profile page
  When the user clicks the edit training info button
  And the user inputs a new specialization
  And the user inputs a new location
  And the user clicks the submit training info button
  Then the specialization and location are updated
