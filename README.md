# Python MS Teams API for Kapacitor Alerts
Please note that kapacitor natively provides an [event handler](https://docs.influxdata.com/kapacitor/v1.5/event_handlers/microsoftteams/) for MS Teams.  
This project is for greater flexibility in relation to proxies and was developed for the Alerting UI in the **inspectIT Ocelot - Configuration Server** [Project](https://github.com/inspectIT/inspectit-ocelot/tree/master/components/inspectit-ocelot-configurationserver).

## Usage
* Download the [kapacitor-teams-handler.zip](https://github.com/NovatecConsulting/kapacitor-ms-teams-handler/releases) 
from the latest Release or create a zip file with all required files with `make bundle`
* Create a "handler script" directory, copy and unzip the ZIP file there. *For example under the kapacitor load directory: 
`/etc/kapacitor/load/handler_scripts/teams-api`.*  
This path is required later in the handler-files. 
* Navigate to the handler script path and install all dependencies: `pip3 install -r requirements.txt`
* To use the MS Teams handler, create one or more handler-files `<custom_name>.yml` under the `/etc/kapacitor/load/handlers` directory.
* Edit the [configurations](configuration) to your specifications *(log path and proxy settings)*.

### Handler-file example
```yml
# /etc/kapacitor/load/handlers/teams-handler-team1.yml
id: ms_teams-issue-handler_team_1                               # handler id in the Ocelot - Configuration Server UI
topic: ms_teams_team_1                                          # channel in the Ocelot - Configuration Server UI
kind: exec
options:
  prog: '/usr/bin/python3'                                      # path to python3
  args:
    - '/etc/kapacitor/load/handler_scripts/teams-api/main.py'   # entrypoint path (required)
    - 'https://outlook.office.com/webhook/xxx'                  # webhook (required)
```
Note that the entrypoint path must be refer to the previous unzipped directory.
The handlers are visible on the inspectIT Ocelot - Configuration Server UI.

### Config
The log path and proxy URLs can be edited in the [configuration.py](configuration/configuration.py) file.

### Testing
The script can be tested with the [example.json](tests/example_alert.json) file: `python3 main.py "https://webhook-url" < tests/example_alert.json`
