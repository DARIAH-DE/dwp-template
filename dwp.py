#!/usr/bin/env python3

from os import fspath

import shutil
from subprocess import run
from pathlib import Path
from shutil import which
import shlex
import re
import sys


def run_pandoc(file: Path | str, args: list[str]) -> int:
    file = Path(file)
    argnames = [arg.split("=")[0] for arg in args]
    pandoc = which("pandoc") or "pandoc"
    args = [pandoc] + args

    markdown_file = file if file.suffix == ".md" else file.with_suffix(".md")
    if file != markdown_file and file.exists():
        # Passing, e.g., a docx starts a conversion unless the markdown already exists
        if not markdown_file.exists():
            print(
                f"{markdown_file} does not exist, trying to create it from {file} ..."
            )
            cmd = [
                pandoc,
                "-t",
                "markdown",
                "-o",
                fspath(markdown_file),
                "--extract-media=.",
                fspath(file),
            ]
            print(shlex.join(cmd))
            result = run(cmd)
            if not markdown_file.exists():
                print(f"Could not create markdown source {markdown_file}")
                return result.returncode or 127

    if not markdown_file.exists():
        print(f"Markdown source {markdown_file} not found.")
        return 127

    pdf_file = markdown_file.with_suffix(".pdf")

    if "-o" not in argnames and "--output" not in argnames:
        args.extend(["-o", fspath(pdf_file)])
    if "--pdf-engine" not in argnames:
        args.append("--pdf-engine=lualatex")
    if "--template" not in argnames:
        args.append("--template=DWP")

    args.append("--citeproc")
    bibfile = markdown_file.with_suffix(".bib")
    if bibfile.exists():
        args.append("--bibliography=" + fspath(bibfile))
    if "--csl" not in argnames:
        if langtag := re.search(r"^lang:\s*(\w+)\s*$", markdown_file.read_text(), re.M):
            if langtag.group(1) == "de":
                args.append("--csl=chicago-author-date-de.csl")
            else:
                args.append("--csl=chicago-author-date.csl")
        else:
            print(
                "Warning: Document language unknown, use a header field like 'lang: en'"
            )
            args.append("--csl=chicago-author-date.csl")
    args.append("--metadata=link-citations:true")
    if "-v" in argnames:
        args.remove("-v")
        args.append("--verbose")
    debug = False
    if "-D" in args:
        args.remove("-D")
        debug = True
    if "--debug" in args:
        args.remove("--debug")
        debug = True

    args.append(fspath(markdown_file))

    print(shlex.join(args))
    result = run(args)
    if result.returncode != 0:
        print(f"pandoc failed with exit code {result.returncode}.")
        tex_file = markdown_file.with_suffix(".tex")
        if debug:
            if "-o" in args:
                args[args.index("-o") + 1] = fspath(tex_file)
            elif "--output" in argnames:
                args[argnames.index("--output") + 1] = "--output=" + fspath(tex_file)
            print(f"Running {shlex.join(args)} to generate {tex_file} ...")
            run(args)
            if tex_file.exists():
                cmdline = [shutil.which("lualatex"), fspath(tex_file)]
                print(f"Running {shlex.join(cmdline)} to debug LaTeX execution ...")
                run(cmdline)
            else:
                print("No tex file created.")
        else:
            print(
                f"""
                  To debug, you can add the option -D or --debug somewhere before the 
                  markdown file name. This will create the tex file and run lualatex
                  manually, so you get all intermediate files in the current directory.
                  It's your responsibility to delete them later ...

                  Alternatively, use -o "{tex_file}" to create only a tex file.
                  """
            )
    else:
        if pdf_file.exists():
            print(f"PDF file {fspath(pdf_file)} has been created.")
    return result.returncode


def usage(msg: str = ""):
    if msg:
        print(msg)
    print(f"Usage: {sys.argv[0]} [--debug] [-v] [pandoc-options] input-file")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    input_file = Path(sys.argv[-1])
    if not input_file.exists():
        usage(f"Input file {input_file} not found")

    sys.exit(run_pandoc(input_file, sys.argv[1:-1]))
