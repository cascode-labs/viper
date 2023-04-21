help:
	@echo ""
	@echo "Build a IDS package or install IDS for development"
	@echo ""
	@echo "Build Packages"
	@echo "  'make Build' will build both a wheel and sdist"
	@echo "Install"
	@echo "  'make install-dev' will install a conda development environment"
	@echo "Build documentation"
	@echo "  'make auto-docs' will continuosly rebuild the docs"
	@echo "     as they are updated"
	@echo "  'make docs' will build the documentation once"
	@echo "Other tasks"
	@echo "  'make clean' will clean up the work area"
	@echo ""

.PHONY: help clean \
		build publish \
		docs  \
		install-dev all

install-dev:
	mamba env create -f environment.yml
	conda activate viper-dev
	pip install --no-deps -e .

clean:
	rm -rf dist

build:
	make clean && \
	flit build && \
	pyinstaller -n viper -F --distpath ./dist/bin viper/cli.py && \
	cp -rf bin dist/ && \
	chmod 775 dist/**

publish:
	flit publish && \
	mkdocs gh-deploy --force \
		-m "Release docs v{version}"

docs:
	mkdocs serve

install-conda-base:
	wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh"
	exec Mambaforge-Linux-x86_64.sh

all: build
	mkdocs build --theme material
