from CutFactory import CutFactory
from PatternTransform import PatternTransform
from TubeFactory import TubeFactory
from OCC.Core.AIS import AIS_Shape
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Display.SimpleGui import init_display
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal

import tkinter as tk
from tkinter import simpledialog


# def TestFunction():
#     window = tk.Tk()
#     window.title("Circle Tube Maker")
#     window.mainloop()



if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()
    context         = display.Context
    tubeFactory     = TubeFactory()
    cutFactory      = CutFactory()
    transform       = PatternTransform()

    tube = tubeFactory.MakeHexagonTube( 200, 50., 5., 2. )

    cut     = cutFactory.MakeEliplePattern( 100., 20., 10. )
    cut     = transform.TransformShape( 0., 0., 0., 30., 0., 30., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    cut     = cutFactory.MakeHexagonPattern( 50., 20., 4. )
    cut     = transform.TransformShape( 0., 0., 80., 30.,40., 90., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    cut     = cutFactory.MakeSquarePattern( 90., 30, 20., 4. )
    cut     = transform.TransformShape( -20., 0., 120., 0., 0., 90., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    cut     = cutFactory.MakeTrianglelePattern( 90., 30, 4. )
    cut     = transform.TransformShape( 0., 5., 120., 40., 0., 120., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    cut     = cutFactory.MakeCirclePatern( 90., 30, )
    cut     = transform.TransformShape( 0., 0., 30., 0., -90., 0., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    cut     = cutFactory.MakePentagonPattern( 90., 30., 2. )
    cut     = transform.TransformShape( 0., 0., 80., 0., -90., 0., cut )
    tube    = BRepAlgoAPI_Cut( tube, cut ).Shape()

    aisCut = AIS_Shape( cut )
    context.Display( aisCut, True )

    aisTube = AIS_Shape( tube )
    context.Display(aisTube, True)

    stepWriter = STEPControl_Writer()
    Interface_Static_SetCVal( "write.step.schema", "AP203" )

    stepWriter.Transfer( aisTube.Shape(), STEPControl_AsIs )
    status = stepWriter.Write( "Test3.stp" )

    # menu_name = 'Tube Maker'
    # add_menu( menu_name )
    # add_function_to_menu( menu_name, TestFunction )

    display.FitAll()
    start_display()
