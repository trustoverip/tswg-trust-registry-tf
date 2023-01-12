## Requirements

### Workflow
ToIP contributors should be able to:
1. Gather: Define, Organize and Assign work towards the development of a ToIP Deliverable based on project outline that aggregates a collection of discrete Markdown files.
2. Author: Use any Markdown editor they desire.
3. Produce: Configure the generation of one or two possible deliverables: General Document, Specification.

### Styling
1. Apply a Material style Theme that is ToIP specific
2. Leverage a Color pallet derives from the [ToIP Logo Assets](https://github.com/trustoverip/logo-assets).
3. Provide configurable navigator with numeric outlines level 1-3: See [Spec-Up](https://identity.foundation/sidetree/spec/) as an example style for the development of specifications.
4. Build upon the Material Theme (not insiders) with Search Suggest and/or Highlight - void of Insider Token requirements.
5. One ToIP Theme with config option for header generated numbering (with or without).

### Versioning
ToIP members should be able to prime to repos using this repo as a GitHub Template Repository.

### Development and Processing
1. Command line tools (make) for generating local test content.
2. Github workflow (actions) for producing GitHub-Pages
3. Layout (outline / organize) multiple markdown files (i.e.: mkdocs.yml)

### Rendering Formats
Minimally, this repo MUST allow for the configuration of generating these rendering formats:
1. Single Markdown file (via pandoc or other plugins)
2. Single PDF (via pdf-export or other plugins)
3. Website/GitHub-Pages
