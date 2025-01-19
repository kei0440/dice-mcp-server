from setuptools import setup, find_packages

setup(
    name="dice-mcp-server",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "dice-mcp-server = dice_mcp_server:roll_dice",
        ],
    },
    author="kei",
    author_email="k.kalapawai@gmail.com",
    description="A simple MCP server for rolling a 6-sided dice.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kei0440/dice-mcp-server",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
