import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='prompt_loader',
    version='0.0.1',
    author='John Ballentine',
    author_email='johnballentine10@gmail.com',
    description='Loads OpenAI prompts from TXT files, including ChatCompletion prompts.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/johnballentine/prompt_loader',
    project_urls = {
        "Bug Tracker": "https://github.com/johnballentine/prompt_loader/issues"
    },
    license='MIT',
    packages=['prompt_loader'],
    setup_requires=['wheel'],
)