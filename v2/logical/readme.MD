

## Logical Model

The general concept is that a Trust Registry provides two main different types of information (NOTE: these names may/likely will change):

* Lookups - information that helps configure systems that are integrating into an ecosystem. Consider these like config files - the place a system would go to find out what the primitives are that it needs.
* Queries - allows systems to get answers to the specific questions it has and needs answers for to do their job. This includes:
  * What Roles are active in the ecosystem? *Roles are generic and a design decision (for TRP) needs to be made about explicit hard-coding of the trust-diamond roles (Issuer of X, Holder of X, and Verifier of X) that were built into the v1 TRP are needed.* 
  * What entities are authorized under a Role?
  * What Resources are available? This one is a generic and may include various known "things" but should (likely) be extensible.
    * Credential Types, Credential Schemas, DID-Linked Resources, Presentation Requests, etc.
  * What Assurance Levels are in use in the ecosystem? *DESIGN DECISION NEEDED - this could be Resource but Assurance Levels are quite critical to understand the context of other things in an ecosystem so it seems that a top-level Assurance Level makes sense.*

Additionally there is a nascent `Metadata` top-level item intended to capture Trust Registry metadata as required.

The following diagram is notional at the moment but captures the above:

![UML Class Diagram](../../out/v2/logical/highlevel/highlevel.svg)

* Consider DIDMethod() -> Methods(type{DID|AID|URI,...})
* TrustRegistry - Mutual Recognition 
* Roles -> tags 
  * interesting more abstract - generically extensible
  * D: maps to Governed (Key) Roles in EGF template
  * T: VC "roles" Holders, Verifier, Issuer are really components.


## Open API Specification

While the TRP may end up having several concrete implementations in the interim an OAS/OpenAPI

### Generating .SVG Files from PlantUML
Visual Studio Code has a graphical way of generating outputs. They end up in the `/out/{path}' folder. As an example the PlantUML file:
* `{projectfolder}/v2/logical/highlevel.puml` will render to:
* `{projectfolder}/out/v2/logical/highlevel/highlevel.svg`



## TRP Layer 

TODO: Add Interface diagram...



REQUIREMENTS

* EGF to TR mapping is the goal. 
* A TR MUST support 
  * mapping the KeyRoles identified in the EGF

* A TrustRegistry SHOULD support:
  * 