## Part IV - Management

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

# Part IV. Management

Our final selection of topics covers working together in a team, and working as teams. No SRE is an island, and there are some distinctive ways in which we work.

Any organization that aspires to be serious about running an effective SRE arm needs to consider training. Teaching SREs how to think in a complicated and fast-changing environment with a well-thought-out and [well-executed training program](https://sre.google/resources/practices-and-processes/training-site-reliability-engineers/) has the promise of instilling best practices within a new hire’s first few weeks or months that otherwise would take months or years to accumulate. We discuss strategies for doing just that in [Accelerating SREs to On-Call and Beyond](/sre-book/accelerating-sre-on-call/).

As anyone in the operations world knows, responsibility for any significant service comes with a lot of interruptions: production getting in a bad state, people requesting updates to their favorite binary, a long queue of consultation requests…managing interrupts under turbulent conditions is a necessary skill, as we’ll discuss in [Dealing with Interrupts](/sre-book/dealing-with-interrupts/).

If the turbulent conditions have persisted for long enough, an SRE team needs to start recovering from operational overload. We have just the flight plan for you in [Embedding an SRE to Recover from Operational Overload](/sre-book/operational-overload/).

We write in [Communication and Collaboration in SRE](/sre-book/communication-and-collaboration/), about the different roles within SRE; cross-team, cross-site, and cross-continent communication; running production meetings; and case studies of how SRE has collaborated well.

Finally, [The Evolving SRE Engagement Model](/sre-book/evolving-sre-engagement-model/), examines a cornerstone of the operation of SRE: the production readiness review (PRR), a crucial step in onboarding a new service. We discuss how to conduct PRRs, and how to move beyond this successful, but also limited, model.

Further Reading from Google SRE

Building reliable systems requires a carefully calibrated mix of skills, ranging from software development to the arguably less-well-known systems analysis and engineering disciplines. We write about the latter disciplines in "The Systems Engineering Side of Site Reliability Engineering" [[Hix15b]](/sre-book/bibliography#Hix15b).

Hiring SREs well is critical to having a high-functioning reliability organization, as explored in "Hiring Site Reliability Engineers" [[Jon15]](/sre-book/bibliography#Jon15). Google’s hiring practices have been detailed in texts like *Work Rules!* [[Boc15]](/sre-book/bibliography#Boc15),[134](#id-OdauGhduDFn) but hiring SREs has its own set of particularities. Even by Google’s overall standards, SRE candidates are difficult to find and even harder to interview effectively.

[134](#id-OdauGhduDFn-marker)Written by Laszlo Bock, Google’s Senior VP of People Operations.

[Previous

Chapter 27 - Reliable Product Launches at Scale](/sre-book/reliable-product-launches/)

[Next

Chapter 28 - Accelerating SREs to On-Call and Beyond](/sre-book/accelerating-sre-on-call/)

Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)