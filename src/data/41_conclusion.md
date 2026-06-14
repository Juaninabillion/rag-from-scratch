## Chapter 34 - Conclusion

1. [Table of Contents](/sre-book/table-of-contents/)
2. [Foreword](/sre-book/foreword/)
3. [Preface](/sre-book/preface/)
4. [Part I - Introduction](/sre-book/part-I-introduction/)
5. [1. Introduction](/sre-book/introduction/)
6. [2. The Production Environment at Google, from the Viewpoint of an SRE](/sre-book/production-environment/)
7. [Part II - Principles](/sre-book/part-II-principles/)
8. [3. Embracing Risk](/sre-book/embracing-risk/)
9. [4. Service Level Objectives](/sre-book/service-level-objectives/)
10. [5. Eliminating Toil](/sre-book/eliminating-toil/)
11. [6. Monitoring Distributed Systems](/sre-book/monitoring-distributed-systems/)
12. [7. The Evolution of Automation at Google](/sre-book/automation-at-google/)
13. [8. Release Engineering](/sre-book/release-engineering/)
14. [9. Simplicity](/sre-book/simplicity/)
15. [Part III - Practices](/sre-book/part-III-practices/)
16. [10. Practical Alerting](/sre-book/practical-alerting/)
17. [11. Being On-Call](/sre-book/being-on-call/)
18. [12. Effective Troubleshooting](/sre-book/effective-troubleshooting/)
19. [13. Emergency Response](/sre-book/emergency-response/)
20. [14. Managing Incidents](/sre-book/managing-incidents/)
21. [15. Postmortem Culture: Learning from Failure](/sre-book/postmortem-culture/)
22. [16. Tracking Outages](/sre-book/tracking-outages/)
23. [17. Testing for Reliability](/sre-book/testing-reliability/)
24. [18. Software Engineering in SRE](/sre-book/software-engineering-in-sre/)
25. [19. Load Balancing at the Frontend](/sre-book/load-balancing-frontend/)
26. [20. Load Balancing in the Datacenter](/sre-book/load-balancing-datacenter/)
27. [21. Handling Overload](/sre-book/handling-overload/)
28. [22. Addressing Cascading Failures](/sre-book/addressing-cascading-failures/)
29. [23. Managing Critical State: Distributed Consensus for Reliability](/sre-book/managing-critical-state/)
30. [24. Distributed Periodic Scheduling with Cron](/sre-book/distributed-periodic-scheduling/)
31. [25. Data Processing Pipelines](/sre-book/data-processing-pipelines/)
32. [26. Data Integrity: What You Read Is What You Wrote](/sre-book/data-integrity/)
33. [27. Reliable Product Launches at Scale](/sre-book/reliable-product-launches/)
34. [Part IV - Management](/sre-book/part-IV-management/)
35. [28. Accelerating SREs to On-Call and Beyond](/sre-book/accelerating-sre-on-call/)
36. [29. Dealing with Interrupts](/sre-book/dealing-with-interrupts/)
37. [30. Embedding an SRE to Recover from Operational Overload](/sre-book/operational-overload/)
38. [31. Communication and Collaboration in SRE](/sre-book/communication-and-collaboration/)
39. [32. The Evolving SRE Engagement Model](/sre-book/evolving-sre-engagement-model/)
40. [Part V - Conclusions](/sre-book/part-V-conclusions/)
41. [33. Lessons Learned from Other Industries](/sre-book/lessons-learned/)
42. [34. Conclusion](/sre-book/conclusion/)
43. [Appendix A. Availability Table](/sre-book/availability-table/)
44. [Appendix B. A Collection of Best Practices for Production Services](/sre-book/service-best-practices/)
45. [Appendix C. Example Incident State Document](/sre-book/incident-document/)
46. [Appendix D. Example Postmortem](/sre-book/example-postmortem/)
47. [Appendix E. Launch Coordination Checklist](/sre-book/launch-checklist/)
48. [Appendix F. Example Production Meeting Minutes](/sre-book/production-meeting/)
49. [Bibliography](/sre-book/bibliography/)

# Conclusion

Written by Benjamin Lutch[162](#id-rq7uXSYFKx)Edited by Betsy Beyer

I read through this book with enormous pride. From the time I began working at Excite in the early ’90s, where my group was a sort of neanderthal SRE group dubbed "Software Operations," I’ve spent my career fumbling through the process of building systems. In light of my experiences over the years in the tech industry, it’s amazing to see how the idea of SRE took root at Google and evolved so quickly. SRE has grown from a few hundred engineers when I joined Google in 2006 to over 1,000 people today, spread over a dozen sites and running what I think is the most interesting computing infrastructure on the planet.

So what has enabled the SRE organization at Google to evolve over the past decade to maintain this massive infrastructure in an intelligent, efficient, and scalable way? I think that the key to the overwhelming success of SRE is the nature of the principles by which it operates.

SRE teams are constructed so that our engineers divide their time between two equally important types of work. SREs staff on-call shifts, which entail putting our hands around the systems, observing where and how these systems break, and understanding challenges such as how to best scale them. But we also have time to then reflect and decide what to build in order to make those systems easier to manage. In essence, we have the pleasure of playing both the roles of the pilot *and* the engineer/designer. Our experiences running massive computing infrastructure are codified in actual code and then packaged as a discrete product.

These solutions are then easily usable by other SRE teams and ultimately by anyone at Google (or even outside of Google…think Google Cloud!) who wants to use or improve upon the experience we’ve accumulated and the systems we’ve built.

When you approach building a team or a system, ideally its foundation should be a set of rules or axioms that are general enough to be immediately useful, but that will remain relevant in the future. Much of what Ben Treynor Sloss outlined in this book’s introduction represents just that: a flexible, mostly future-proof set of responsibilities that remain spot-on 10 years after they were conceived, despite the changes and growth Google’s infrastructure and the SRE team have undergone.

As SRE has grown, we’ve noticed a couple different dynamics at play. The first is the consistent nature of SRE’s primary responsibilities and concerns over time: our systems might be 1,000 times larger or faster, but ultimately, they still need to remain reliable, flexible, easy to manage in an emergency, well monitored, and capacity planned. At the same time, the typical activities undertaken by SRE evolve by necessity as Google’s services and SRE’s competencies mature. For example, what was once a goal to "build a dashboard for 20 machines" might now instead be "automate discovery, dashboard building, and alerting over a fleet of tens of thousands of machines."

For those who haven’t been in the trenches of SRE for the past decade, an analogy between how SRE thinks about complex systems and how the aircraft industry has approached plane flight is useful in conceptualizing how SRE has evolved and matured over time. While the stakes of failure between the two industries are very different,
certain core similarities hold true.

Imagine that you wanted to fly between two cities a hundred years ago. Your airplane probably had a single engine (two, if you were lucky), a few bags of cargo, and a pilot. The pilot also filled the role of mechanic, and possibly additionally acted as cargo loader and unloader. The cockpit had room for the pilot, and if you were lucky, a co-pilot/navigator. Your little plane would bounce off a runway in good weather, and if everything went well, you’d slowly climb your way through the skies and eventually touch down in another city, maybe a few hundred miles away. Failure of any of the plane’s systems was catastrophic, and it wasn’t unheard of for a pilot to have to climb out of the cockpit to perform repairs in-flight! The systems that fed into the cockpit were essential, simple, and fragile, and most likely were not redundant.

Fast-forward a hundred years to a huge 747 sitting on the tarmac. Hundreds of passengers are loading up on both floors, while tons of cargo are simultaneously being loaded into the hold below. The plane is chock-full of reliable, redundant systems. It’s a model of safety and reliability; in fact, you’re actually safer in the air than on the ground in a car. Your plane will take off from a dotted line on a runway on one continent, and land easily on a dotted line on another runway 6,000 miles away, right on schedule—within minutes of its forecasted landing time. But take a look into the cockpit and what do you find? Just two pilots again!

How has every other element of the flight experience—safety, capacity, speed, and reliability—scaled up so beautifully, while there are still only two pilots? The answer to this question is a great parallel to how Google approaches the enormous, fantastically complex systems that SRE runs. The interfaces to the plane’s operating systems are well thought out and approachable enough that learning how to pilot them in normal conditions is not an insurmountable task. Yet these interfaces also provide enough flexibility, and the people operating them are sufficiently trained, that responses to emergencies are robust and quick. The cockpit was designed by people who understand complex systems and how to present them to humans in a way that’s both consumable and scalable. The systems underlying the cockpit have all the same properties discussed in this book: availability, performance optimization, change management, monitoring and alerting, capacity planning, and emergency response.

Ultimately, SRE’s goal is to follow a similar course. An SRE team should be as compact as possible and operate at a high level of abstraction, relying upon lots of backup systems as failsafes and thoughtful APIs to communicate with the systems. At the same time, the SRE team should also have comprehensive knowledge of the systems—how they operate, how they fail, and how to respond to failures—that comes from operating them day-to-day.

[162](#id-rq7uXSYFKx-marker)Vice President, Site Reliability Engineering, for Google, Inc.

[Previous

Chapter 33 - Lessons Learned from Other Industries](/sre-book/lessons-learned/)

[Next

Appendix A - Availability Table](/sre-book/availability-table/)

Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)