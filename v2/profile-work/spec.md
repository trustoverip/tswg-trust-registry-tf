## Discovery: Additional Service Discovery Using Profile Definitions on a DID Document

**Specification Status:** Pre-Draft 0.0.1  
**Latest Draft**:   
**Previous Draft:**  

### Editors

// TODO: figure this out.

### Contributors

// TODO

### Introduction

This specification outlines the structure and requirements for enabling
additional service discovery through profile definitions within a Decentralized
Identifier (DID) document. By integrating service endpoints and profile
information, this approach enhances the capabilities of DIDs for decentralized
and self-sovereign identity systems. Some of the possible advantages include: 

- service and profile crawlers become possible, enabling better service
discovery and interoperability across services. 
- better descriptive power for individual services
- composibility of capabilities for succinct representation of capabilities.

### Objective

The purpose of this specification is to enhance the ability for an endpoint
system and user to discover capabilities of a service within a decentralized
context. Developed within the Trust Registry Task Force at Trust Over IP, this
spec offers a straightforward yet effective discovery layer for both legacy and
new trust registry services. The intended audience includes individuals or
entities seeking to improve service interoperability with their existing services or on new services.

### Service Endpoint Profile Specification

The data structure outlined in this specification is designed to establish a
consistent approach for integrating service endpoint profiles within a DID
document. Adherence to the subsequent guidelines is mandatory:

- It is imperative that this structure takes the form of a singular struct.
- The ensuing properties are obligatory:
  - `uri`: A URI attribute delineating the interaction's endpoint address.
  - A choice between the ensuing options:
    - `profile`: A JSON Profile document that can be resolved through HTTPS. Further requisites are detailed in the "Profile Document" section.
    - `definition`: If provided, this signifies the resolvable URI attribute
      enmeshed within the DID document. The corresponding definition is required to comply with the specifications delineated in the subsequent profile document section.

An array of structs is not valid.

**Example**

This following is an portion from the DID Document. 

```json
{
  "@context":[
      "https://www.w3.org/ns/did/v1",
      "https://trustoverip.org/profile/v2"
  ],
  ...
  "service": [{
    "id": "did:example:123#trust-registry",
    "type": "TrustRegistry", 
    "serviceEndpoint": {
        "profile": "https://trustoverip.org/profiles/trp/v2",
        "uri": "https://my-tr-service/"
    }
  }]
}
```

#### JSON Schema for Service Endpoint Struct

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "uri": {
      "type": "string",
      "format": "uri"
    },
    "profile": {
      "type": "string",
      "format": "uri"
    },
    "definition": {
      "type": "string",
      "format": "uri"
    }
  },
  "required": ["uri"],
  "anyOf": [
    { "required": ["profile"], "not": { "required": ["definition"] } },
    { "required": ["definition"], "not": { "required": ["profile"] } }
  ],
  "additionalProperties": false
}
```
    
### Profile Document Specification

#### Profile Data Model

The profile data model is heavily inspired by the VC Data Model.

In this section, we delve into the intricacies of the profile data payload
structure, designed to encapsulate essential information within a decentralized
context. The structured data adheres to a comprehensive schema, ensuring
consistency and coherence in the representation of profiles associated with
Decentralized Identifiers (DIDs). By adhering to this structure, service
endpoint profiles can integrate with DID documents, fostering
enhanced service discovery and interaction.

The profile data payload is composed of three primary components, each serving a distinct purpose:

**Metadata:** This segment provides overarching details about the profile, offering
insight into its origins, content, and context. Key attributes encompass the
decentralized identifier (DID), profile type, creation timestamp, media type,
version, and descriptive elements that collectively contribute to the profile's
identity and purpose.

**Service Descriptors:** Here, we will define the capabilities or services linked to the profile
data, but is not included in this version. By specifying the functionalities that the profile embodies, this section
clarifies the utility and scope of the profile within the DID ecosystem. 

**Proof:** This component encapsulates information related to the authentication and integrity verification of the profile data. Various properties, including the proof type, creation timestamp, proof value, and verification method, work in
concert to substantiate the authenticity of the profile's content and source.

Throughout this section, we dissect the schema-driven structure of the profile
data payload, elucidating its constituent elements and their roles in enabling
robust, secure, and standardized profile integration within the realm of
Decentralized Identifiers. By comprehending the nuances of this payload format,
stakeholders can harness the power of interoperable profiles to facilitate
seamless interactions and enriched service discovery experiences.

**Profile Document Data Model**
```mermaid
graph LR
    subgraph Profile Document
        Metadata[Metadata]
        Descriptors[Service Descriptors]
        Proofs[Proofs]
    end
```

#### Profile Data Model Specification 

A profile data model is a document with the following properties:

* The document **MUST** have a `metadata` object with the following properties:
    * The `id` property **MUST** be present and **MUST** be a DID. 
    * The document**MUST** have a `type` property and the the value of the `type` property **MUST** be, or map to (through interpretation of the @context property), one or more URIs. If more than one URI is provided, the URIs MUST be interpreted as an unordered set. It is RECOMMENDED that each URI in the type be one which, if dereferenced, results in a document containing machine-readable information about the type.
    * The document **MUST** contain a `profileType` property. If present, is a string indicating the specific type or category of the profile. This property can help categorize and classify the profile data further.
    * The document MAY contain a `checksum` property. If present, holds a string value representing a checksum. This checksum can be used to verify the integrity of the profile data, ensuring that it has not been tampered with.
    * The document MAY contain a `created` property, which is an ISO-8601 timestamp indicating the date and time when the profile data was created or initially recorded.
    * The document MAY contain a `mediaType` property, if present, indicates the media type of the content within the profile. This property can specify the format or structure of the profile data content.
    * The document MAY contain a `name` property, if provided, is a human-readable name assigned to the profile. It offers a recognizable label for the profile data.
    * The document MAY contain a `previous` property. If included, refers to a previous CID of the profile data. This reference can facilitate tracking changes and updates to the profile.
    * The document MAY contain a `description` property. if given, offers a detailed textual description of the profile. This description can provide insights into the purpose, content, and usage of the profile data.
    * The document MAY contain a `short_description` property. If available, provides a succinct summary or brief overview of the profile. This summary can be useful for quick references.
    * The document MAY contain a `validity_period` property. When present, contains a combined date-time string representing the period during which the profile data is considered valid. This property helps manage the temporal validity of the data.
    * The document MAY contain a `docs_url` property, if supplied, is a URL pointing to documentation related to the profile data. This URL can lead to additional resources or information about the profile.
    * The document MAY contain a `version` property. If given, holds a string indicating the version of the profile data. This version should follow the semantic versioning (semver) format for version numbering.
    * The document MAY contain a `tags` property. If present, is an array of strings that serve as tags associated with the profile data. These tags can aid in searchability and categorization of the profile. This is useful for indexers. 
      
#### JSON Schema

The Profile Document provides a comprehensive framework for capturing profile-related information within the DID document.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "The decentralized identifier representing the profile in the DID format."
        },
        "profileType": {
          "type": "string",
          "description": "A string indicating the type of the profile."
        },
        "checksum": {
          "type": "string",
          "description": "A checksum value for data integrity validation."
        },
        "created": {
          "type": "string",
          "description": "Timestamp indicating profile creation date."
        },
        "mediaType": {
          "type": "string",
          "description": "The media type of the profile content."
        }, 
        "name": {
          "type": "string",
          "description": "A human-readable name for the profile."
        },
        "previous": {
          "type": "string",
          "description": "Reference to a previous version of the profile data."
        },
        "description": {
          "type": "string",
          "description": "A detailed description of the profile."
        },
        "short_description": {
          "type": "string",
          "description": "A concise description of the profile."
        },
        "validity_period": {
          "type": "string",
          "format": "date-time",
          "description": "Combined date-time string indicating the validity period."
        },
        "docs_url": {
          "type": "string",
          "format": "uri",
          "description": "URL to documentation for the profile data."
        },
        "version": {
          "type": "string",
          "description": "The version of the profile data, following semver."
        },
        "tags": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Tags associated with the profile data."
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": true
    },
    "definitions": {
      "type": "object",
      "description": "Defines capabilities or services related to the profile data."
    },
    "proof": {
      "type": "object",
      "description": "Information related to proofing the authenticity of the profile data."
      // Additional properties related to proofing can be added here.
    }
  },
  "required": ["metadata"],
  "additionalProperties": false
}
```

#### Profile Document Sample 

The following describes a sample profile document.

```json
{
  "metadata": {
    "id": "did:example:123456",
    "profileType": "TrustRegistry",
    "checksum": "abcdef123456",
    "created": "2023-08-18T12:34:56Z",
    "mediaType": "application/json",
    "description": "An RestfulAPI that describes how an ecosystem based on trust can query and interact with a service to perform a query agasint a trusted regsitry.",
    "short_description": "The open standard trust task protocol defined by the ToIP Foundation to perform the trust task of querying a trust registry.",
    "validity_period": {
        "start": "2023-08-18T12:34:56Z",
        "end" : "2024-08-18T12:34:56Z"
    },
    "docs_url": "https://trustoverip.org/trustregistryprotocol",
    "version": "2.0.0",
    "tags": ["toip", "trustregistryprotocol"]
  },
  "proof": {
    "type": "Ed25519Signature",
    "created": "2023-08-18T12:34:56Z",
    "proofValue": "abcdefg123456",
    "verificationMethod": "did:example:123456#key1"
  }
}
```

