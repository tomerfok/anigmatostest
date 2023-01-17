# tasks
## Task #1
Given a MongoDB database hosted locally (as described above), write a Python
command line script that retrieves all documents in a collection called "customers" and
prints their names and addresses to the console. The script should be invoked from the
command line as follows

todo list:
- install mongodb : done
- start mongodb : done
- connect to mongodb : done
- create new db : done
- create new collection : done
- add sample data to collection : done
- verify data : done

command to run: python ./customers-dump.py

## Task #2

Using Flask, create an app which exposes an endpoint that accepts a GET request and
returns a JSON object containing information from a Firestore table called "products".
The endpoint should accept a query parameter called "id" that is used to retrieve the
specific product. The endpoint should be accessible via http://localhost:8080/ URL.

todolist:
- install Google Cloud SDK : done
- Cloud Tools VScode extentsion : done
- set up GCP project : done
- authenticate to GCP : done
- install necessary python libraries : done
- configure the local enviroment variables : done
- deploy on GCP  
- create firebase project : done
- create enable firestore : done
- create new collection : done
- add sample data : done
### Examples of environment variables configuration
export GOOGLE_APPLICATION_CREDENTIALS=C:\Users\tomer\AppData\Roaming\gcloud\application_default_credentials.json
export GOOGLE_APPLICATION_CREDENTIALS=%APPDATA%\gcloud\application_default_credentials.json
export SQL_USER=%APPDATA%\gcloud\application_default_credentials.json
export SQL_PASSWORD=%APPDATA%\gcloud\application_default_credentials.json

### Code variation
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\tomer\\AppData\\Roaming\\gcloud\\application_default_credentials.json"

command to create data: python firestoreinest.py
command to run web server: python main.py


#########################################
## Cloud deployment error
tomer@DESKTOP-TNNSRLJ MINGW64 /f/VSCode Projects/anigmatostest/anigmatostest (main)        
$ gcloud run deploy
Deploying from source. To deploy a container use [--image]. See https://cloud.google.com/run/docs/deploying-source-code for more details.
Source code location (F:\VSCode Projects\anigmatostest\anigmatostest):  y
Next time, use `gcloud run deploy --source .` to deploy the current directory.

Service name (y):  y
API [run.googleapis.com] not enabled on project [1006404769026]. Would you like to enable 
and retry (this will take a few minutes)? (y/N)?  y

Enabling service [run.googleapis.com] on project [1006404769026]...
ERROR: (gcloud.run.deploy) FAILED_PRECONDITION: Billing account for project '1006404769026' is not found. Billing must be enabled for activation of service(s) 'run.googleapis.com,containerregistry.googleapis.com' to proceed.
Help Token: AXyI5c_Lkq1OQb_SfVt-krQgDoZ9ZFHcF__WKcrhIvbQ8ltrVhX-4p_rLvtZccty0Ih-DxK6QKtxUZTXZCGib2bB2LvegxITptwZ4QbE-7-MIYc2
- '@type': type.googleapis.com/google.rpc.PreconditionFailure
  violations:
  - subject: ?error_code=390001&project=1006404769026&services=run.googleapis.com&services=containerregistry.googleapis.com
    type: googleapis.com/billing-enabled
- '@type': type.googleapis.com/google.rpc.ErrorInfo
  domain: serviceusage.googleapis.com/billing-enabled
  metadata:
    project: '1006404769026'
    services: run.googleapis.com,containerregistry.googleapis.com
  reason: UREQ_PROJECT_BILLING_NOT_FOUND
