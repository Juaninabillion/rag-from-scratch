## Appendix C - Example Incident State Document

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

# Example Incident State Document

**Shakespeare Sonnet++ Overload: 2015-10-21**  
Incident management info: *https://incident-management-cheat-sheet*

*(Communications lead to keep summary updated.)*  
**Summary**: Shakespeare search service in cascading failure due to newly discovered sonnet not in search index.

**Status**: active, incident #465

**Command Post(s)**: `#shakespeare` on IRC

**Command Hierarchy** *(all responders)*

* Current Incident Commander: jennifer

  + Operations lead: docbrown
  + Planning lead: jennifer
  + Communications lead: jennifer
* Next Incident Commander: *to be determined*

*(Update at least every four hours and at handoff of Comms Lead role.)*  
**Detailed Status** (last updated at 2015-10-21 15:28 UTC by jennifer)

**Exit Criteria:**

* New sonnet added to Shakespeare search corpus **TODO**
* Within availability (99.99%) and latency (99%ile < 100 ms) SLOs for 30+ minutes **TODO**

**TODO list and bugs filed:**

* Run MapReduce job to reindex Shakespeare corpus **DONE**
* Borrow emergency resources to bring up extra capacity **DONE**
* Enable flux capacitor to balance load between clusters (Bug 5554823) **TODO**

**Incident timeline** *(most recent first: times are in UTC)*

* 2015-10-21 15:28 UTC jennifer

  + Increasing serving capacity globally by 2x
* 2015-10-21 15:21 UTC jennifer

  + Directing all traffic to USA-2 sacrificial cluster and draining traffic from other clusters so they can recover from cascading failure while spinning up more tasks
  + MapReduce index job complete, awaiting Bigtable replication to all clusters
* 2015-10-21 15:10 UTC martym

  + Adding new sonnet to Shakespeare corpus and starting index MapReduce
* 2015-10-21 15:04 UTC martym

  + Obtains text of newly discovered sonnet from *shakespeare-discuss@* mailing list
* 2015-10-21 15:01 UTC docbrown

  + Incident declared due to cascading failure
* 2015-10-21 14:55 UTC docbrown

  + Pager storm, `ManyHttp500s` in all clusters

[Previous

Appendix B - A Collection of Best Practices for Production Services](/sre-book/service-best-practices/)

[Next

Appendix D - Example Postmortem](/sre-book/example-postmortem/)

Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)