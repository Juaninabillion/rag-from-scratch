## Appendix E - Launch Coordination Checklist

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

# Launch Coordination Checklist

This is Google’s original Launch Coordination Checklist, circa 2005, slightly abridged for brevity:

**Architecture**

* Architecture sketch, types of servers, types of requests from clients
* Programmatic client requests

**Machines and datacenters**

* Machines and bandwidth, datacenters, N+2 redundancy, network QoS
* New domain names, DNS load balancing

**Volume estimates, capacity, and performance**

* HTTP traffic and bandwidth estimates, launch “spike,” traffic mix, 6 months out
* Load test, end-to-end test, capacity per datacenter at max latency
* Impact on other services we care most about
* Storage capacity

**System reliability and failover**

* **What happens when:**
  + Machine dies, rack fails, or cluster goes offline
  + Network fails between two datacenters

* **For each type of server that talks to other servers (its backends):**
  + How to detect when backends die, and what to do when they die
  + How to terminate or restart without affecting clients or users
  + Load balancing, rate-limiting, timeout, retry and error handling behavior
* Data backup/restore, disaster recovery

**Monitoring and server management**

* Monitoring internal state, monitoring end-to-end behavior, managing alerts
* Monitoring the monitoring
* Financially important alerts and logs
* Tips for running servers within cluster environment
* Don’t crash mail servers by sending yourself email alerts in your own server code

**Security**

* Security design review, security code audit, spam risk, authentication, SSL
* Prelaunch visibility/access control, various types of blacklists

**Automation and manual tasks**

* Methods and change control to update servers, data, and configs
* Release process, repeatable builds, canaries under live traffic, staged rollouts

**Growth issues**

* Spare capacity, 10x growth, growth alerts
* Scalability bottlenecks, linear scaling, scaling with hardware, changes needed
* Caching, data sharding/resharding

**External dependencies**

* Third-party systems, monitoring, networking, traffic volume, launch spikes
* Graceful degradation, how to avoid accidentally overrunning third-party services
* Playing nice with syndicated partners, mail systems, services within Google

**Schedule and rollout planning**

* Hard deadlines, external events, Mondays or Fridays
* Standard operating procedures for this service, for other services

[Previous

Appendix D - Example Postmortem](/sre-book/example-postmortem/)

[Next

Appendix F - Example Production Meeting Minutes](/sre-book/production-meeting/)

Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)