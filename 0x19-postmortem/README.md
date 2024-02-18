# Post-Mortem: Nginx Service Unavailability on Port 80

**Incident Date**: January 12, 2024  
**Authors**: Kingsley Usa  
**Status**: Resolved

## Summary

On January 12, 2024, at 6:25 AM, an outage occurred where Nginx failed to bind to port 80, the default HTTP port, on our production server. This resulted in the complete unavailability of our web services to end users. The service was restored at 1:34 PM, with a total downtime of seven hours.

## Impact

Approximately 2,100 users were affected, and the outage resulted in an inability to access our web application. No data loss was reported, and the security of our system remained intact throughout the incident.

## Root Causes

An investigation revealed that the Nginx service was not properly started due to a port conflict on port 80. Another service, Apache, was unintentionally configured to also listen on port 80, which prevented Nginx from binding to this port.

## Trigger

The conflicting service was automatically updated and restarted as part of our routine system updates, which went into effect without a preceding check for port availability.

## Action Items

* [ ] Implement a check for port availability before system updates.
* [ ] Review and update service configurations to prevent future port conflicts.
* [ ] Enhance system monitoring to detect and alert on port conflicts.

## Resolution and Recovery

The issue was resolved by halting the conflicting service and releasing port 80. Nginx was then restarted, which successfully bound to port 80, and restored web service availability.

## Detection

Our monitoring system detected the issue, which reported critical alerts when the web service became unavailable. The alerts were promptly relayed to the on-call engineering team.

## Lessons Learned

- Always ensure port exclusivity for critical services during configuration changes.
- Pre-deployment and post-deployment checks should include validation of service start-up and port binding.
- Monitoring systems are vital and should include checks for common failures like port conflicts.

## Timeline

- **6:24 AM** - Monitoring system reported downtime.
- **8:34 AM** - On-call engineer began investigating the issue.
- **9:11 AM** - Port conflict identified as the root cause.
- **12:57 PM** - Conflicting service stopped, freeing port 80.
- **1:34 PM** - Nginx restarted and service availability confirmed.
