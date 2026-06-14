## Appendix F - Example Production Meeting Minutes

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

# Example Production Meeting Minutes

**Date**: 2015-10-23

**Attendees**: agoogler, clarac, docbrown, jennifer, martym

**Announcements**:

* Major outage (#465), blew through error budget

**Previous Action Item Review**

* Certify Goat Teleporter for use with cattle (bug 1011101)
  + Nonlinearities in mass acceleration now predictable, should be able to target accurately in a few days.

**Outage Review**

* New Sonnet (outage 465)
  + 1.21B queries lost due to cascading failure after interaction between latent bug (leaked file descriptor on searches with no results) + not having new sonnet in corpus + unprecedented & unexpected traffic volume
  + File descriptor leak bug fixed (bug 5554825) and deployed to prod
  + Looking into using flux capacitor for load balancing (bug 5554823) and using load shedding (bug 5554826) to prevent recurrence
  + Annihilated availability error budget; pushes to prod frozen for 1 month unless docbrown can obtain exception on grounds that event was bizarre & unforeseeable (but consensus is that exception is unlikely)

**Paging Events**

* `AnnotationConsistencyTooEventual`: paged 5 times this week, likely due to cross-regional replication delay between Bigtables.
  + Investigation still ongoing, see bug 4821600
  + No fix expected soon, will raise acceptable consistency threshold to reduce unactionable alerts

**Nonpaging Events**

* None

**Monitoring Changes and/or Silences**

* `AnnotationConsistencyTooEventual`, acceptable delay threshold raised from 60s to 180s, see bug 4821600; TODO(martym).

**Planned Production Changes**

* USA-1 cluster going offline for maintenance between 2015-10-29 and 2015-11-02.
  + No response required, traffic will automatically route to other clusters in region.

**Resources**

* Borrowed resources to respond to sonnet++ incident, will spin down additional server instances and return resources next week
* Utilization at 60% of CPU, 75% RAM, 44% disk (up from 40%, 70%, 40% last week)

**Key Service Metrics**

* **OK** 99ile latency: 88 ms < 100 ms SLO target [trailing 30 days]
* **BAD** availability: 86.95% < 99.99% SLO target [trailing 30 days]

**Discussion / Project Updates**

* Project Molière launching in two weeks.

**New Action Items**

* TODO(martym): Raise `AnnotationConsistencyTooEventual` threshold.
* TODO(docbrown): Return instance count to normal and return resources.

[Previous

Appendix E - Launch Coordination Checklist](/sre-book/launch-checklist/)

[Next

Bibliography](/sre-book/bibliography/)

Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)