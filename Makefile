SRC=hvy_global_kindtypes.f90 harvey.f90 hvy_setup_mesh.f90 hvy_print_mesh.f90 hvy_calc_alpha.f90 \
                        hvy_calc_source_terms.f90 hvy_assemble_rhs.f90 \
                        hvy_assemble_coeffs.f90 tridag_ser.f90 Gsselm.f90


.PHONY: doc harvey help test clean
.SUFFIXES:

TEST_SUITE := $(abspath qa)
DOC_SOURCE := $(abspath doc)
SOURCEPATH := $(abspath src)
DATE_STAMP := $(shell date +%Y%m%d%H%M%S)
PPID_STAMP := $(shell echo $$PPID)

SRC_=$(abspath $(addprefix $(SOURCEPATH)/,$(SRC)))

# Find Doxyfile
VPATH := $(DOC_SOURCE):$(TEST_SUITE):$(SOURCEPATH):build

# Find only top-level README.md
vpath %.md .
vpath doxygen.log build/Doc

markdown := $(wildcard doc/markdown/*.md doc/markdown/*/*.md)
python := $(wildcard src/*.py qa/hvy_qa_test/*.py)

help:
	@echo "help:   Prints this help screen"
	@echo "doc:    Builds Doxygen documentation"
	@echo "harvey: Builds Fortran"
	@echo "test:   Runs full QA test suite"


doxygen.log: Doxyfile customdoxygen.css README.md $(markdown)
	mkdir -p ./build/Doc
	cd ./build/Doc && doxygen $(DOC_SOURCE)/Doxyfile > doxygen.log

doc: doxygen.log

github:
	ghp-import --no-jekyll --no-history --push ./build/Doc/html

test: harfort.so
	mkdir -p ./build/QA
	cp -r $(TEST_SUITE)/hvy_qa_test/1DHeatEquation ./build/QA/
	cd ./build/QA && robot --exitonfailure --pythonpath $(TEST_SUITE)/hvy_qa_test --pythonpath $(SOURCEPATH) --pythonpath .. --extension rst --loglevel DEBUG $(TEST_SUITE)
	#cp QA/test*.png Doc/images/

harvey: harfort.so

harfort.so: $(SRC)
	mkdir -p ./build
	cd ./build && f2py -c --f90flags="-ffree-form" --opt="-O2" -m harfort $(SRC_)
	#f2py -c --f90flags="-ffree-form -fprofile-arcs -ftest-coverage" --opt="-O0" -m harfort $(SRC)
	cd ./build && ln -fs harfort.*.so harfort.so

clean:
	rm -f ./build/Doc/doxygen.log

cleaner: clean
	rm -rf ./build
