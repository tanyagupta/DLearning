# D's learning




```
python main.py
```

To run the visual tests:

```
python -m visuals.basic
python -m visuals.complex
python -m visuals.styles

```

To run the unit tests:

```
python run_tests.py
```

### Schedule ###
Since we are in different timezones, we will have to work mostly offline. We do not have much time left so we will have to work very hard but very smart too.

1. Focus on code - less on theory.
2. Get the basic window running soon. IA today.
3. We re-assess tomorrow


 ## 03.29.2023

I will update helpful code and comments here. You copy the relevant code into your local template copy. Do your work their and give me results.

We will work on grid.py and sandbox.py mostly today.



1. We will implement the constructor
  `
  def __init__(self, draw_style, x, y) -> None:
  `
      we will check for draw_style
          The style with which colours will be drawn.
          Should be one of DRAW_STYLE_OPTIONS
          This draw style determines the LayerStore used on each grid square.
      - x, y: The dimensions of the grid.

      Should also intialise the brush size to the DEFAULT provided as a class variable.
      """




      raise NotImplementedError()

  def increase_brush_size(self):
      """
      Increases the size of the brush by 1,
      if the brush size is already MAX_BRUSH,
      then do nothing.
      """
      raise NotImplementedError()

  def decrease_brush_size(self):
      """
      Decreases the size of the brush by 1,
      if the brush size is already MIN_BRUSH,
      then do nothing.
      """
      raise NotImplementedError()

  def special(self):



       """
      Initialise the grid object.
      - draw_style:
          The style with which colours will be drawn.
          Should be one of DRAW_STYLE_OPTIONS
          This draw style determines the LayerStore used on each grid square.
      - x, y: The dimensions of the grid.

      Should also intialise the brush size to the DEFAULT provided as a class variable.
      """




      raise NotImplementedError()

  def increase_brush_size(self):
      """
      Increases the size of the brush by 1,
      if the brush size is already MAX_BRUSH,
      then do nothing.
      """
      raise NotImplementedError()

  def decrease_brush_size(self):
      """
      Decreases the size of the brush by 1,
      if the brush size is already MIN_BRUSH,
      then do nothing.
      """
      raise NotImplementedError()

  def special(self):


#### Questions to D
1. What data structure should be the grid?
2



1. Get sandbox running
  1. Copy sandbox.py into your own template directory
  2. From cmd python    
