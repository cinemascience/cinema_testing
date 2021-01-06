### Running tests

These tests take advantage of ParaView's UI and Catalyst testing framework to run a set of Cinema database tests. To run these tests:

1. Clone this repository

2. Copy the testing dataset ``can.ex2`` from wherever it is on your system into the ``test/`` directory.

3. Type ``./run_tests`` with arguments and *full* paths to each of the following: paraview executable, pvbatch executable, filedriver.py script (located in paraview source repo), and web browser of choice (Firefox is recommended) and the test script will run. It will open ``ParaView``, create outputs, check those, and open viewers on the resulting databases.
  - Example: ``./run_tests -p /Users/stam/projects/paraview/master-build/bin/paraview.app/Contents/MacOS/paraview -b /Users/stam/projects/paraview/master-build/bin/pvbatch -f /Users/stam/projects/paraview/src/Examples/Catalyst/SampleScripts/filedriver.py -w firefox``

NOTE: We note that the step of visualizing the databases in cinema viewers currently works only on OSX. The scripts have been run on OSX only at this point, but should translate well to other platforms.

### Bugs
NOTE: 'Filed' column records whether or not the issue has been filed at github.kitware.org.

| Filed   | Fixed   | Bug                                                                                                                                                                                  |
| :-----: | :-----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| x       | x       | Extracts from multiple views could overwrite eachother (reported in https://gitlab.kitware.com/paraview/paraview/-/issues/20111#note_843540)                                         |
| x       | x       | Could not set start and end time in xml test (reported in https://gitlab.kitware.com/paraview/paraview/-/issues/20271)                                                               |
| x       | x       | Filedriver.py did not work with new catalyst states (reported by email, fixed in https://gitlab.kitware.com/paraview/paraview/-/merge_requests/4445)                                 |
| x       |         | Batch catalyst script with no timesteps not dumping anything (reported in https://gitlab.kitware.com/paraview/paraview/-/issues/20423)                                               |
| x       |         | Interactive and Batch extracts not identical. Old issue coming back in 5.9.0-RC3 (reported in https://gitlab.kitware.com/paraview/paraview/-/issues/18969#note_880163)               |


### Interactive Tests

| Pass | Test | CDB |Views| Camera | Notes |
|:----:|------|-----|:---:|--------|-------|
| + | ``test_cdb_notimesteps`` | images |1| static |  |
| + | ``test_cdb_geom`` | geom |1| none |  |
| + | ``test_cdb_geom_and_images`` | geom, images |1| static |  |
| + | ``test_cdb_static_camera`` | images |1| static |  |
| + | ``test_cdb_phi_theta`` | images |1| phi_theta |  |
| + | ``test_cdb_twoview_static`` | images, images |2| static |  |
| + | ``test_cdb_twoview_phi_theta`` | images, images |2| phi_theta |  |


### Catalyst Tests

| Pass   | Test                                      | CDB              | Camera               | Notes                                                                              |
| :----: | ----------------------------------------- | ---------------- | -------------------- | ---------------------------------------------------------------------------------- |
| x      | ``test_cdb_notimesteps``                  | images           | static               | New failure. Posted in https://gitlab.kitware.com/paraview/paraview/-/issues/20423 |
| +      | ``test_cdb_geom``                         | geom             | none                 |                                                                                    |
| +      | ``test_cdb_geom_and_images``              | geom, images     | none, static         |                                                                                    |
| +      | ``test_cdb_static_camera_catalyst``       | images           | static               |                                                                                    |
| +      | ``test_cdb_phi_theta_catalyst``           | images           | phi_theta            |                                                                                    |
| +      | ``test_cdb_twoview_static_catalyst``      | images, images   | static, static       |                                                                                    |
| +      | ``test_cdb_twoview_phi_theta_catalyst``   | images, images   | phi_theta, phi_theta |                                                                                    |
