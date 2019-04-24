
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory='data/test_cdb_static_camera_catalyst.cdb'

# makes a cinema D index table
make_cinema_table=True

#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.6.0-1408-gef655b8517
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.6.0-1408-gef655b8517

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.6.0-1408-gef655b8517
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [1598, 2210]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [0.21706008911132812, 4.0, -5.110947132110596]
      renderView1.StereoType = 'Crystal Eyes'
      renderView1.CameraPosition = [42.82768016198176, 43.91240033432172, -27.713123836065115]
      renderView1.CameraFocalPoint = [0.21706008911132788, 3.999999999999999, -5.110947132110596]
      renderView1.CameraViewUp = [-0.2566356727440152, -0.2540905875057856, -0.9325106459532735]
      renderView1.CameraParallelScale = 13.391445890217907
      renderView1.Background = [0.4117647058823529, 0.4117647058823529, 0.4117647058823529]
      renderView1.BackEnd = 'OSPRay raycaster'

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='RenderView1_%t.png', freq=1, fittoscreen=0, magnification=1, width=1598, height=2210, cinema={'tracking': {'object': 'None'}, 'composite': False, 'initial': {'eye': [42.8277, 43.9124, -27.7131], 'at': [0.21706, 4, -5.11095], 'up': [-0.256636, -0.254091, -0.932511]}, 'camera': 'static', 'floatValues': True, 'noValues': True})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'ExodusIIReader'
      # create a producer from a simulation input
      canex2 = coprocessor.CreateProducer(datadescription, 'input')

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from canex2
      canex2Display = Show(canex2, renderView1)

      # get color transfer function/color map for 'DISPL'
      dISPLLUT = GetColorTransferFunction('DISPL')
      dISPLLUT.RGBPoints = [2.4611168269148833, 0.231373, 0.298039, 0.752941, 11.222557997023772, 0.865003, 0.865003, 0.865003, 19.98399916713266, 0.705882, 0.0156863, 0.14902]
      dISPLLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'DISPL'
      dISPLPWF = GetOpacityTransferFunction('DISPL')
      dISPLPWF.Points = [2.4611168269148833, 0.0, 0.5, 0.0, 19.98399916713266, 1.0, 0.5, 0.0]
      dISPLPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      canex2Display.Representation = 'Surface'
      canex2Display.ColorArrayName = ['POINTS', 'DISPL']
      canex2Display.LookupTable = dISPLLUT
      canex2Display.OSPRayScaleArray = 'GlobalNodeId'
      canex2Display.OSPRayScaleFunction = 'PiecewiseFunction'
      canex2Display.SelectOrientationVectors = 'GlobalNodeId'
      canex2Display.ScaleFactor = 1.9778103828430176
      canex2Display.SelectScaleArray = 'GlobalNodeId'
      canex2Display.GlyphType = 'Arrow'
      canex2Display.GlyphTableIndexArray = 'GlobalNodeId'
      canex2Display.GaussianRadius = 0.09889051914215088
      canex2Display.SetScaleArray = ['POINTS', 'GlobalNodeId']
      canex2Display.ScaleTransferFunction = 'PiecewiseFunction'
      canex2Display.OpacityArray = ['POINTS', 'GlobalNodeId']
      canex2Display.OpacityTransferFunction = 'PiecewiseFunction'
      canex2Display.DataAxesGrid = 'GridAxesRepresentation'
      canex2Display.PolarAxes = 'PolarAxesRepresentation'
      canex2Display.ScalarOpacityFunction = dISPLPWF
      canex2Display.ScalarOpacityUnitDistance = 1.3901072164734265

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      canex2Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 10088.0, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      canex2Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 10088.0, 1.0, 0.5, 0.0]

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for dISPLLUT in view renderView1
      dISPLLUTColorBar = GetScalarBar(dISPLLUT, renderView1)
      dISPLLUTColorBar.Title = 'DISPL'
      dISPLLUTColorBar.ComponentTitle = 'Magnitude'

      # set color bar visibility
      dISPLLUTColorBar.Visibility = 1

      # show color legend
      canex2Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(canex2)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'input': [1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['DISPL', 0]]
    coprocessor.SetRequestedArrays('input', arrays)
  coprocessor.SetInitialOutputOptions(timeStepToStartOutputAt,forceOutputAtFirstCall)

  if rootDirectory:
      coprocessor.SetRootDirectory(rootDirectory)

  if make_cinema_table:
      coprocessor.EnableCinemaDTable()

  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(False, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
