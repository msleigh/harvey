## Code Quality - Python

- [ ] Remove commented-out dead code in hvy_mesh.py:81-107
- [ ] Remove or document commented-out code in hvy_global_phys_data.py (entire file)
- [ ] Fix docstring copy-paste error: "Initialise new material" → "Initialise new region" in hvy_global_reg_data.py:12
- [ ] Complete placeholder docstring "More detailed information" in hvy_mats.py:12
- [ ] Use `sys.exit(1)` instead of `sys.exit()` for error exits in hvy_user_input.py:105
- [ ] Remove or complete comment "why not just = xsize?" in hvy_regs.py:22
- [ ] Add type hints to Python source files

## Code Quality - Fortran

- [ ] Clean up uncertain comment "Only need this for the explicit solution...?????" in harvey.f90:256
- [ ] Remove unused `fullmatrix` array in harvey.f90:102,352-374
- [ ] Resolve or remove commented visibility declarations in hvy_global_kindtypes.f90:5-6
- [ ] Document or remove placeholder source term code in hvy_calc_source_terms.f90:25

## Test Suite

- [ ] Replace `assert X == True/False` with `assert X` / `assert not X` in multiple tests
- [ ] Remove debug print statements in test14.py:72, test16.py:72, test18.py:43,47,96
- [ ] Enable commented-out assertion in test8.py:37
- [ ] Remove unused `phiFS` variables in test8.py:40, test13.py:38, test18.py:40
- [ ] Document tolerance selection rationale (varies from 5e-9 to 1.0 across tests)
- [ ] Address TODO for hardcoded L=pi in test3.py:23
- [ ] Consolidate duplicated test code across test8/9/11/12 and test13/14

## Documentation

- [ ] Replace placeholder "Specify the time-step in ??" with actual units in harvin.py:48 and all test*_in.py files (19 files)
- [ ] Expand references.md with additional citations (Crank-Nicholson, numerical stability sources)
- [ ] Add external blog URL from analsols.md:898 to references
- [ ] Document Fortran/Python interface architecture
- [ ] Document how to add new test cases
- [ ] Add version badge or version info to README
- [ ] Add Windows support status note to README

## Build System

- [ ] Add complete project metadata to pyproject.toml (authors, license, keywords, classifiers)
- [ ] Add `[project.optional-dependencies]` for dev/docs/test groups
- [ ] Pin doxypypy version in Dockerfile.docs
- [ ] Document required working directory for Doxygen builds
