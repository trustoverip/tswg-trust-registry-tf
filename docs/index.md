# Trust Registry Specification

## ToIP Trust Registry Requirements

### A ToIP-compliant trust registry:

1. MUST be identified by a trust registry DID generated using a ToIP-compliant DID method.
2. MUST support all mandated requirements of the Good Health Pass (GHP[^1]) Trust Registry Protocol Specification.
3. SHOULD incorporate throttling, DDOS protection, etc.
4. MAY limit the DID methods permitted to be used for the registered DIDs to a subset of the
available DID methods.

### Trust Registry Protocol
The ToIP Trust Registry Protocol:

1. ~~MUST be an open standard royalty-free specification.~~
2. ~~MUST be specified in either:~~
   1. ~~A GHP Trust Registry Protocol Specification.~~
   2. ~~A more general purpose trust registry protocol specification if it meets all the
requirements in these recommendations.~~
3. MUST support trust registry service endpoint resolution using ToIP-compliant DID methods.
   1. SHOULD support the GHP X.509 Subject Alternative Name URI Specification[^2]. 
4. ~~MUST~~ SHOULD provide a registration method.
5. SHOULD provide a revocation method.
6. SHOULD provide a verifier access request method.
7. MUST support queries consisting of the following parameters to indicate entity (e.g. Issuer or Verifier) authorization:
   1. Governance Framework DID
   2. Issuer DID
   3. Verifiable credential type URI

9. MUST return exactly one of the following status values:
   1. Not found
   2. Current
   3. Expired (not renewed after the previous valid registration period)
   4. Terminated (voluntarily terminated by the issuer)
   5. Revoked (involuntarily termination made by the governing authority)
10. MUST return exactly two date values (formatted to comply with RFC3339, as UTC/Z - with no
offset):
    1. AuthorizationStartDate - which indicates the data that the Issuer’s authorization started.
    2. AuthorizationEndDate[^3] - which may be null for Issuers that are currently, at time of the
query, an Authorized Issuer. If an Issuer is not currently an Authorized Issuer, but had been in the past, the date
that they lost that status will be returned. (NOTE: Where more than one non-contiguous authorization time blocks exist only the most recent will be returned.)

### Issuers
ToIP-compliant issuers:

1. MUST be identified by a URI. 
   1. SHOULD be identified by an issuer DID generated using a ToIP-compliant DID method.
2. MUST register the issuer DID in the trust registry of any specific EGF under which the issuer
wishes to issue GHP-compliant credentials.
3. MUST issue GHP-compliant verifiable credentials that meet the following requirements:
3.1. The verifiable credential includes a claim specified in the GHP Verifiable Credentials
Specification whose value is the trust registry DID for the specific EGF under which the
credential or pass was issued.
3.2. The value of the verifiable credential issuer ID is the issuer DID registered in the trust
registry identified by the trust registry DID.
3.3. The value of the verifiable credential type is a GHP credential type URI specified in the
GHP EGF. 
### Recommended Timelines
#### Phase One (30 Day Horizon)

GHP-compliant specific governing authorities:

1. SHOULD manually maintain a list of authorized issuers in a DID document using a did:web: URL
as specified GHP Trust Registry Protocol Specification.
1. SHOULD participate in development of the GHP Trust Registry Protocol Specification.
1. SHOULD publish their trust registry development plans.
#### Phase Two (90 Day Horizon)
GHP-compliant specific governing authorities:

1. SHOULD publish their trust registry policies and specifications in their specific EGF.
2. SHOULD have their trust registry implemented.
3. SHOULD pass a GHP-compliant trust registry protocol test suite.
4. SHOULD maintain a list of the trust registry DIDs of other GHP-compliant peer governing
authorities.
#### Phase Three (180 Day Horizon)
GHP-compliant specific governing authorities:
    1. MUST have implemented a GHP-compliant trust registry.
    2. MUST meet all requirements in their specific EGF. 

---
Sources:
1. <a target="_blank" href="assets/GHPC.Interoperability.Blueprint_v0.1.0_May.25.2021.pdf">GHPC Interoperability Blueprint - May 25 2021.pdf</a>


# REMOVED REQUIREMENTS
The following requirements were removed from the current requirement specification as they either are not clear or are relevant for future implementation.

## Unclear

## FUTURE

#TODO

* Authentication - 
  * Allow Options
  * Provide Guidance on some ideas (e.g. bearerAuth)
  * Registry
  * Allow for DID-informed architecture
  * 
* FUTURE:
  * Create DID Document linkage - endpoints, etc.
  * Create DIDComm exchange that allows equivalent to the main calls (CheckIssuer(), CheckVerifier(), GetOffLineFile()...)
  
* Recommended Service Endpoint - as defined in DID Document 
  * Lives at DID level so outside of the API and Spec (i.e. not prescriptive in current version) so those that want to can do this without requiring changes to the API.


  REGISTRY - if they participate with X.509 they use a SAN (Subject Alternative Name)
  - when an X.509 issues a VerCred, they MUST use SAN in it's "did:key:SAN" format... in the credential signing attribute (MORE DETAIL)


  ### Footnotes
  [^1]:[Good Health Pass Blueprint v1](TODO)
  [~2]:TODO-Link for X.509 spec.
  