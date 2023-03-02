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

- Trust Registry
- Governing Authority
- Trust Ecosystem
- Administering Body
- Governance Framework
- Governance Role
- Trust Context
- Trust Decision
- Jurisdiction
- Trust test: @Neil to elaborate on this.

## Requirements:

### Design Requirements

### Design Principles

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

### Functional Requirements

A trust registry proposal MUST be able to support the following queries:

#### Trust Registry Descriptive Functional Requirements

- Describe the Governing Authority of this Ecosystem?
- Who is the Administering Authority of this Ecosystem?
- What roles are recognized in the {EGF}?
- What governance framework is the trust registry operating with.

#### Issuer Functional Requirements

- A trust registry MAY describe an issuer and provide reasons for why you can
  trust the issuer (i.e key management, etc)
- A trust registry MAY attest to why the issuer is/is not qualified for a claim.
- A trust registry MAY describe if an issuer is authorized to make a claim.
- A trust registry MAY describe who authozied the issuer for the registry.
- A trust registry MAY provide descriptions on how their governance framework
  operates.

#### Holder Functional Requirements

- A trust registry MAY present reasons why a holder is trustworthy for a
  credential, such as authorized wallets for holding the credential.

### Technical Requirements

- Transport agnostic
- Allow for trust chaining
- Ephermeral Scoping
