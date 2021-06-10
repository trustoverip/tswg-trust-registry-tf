#  Contributor's Guide
This document provides instructions for developing documentation and specifications using the **ToIP MkDocs Material Theme**.

## Audience
These instructions are pertinent to all ToIP contributors that seek to provide content towards the objective of this ToIP deliverable. Contributors may fall into one of the following categories:

| Role | Activities |
| --- | --- |
| Content Author | Use an editor of choice to write sections of the target deliverable using Markdown files as fragments of the ultimate deliverable document or specification. |
| GitHub skilled developer | Github savvy contributor that collects Markdown files from other contributors and manages commits and pull-requests as a representative of the team of  contributors/ |
| Both | Provider of content and manager of Github interactions. |

## Preparation

### Education

* [Markdown Tutorial](https://www.markdowntutorial.com/)
* Markdown Documentation
    * [Getting Started with Markdown](https://www.markdownguide.org/getting-started/)
    * [Markdown Basics](https://www.markdownguide.org/basic-syntax/)
    * [Mastering the Markdown Language](https://guides.github.com/features/mastering-markdown/)

### Authoring Tools

* Markdown Converters for Word Processors
    * MS-Word to Markdown
        * [Word-to-Markdown](https://word2md.com/)
        * [Writage](https://www.writage.com/)
        * [How to convert Word Docs to Markdown](https://medium.com/@ravinduk369/convert-a-ms-word-document-to-markdown-e0e99c41cfab)
    * Google Docs to Markdown
        * [G-Suite Plugins](https://gsuite.google.com/marketplace/app/docs_to_markdown/700168918607)
        * [How to convert Google Docs to Markdown](https://unslush.substack.com/p/how-to-convert-a-google-doc-to-markdown)
* Integrated development environment (IDE)
    * [Visual Studio](https://code.visualstudio.com/)
    * [Atom](https://atom.io)

## Setup Authoring Environment

If you are a _Content Author_ and **will not** work with `git` or do local testing of the content you are contributing, you can IGNORE these setup instructions. However, you will need to coordinate with a fellow contributor who will incorporate your work for you.

### Install Dependencies

| Required Software | MacOS Installation Instructions | Windows Installation Instructions |
| --- | --- | --- |
| Docker | [Docker Desktop][1]| [Docker Desktop][1]|
| `make` | Type `xcode-select --install` in a terminal window.|[Install Chocolatey Package Installer](https://chocolatey.org/install), then install [make via choco](https://chocolatey.org/packages/make)|
| `git` | Type `xcode-select --install` in a terminal window OR [Git Installer][2] | [Git Installer][2]|

  [1]: https://www.docker.com/products/docker-desktop
  [2]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Understanding Development Process
This repo leverages standard *pull-request* code collaboration processing. Contributors to this repo should create a `fork` and then use that `fork` as the `origin `for their `local machine` based development environment.

![remote-upstream](https://i.stack.imgur.com/cEJjT.png)

Learn more about [GitHub Forks](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

### Deployment
This repository contains a GitHub Action workflow that will automatically deploy your generated content when you commit your changes to:

```
https://trustoverip.github.io/<repository_name>
```

When you're forking this repository, you may need to activate GitHub Actions for your fork, as GitHub disables them by default. This is as easy as clicking on __Actions__ in the top bar of your repository and clicking the button that is shown. If no button is shown, you're good to go.

### Local Development Process
This repository uses simple `make` commands to manage the building and testing of content for this repo.

Open a Terminal Window and enter this command:

```
$ make
```

#### Prepare Development Environment

1. Clone repository

    ```
    cd <path>/<target_work_folder>
    git clone REPO_LINK
    git remote
    ```

2. Setup Environment
Now we will establish your upstream connections and build the necessary Docker containers for our development environment.

```
$ make setup
```

#### Develop content
_Optional_: You can skip these steps and jump to iterative development and testing.

1.  Launch the development environment

```
$ make devenv
$bash$
```

Your terminal prompt will now be within the docker container environment.

2. Iteratively develop documentation content by editing the markdown files and repeating the following command which will generate static HTML content and show any errors/warnings you may want to resolve.

```
$bash$ make dev
```

3. Exit the development environment (container)

```
$bash$ exit
$
```

#### Iterative development and testing
1.  Launch the development environment

```
$ make devenv
$bash$
```

Your terminal prompt will now be within the docker container environment.

2. Launch the Test Server

```
$bash$ make test
```

3. Iteratively develop documentation content by editing the markdown files. Each time you save a file, the test server will automatically refresh content for your review using your web browser pointed at: [localhost](localhoat:8800). See your `Makefile` for actual PORT number.

3. Exit the Develop and Test environment (container)

```
Enter <control-c> to halt the test server

$bash$ exit
$
```

#### Generate HTML and PDF Docs
This repo will combine all contributed content into a single Markdown file which is then used to produce standalone HTML and  PDF files. Internal scripts will preprocess and concatenate all Markdown files in the order specified in `mkdocs.yml`. The scripts will ensure that internal links to pages and anchors are correct.

1. Launch the Publish Environment

```
$ make pubenv
$bash$
```

Your terminal prompt will now be within the docker container environment.

2. Run the publishing process which will generate various versions of the contnet in the `./publish` folder.

```
$bash$ make publish
```

3. Exit the publishing environment (container)

```
Enter <control-c> to halt the test server

$bash$ exit
$
```

#### Commit Code
To complete the development process, follow normal **git commit** and **git push** processing. The ```.gitignore``` file will prevent the pushing of the static HTML content.

#### Resync with Upstream
Before each coding session, ensure your ```fork``` and ```local-machine``` are in sync with changes made to the ```upstream``` repo.

```
$ make rebase
```
