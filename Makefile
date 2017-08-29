.PHONY: build test

build:
	@echo "Building from templates..."
	@python codegen/build.py 
	@find out -type f \( -iname '*.[ch]' -o -iname '*.ts' \) | xargs -r clang-format -i

test:
	@echo "Testing..."
	@python -m unittest discover
