#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module Docstring"""

pbs_script_template_filename = "template_pbs_script.sh"
config_file_template_filename = "template_config_file.txt"

f = file(pbs_script_template_filename)
# O único parâmetro no template é o nome do arquivo de configuração
pbs_script_template = f.read()
f.close()

f = file(config_file_template_filename)
# Os parâmetros no template são: Nt, Ns, K
config_file_template = f.read()
f.close()


# Variaveis xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Nt = 2
Ns = 1
# Serão gerados um script e um arquivo de configuraçao para cada valor de K
K = range(8, 65, 4)
#K = [8]
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


script_names = ""

for k in K:
    pbs_script_filename = "FP_{0}_G{1}{2}.sh".format(k, Nt, Ns)
    config_file_name = "FP_{0}_G{1}{2}_config.txt".format(k, Nt, Ns)
    script = file(pbs_script_filename, 'w')
    config = file(config_file_name, 'w')
    script.write(pbs_script_template.format(config_file_name))
    config.write(config_file_template.format(k, Nt, Ns))
    script.close()
    config.close()
    print('Script "{0}" criado'.format(pbs_script_filename))
    print('Arquivo de configuração "{0}" criado'.format(config_file_name))

    script_names = script_names + pbs_script_filename + "\n"


script_names_file = file("all_script_names.txt", 'w')
script_names_file.write(script_names)
script_names_file.close()
