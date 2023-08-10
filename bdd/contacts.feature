Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <middlename>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact
  Examples:
  | firstname  | lastname  | middlename  |
  | fn1        | ln1       | mn1         |
  | fn2        | ln2       | mn2         |


Scenario: Delete a contact
  Given non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario: Modify some contact
  Given non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list to <firstname>, <lastname> and <middlename>
  Then the new contact list is equal to the old list and contact is modified

  Examples:
  | firstname  | lastname  | middlename  |
  | fn1        | ln1       | mn1         |
  | fn2        | ln2       | mn2         |
