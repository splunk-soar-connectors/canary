[comment]: # "Auto-generated SOAR connector documentation"
# Canary

Publisher: Splunk  
Connector Version: 1\.0\.3  
Product Vendor: ThinkST  
Product Name: Canary  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.5\.15922  

This app supports ingestion and investigative actions on the ThinkST Canary API Service

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Canary asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**domain** |  required  | string | Domain used for Canary Website\. For example \(https\://\*domain\*\.canary\.tools\)
**api\_key** |  required  | password | API Key from Canary Website

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[on poll](#action-on-poll) - Ingest unacknowledged incidents from Canary  
[update incident](#action-update-incident) - Acknowledge existing Canary incident  
[list incidents](#action-list-incidents) - Get the list of existing Canary Incidents  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'on poll'
Ingest unacknowledged incidents from Canary

Type: **ingest**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'update incident'
Acknowledge existing Canary incident

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident** |  required  | The incident key of an existing Incident | string | 
**incident\_state** |  required  | State to make incident | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.incident | string | 
action\_result\.parameter\.incident\_state | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list incidents'
Get the list of existing Canary Incidents

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**incident\_state** |  required  | State of incidents to list | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.incident\_state | string | 
action\_result\.data\.\*\.devices\.\*\.description\.acknowledged | string | 
action\_result\.data\.\*\.devices\.\*\.description\.created | string | 
action\_result\.data\.\*\.devices\.\*\.description\.created\_std | string | 
action\_result\.data\.\*\.devices\.\*\.description\.description | string | 
action\_result\.data\.\*\.devices\.\*\.description\.dst\_host | string |  `ip` 
action\_result\.data\.\*\.devices\.\*\.description\.dst\_port | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.HOSTNAME | string |  `ip`  `host name` 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.PASSWORD | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.PATH | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.SETTINGS | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.SKIN | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.USERAGENT | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.USERNAME | string |  `user name` 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.timestamp | numeric | 
action\_result\.data\.\*\.devices\.\*\.description\.events\.\*\.timestamp\_std | string | 
action\_result\.data\.\*\.devices\.\*\.description\.events\_count | string | 
action\_result\.data\.\*\.devices\.\*\.description\.ip\_address | string | 
action\_result\.data\.\*\.devices\.\*\.description\.ippers | string | 
action\_result\.data\.\*\.devices\.\*\.description\.local\_time | string | 
action\_result\.data\.\*\.devices\.\*\.description\.logtype | string | 
action\_result\.data\.\*\.devices\.\*\.description\.mac\_address | string | 
action\_result\.data\.\*\.devices\.\*\.description\.name | string | 
action\_result\.data\.\*\.devices\.\*\.description\.node\_id | string | 
action\_result\.data\.\*\.devices\.\*\.description\.notified | string | 
action\_result\.data\.\*\.devices\.\*\.description\.src\_host | string |  `ip` 
action\_result\.data\.\*\.devices\.\*\.description\.src\_host\_reverse | string | 
action\_result\.data\.\*\.devices\.\*\.description\.src\_port | string | 
action\_result\.data\.\*\.devices\.\*\.id | string | 
action\_result\.data\.\*\.devices\.\*\.summary | string | 
action\_result\.data\.\*\.devices\.\*\.updated | string | 
action\_result\.data\.\*\.devices\.\*\.updated\_id | numeric | 
action\_result\.data\.\*\.devices\.\*\.updated\_std | string | 
action\_result\.data\.\*\.feed | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.acknowledged | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.created | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.created\_std | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.description | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.dst\_host | string |  `ip` 
action\_result\.data\.\*\.incidents\.\*\.description\.dst\_port | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.HOSTNAME | string |  `ip`  `host name` 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.PASSWORD | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.PATH | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.SETTINGS | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.SKIN | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.USERAGENT | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.USERNAME | string |  `user name` 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.timestamp | numeric | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\.\*\.timestamp\_std | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.events\_count | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.ip\_address | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.ippers | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.local\_time | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.logtype | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.mac\_address | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.name | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.node\_id | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.notified | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.src\_host | string |  `ip` 
action\_result\.data\.\*\.incidents\.\*\.description\.src\_host\_reverse | string | 
action\_result\.data\.\*\.incidents\.\*\.description\.src\_port | string | 
action\_result\.data\.\*\.incidents\.\*\.id | string | 
action\_result\.data\.\*\.incidents\.\*\.summary | string | 
action\_result\.data\.\*\.incidents\.\*\.updated | string | 
action\_result\.data\.\*\.incidents\.\*\.updated\_id | numeric | 
action\_result\.data\.\*\.incidents\.\*\.updated\_std | string | 
action\_result\.data\.\*\.max\_updated\_id | numeric | 
action\_result\.data\.\*\.result | string | 
action\_result\.data\.\*\.updated | string | 
action\_result\.data\.\*\.updated\_std | string | 
action\_result\.data\.\*\.updated\_timestamp | numeric | 
action\_result\.summary\.count | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 