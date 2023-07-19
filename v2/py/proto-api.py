from fastapi import FastAPI
import uvicorn

api_description = """
This is just an example of a possible API that supports the Trust Registry Protocol v2.0. It is a mockup.

## Resources

## Roles
The system is based on handling of roles - in that an Entity, identified by a DID, is working in a particular role (or roles). The trust registry will answer queries on a role basis.

## Main Queries

With the TRP API you can do two main things, all in relation to the root EGF:

## Queries
Query the Trust Registry to see whether an Entity is authorized in a particular way. 
| method | description |
| ------ | ----------- |
| `/query/authorized/{role}` |**AuthorizedUnderRole(entityDID, role)** - Is this entity authorized under this particular `role`?|
|`/query/recognizedregistry` |**RecognizedRegistry(trustregistryDID)** - Is the Trust Registry, identified by DID recognized by this Trust Registry (i.e. does the Trust Registry that is being queried recognize the other Trust Registry)?|
|`/query/resource/` |**GetResource(resourceDID)** - returns the resource identified by `resourceDID`|

## Lookups

Gather the information needed to interact with this particular Trust Registry
| method | description |
| ------ | ----------- |
|`/lookup/roles` |**List Roles** - list the Roles that are supported by this Trust Registry (under the EGF)|
|`/lookup/resourcetypes` |**List Resource Types** - list the Resource Types that are supported by this Trust Registry (under the EGF)|
|`/lookup/assurancelevels` |**List Assurance Levels** - simple array of strings used to provide tokens for the LOAs used in this EGF. [Could do by `role`?]|
|`/lookup/didmethods` |**List Supported DID Methods** - List the supported DID Methods (under the EGF)|
|`/lookup/metadata` |**Metadata** - get metadata about the Trust Registry endpoint... - **OR** move to /metadata/ level...|

## Conventions

* DIDs are passed in as a URL parameter. 



"""

tags_metadata = [
  {
    "name":
    "lookups",
    "description":
    "Operations aimed at providing configuration and lookup information for integrators.",
  },
  {
    "name": "queries",
    "description":
    "Operations aimed at answering direct queries about authoritativeness.",
    "externalDocs": {
      "description": "SAMPLE - REPLACE",
      "url": "https://fastapi.tiangolo.com/",
    },
  },
]

app = FastAPI(title="TrustRegistryProtocol",
              version="0.0.2",
              description=api_description,
              openapi_tags=tags_metadata)

assuranceLevelList = ["TODO LOAs"]
metadata = ["TODO-metadata"]
didMethodList = ["did:indy", "did:ion", "did:cheqd"]
resourceTypeList = ["anoncreds:cred-def","anoncreds:schema-def","anoncreds:revocation-list","logo:connection"]

resourceTypes = [
  "anoncreds:credential_def", "anoncreds:schema_def", "meta:logo",
  "oca:overlay345", "didcomm:presentationrequest122"
]

roleList = ["vc:issuer", "vc:holder", "vc:verifier", "vc:walletapp", "ca:bc:signer"]


@app.get("/lookup/roles", tags=["lookups"])
async def read_roles():
  return roleList


@app.get("/lookup/metadata", tags=["lookups"])
async def read_metadata():
  return metadata


@app.get("/lookup/assurancelevels", tags=["lookups"])
async def read_assurancelevels():
  return assuranceLevelList


@app.get("/lookup/resourcetypes", tags=["lookups"])
async def read_resourcetypelist():
  return resourceTypeList


@app.get("/lookup/resourcetypes", tags=["lookups"])
async def read_resourcetypes():
  return resourceTypes


@app.get("/lookup/didmethods", tags=["lookups"])
async def read_didmethods():
  return didMethodList

# TODO: Data Dump

# TODO: "Roles" better term?

# TODO: Roles - exemplars...

# 
# QUERY METHODS

@app.get("/query/authorized/{role}/", tags=["queries"])
async def read_authorizedByRole(role, did):
  return {"todo-role": role, "todo-did": did}

@app.get("/query/recognizedregistry", tags=["queries"])
async def read_recognizedregistry(did):
  return {"todo-recognizedregistry": did}

@app.get("/query/resource", tags=["queries"])
async def read_resource(did):
  return {"todo-resourcegetter": did}




uvicorn.run(app, port=8080, host="0.0.0.0")
