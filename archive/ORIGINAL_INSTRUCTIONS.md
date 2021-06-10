#  Trust over IP - Documentation and Specification Template
This repo is a [GitHub Repo Template][1] for creating GitHub repositories within the ToIP GitHub Organization. Newly generated repos will contain all the necessary code for using MkDocs for the development of [ToIP Deliverables][2].

The **ToIP MkDocs Material Theme** a ready-to-use setup for a ToIP branded version of [MkDocs][3], a static site generator geared towards (technical) project documentation and specification development. The theme is a customized version of [Material for MkDocs][4].

## Purpose
This repo has been developed to address the [requirements](./REQUIREMENTS.md) of [ToIP Foundation][5] contributors with respect to the [authoring process][6] for [ToIP Deliverables][2].

## Contributor's Guide
Once the new repo instance has been configured, Documentation and Specification contributors should familiarize themselves with the [Contributor's Guide](https://github.com/trustoverip/mkdocs-material/blob/main/DEV_README.md).

## Usage
The following instructions pertain to the initial configuration of a new repository instance that has been primed using [trustoverip/mkdocs-material GitHub Repo Template][12].

### Prime and clone a new repository
1. Generate a new repository from this template repository (see [GitHub docs][7]).
2. Clone the new repository (see [GitHub docs][8]).

### Pick a theme style
This repo supports the use of a *Specification* styled theme when the [ToIP Deliverable Type Indicator][9] is `TSS`. In all other cases, a *General Documentation* styled theme is provided.

1. Open the repository using your favorite IDE (i.e. [Visual Studio Code][10], [Atom][11]).
2. Apply your style selection

| Style | Configuration Action | View Demo |
| --- | --- | --- |
| _General Documentation_ | Move the `mkdocs.spec.yml` file, which is located at the root of the repo, to the `archive` folder. | [ToIP MkDocs Theme for Documentation](https://trustoverip.github.io/deliverables/)|
| _Specification_ | Move the `mkdocs.yml` file to the `archive` folder, and rename `mkdocs.spec.yml` to `mkdocs.yml`. | [ToIP MkDocs Theme for Specs](https://squidfunk.github.io/toip-demo-spec/)|

### Configure MkDocs

[MkDocs][3] uses a [YAML file][13] to configure the operational properties for the document generator.

1. Open the repository using your favorite IDE (i.e. [Visual Studio Code][10], [Atom][11]).
2. Edit the `mkdocs.yml` file and find the sections depicted below:

    ```
    # Project information
    site_name: Trust over IP – General Template
    site_url: https://trustoverip.github.io/mkdocs-material/
    site_author: Jane Doe
    site_description: >-
      Trust over IP Foundation template for general documentation
      and technical specification using Material for MkDocs

    # Repository information
    repo_name: trustoverip/mkdocs-material
    repo_url: https://github.com/trustoverip/mkdocs-material

    # Content Generator Settings
    docs_dir: 'content'
    site_dir: 'html'
    ```

3. Update the following settings:

    1. `site_name`: Set to ToIP Deliverables name using the naming convention `<TypeIndicator><4digitID>: <DeliverableName>`. For example,  _BP000: Utility Selection Criteria_.

    2. `site_url`: Set to the GitHub Pages URL that will serve up this new repo site.

    3. `site_author`: Set to the sponsoring ToIP WG. For example, _ToIP Governance Stack WG_.

    4. `site_description`: Set to a short description of the ToIP Deliverable being documented by this repo.

    5. `repo_name`: Set using name of the new GitHub repo.

    6. `repo_url`: Set using the URL of the new GitHub repo.

    7. `docs_dir`: Enter the preferred directory name for where the content for this document/spec will reside.

    8. `site_dir`: Enter the preferred directory name for where the static HTML pages will be generated from Markdown files.

    9. `extra.title`: Set to ToIP Deliverables name using the naming convention `<TypeIndicator><4digitID>: <DeliverableName>`. For example,  _BP000: Utility Selection Criteria_.

### Configure Makefile

1. Open the repository using your favorite IDE (i.e. [Visual Studio Code][10], [Atom][11]).
2. Edit the `Makefile` file and find the variables depicted below:

    ```
    REPO_NAME ?= mkdocs-material
    UPSTREAM_REPO ?= https://github.com/trustoverip/mkdocs-material.git
    DEV_IMAGE ?= trustoverip/mkdocs-material-devenv
    PANDOCS_IMAGE ?= trustoverip/pandocs-devenv
    DEV_SITE_PORT ?= 7500
    DEV_HOST_DIR ?= host_mkdocs
    PUB_HOST_DIR ?= host_pandocs
    PUBLISH_DIR ?= publish
    ```

3. Update the following settings:

    1. `REPO_NAME`: Provide the GitHub repository name.
    2. `UPSTREAM_REPO`: Set using the GitHub Repo Clone URL.
    3. `DEV_SITE_PORT`: Pick a port that will be used for the local test server: _https://localhost:8080_

### Update Readme
1. Open the repository using your favorite IDE (i.e. [Visual Studio Code][10], [Atom][11]).
2. Based on the type of deliverable that will be associated with this new repo, copy the appropriate `template` from the [templates folder within the trustoverip/deliverables repo][15] to `./archive/SUGGESTED_OUTLINE.md`.
3. Move `README.md` to the `archive` folder. Rename it to `ORIGINAL_INSTRUCTIONS.md`.
4. Rename `DOC_README.md` to `README.md`
5. Update `README.md` accordingly.

    1. At the top of your file modify the _title_ so it is in the form:

        ```
        <TypeIndicator><4digitID>: Friendly Version of Your Title.
        ```

    2. Refer to the _Contribution Options_ of the [ToIP Deliverables Portal][14].


[1]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-template-repository
[2]: https://github.com/trustoverip/deliverables/blob/master/_process/work_products.md
[3]: https://www.mkdocs.org/
[4]: https://squidfunk.github.io/mkdocs-material/
[5]: https://trustoverip.org
[6]: https://trustoverip.github.io/deliverables/process/process_concepts/
[7]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template
[8]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[9]: https://trustoverip.github.io/deliverables/process/work_product_mgmt/#type-indicators
[10]: https://code.visualstudio.com/
[11]: https://atom.io
[12]: https://github.com/trustoverip/mkdocs-material
[13]: https://en.wikipedia.org/wiki/YAML#:~:text=yaml.org,is%20being%20stored%20or%20transmitted.
[14]: https://trustoverip.github.io/deliverables/
[15]: https://github.com/trustoverip/deliverables/tree/master/templates
