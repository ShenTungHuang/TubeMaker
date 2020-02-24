from FaceFactory import FaceFactory
from OCC.Core.gp import gp_Vec
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Extend.ShapeFactory import make_extrusion


class CutFactory:

    def __init__(self):
        self.__face = FaceFactory()


    def MakeCirclePatern(self, Length: float, Diameter: float) -> TopoDS_Compound:
        section = self.__face.MakeCircleFace( Diameter / 2.0 )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeEliplePattern(self, Length: float, Major: float, Minor: float) -> TopoDS_Compound:
        section = self.__face.MakeEllipsFace( Major, Minor )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeTrianglelePattern(self, Length: float, Diameter: float, Radius: float) -> TopoDS_Compound:
        section = self.__face.MakeTriangleFace( Diameter, Radius )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeSquarePattern(self, Length: float, Width: float, High: float, Radius: float) -> TopoDS_Compound:
        section = self.__face.MakeSquareFace( Width, High, Radius )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakePentagonPattern(self, Length: float, Diameter: float, Radius: float) -> TopoDS_Compound:
        section = self.__face.MakePentagonFace( Diameter, Radius )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeHexagonPattern(self, Length: float, Diameter: float, Radius: float) -> TopoDS_Compound:
        section = self.__face.MakeHexagonFace( Diameter, Radius )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )