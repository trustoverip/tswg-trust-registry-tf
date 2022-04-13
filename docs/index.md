# ToIP Trust Registry Protocol V1 Specification
## Working Draft Deliverable

_**Editor’s Note:** This is currently a Draft Deliverable of the [Trust Registry Task Force](https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force) of the ToIP Technology Stack Working Group. For more on the structure of this Task Force and purpose of this deliverable, please see the [TRTF home page](https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force)._

_**Status—2021-09-16:** This deliverable is currently a Community Review Draft. The Trust Registry Task Force meeting is now meeting as part of the Technology Architecture Task Force meetings on Thursdays from 07:00-8:00 PT / 15:00-16:00 UTC and again at 1:00-2:00PM PT / 21:00-22:00 UTC. See the [ToIP Calendar](https://wiki.trustoverip.org/display/HOME/Calendar+of+ToIP+Meetings) for Zoom meeting info._

_**How to contribute:** please add any comments or edits in Suggest Mode. The editors will periodically review and resolve new contributions._

_NOTE: All diagrams developed by contributors should be accompanied by the source._

# Table of Contents  
  * [Contributors](#contributors)
  * [Terminology](#terminology)
  * [Purpose](#purpose)
  * [Motivations](#motivations)
  * [Conceptual Diagrams](#conceptual-diagrams)
  * [Scope](#scope)
  * [Governing Authorities](#governing-authorities)
  * [Trust Registry Service Property](#trust-registry-service-property)
  * [Trust Registry Protocol](#trust-registry-protocol)
  * [Data Model](#data-model)
- [APPENDIX A: OpenAPI Specification](#appendix-a--openapi-specification)


# Contributors

To comply with the intellectual property rights protections in[ the charter of the ToIP Foundation](https://docs.google.com/document/d/1hJ4YWH_efrYTRvzRI1N9YHwhUOyI_ScrPmI1D9T4_oc/edit?usp=sharing) (as required by all Joint Development Foundation projects hosted by the Linux Foundation), all contributors in any capacity to this Draft Deliverable MUST be current members of the ToIP Foundation. The following contributors each certify that they meet this requirement:

**Editors**



* [Darrell O'Donnell](https://wiki.trustoverip.org/display/~darrell.odonnell), Continuum Loop Inc.
* [Drummond Reed](https://wiki.trustoverip.org/display/~drummondreed), Evernym

**Contributors**



* Antti Kettunen
* Dan Bachenheimer, Accenture
* Eric Drury, Forth Consulting
* Jim St. Clair, Lumedic
* Sankarshan Mukhopadhyay, Dhiway
* Scott Perry, Scott S. Perry CPA
* Vikas Malhotra, WOPLLI Technologies


# Terminology

In this document, the key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL", when appearing in ALL CAPITALS, are to be interpreted as described in[ RFC 2119](https://tools.ietf.org/html/rfc2119).

All other terms in **bold** will be defined in one or more ToIP glossaries in the process specified by the ToIP [Concepts and Terminology Working Group](https://wiki.trustoverip.org/pages/viewpage.action?pageId=65700).


# Purpose

The purpose of this **ToIP specification** is to define a standard interoperable protocol for interacting with a global web of **peer trust registries**, each of which can answer queries about whether a particular **party** is trusted and authorized to perform a particular **action** in a particular **digital trust ecosystem**, as well as which **peer trust registries** trust each other.


# Motivations

A core role within **Layer 4** of the **ToIP stack** is a **trust registry** (previously known as a **member directory**). This is a network service that enables the **governing authority** for an **ecosystem governance framework (EGF)** to specify what **governed parties** are authorized to perform what **actions** under the EGF. For example:



1. Which **issuers** are **authorized** to issue what types of **verifiable credentials**.
2. Which **verifiers** are **authorized** to request what types of **verifiable presentations**.
3. What other **governing authorities** are trusted to authorize which **parties** can perform what **actions** within their own **trust registries**.

As with all layers of the **ToIP stack**, the purpose of a **ToIP specification** is to enable the technical interoperability necessary to support **transitive trust** within and between different **trust communities** implementing the **ToIP stack**. In this case, the desired interoperability outcome is a common protocol that works between any number of decentralized **peer trust registries** operated by independent **governing authorities** representing multiple legal and business **jurisdictions**. One specific example of this need is the **digital trust ecosystem** defined by the [Interoperability Working Group for Good Health Pass](https://wiki.trustoverip.org/pages/viewpage.action?pageId=73790) (GHP). 


# Conceptual Diagrams

Figure 1 represents a conceptual overview of a **digital trust ecosystem** that illustrates the central role of a **trust registry**.



![Overview diagram of key components of a digital trust ecosystem](https://user-images.githubusercontent.com/103072929/162291419-2f769d2e-98c5-409b-af94-4a3f80eb812a.png)


**Figure 1: Overview diagram of key components of a digital trust ecosystem**



Figure 2 is a conceptual overview of a network of independent **trust registries** representing different **digital trust ecosystems**, all of which can interoperate using the ToIP Trust Registry Protocol to enable **transitive trust** across any two ecosystems.


![A network of trust registries who are all peers](https://user-images.githubusercontent.com/103072929/162291450-0358da28-ac1c-4a4c-b931-97a3d2af2450.png)


**Figure 2: A network of trust registries who are all peers**


# Scope

In the first version of this specification (V1), the following **requirements** represent specific limitations on scope. Subsequent versions MAY remove or revise these limitations.

The ToIP Trust Registry Protocol V1 defined in this specification:



1. SHALL support query operations for the current status of a **registry entry**.
2. SHALL NOT support query operations for the history of a **registry entry**. 
    1. This SHOULD be considered for V2.
3. SHALL NOT support query operations for metadata about a **trust registry**.
    2. This SHOULD be considered for V2, including such attributes as:
        1. Legal name of **trust registry** service
        2. Legal name of **trust registry** operator (if different)
        3. Description
        4. Language variants supported (for text items returned)
        5. List of **ecosystem governance frameworks** (EGFs) served (DID, name, supported **credential type URIs**, supported **presentation type URIs**)
4. SHALL NOT include support for a DIDComm interface, only a REST interface.
    3. A DIDComm interface SHOULD be included in V2.
5. SHALL NOT support the following capabilities, which should be considered in future versions:
    4. Automated **rules** processing.
    5. API-based operations for **registering parties**.
    6. An alternative architecture based on **chained credentials** as defined by the ToIP [Authentic Chained Data Container](https://wiki.trustoverip.org/display/HOME/ACDC+%28Authentic+Chained+Data+Container%29+Task+Force) (ACDC) specifications.


# Governing Authorities

**Governing authorities** compliant with this specification:



1. MUST have exactly one **primary trust registry**.
2. MAY have zero or more **secondary trust registries**. (The **primary trust registry** plus all **secondary trust registries** are collectively the **authorized trust registries**.)
3. MUST publish an **EGF** that meets the **requirements** in:
    1. This specification.
    2. The [ToIP Governance Architecture Specification](https://wiki.trustoverip.org/pages/viewpage.action?pageId=71241). Note that this includes the requirement that the **EGF** and all **governed parties** (which includes **authorized issuers** and **authorized verifiers**) must be identified with a **DID**.
4. MUST publish, in the **DID document** associated with the **DID** identifying its **EGF**, a **service property **specifying the **service endpoint** for its **primary trust registry** that meets the **requirements** in the _[Trust Registry Service Property](#trust-registry-service-property)_ section.
5. MUST publish in its **EGF** a list of any other EGFs governing **secondary trust registries.**
6. MUST specify in the EGF any additional **requirements** for an **authorized trust registry**, including:
    3. **Information trust requirements**.
    4. Technical **requirements**.
    5. Operational **requirements**.
    6. Legal contracts.
7. MUST specify in its **EGF** (or in any referenced **credential governance framework**) **requirements** for:
    7. An **authorized issuer**, including:
        1. The **EGF URI** that MUST be included as a **claim** in any authorized **credential**.
        2. The **credential type URI** that MUST be used for any authorized **credential**.
    8. An **authorized verifier**, including:
        3. The **presentation type URI** that an **authorized verifier** MUST use for any authorized **presentation request**.
8. SHOULD specify in the **EGF** the following **requirements** for an **authorized trust registry** and any **registered party** (i.e., issuer, verifier, or peer trust registry):
    9. The set of **DID methods** authorized for use in the ecosystem.
    10. The **requirements** to become authorized.
    11. How to request registration.
    12. The **requirements** for assignment of each **status value** for a **registry entry**.
    13. Access control mechanisms.
    14. How to request access.


# Trust Registry Service Property

The **DID document** for the **DID** that identifies an **EGF** compliant with this specification MUST include a service property that meets the **requirements** [in section 5.4 of the W3C Decentralized Identifiers (DIDs) 1.0 specification](https://www.w3.org/TR/did-core/#services) plus the following additional **requirements**:



* The value of the `type` property MUST be `TrustRegistry`.
* The value of the `serviceEndpoint` property MUST be exactly one HTTPS URI.


# Trust Registry Protocol

The authoritative technical specifications for the API calls in the ToIP Trust Registry Protocol V1 are specified in Appendix A (OpenAPI YAML file). This section contains a textual description of the **requirements**.

**Trust registries** implementing this protocol:



1. MUST maintain the service implementing this protocol at the HTTPS URI specified in the _[Trust Registry Service Property](#trust-registry-service-property)_ section.
2. MUST return responses to queries for the **status value** of a **registry entry** that satisfies one or more of the following sets of query parameters:
    1. **Authorized issuers**: EGF URI, **credential type URI**, issuer URI
    2. **Authorized verifiers**: EGF URI, **presentation type URI**, verifier URI
    3. **Trusted peer registries for authorized issuers:** EGF URI, **credential type URI**, EGF URI
    4. **Trusted peer registries for authorized verifiers:** EGF URI, **presentation type URI**, EGF URI
3. MUST return responses using the data model specified in the _[Data Model](#data-model)_ section.
4. MUST return exactly one of the following **status values** for a **registry entry** satisfying the query parameters:
    5. `Not found`
    6. `Current`
    7. `Expired` (not renewed after the previous valid registration period)
    8. `Terminated` (voluntary termination by the **registered party**)
    9. `Revoked` (involuntary termination by the **governing authority**)
5. For queries returning a **status value** other than `Not Found`, the response MUST return the following values:
    10. The parameter values exactly as supplied in the query (so responses can be stateless).
    11. The **status value**.
    12. Exactly two **datetime values** conforming to the following requirements:
        1. The value labels MUST be:
            1. `AuthorizationStartDate`
            2. `AuthorizationEndDate`
        2. The values MUST be formatted to comply with [RFC 3339](https://tools.ietf.org/html/rfc3339) in the UTC/Z time zone with no offset.
        3. The `AuthorizationStartDate` MUST be the date that the **registered party’s** authorization began.
        4. The `AuthorizationEndDate` MUST be either:
            3. `Null` for an entry whose **status value** is `Current` at the time of the query.
            4. A specific date value if the **registered party’s** **status value** is `Expired`, `Terminated` or `Revoked.`
        5. If a **registered party** has multiple entries (representing an authorization history), the most recent value MUST be returned. 

# Data Model

The authoritative technical specifications for the data model for requests and responses in the ToIP Trust Registry Protocol V1 are specified in Appendix A ([OpenAPI YAML file](https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/api/toip.trustregistry.api.yaml)). This section contains a textual description of the requirements.

![textual description of the requirements](https://user-images.githubusercontent.com/103072929/162291432-c85e9977-de52-4403-94c7-3c7fcbcccc98.png)


# APPENDIX A: OpenAPI Specification

The OpenAPI YAML file can be found here: [https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/api/toip.trustregistry.api.yaml](https://github.com/trustoverip/tswg-trust-registry-tf/blob/main/api/toip.trustregistry.api.yaml) 

<&lt;TODO: to replace with a tagged commit once we have “locked” things down.>>

