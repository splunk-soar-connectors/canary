# Canary for SOAR

Publisher: Splunk Community \
Connector Version: 2.1.0 \
Product Vendor: ThinkST \
Product Name: Canary \
Minimum Product Version: 5.5.0

This app supports ingestion and investigative actions on the ThinkST Canary API Service

### Configuration variables

This table lists the configuration variables required to operate Canary for SOAR. These variables are specified when configuring a Canary asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**domain** | required | string | Domain used for Canary Website. For example (https://\*domain\*.canary.tools) |
**api_key** | required | password | API Key from Canary Website |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[on poll](#action-on-poll) - Ingest unacknowledged incidents from Canary \
[update incident](#action-update-incident) - Acknowledge existing Canary incident \
[add ip ignorelist](#action-add-ip-ignorelist) - Add new IP to Canary global Ignore List \
[remove ip ignorelist](#action-remove-ip-ignorelist) - Remove IP from Canary global IgnoreList \
[test ip ignorelist](#action-test-ip-ignorelist) - Test if IP has been globally ignored \
[list incidents](#action-list-incidents) - Get the list of existing Canary Incidents

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'on poll'

Ingest unacknowledged incidents from Canary

Type: **ingest** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'update incident'

Acknowledge existing Canary incident

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident** | required | The incident key of an existing incident | string | |
**incident_state** | required | State to make incident | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.incident | string | | |
action_result.parameter.incident_state | string | | |
action_result.data | string | | |
action_result.summary | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'add ip ignorelist'

Add new IP to Canary global Ignore List

Type: **contain** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip_address** | required | IP Address to add to global Ignore List | string | `ip` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.data.\* | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |
action_result.summary | string | | |
action_result.parameter.ip_address | string | `ip` | |

## action: 'remove ip ignorelist'

Remove IP from Canary global IgnoreList

Type: **contain** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip_address** | required | IP Address to remove from global Ignore List | string | `ip` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.data.\* | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |
action_result.summary | string | | |
action_result.parameter.ip_address | string | `ip` | |

## action: 'test ip ignorelist'

Test if IP has been globally ignored

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip_address** | required | IP Address to test on global Ignore List | string | `ip` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.data.\* | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |
action_result.summary | string | | |
action_result.parameter.ip_address | string | `ip` | |

## action: 'list incidents'

Get the list of existing Canary Incidents

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident_state** | required | State of incidents to list | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.incident_state | string | | acknowledged |
action_result.data.\*.devices.\*.description.acknowledged | string | | True |
action_result.data.\*.devices.\*.description.created | string | | 1540514762 |
action_result.data.\*.devices.\*.description.created_std | string | | 2018-10-26 00:46:02 UTC+0000 |
action_result.data.\*.devices.\*.description.description | string | | HTTP Login Attempt |
action_result.data.\*.devices.\*.description.dst_host | string | `ip` | 122.122.122.122 |
action_result.data.\*.devices.\*.description.dst_port | string | | 80 |
action_result.data.\*.devices.\*.description.events.\*.HOSTNAME | string | `ip` `host name` | 122.122.122.122 |
action_result.data.\*.devices.\*.description.events.\*.PASSWORD | string | | root |
action_result.data.\*.devices.\*.description.events.\*.PATH | string | | /folder |
action_result.data.\*.devices.\*.description.events.\*.SETTINGS | string | | |
action_result.data.\*.devices.\*.description.events.\*.SKIN | string | | vmware |
action_result.data.\*.devices.\*.description.events.\*.USERAGENT | string | | Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0 |
action_result.data.\*.devices.\*.description.events.\*.USERNAME | string | `user name` | root |
action_result.data.\*.devices.\*.description.events.\*.timestamp | numeric | | 1540514762 |
action_result.data.\*.devices.\*.description.events.\*.timestamp_std | string | | 2018-10-26 00:46:02 UTC+0000 |
action_result.data.\*.devices.\*.description.events_count | string | | 1 |
action_result.data.\*.devices.\*.description.ip_address | string | | |
action_result.data.\*.devices.\*.description.ippers | string | | |
action_result.data.\*.devices.\*.description.local_time | string | | 2018-10-26 00:46:01 |
action_result.data.\*.devices.\*.description.logtype | string | | 3001 |
action_result.data.\*.devices.\*.description.mac_address | string | | |
action_result.data.\*.devices.\*.description.name | string | | ATHQESXP01 |
action_result.data.\*.devices.\*.description.node_id | string | | 000000002f391f1d |
action_result.data.\*.devices.\*.description.notified | string | | False |
action_result.data.\*.devices.\*.description.src_host | string | `ip` | 122.122.122.122 |
action_result.data.\*.devices.\*.description.src_host_reverse | string | | |
action_result.data.\*.devices.\*.description.src_port | string | | 60222 |
action_result.data.\*.devices.\*.id | string | | incident:httplogin:b4a7013dfe899ce773353c5c:122.122.122.122:1540514762 |
action_result.data.\*.devices.\*.summary | string | | HTTP Login Attempt |
action_result.data.\*.devices.\*.updated | string | | Fri, 26 Oct 2018 00:46:48 GMT |
action_result.data.\*.devices.\*.updated_id | numeric | | 71 |
action_result.data.\*.devices.\*.updated_std | string | | 2018-10-26 00:46:48 UTC+0000 |
action_result.data.\*.feed | string | | Acknowledged Incidents |
action_result.data.\*.incidents.\*.description.acknowledged | string | | True |
action_result.data.\*.incidents.\*.description.created | string | | 1540514762 |
action_result.data.\*.incidents.\*.description.created_std | string | | 2018-10-26 00:46:02 UTC+0000 |
action_result.data.\*.incidents.\*.description.description | string | | HTTP Login Attempt |
action_result.data.\*.incidents.\*.description.dst_host | string | `ip` | 122.122.122.122 |
action_result.data.\*.incidents.\*.description.dst_port | string | | 80 |
action_result.data.\*.incidents.\*.description.events.\*.HOSTNAME | string | `ip` `host name` | 122.122.122.122 |
action_result.data.\*.incidents.\*.description.events.\*.PASSWORD | string | | root |
action_result.data.\*.incidents.\*.description.events.\*.PATH | string | | /folder |
action_result.data.\*.incidents.\*.description.events.\*.SETTINGS | string | | userid=tsv.dsnd@at.govt.nz,username=,totp_enable=False,sensitive_data_masking_enable=True,auth_token_enable=False,incident_webhooks_enable=False,slack_incident_webhook=,hipchat_integration_url=,generic_incident_webhook=,email_notification_enable=True,email_notification_addresses=tsb.dnsdk@at.govt.nz,tvsb.bsysj@at.govt.nz,sms_notification_enable=False,summary_email_enable=True,summary_email_addresses=ndsjdn.dsnsn@at.govt.nz, bajhjdnj@at.govt.nz,notify_settings_change_enable=True,notify_device_settings_change_enable=True,whitelist_enable=False,whitelist_ips=,whitelist_oids_enable=False,whitelist_oids=,ssh_credential_watches_enable=False,ssh_credential_watches=,ssh_credential_watch_only=False,sms_notification_numbers=,update_automatically_enable=True,canarytokens_alerts_enable=True,canarytokens_user_domains_enable=False,canarytokens_user_domains=,canarytokens_webroot_enable=False,canarytokens_webroot=<html><body><h1>It works!</h1>

<p>This is the default web page for this server.</p>
 <p>The web server software is running but no content has been added, yet.</p>
 </body></html>,smtp_host=,smtp_port=,smtp_from_address=,smtp_username=,smtp_password=,smtp_starttls=,syslog_fwd_enable=False,syslog_fwd_remote_host=,syslog_fwd_remote_port=,syslog_fwd_protocol=tcp,syslog_fwd_fmt=custom,syslog_fwd_facility=local0,syslog_fwd_priority=emerg  |
action_result.data.\*.incidents.\*.description.events.\*.SKIN | string |  |   vmware  |
action_result.data.\*.incidents.\*.description.events.\*.USERAGENT | string |  |   Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0  |
action_result.data.\*.incidents.\*.description.events.\*.USERNAME | string |  `user name`  |   root  |
action_result.data.\*.incidents.\*.description.events.\*.timestamp | numeric |  |   1540514762  |
action_result.data.\*.incidents.\*.description.events.\*.timestamp_std | string |  |   2018-10-26 00:46:02 UTC+0000  |
action_result.data.\*.incidents.\*.description.events_count | string |  |   1  |
action_result.data.\*.incidents.\*.description.ip_address | string |  |   |
action_result.data.\*.incidents.\*.description.ippers | string |  |   |
action_result.data.\*.incidents.\*.description.local_time | string |  |   2018-10-26 00:46:01  |
action_result.data.\*.incidents.\*.description.logtype | string |  |   3001  |
action_result.data.\*.incidents.\*.description.mac_address | string |  |   |
action_result.data.\*.incidents.\*.description.name | string |  |   ATHQESXP01  |
action_result.data.\*.incidents.\*.description.node_id | string |  |   000000002f391f1d  |
action_result.data.\*.incidents.\*.description.notified | string |  |   False  |
action_result.data.\*.incidents.\*.description.src_host | string |  `ip`  |   122.122.122.122  |
action_result.data.\*.incidents.\*.description.src_host_reverse | string |  |   |
action_result.data.\*.incidents.\*.description.src_port | string |  |   60222  |
action_result.data.\*.incidents.\*.id | string |  |   incident:httplogin:b4a7013dfe899ce773353c5c:122.122.122.122:1540514762  |
action_result.data.\*.incidents.\*.summary | string |  |   HTTP Login Attempt  |
action_result.data.\*.incidents.\*.updated | string |  |   Fri, 26 Oct 2018 00:46:48 GMT  |
action_result.data.\*.incidents.\*.updated_id | numeric |  |   71  |
action_result.data.\*.incidents.\*.updated_std | string |  |   2018-10-26 00:46:48 UTC+0000  |
action_result.data.\*.max_updated_id | numeric |  |   79  |
action_result.data.\*.result | string |  |   success  |
action_result.data.\*.updated | string |  |   Sun, 28 Oct 2018 22:33:20 GMT  |
action_result.data.\*.updated_std | string |  |   2018-10-28 22:33:20 UTC+0000  |
action_result.data.\*.updated_timestamp | numeric |  |   1540766000  |
action_result.summary.count | numeric |  |   5  |
action_result.message | string |  |   Count: 5  |
summary.total_objects | numeric |  |   1  |
summary.total_objects_successful | numeric |  |   1  |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
