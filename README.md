# ToIP  TSS0001>: Trust Registry Specification
- Authors: [Michael Boyd](mailto:michael@trinsic.id)
- Status: [PROPOSED](https://trustoverip.github.io/deliverables/process/lifecycle_management/#proposed)
- Since: YYYY-MM-DD (date you submit your PR)
- Status Note: (explanation of current status)  
- Supersedes: (link to anything this ToIP Deliverable  supersedes)
- Start Date: YYYY-MM-DD (date you started working on this idea)
- Tags: (see [Tag Options](https://trustoverip.github.io/deliverables/process/tags)

## Summary

In most real-world credential exchange scenarios, a credential holder or verifier has the question “How do I know the issuer of this credential is trustworthy?”

Credential holders may also be uneasy about sharing information with a verifier if trust in the verifier has not been established.

These problems can be solved by having a trusted third party vouch for the trustworthiness of a credential exchange participant.

A trust registry is a list of authorized issuers and verifiers in the ecosystem and the types of credentials and passes they are authorized to issue and verify.
## Purpose
This repo manages the development and maintenance of the subject ToIP deliverable. It contains the tools necessary to generate multiple renderings formats.

1. Interactive Online Website: [GitHub Pages](https://<ORG_NAME>.github.io/<REPO_NAME>/)
2. Printable Documents
    * [PDF Version](./publish/<DOC_NAME>.pdf)
    * [HTML Version](./publish/<DOC_NAME>.html)
    * [Standalone Markdown](./publish/<DOC_NAME>.md)

## Contributor's Guide
Documentation and Specification contributors should familiarize themselves with the [Authoring Process](https://github.com/trustoverip/trust-registry-spec/blob/main/DEV_README.md). <-- TODO: fix broken link with right repo name once contributed

## Build and Deploy
Local running instructions:
```
pip install -r requirements.txt
mkdocs serve
```

Local deploy instructions:
```
mkdocs gh-deploy --site-dir html
```
_//todo: make github actions and get docker working..._
## Related Resources

1. [ToIP Deliverables Portal - Status](https://trustoverip.github.io/deliverables/results/proposed/)
2. [ToIP Contributor's Workflow](https://trustoverip.github.io/deliverables/process/process_concepts/)


## License

Copyright mode: 
* Creative Commons Attribution 4.0. 
* Patent mode: W3C Mode (based on the W3C Patent Policy).
* Source code: Apache 2.0, available at http://www.apache.org/licenses/LICENSE-2.0.html. The Trust Registry TF is not expected to produce source code beyond a Swagger API specification.
