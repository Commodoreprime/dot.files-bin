#!/bin/bash

helpfile() {
    printf "dotfiles [deploy -d|--domain DOMAIN | add file1 fileN ... | remove file1 fileN ...]

Manage dotfiles in a literal but still flexible manner

Commands:
    deploy  Symlink, hardlink, or copy files from under a domain to under the real path
        -d|--domain DOMAIN      Specify a domain to copy one or multiple files under to
    add     Copy files to a domain
    remove  Remove files from a domain
options:
    
--domain is required for deploy but not nessisarily required for add or remove
\n"
}

case "$1" in
    -d|--deploy) shift 2
    python3 .bin/manage ;;
    *) helpfile ;;
esac
