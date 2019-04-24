#### Running tests

1. edit a file called ``myenv.env`` in this directory, and define two environment variables:
    - ``CINEMATESTING\_PARAVIEW`` This is the location of your ParaView executable
    - ``CINEMATESTING\_BROWSER`` This is the name of your preferred browser 

2. copy the testing dataset can.ex2 from whereever it is on your system into the ``test/`` directory.

3. type ``./run_tests`` and the test script will run. It will open ``ParaView``, create outputs, check those, and open viewers on the resulting databases.


