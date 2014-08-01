pbs-script-generator
====================

Create PBS scripts from a template.

The idea is to run the `create_scripts.py` file, which will read the two
template files and generate several scripts and configuration files.

Furthermore, `create_scripts.py` also creates a file called
all_script_names.txt with the name of the generated scripts. You can use
the `simulate_all.sh` script to read this txt file and call `qsub` on each
name in the txt file.
