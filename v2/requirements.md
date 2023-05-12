# Trust Registry Protocol Proposal Requirements Document:

### Overview:

This document outlines the requirements for proposals, not the specifications
themselves. The goal of this document is to give direction to
contributors/editors of the Trust Registry Protocol so that there is a clear set
of guidelines for evaluation and acceptance.

**STATUS:** WORKING DRAFT

### Scope:

The proposal scope is specifically limited to the requirements presented by the
"Trust Registry API" box denoted below. Anything outside of that box, Trust
Tasks, Business/Human Decisions, Applications, TSP, and other Trust Input
Sources are out of scope.

![](https://i.imgur.com/DZuIfRN.png)

### Audience:

The proposal stage should be focused on the specification guide. Thus, the key
audience for this guide is developers interested in providing access
toimplementing a new or existing trust registry. That does NOT include other
stakeholders, such as security teams, process teams, QA testing teams, and many
others that may be a part of the non-normative section

## Terminology

## Design Principles

- **Generalizable:** We don't anchor too much on a particular use case. These
  deliverables should be generalizable and aware that many use cases are not
  discovered yet. I like taking it to the extreme: How do you use this in a
  village?
- **Conceptually anchored:** We have a clear conceptual model to anchor against
  for a long time, with a clear way to define "breaking" updates to the model.
- Easy to adopt: We can make adoption as easy as possible and accommodate as
  many existing trust frameworks as possible with minimal change overhead
- **Flexible:** We should have robust standards for trust decision making that
  can accommodate a lot of trust decision frameworks (some known, but many
  unknown).
- **Technologically Robust:** A requirement that there is some technological
  robustness to the deliverable, in that it can handle (or be used in) many
  technical situations (e.g. out of band, centralized or decentralized
  contexts).
- **Preference toward running code:** We believe in rough consensus and running
  code.

## Requirements:

#### Functional Requirements

- Query Operations
  - SHOULD allow Trust Registry Metadata Queries, e.g.:
  - SHOULD allow Ecosystem Scope Queries
  - SHOULD allow Governance Processes Queries
  - SHOULD allow Policy and Standards Queries

#### Technical Requirements

- Transport Mechanisms
  - SHOULD be transport agnostic
  - SHOULD consider widely used transports for adoptability
  - MAY support P2P transactions.
- Stack Compatibility
  - MUST be compatible with the ToIP stack
  - SHOULD heavily consider compatibility with other systems to facilitate adoption.
- Discovery
  - The proposal SHOULD explain its approach toward discovery and how it relates
    to the rest of the technology architecture specification.
  - Trust Registry SHOULD support decentralized discovery
  - Trust Registry identifiers MUST be unique within an ecosystem.
- Temporal Limitations
  - SHOULD support temporal boundaries for claims and payloads.
  - SHOULD support preventing timing attacks.
- Privacy and Security Requirements
  - MUST be compatible with secure message and transport models. Varying
    levels of assurance MAY be acceptable. (i.e HTTPS vs. HTTP vs. TSP)
  - MUST respect a "reasonable" level of privacy whene interacting with the
    TR. Proposals with higher respects for privacy will be considered more valuable.
  - MUST be compatible with public and private trust registries.
  - The cryptographic module SHOULD ensure support for quantum-safe cryptography
    using cryptographic algorithms, cryptographic parameter sizes, key lengths
    and crypto periods which are configurable, and which can be updated within
    protocols, applications and services to be consistent with transition
    guidance in time to meet specified transition dates.
- Revocation
  - MAY support a requirement for revocation
- Versioning
  - MUST support a method for versioning the TR and the documents the TR provides
  - MUST support protocol versioning and future updates.

#### Data Requirements

- Chaining
  - SHOULD support trust chaining
- Verifiability
  - SHOULD support atomic verification.
- Data Model
  - MAY be compatible with the DIF Trust Establishment Specification
  - Existing patterns SHOULD leverage from DID Core where possible
  - Lookup patterns SHOULD allow for Service Discovery and Resource Discovery
- Message Models
  - TBD
- Feedback/Error Requirements
  - SHOULD provide a way to respond with appropriate errors given an
    unauthorized, malformed, or incomplete request

#### Governance Requirements

- Traceability Requirements
  - MUST be traceable via governance
- Uniqueness Requirements
  - Registrants MUST have a globally unique identifier. An entity has a one to many relationship with registration.
  - Each registration within a registry MUST be unique within the registry but MAY not be unique within the global context.
  - Each entity MAY be consistently identifiable in multiple contexts.
  - A registration MAY have multiple versions of the registration. If there are multiple registrations, a registration MUST identify which version is the active (primary). Other registrations are considered historical
  - Individual entries / versions of the registry should be uniquely identifiable
- Back-end Requirements
  - Each unique entry / version SHOULD be stored persistently
  - Trust Registries MAY be able to be retrieved / checked against in offline
    contexts
  - Implementations should be VDR-agnostic, with a core data model and anything
    method-specific as part of the “metadata”. This should work for DWN / KERI /
    blockchains / databases etc.
- Issuer Requirements:
  - A TR SHOULD be able to answer the claim of how it gets authority
  - A TR SHOULD be able to define their accountability.

#### Adoption Requirements

- [Timing: Proposals to begin early June. Worth discussing, but sooner is better (e.g., moderate changes to an existing protocol, finish within 6 months)](https://github.com/trustoverip/tswg-trust-registry-tf/discussions/93)
- [Adoption Goals: Expectations are medium. Should be usable in a reasonable number of major ecosystems](https://github.com/trustoverip/tswg-trust-registry-tf/discussions/95)

#### Additional Considerations

- MAY have additional information on compatibility with existing trust registries

#### Key Systems to Consider

- EU TRAIN
- EU Trust Lists
- [DIACC Trust Registry](https://diacc.ca/trust-framework/pctf-trust-registries/)
- [Cira Trust Registry]()
- [AAMVA mDL](https://www.aamva.org/getmedia/b801da7b-5584-466c-8aeb-f230cef6dda5/mDL-Implementation-Guidelines-Version-1-2_final.pdf)
- [Education (Ethiopia)]()
- [Technical Specification for Digital Credentials and Digital Trust Services](https://dgc-cgn.org/standards/find-a-standard/standards-in-digital-credentials/digital-credentials/)
