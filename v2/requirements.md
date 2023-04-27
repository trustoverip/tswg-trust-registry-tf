# Trust Registry Protocol Proposal Requirements Document:

### Overview:

### Scope:

The proposal scope is specifically limited requirements presented by the "Trust
Registry API" box denoted below. Anything outside of that box, Trust Tasks,
Business/Human Decisions, Applications, TSP, and other Trust Input Sources are
out of scope.

![](https://i.imgur.com/DZuIfRN.png)

### Audience:

The proposal stage should be focused on the specification guide. Thus, the key
audience for this guide is developers interested in implementing a trust
registry. That does NOT include other stakeholders, such as security teams,
process teams, QA testing teams, and many others that may be a part of the
non-normative section.

## Terminology

## Design Principles

- **Generalizable**: We don't anchor too much on a particular use case. These
  deliverables should be generalizable and aware that many use cases are not
  discovered yet. I like taking it to the extreme: How do you use this in a
  village?
- **Conceptually anchored:** We have a clear conceptual model to anchor against
  for a long time, with a clear way to define "breaking" updates to the model.
- **Easy to adopt** We can make adoption as easy as possible and accomodate as
  many existing trust frameworks as possible with minimal change overhead
- **Flexible:** We should robust standard for trust decision making that can
  accomodate a lot of trust decision frameworks ( some known, but many unknown
  ).
- **Technologically Robust:** A requirement that there is some technological
  robustness to the deliverable, in that it can handle many technical situations
  (i.e out of band, centralized or decentralized contexts, etc ).

## Requirements:

### Functional Requirements

#### Query Operations

- Trust Registry Metadata Queries
  - Legal name of the trust registry
  - Legal name of the TR operator
  - Multi-language support
  - List ecosystem governance frameworks

#### Technical Requirements

- Transport Mechanisms
  - SHOULD be transport agnostic
  - SHOULD consider widely used transports for adoptability
  - MAY support P2P transactions.
- Stack Compatibility
  - MUST be compatible with the ToIP stack
  - MAY be compatible to other stacks.
- Discovery
  - SHOULD support decentralized discovery
  - MUST support decentralized identification i.e DIDs
  - If using DID&rsquo;s, existing DID resolvers ARE PREFERRED be able to resolve and dereference to Trust Registries
- Temporal Limitations
  - SHOULD support temporal boundaries for claims and payloads.
  - SHOULD support preventing timing attacks.
- Privacy and Security Requirements
  - MUST be compatible with secure message and transport models. Varying
    levels of assurance MAY be acceptable. (i.e HTTPS vs. HTTP vs. TSP)
  - MUST respect a &ldquo;reasonable&rdquo; level of privacy whene interacting with the
    TR. Proposals with higher respects for privacy will be considered more valuable.
  - MUST be compatible with public and private trust registries.
- Revocation
  - MAY support a requirement for revocation
- Versioning
  - MUST support a method for versioning the TR and the documents the TR provides
  - MUST support protocol versioning and future updates.

#### Data Requirements

- Chaining
  - MUST support trust chaining
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

- Uniqueness Requirements
  - Registrant MUST have a globally unique identifier. An entity has a one to many relationship with registration.
  - Each registration within a registry MUST be unique within the registry but MAY not be unique within the global context.
  - Each entity MAY be consistently identifiable in multiple contexts.
  - A registration MAY have multiple versions of the registration. If there are multiple registrations, a registration MUST identify which version is the active (primary). Other registrations are considered historical
  - Individual entries / versions of the registry should be uniquely identifiable
- Back-end Requirements
  - Each unique entry / version SHOULD be stored persistently
  - Trust Registries MAY be able to be retrieved / checked against in offline contexts
  - Implementations should be VDR-agnostic, with a core data model and anything method-specific as part of the “metadata”. This should work for DWN / KERI / blockchains / databases etc.

#### Adoption Requirements

- Timing:
- Adoption Goals:
