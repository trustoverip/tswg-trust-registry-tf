# Placeholder TRTF README v2



## UPDATE 2023-09-07

Key changes made:
  * shifting to OAS/Swagger (.yaml format) for main developer-level documentation.
  * Diagrams will be used but OAS file is the source-of-truth.


## Requirements

Requirements capture is located at:

* [requirements.md](../v2/requirements.md) - contains a rudimentary set of requirements (WORK IN PROGRESS - really just started)
* 



## OpenAPI Specification

The first "concrete" API specification is an Open API Specification v3 YAML file. 

[OAS (.yaml) for TRP v2](../v2/api/WIP.toip.trustregistry.api.yaml)



## Logical Model


### High-Level

We provide a high-level object model (NOTE: source of truth is the Swagger as this diagram may be out of date during development)

![High Level Object Model](../out/v2/logical/highlevel/highlevel.svg)



### Integration Model

As the TRP is a protocol, those systems that don't natively support it can be connected via "bridge". 

An early example is shown below:
![C4 Systems Model - showing native TRP support on one system, bridged support to two other systems (e.g. TRAIN and EU Trusted List ARF)](../out/v2/logical/protocol-bridging/protocol-bridging.svg)


