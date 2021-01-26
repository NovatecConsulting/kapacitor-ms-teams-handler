# Python MS Teams API for Kapacitor Alerts
A respective setting already exists in the [kapacitor configuration](https://docs.influxdata.com/kapacitor/v1.5/event_handlers/microsoftteams/). 

This project is for greater flexibility in relation to proxies and was developed for the Alerting UI in the **inspectIT Ocelot - Configuration Server** [Project](https://github.com/inspectIT/inspectit-ocelot/tree/master/components/inspectit-ocelot-configurationserver).

## Installation
Install all dependencies.

```bash
pip install -r requirements.txt
```

## Usage
### Bundle
Create a zip file with all required files:
```bash
make bundle
```
Create a "/teams-api" directory under the kapacitor load directory (default: /etc/kapacitor/load/handler_scripts), copy and unzip the created zip file there.
One or more handlers can be created under the /etc/kapacitor/load/handlers directory.

Optional: Edit the [configurations](configuration)

Example "teams-handler-team1.yml":
```yml
id: ms_teams-issue-handler_team_1
topic: ms_teams_team_1
kind: exec
options:
  prog: '/usr/bin/python3'
  args:
    - '/etc/kapacitor/load/handler_scripts/teams-api/main.py' # python file path (required)
    - 'https://outlook.office.com/webhook/xxx' # webhook (required)
```
This handler will be visible on the inspectIT Ocelot - Configuration Server UI, if the Alerting settings are enabled.

### Config
The Log Path can be edited in the [configuration.py](configuration/configuration.py) file.
