SRC=hvy_global_kindtypes.f90 harvey.f90 hvy_setup_mesh.f90 hvy_print_mesh.f90 hvy_calc_alpha.f90 \
                        hvy_calc_source_terms.f90 hvy_assemble_rhs.f90 \
                        hvy_assemble_coeffs.f90 tridag_ser.f90 Gsselm.f90


.PHONY = doc, harvey, help, test

TEST_SUITE = ../qa
DATE_STAMP := $(shell date +%Y%m%d%H%M%S)
PPID_STAMP := $(shell echo $$PPID)

# Find Doxyfile
VPATH = Doc

# Find README.md
vpath %.md ..

markdown := $(wildcard Doc/markdown/*/*.md)
python := $(wildcard *.py ../qa/hvy_qa_test/*.py)
fortran := $(wildcard *.f90)

help:
	@echo "help:   Prints this help screen"
	@echo "doc:    Builds Doxygen documentation"
	@echo "harvey: Builds Fortran"
	@echo "test:   Runs full QA test suite"


doxygen.log: Doxyfile README.md
	cd Doc && doxygen > doxygen.log

doc: doxygen.log

github:
	ghp-import --no-jekyll --no-history --push ../doc/html

test: harfort.so
	mkdir -p ./QA
	#cp ./*.py harfort.so ./QA/
	#cp $(TEST_SUITE)/hvy_qa_test/*.py ./QA/
	cp -r $(TEST_SUITE)/hvy_qa_test/1DHeatEquation ./QA/
	cd QA && robot --exitonfailure --pythonpath ../$(TEST_SUITE)/hvy_qa_test --pythonpath .. --extension rst --loglevel DEBUG ../$(TEST_SUITE)
	#cp QA/test*.png Doc/images/

harvey: harfort.so

harfort.so: $(SRC)
	f2py -c --f90flags="-ffree-form" --opt="-O2" -m harfort $(SRC)
	#f2py -c --f90flags="-ffree-form -fprofile-arcs -ftest-coverage" --opt="-O0" -m harfort $(SRC)
	ln -fs harfort.*.so harfort.so

clean:
	rm -f harfort.cpython-38-darwin.so.dSYM

cleaner: clean
	rm -rf harfort.so harfort.*.so ../doc/html ../doc/latex Doc/doxygen.log
