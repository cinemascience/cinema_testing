### Running tests

These tests take advantage of ParaView's UI and Catalyst testing framework to run a set of Cinema database tests. To run these tests:

1. Clone this repository
2. Edit a file called ``myenv.env`` in this directory, and define two environment variables:
    - ``CINEMATESTING_PARAVIEW`` This is the location of your ParaView executable
    - ``CINEMATESTING_PVBATCH``  This is the location of your pvbatch executable
    - ``CINEMATESTING_FILEDRIVER``  This is the location of the filedriver.py script (Can be found in the paraview source at Examples/Catalyst/SampleScripts/filedriver.py)
    - ``CINEMATESTING_BROWSER``  This is the name of your preferred browser 

3. Copy the testing dataset ``can.ex2`` from wherever it is on your system into the ``test/`` directory.

4. Type ``./run_tests`` and the test script will run. It will open ``ParaView``, create outputs, check those, and open viewers on the resulting databases.

5. We note that the step of visualizing the databases in cinema viewers currently works only on OSX. The scripts have been run on OSX only at this point, but should translate well to other platforms.

### Bugs
NOTE: 'Filed' column records whether or not the issue has been filed at github.kitware.org.

| Filed | Bug |
|:-----:|-----|
|x|ParaView's exported ``data.csv`` final column should be ``FILE`` instead of ``FILES``|
|x|Interactive test: Two views static camera [``data.csv``](results/twoviews.csv) does not distinguish between images from two views|
|x|Interactive test: Two views phi theta camera [``data.csv``](results/twoviews_phitheta.csv) does not distinguish between images from two views|
|x|Output from running ``File->Export Now`` and catalyst scripts should be identical. In practice, the catalyst run includes a ``cinema`` directory in the image path. These should be identical.|

### Interactive Tests

| Pass | Test | CDB | Camera | Notes |
|:----:|------|-----|--------|-------|
| + | ``test_cdb_static_camera`` | images | static | |
| + | ``test_cdb_phi_theta`` | images | phi_theta | |
| - | ``test_cdb_twoview_static`` | images, images | static | [``data.csv``](results/twoviews.csv) does not distinguish between images from two views |
| - | ``test_cdb_twoview_phi_theta`` | images, images | phi_theta | [``data.csv``](results/twoviews_phitheta.csv) does not distinguish between images from two views |


### Catalyst Tests

| Pass   | Test                                      | CDB              | Camera      | Notes       |
| :----: | ----------------------------------------- | ---------------- | ----------- | ----------- |
| +      | ``test_cdb_static_camera_catalyst``       | images           | static      | one view    |
|        | ``test_cdb_phi_theta_catalyst``           | images           | phi_theta   | one view    |
|        | ``test_cdb_twoview_static_catalyst``      | images, images   | static      | two views   |
|        | ``test_cdb_twoview_phi_theta_catalyst``   | images, images   | phi_theta   | two views   |
