# :crocodile: Developing a Programming Language, CMPSC 201 Fall 2020: LAB 02 Assignment

## DUE: September 29th by 3:00pm

[![Actions Status](../../workflows/build/badge.svg)](../../actions)

## Table of Contents

* [Summary](#summary)

* [Objectives](#objectives)

* [Reading Assignment](#reading-assignment)

* [Accessing the Repository](#accessing-the-repository)

* [Creating a Programming Language](#creating-a-programming-language)

  * [Tasks](#tasks)

  * [Grammar](#grammar)

  * [Scanner](#scanner)

  * [Parser](#parser)

  * [Test Cases](#test-cases)

* [Running and Testing](#running-and-testing)

  * [Docker](#docker)

  * [GatorGrader](#gatorgrader)

  * [GitHub Actions CI](#github-actions-ci)

* [Evaluation](#evaluation)

* [Problems](problems)

## Summary

Designed for use with [GitHub Classroom](https://classroom.github.com/), this
repository contains starter materials for lab 02 in [Computer Science 201 Fall
2020](https://cs.allegheny.edu/sites/jjumadinova/teaching/201). The lab02
assignment invites teams of two or three to design a simple programming language
and to implement a lexical analyzer and a parser for the specified language.

Please watch a video introducing this lab assignment under the course's YouTube
playlist:
[Lab 02 Assignment Introduction](https://www.youtube.complaylist?list=PLz9YRLfRGO9JpJfVknMPnK_jagA0mgxN0)

## Objectives

* To design a grammar for a simplistic language.

* To learn how to implement a lexer and a parser using appropriate tools.

* To develop deeper understanding of the language design and compilation phases.

## Reading Assignment

To understand the concepts covered in this assignment, you should read Chapters 1
and 2 of the "Programming Language Pragmatics" textbook. You should also
study the program developed as a part of class activity 3, examine
example programs provided in this lab02 starter repository, and study
the documentation of [SLY](https://sly.readthedocs.io/en/latest/) and the
examples provided in
[SLY GitHub Repository](https://github.com/dabeaz/sly/tree/master/example).

If you have not done so already, please read all of the relevant
[GitHub Guides](https://guides.github.com/) that explain how to use
many of the features
that GitHub provides. In  particular,  please  make  sure  that  you  have  read
guides  such  as  "Understanding the GitHub flow", "Mastering  Markdown"
and "Documenting Your Projects on GitHub";
each of them will help you to understand how to use both GitHub and GitHub Classroom.
Each team is expected to use branching and appropriate GitHub flow processes as
the work on the lab progresses.

## Accessing the Repository

For this assignment, we will be using a group assignment functionality of
GitHub Classroom. For group assignments only one person will be creating the
team on GitHub Classroom while the other
team members will join that team. Please form a team consisting of two or three
members, assign one person to be the designated team manager.

The selected team manager should go into the #labs channel in our Slack team and
find the announcement that provides a link for it. Copy this link and paste it
into your web browser. Now, you should accept the laboratory assignment and
create a new team with a unique and descriptive team name
(under "Or Create a new team").
Now the other members of the team can click on the assignment link in the #labs
channel and select their team from the list under "Join an Existing Team".
When other team members join their group in GitHub Classroom, a team is created
in our GitHub organization. Teams have pretty cool functionality, including
threaded comments and emoji support. Every team member will be able to push
and pull to their team’s repository.

## Team Work

Each member of the class will be arranged into a team at the beginning
of the lab session. Class members are invited to select their own teams consisting
of two or three individuals.

Your team should use GitHub and its features (e.g., issue tracker, pull requests,
commit log, and code review request) to complete all of the tasks referenced in
the previous section.  Since  multiple  approaches  may  support
the  effective  completion  of  the required  documents, this assignment
does not dictate team organization or communication strategies. Each team is
expected to follow the [Code of Conduct](https://github.com/allegheny-computer-science-201-f2020/lab01-cs201f2020/blob/main/conduct.md)
the class members developed for this course.

## Creating a Programming Language

For this laboratory assignment,  your  task  is to design a specification
for a very simple toy programming language and implement a scanner and a parser
for this language.
You are encouraged to be creative in your design of a language, however it
should satisfy the certain minimal requirements outlined below.

### Grammar

Once you have an idea for the type of a language to construct, the
first step should be to define its grammar. Please construct grammar rules
in a BNF format that generate your language in the appropriate section of
the `report.md` file.

Your grammar should be a CFG grammar that starts with a start terminal and
provides rules for things such statements, expressions, and derivations of
all non-terminals.

### Scanner

After you identified the features that your source language will support through
the design of its grammar, you should implement a scanner to produce a token
stream for your language. You can use [SLY](https://github.com/dabeaz/sly)
to make the implementation of the
scanner easier, or alternatively, you can also use its predecessor
[PLY](https://www.dabeaz.com/ply/). Your scanner will transform the source
file into a series of meaningful tokens containing information that will be
used by the parser. You should begin by making a list of all items your
scanner needs to handle based on the features of your source language.

At the minimum, your scanner should support the following:

* skip over white space (if appropriate for your source language),
* recognize all keywords and return the correct token,
* recognize literals and return the correct token,
* recognize identifiers and return the correct token,
* recognize at least three data types (for example, int, float and a String),
* recognize at least one conditional statement,
* recognize new lines,
* recognize comments,
* report lexical errors for invalid characters and any other improper lexical notations you are able to catch at this point.

It is recommended that you add token types one at a time and test after each addition.
For any items that are not explicitly defined in your source language
documentation, you can make any assumptions as appropriate.

### Parser

Once you are able to generate a token stream for various inputs appropriate for
your language, you will expand the front-end of your compiler by implementing
a parser for it. Please note that at this stage it is likely that you will need
to expand and/or modify parts of your scanner to get your parsing to work
correctly - this is okay and expected!
Any conflicts can be resolved in a multitude of ways (rewriting the productions,
setting precedence, etc.) and you are free to take whatever approach appeals to
you. All you need to ensure is that you end up with a grammar that is free of
conflicts and errors.

To implement a parser you need to add the rules for each of your language's
grammar features. Remember that syntax analysis is only responsible for
verifying that the sequence of tokens forms a valid sentence given the
definition of the grammar. Given that some
grammars can be somewhat loose, some apparently nonsensical constructions will
parse correctly since you are not doing any of the work for verify semantic
validity (type checking, declare before use, etc.).

### Test Cases

To ensure that your scanner and your parser operate correctly, you are to
create at least ten input examples to use in testing. These inputs should contain
Strings that represent different combinations of what your language allows
and should contain an equal number of inputs that run without errors and those
that produce some lexical and parsing errors.
The output from the input test cases can be printed to the terminal or to
the file.

## Running and Testing

### Docker

To run your Python program using Docker Desktop, you need to first create a
Docker image and then create and run the Docker container, using the following
two commands, which are appropriate for your operating system.

*Mac/Linux:*

`docker build -t sly .`

`docker run --rm -v $(pwd)/src:/root sly python3 lab02.py`

*Windows:*

`docker build -t sly .`

`docker run --rm -v "%cd%/src":/root sly python3 lab02.py`

### GatorGrader

To assess the minimum completeness of the lab submission materials,
you can use the GatorGrader tool.
Once you have installed [Docker
Desktop](https://www.docker.com/products/docker-desktop), you can use the
following `docker run` command to start `gradle grade` as a containerized
application, using the [DockaGator](https://github.com/GatorEducator/dockagator)
Docker image available on
[DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

```bash
docker run --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator
```

This command will use `"$(pwd)"` (i.e., the current directory) as
the project directory and `"$HOME/.dockagator"` as the cached GatorGrader
directory. Please note that both of these directories must exist, although only
the project directory must contain something. Generally, the project directory
should contain the source code and technical writing of this assignment, as
provided to a student through GitHub. Additionally, the cache directory should
not contain anything other than directories and programs created by DockaGator,
thus ensuring that they are not otherwise overwritten during the completion of
the assignment. To ensure that the previous command will work correctly, you
should create the cache directory by running the command `mkdir
$HOME/.dockagator`. If the above `docker run` command does not work correctly on
the Windows operating system, you may need to instead run the following command
to work around limitations in the terminal window:

```bash
docker run --rm --name dockagator \
  -v "$(pwd):/project" \
  -v "$HOME/.dockagator:/root/.local/share" \
  gatoreducator/dockagator
```

Since the above `docker run` command uses a Docker images that, by default, runs
`gradle grade` and then exits the Docker container, you may want to instead run
the following command so that you enter an "interactive terminal" that will
allow you to repeatedly run commands within the Docker container.

```bash
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

Once you have typed this command, you can use the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) in the Docker container by
typing the command `gradle grade` in your terminal. Running this command will
produce a lot of output that you should carefully inspect. If GatorGrader's
output shows that there are no mistakes in the assignment, then your source code
and writing are passing all of the automated baseline checks. However, if the
output indicates that there are mistakes, then you will need to understand what
they are and then try to fix them.

Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker container stop ID`: stop the running container with specified ID
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

### GitHub Actions CI

GitHub Actions CI is configured to check the Markdown files in
the repository with "mdl".  If your program and the writing meets the
minimal established requirements, then you will see a green :heavy_check_mark:
in the listing of
commits in GitHub.  If your submission does not meet the requirements,
a red :heavy_multiplication_x: will appear instead.  Since this assignment
contains a large creative and open-ended portion, the majority of your lab grade
will be based on the satisfaction of the requirements outlined in the previous
sections.

## Evaluation

The grade that a student receives on this assignment will have the following
components. In addition
to these three main components, student's grade may be affected by their
adherence or the lack of adherence to the[Code of Conduct](https://github.com/allegheny-computer-science-201-f2020/lab01-cs201f2020/blob/main/conduct.md) developed for this course.

* Percentage  of  Correct  GatorGrader  Checks  and  GitHub Actions  CI  Build Status [up  to 15%]: Students are encouraged to repeatedly revise their submission to ensure that it passes all of GatorGrader's checks and receives a CI pass.

* Mastery of Technical Writing [up to 15%]:  Students will also receive a portion of the lab grade when the responses to the technical writing questions presented in the 'writing/report.md' reveal a mastery of both writing skills and conceptual and technical knowledge.  To receive this portion of the grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

* Mastery  of  Technical  Knowledge  and  Skills  [up  to  70%]: Students will  receive  a largest portion of their assignment grade when their project implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this project.  As a part of this grade, the instructor will assess aspects of the project including, but not limited to,
the designed grammar, correctness of the scanner and the parser, the completeness and correctness of the test cases, and the use of effective source code comments, and Git commit messages.

## Problems

If you have any problems with this assignment, then please create an issue
in this repository using the "Issues" link at the top of this site.
