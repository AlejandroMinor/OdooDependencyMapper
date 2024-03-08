import os
import ast
def create_list_of_paths_with_manifest(main_path):
    paths_list = []
    for root, _, files in os.walk(main_path):
        for file in files:
            if file == '__manifest__.py':
                paths_list.append(root)
    return paths_list

def read_manifest(manifest_path):
    with open(manifest_path, 'r') as manifest_file:
        manifest_content = manifest_file.read()
    manifest = ast.literal_eval(manifest_content)
    return manifest

def create_md_file(project_path, output_path):
    paths_list = create_list_of_paths_with_manifest(project_path)
    for record in paths_list:
        manifest = read_manifest(record + '/__manifest__.py')
        module_name = os.path.basename(record)
        dependencies = manifest.get('depends', [])
        with open(f'{output_path}/{module_name}.md', 'w') as md_file:
            md_file.write(f'# {module_name}\n\n')
            md_file.write('Dependencies:\n\n')
            for dependency in dependencies:
                md_file.write(f'- [{dependency}](./{dependency}.md)\n')

main_path = '/home/minor/Odoo_Custom_Modules'
output_path = '/home/minor/Dependencias'
create_md_file(main_path, output_path)


