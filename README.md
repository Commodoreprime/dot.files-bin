# dot.files - the programs

This repository contains management software and information for managing dotfiles.

## Implementation

Three ways of using this is either to 1) clone this repository on its own and use the tools, 2) clone as a [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to a preexisting dotfile repository as a directory named .bin or something, or 3) Fork and drop dotfiles in the same fork, if you go this way, it is recommended to move the files here into a directory named `.bin` but you do you.
# structure

This file explains the architecture of the project and how its intended to work

## Directory tree design

The goal of the directory structure is to be as literal in file location as possible while still retaining flexiblity.

For example a file located at `~/.local/bin/text2speech` would be mirrored under the home domain as `home/.local/bin/text2speech`.

Any directory in the root of this repository starting with a `.` is ignored.

## Key files

- meta.json
  This is a file that lists metadata information in a json format.

  Format:
  ```json
  {
    "<domain name>": {
      "real_dir": "<directory and/or bash variables>"
    }
  }
  ```

  - domain name: The name is case sensitive and points to a directory which is on the same level as meta.json
    - real\_dir: This points to a real directory when deploying, adding, or removing.
