Scenario Outline: Add new group
 Given a group list
 Given a group with <name>, <logo> and <comment>
 When I add the group to the list
 Then the new list is equal to the old list with the add group

Examples:
|name  | logo  | comment  |
|name1 | logo1 | comment1 |
|name2 | logo2 | comment2 |