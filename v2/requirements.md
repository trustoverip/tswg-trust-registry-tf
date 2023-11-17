
# ToIP Trust Registry Protocol V2 Specification
## Working Draft Deliverable

_**Editor’s Note:** This is currently a Draft Deliverable of the [Trust Registry Task Force](https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force) of the ToIP Technology Stack Working Group. For more on the structure of this Task Force and purpose of this deliverable, please see the [TRTF home page](https://wiki.trustoverip.org/display/HOME/Trust+Registry+Task+Force)._

_**How to contribute:** please add any comments or edits in your own cloned repository and make pull requests. The editors will periodically review and resolve new contributions._

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

* Antti 
* Andor
* Christine Martin, Continuum Loop
* Jacques Latour, CIRA

**Editors**

* Darrell O'Donnell, Continuum Loop
* 
* 


**Contributors**


# Terminology

In this document, the key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL", when appearing in ALL CAPITALS, are to be interpreted as described in[ RFC 2119](https://tools.ietf.org/html/rfc2119).

All other terms in **bold** will be defined in one or more ToIP glossaries in the process specified by the ToIP [Concepts and Terminology Working Group](https://wiki.trustoverip.org/pages/viewpage.action?pageId=65700).


# Purpose
The purpose of this **ToIP specification** is to define a standard interoperable protocol for interacting with a global web of **peer trust registries**, each of which can answer queries about whether a particular **party** is trusted and authorized to perform a particular **action** in a particular **digital trust ecosystem**, as well as which **peer trust registries** trust each other.

# Motivations

A core role within **Layer 4** of the **ToIP stack** is a **trust registry** (previously known as a **member directory**). This is a network service that enables the **governing authority** for an **ecosystem governance framework (EGF)** to specify what **governed parties** are authorized to perform what **actions** under the EGF. For example:

[`TODO:` - revise bullets to reflect registry-of-registry, registry signalling, and non-credential use as well.]

1. Which **issuers** are **authorized** to issue what types of **verifiable credentials**.
2. Which **verifiers** are **authorized** to request what types of **verifiable presentations**.
3. What other **governing authorities** are trusted to authorize which **parties** can perform what **actions** within their own **trust registries**.

As with all layers of the **ToIP stack**, the purpose of a **ToIP specification** is to enable the technical interoperability necessary to support **transitive trust** within and between different **trust communities** implementing the **ToIP stack**. In this case, the desired interoperability outcome is a common protocol that works between any number of decentralized **peer trust registries** operated by independent **governing authorities** representing multiple legal and business **jurisdictions**. One specific example of this need is the **digital trust ecosystem** defined by the [Interoperability Working Group for Good Health Pass](https://wiki.trustoverip.org/pages/viewpage.action?pageId=73790) (GHP). 

Registry of Registries (RoR) core function is the registration of other trusr registry.  RoR also includes lookup function to find trust registries based on known credential type

1. What other **governing authorities** are trusted to authorize which **parties** can perform what **actions** within their own **trust registries**.
2. Which **trust registry** are known to issue certain type of of **verifiable credentials**
	a. for example, which trust registry is known to issue university diplomas?
3. Which **trust registry** are known to operate in a given **EFG**.

# Conceptual Diagrams

[`TODO:` - replace with simpleer diagram(s).]

![](../out/v2/logical/highlevel/highlevel.svg)

# Scope

1. SHALL support query operations for the current status of a **registry entry**.
2. SHALL NOT support query operations for the history of a **registry entry**. 
    1. This SHOULD be considered for V2.
3. [`TODO:`- ***REVISE** to reflect minimum-viable-metadata*] SHALL NOT support query operations for metadata about a **trust registry**. 

    2. This SHOULD be considered for V2, including such attributes as:
        1. [TODO: ADD IN] Legal name and jurisdiction of **governing authority** for the **trust registry** service
        2. [TODO: ADD IN] Legal name and jurisdiction of **administering authority** for the **trust registry** operator (if different)
        3. [TODO: ADD IN]Description
        4. Language variants supported (for text items returned)
        5. [TODO: ADD IN] List of **ecosystem governance frameworks** (EGFs) served (DID, name, supported **credential type URIs**, supported **presentation type URIs**)
4. SHALL NOT include support for a DIDComm interface, only a REST interface.

    3. A DIDComm interface SHOULD be included in V2.

5. SHALL NOT support the following capabilities, which should be considered in future versions:

    4. Automated **rules** processing.
    5. ~~API-based operations for **registering parties**.~~ (rationale - this goes way beyond what any system-of-record would be willing to support and introduces security concern. NOTE: This requirement may apply to a different "thing")
    6. DIDComm native (trust task) protocol.
    6. An alternative architecture based on **chained credentials** as defined by the ToIP [Authentic Chained Data Container](https://wiki.trustoverip.org/display/HOME/ACDC+%28Authentic+Chained+Data+Container%29+Task+Force) (ACDC) specifications.

# Governing Authorities

**Governing authorities** compliant with this specification:

1. MUST have exactly one **primary trust registry**.
2. MAY have one or more **secondary trust registries**.

The **primary trust registry** plus all **secondary trust registries** are collectively referred to as the **authorized trust registries**.

3. MUST publish an **EGF** that meets the **requirements** of:

    - i. This specification.
    - ii. The [ToIP Governance Architecture Specification](https://wiki.trustoverip.org/pages/viewpage.action?pageId=71241). Note that this includes the requirement that the **EGF** and all **governed parties** (which includes **authorized issuers** and **authorized verifiers**) must be identified with a **DID**.
4. MUST publish, in the **DID document** associated with the **DID** identifying its **EGF**, a **service property **specifying the **service endpoint** for its **primary trust registry** that meets the **requirements** in the _[Trust Registry Service Property](#trust-registry-service-property)_ section.
5. MUST publish in its **EGF** a list of any other EGFs governing **secondary trust registries.**
6. MUST specify in the EGF any additional **requirements** for an **authorized trust registry**, including:

    - i. **Information trust requirements**.
    - ii. Technical **requirements**.
    - iii. Operational **requirements**.
    - iv. Legal contracts.
7. MUST specify in its **EGF** (or in any referenced **credential governance framework**) **requirements** for:
    - i. all `authorization` values that are used by the trust registry.
    - ii. all `assurance levels`, specified with unique names, that are service by the trust registry, and what `authorization` values they apply to.
    - iii. all `DID Methods` that are supported by the ecosystem, and serviced by the trust registry.
    - iv. all related `resources` that are to be serviced by the trust registry. 
   - v. any `metadata`` required by implementors (e.g. claim name that is mandatory if pointing a credential back to an EGF.) [this is a weak example]
   - vi. ???a statement about the basis the trust registry claims to be authoritative???
   - vii. ???means by which others are able to verify the asserted authority???
8. SHOULD specify in the **EGF** the following **requirements** for an **authorized trust registry** and any **registered party** (i.e., issuer, verifier, or peer trust registry):
   - i. The **requirements** to become authorized.
   - ii. How to request registration.
   - iii. The **requirements** for assignment of each **authorization** for a **registry entry**.
   - v. Any access limitations (e.g. unrestricted public access, authentication-limited access).
   - vi. How to request access where unrestricted public access is not available.



# Trust Registry Service Property

The **DID document** for the **DID** that identifies an **EGF** compliant with this specification MUST include a service property that meets the **requirements** [in section 5.4 of the W3C Decentralized Identifiers (DIDs) 1.0 specification](https://www.w3.org/TR/did-core/#services) plus the following additional **requirements**:

* The value of the `type` property MUST be `TrustRegistry`.
* The value of the `serviceEndpoint` property MUST be exactly one HTTPS URI.

[`TODO:` reconcile above with Profiles concept. ]

[`TODO:` The issuer/verifier needs to state their primary trust registry affiliation (a trust relationship) - is this a new section?]


# Trust Registry Protocol

The authoritative technical specifications for the API calls in the ToIP Trust Registry Protocol V1 are specified in Appendix A (OpenAPI YAML file). This section contains a textual description of the **requirements**.

**Trust registries** implementing this protocol:

1. MUST maintain the service implementing this protocol at the HTTPS URI specified in the _[Trust Registry Service Property](#trust-registry-service-property)_ section.
2. MUST return responses to queries for the **status value** of a **registry entry** that satisfies one or more of the following sets of query parameters:
    - i. **Entity Authorization**: entityDID, authorization
    - ii. **Recognized Registry:** entityDID
3. MUST return responses using the data model specified in the _[Data Model](#data-model)_ section.
4. MUST return exactly one of the following **status values** for a **registry entry** satisfying the query parameters:
    - i. `Not found`
    - ii. `Current`
    - iii. `Expired` (not renewed after the previous valid registration period)
    - iv. `Terminated` (voluntary termination by the **registered party**)
    - v. `Revoked` (involuntary termination by the **governing authority**)
5. For queries returning a **status value** other than `Not Found`, the response MUST return the following values:
    - i. The parameter values exactly as supplied in the query (so responses can be stateless).
   - ii. The **status value**.
   - iii. Exactly two **datetime values** conforming to the following requirements:
        - a. The value labels MUST be:
            - i. `AuthorizationStartDate`
            - ii. `AuthorizationEndDate`
        - b. The values MUST be formatted to comply with [RFC 3339](https://tools.ietf.org/html/rfc3339) in the UTC/Z time zone with no offset.
        - c. The `AuthorizationStartDate` MUST be the date that the **registered party’s** authorization began.
        - d. The `AuthorizationEndDate` MUST be either:
            - i. `Null` for an entry whose **status value** is `Current` at the time of the query.
            - ii. A specific date value if the **registered party’s** **status value** is `Expired`, `Terminated` or `Revoked.`
        - e. If a **registered party** has multiple entries (representing an authorization history), the most recent value MUST be returned. 

# Data Model 

`TODO:` build out data model pieces - do work on OAS/Swagger, then move here.

# Appendix A: Consolidated Requirements

For ease of reference, the following table consolidates all normative requirements in this specification. Each requirement is linked to the section in which it appears.

`THE FOLLOWING REQUIREMENTS IN THE TABLE ARE JUST EXAMPLES FOR NOW.`

| Req # | Description | Section |
|---------|--------------|-----------|
| | **General ToIP Architecture Requirements**| |
| A.1 | MUST have exactly one **primary trust registry**. | [LINK] |
|A.2 | MAY have zero or more **secondary trust registries**. (The **primary trust registry** plus all **secondary trust registries** are collectively the **authorized trust registries**.) | [LINK]|
|A.3|MUST publish an **EGF** that meets the **requirements** in: 
|A.3.1|    This specification. | [LINK]
|A.3.2| The [ToIP Governance Architecture Specification](https://wiki.trustoverip.org/pages/viewpage.action?pageId=71241). Note that this includes the requirement that the **EGF** and all **governed parties** (which includes **authorized issuers** and **authorized verifiers**) |[LINK]|
