### Running tests

These tests take advantage of ParaView's UI testing framework to run a set of Cinema database tests.

1. Edit a file called ``myenv.env`` in this directory, and define two environment variables:
    - ``CINEMATESTING\_PARAVIEW`` This is the location of your ParaView executable
    - ``CINEMATESTING\_BROWSER`` This is the name of your preferred browser 

2. Copy the testing dataset can.ex2 from whereever it is on your system into the ``test/`` directory.

3. Type ``./run_tests`` and the test script will run. It will open ``ParaView``, create outputs, check those, and open viewers on the resulting databases.

### Tests

| Pass | Test | CDB | Camera | Notes |
|:----:|------|-----|--------|-------|
| + | ``test_cdb_static_camera`` | images | static | |
| + | ``test_cdb_phi_theta`` | images | phi_theta | |
| - | ``test_cdb_twoview_static`` | images, images | static | [``data.csv``](results/twoviews.csv) cannot distinguish between the two views |
|   | ``test_cdb_twoview_phi_theta`` | images, images | phi_theta | two views|




