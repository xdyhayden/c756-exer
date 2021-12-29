# Defining aliases for bash and Git

Use this directory to define aliases for bash and Git, by creating the following files:

* `bash_aliases`: A list of alias commands for bash.  Example:

   ~~~bash
   alias cpi="\cp -i"
   ~~~

* `gitconfig`: Configuration for Git. Includes your name, email, and any Git aliases. Note that
  some Git configuration parameters that you might have set in your host OS (Windows or macOS) may need to be
  set differently or not included at all in this file if they do not make sense in a
  Linux container.  For example, any `credential` entry should probably not be included in
  this file.  You will probably also want to use a different `core.editor` entry.

To define these aliases in your current shell, source the script `tools/profiles.sh`:

~~~bash
/home/k8s# . tools/profiles.sh
~~~

The '`.`' in the above statement is the shell `source` command.

You will have to source the script every time you start a container.