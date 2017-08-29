############################################################################
# DrawingWindow.py - Michael Haimes, Leslie Kaelbling                      #
############################################################################
#    MIT SoaR 2.0 - A Python abstraction layer for MobileRobots            #
#    Pioneer3DX robots, and a simulator to simulate their operation        #
#    in a python environment (for testing)                                 #
#                                                                          #
#    Copyright (C) 2006-2007 Michael Haimes <mhaimes@mit.edu>              #
#                                                                          #
#   This program is free software; you can redistribute it and/or modify   #
#   it under the terms of the GNU General Public License as published by   #
#   the Free Software Foundation; either version 2 of the License, or      #
#   (at your option) any later version.                                    #
#                                                                          #
#   This program is distributed in the hope that it will be useful,        #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#   GNU General Public License for more details.                           #
#                                                                          #
#   You should have received a copy of the GNU General Public License along#
#   with this program; if not, write to the Free Software Foundation, Inc.,#
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.            #
############################################################################

### Hacked by LPK to be independent of SoaR

import tkinter
import tkinter.filedialog
import math
from . import tk

class DrawingWindow:

    def __init__(self, windowWidth, windowHeight, x_min, x_max, y_min, y_max,
                 title):
        # start tk if it hasn't been done already
        tk.init()
        self.title = title
        # Make a window to draw on
        self.top=tkinter.Toplevel()
        self.top.wm_title(title)
        self.top.protocol('WM_DELETE_WINDOW', self.destroy)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.canvas = tkinter.Canvas(self.top, width=self.windowWidth,
                                     height=self.windowHeight, 
                                     background="white")
        self.canvas.pack()
#        self.save_btn = Tkinter.Button(self.top, text="Save",
#                                       command=self.save)
#        self.save_btn.pack()
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max if x_max else width
        self.y_max = y_max if y_max else height

        # multiply an input value by this to get pixels
        self.xScale = windowWidth / float(self.x_max - self.x_min)
        self.yScale = windowHeight / float(self.y_max - self.y_min)

    def destroy(self):
        self.top.destroy()

    def save(self):
        filename = \
            tkinter.filedialog.asksaveasfilename(filetypes=[("PS", "*.ps")],
                                           defaultextension=".ps",
                                           title="Save Window to ...")
        if len(filename) == 0:
            return
        self.canvas.update()
        self.canvas.postcript(file = filename)

    def scaleX(self, x):
        # real value to pixels
        return self.xScale * (x - self.x_min)
    
    def scaleY(self, y):
        return self.windowHeight - self.yScale * (y - self.y_min)
    
    def scaleYMag(self, y):
        return self.yScale * (y - self.y_min)

    def drawPoint(self, x, y, color = "blue"):
        windowX = self.scaleX(x)
        windowY = self.scaleY(y)
        return self.canvas.create_rectangle(windowX-1, windowY-1, windowX+1,
                                     windowY+1, fill = color, outline = color)

    def draw_robotWithNose(self, x, y, theta, color = "blue", size = 6):
        rawx = math.cos(theta)
        rawy = math.sin(theta)
        hx, hy = 0.15, 0.0
        noseX = x+rawx*hx-rawy*hy
        noseY = y+rawy*hx+rawx*hy
        return self.draw_robot(x,y,noseX,noseY,color=color,size=size)

    def draw_robot(self, x, y, noseX, noseY,color = "blue", size = 8):
        windowX = self.scaleX(x)
        windowY = self.scaleY(y)
        hsize = int(size)/2   # For once, we want the int division!
        return (self.canvas.create_rectangle(windowX-hsize, windowY-hsize,
                                     windowX+hsize, windowY+hsize,
                                     fill = color, outline = color), 
        self.canvas.create_line(windowX, windowY,
                                self.scaleX(noseX),self.scaleY(noseY),
                                fill=color, width=2, arrow="last"))

    def drawSquare(self, x, y, size, color = "blue"):
        windowX = self.scaleX(x)
        windowY = self.scaleY(y)
        xhsize = size * self.xScale / 2
        yhsize = size * self.yScale / 2
        return self.canvas.create_rectangle(windowX-xhsize, windowY-yhsize,
                                            windowX+xhsize, windowY+yhsize,
                                            fill = color, outline = color)

    def draw_text(self, x, y, label, color="blue"):
        windowX = self.scaleX(x)
        windowY = self.scaleY(y)
        # LPK:  just took out this line
        #self.canvas.delete(Tkinter.ALL)
        return self.canvas.create_text(windowX, windowY, text=label,
                                       fill = color)
        # font="Arial 20",fill="#ff0000"


    def drawRect(self, coordinateIndices1, coordinateIndices2, color = "black"):
        (x1,y1) = coordinateIndices1
        (x2,y2) = coordinateIndices2
        return self.canvas.create_rectangle(self.scaleX(x1), self.scaleY(y1),
                                            self.scaleX(x2), self.scaleY(y2),
                                            fill = color)

    def draw_line_seg(self, x1, y1, x2, y2, color = "black", width = 2):
        return self.canvas.create_line(self.scaleX(x1),self.scaleY(y1),
                                       self.scaleX(x2),self.scaleY(y2),
                                       fill = color,
                                       width = width)

    def drawUnscaledLineSeg(self, x1, y1, xproj, yproj, color = "black",
                            width = 1):
        return self.canvas.create_line(self.scaleX(x1),self.scaleY(y1),
                                       self.scaleX(x1)+xproj,self.scaleY(y1)-yproj,
                                       fill = color,
                                       width = width)

    def drawUnscaledRect(self, x1, y1, xproj, yproj, color = "black"):
        return self.canvas.create_rectangle(self.scaleX(x1)-xproj,
                                            self.scaleY(y1)+yproj,
                                            self.scaleX(x1)+xproj,
                                            self.scaleY(y1)-yproj,
                                            fill = color)
            
    def drawLine(self, lineParams, color = "black"):
        (a,b,c) = lineParams
        if abs(b) < 0.001:
            startX = self.scaleX(-c/a)
            endX = self.scaleX(-c/a)
            startY = self.scaleY(self.y_min)
            endY = self.scaleY(self.y_max)
        else:
            startX = self.scaleX(self.x_min)
            startY = self.scaleY(- (a * self.x_min + c) / b)
            endX = self.scaleX(self.x_max)
            endY = self.scaleY(- (a * self.x_max + c) / b)
        return self.canvas.create_line(startX, startY, endX, endY, fill = color)

    def delete(self, thing):
        self.canvas.delete(thing)
  
    def clear(self):
        self.canvas.delete("all")
