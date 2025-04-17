import os

# Define the project root directory
root_dir = 'app'

# Define the subdirectories and files for each module
modules = {
    'templates': ['index.html', 'raw_material.html', 'production_device.html', 'complementary_product.html', 'main_product.html', 'settings.html'],
    'static': ['css/', 'js/']
}

# Define the root files
root_files = ['__init__.py', 'routes.py', 'models.py', 'forms.py', 'utils.py', 'config.py']

# Create the root directory if it doesn't exist
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

# Change to the root directory
os.chdir(root_dir)

# Create each subdirectory and its files
for module, files in modules.items():
    # Create the module directory if it doesn't exist
    if not os.path.exists(module):
        os.mkdir(module)

    # Change to the module directory
    os.chdir(module)

    # Create each file or directory in the module
    for file in files:
        if '/' in file:  # If it's a directory, create it
            os.mkdir(file)
        else:  # If it's a file, create an empty one
            open(file, 'w').close()

    # Go back to the root directory
    os.chdir('..')

# Create each root file
for file in root_files:
    open(file, 'w').close()
