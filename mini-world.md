# Mini-world description

John is a developer team leader that guides his teammates on the development of several projects 
that happens in parallel. The team is composed by different roles, such as lead, developer and manager. 
He tracks the team history in terms of (1) when a member joined, (2) when a member leaved and (3) 
when a member got a promotion.

There is no directly responsibility of a Software for a teammate. The teammates participate in all 
of them, although one more than others. It's based on the tasks log-work from the task management 
system that John follows whom is involved in which project.

###### The Software is composed by its function requirements' tasks. After a function requirement be 

described, the team uses the information to create all tasks needed in order to complete the implementation. 
A group of function requirements compose a software version that will be released for the users.

John knows how long time will take a given function requirement after summing the estimation time 
for all its tasks. Forward, he knows how long time will take to release a new version, which is 
nothing more than a group of function requirements. However, it's not uncommon of tasks being 
raised during development, which is tracked to identify failures on the estimation process.

John prepares reports periodically to share the team progress and a updated road-map for the stakeholders.
One of these reports is made weekly for the team itself, where John dumps the tasks data for each 
Software and presents all charts that give the overall vision about the work performed. 
The other report is made monthly for the directors, where it's presented the project development 
progress based on version road-map of each software, where is possible to see what was released to 
the end-user and what will come next.

# Entities relationships

1. Team is composed by one or more Teammate
2. Team is composed by one Teammate (Leader)
3. Teammate plays one Role
4. Teammate (Leader) leads one or more Teammate
5. Teammate develops one or more Software
6. Teammate (Leader) tracks Team History
7. Teammate (Leader) tracks Software
8. Teammate executes one or more Task
9. Teammate logs one or more log-work
10. Task may have one or more log-work
11. Software may have zero or more Function Requirement
12. Software may have zero or more Task
13. Function Requirement may have one or more Task
14. Team create zero or more Task
15. Software has one or more Software Version
16. Software Version is composed by one or more Function Requirement
17. Task has estimation-time
18. Task has log-work
19. Function Requirement has full-estimation-time
20. Function Requirement has full-log-work
21. Software Version has full-estimation-time
22. Software Version has full-log-work
23. Software has full-estimation-time
24. Software has full-log-work
25. Report has a level
26. Report has interval-period of dates
27. Report has finished Functional Requirement
28. Report has next Functional Requirement

# Entities relationships after implementation

1. Team is composed by zero or one Teammate (Manager)
2. Team is composed by zero or  more Teammate (Leader)
3. Team is composed by zero or more  SubTeam
4. SubTeam is composed by zero or more Teammate