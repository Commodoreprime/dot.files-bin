# dot.files - structure

This file explains the architecture of the project and how its """intended""" to work

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
      "real_dir": "<directory or bash variable>"
    }
  }
  ```

  - domain name: The name is case sensitive and points to a directory which is on the same level as meta.json
    - real\_dir: This points to a real directory when deploying or syncing

