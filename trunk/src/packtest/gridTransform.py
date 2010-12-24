''' Several Transformation Functions '''
class GridTransform:

  def negTransAxisX(self,x,y,maxX,maxY,width):
      ''' returns an Transformed x value for the Crossgrid'''
      if x == 0.0 and y == 0.0:
          x = 0.5 *width
      elif x == 0.0 and y <> 0.0:
          x = 0.5*width
      elif x <> 0.0 and y ==0.0:
          x = 0.5 * width + (0.45*width)/(maxX/x)   
      elif x <> 0.0 and y <> 0.0:
          x = 0.5 * width + (0.45*width)/(maxX/x)
           
      return x
  
  def negTransAxisY(self,x,y,maxX,maxY,height):
      ''' returns an Transformed y value for the Crossgrid'''
      if x == 0.0 and y == 0.0:
          y = 0.5 *height
      elif x == 0.0 and y <> 0.0:
          y = 0.5 * height - (0.45*height/(maxY/y))
      elif x <> 0.0 and y ==0.0:
          y = 0.5 * height    
      elif x <> 0.0 and y <> 0.0:
          y = 0.5 * height - (0.45*height/(maxY/y))
           
      return y
          
  def transAxisX(self,x,y,maxX,maxY,width):
      ''' returns an Transformed x value for the L Grid'''
      if x == 0.0 and y == 0.0:
          x = 0.1 * width
      elif x == 0.0 and y <> 0.0:
         x = 0.1 * width
      elif x <> 0.0 and y == 0.0:
         x = 0.1 * width + (0.8*width)/(maxX/x)
      elif x<>0.0 and y <> 0.0:        
          x = 0.1 * width + (0.8*width)/(maxX/x)
          
      return x
   
  def transAxisY(self,x,y,maxX,maxY,height):
      ''' returns an Transformed y value for the L Grid'''
      if x == 0.0 and y == 0.0:
          y = 0.9 * height
      elif x == 0.0 and y <> 0.0:
         y = 0.9 * height - (0.8*height)/(maxY/y)
      elif x <> 0.0 and y == 0.0:
         y = 0.9 * height
      elif x<>0.0 and y <> 0.0:        
          y = 0.9 * height - (0.8*height)/(maxY/y)   
      
      return y