from FaceFactory import FaceFactory
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Vec
from OCC.Core.TopoDS import TopoDS_Face, TopoDS_Compound
from OCC.Core.TopTools import TopTools_ListOfShape
from OCC.Extend.ShapeFactory import make_extrusion


class TubeFactory:

    def __init__(self):
        self.__face = FaceFactory()


    def MakeCircleTube(self, Length: float, Diameter: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakeCircleSection( Diameter, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeElipleTube(self, Length: float, Major: float, Minor: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakeElipSection( Major, Minor, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeTriangleleTube(self, Length: float, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakeTriangleSection( Diameter, Radius, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeSquareTube(self, Length: float, Width: float, High: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakeSquareSection( Width, High, Radius, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakePentagonTube(self, Length: float, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakePentagonSection( Diameter, Radius, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def MakeHexagonTube(self, Length: float, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        section = self.__MakeHexagonSection( Diameter, Radius, Thickness )

        return make_extrusion( section, Length, gp_Vec( 0., 0., 1. ) )


    def __MakeCircleSection(self, Diameter: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakeCircleFace( Diameter / 2.0 )
        face2 = self.__face.MakeCircleFace( ( Diameter / 2.0 ) - Thickness )

        return self.__CutFace( face1, face2 )


    def __MakeElipSection(self, Major: float, Minor: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakeEllipsFace( Major, Minor )
        face2 = self.__face.MakeEllipsFace( Major - Thickness, Minor - Thickness )

        return self.__CutFace( face1, face2 )


    def __MakeTriangleSection(self, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakeTriangleFace( Diameter, Radius )
        face2 = self.__face.MakeTriangleFace( Diameter - ( 2 * Thickness ), Radius )

        return self.__CutFace( face1, face2 )


    def __MakeSquareSection(self, Width: float, High: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakeSquareFace( Width, High, Radius )
        face2 = self.__face.MakeSquareFace( Width - ( 2 * Thickness ), High - ( 2 * Thickness ), Radius )

        return self.__CutFace( face1, face2 )


    def __MakePentagonSection(self, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakePentagonFace( Diameter, Radius )
        face2 = self.__face.MakePentagonFace( Diameter - ( 2 * Thickness ), Radius )

        return self.__CutFace( face1, face2 )


    def __MakeHexagonSection(self, Diameter: float, Radius: float, Thickness: float) -> TopoDS_Compound:
        face1 = self.__face.MakeHexagonFace( Diameter, Radius )
        face2 = self.__face.MakeHexagonFace( Diameter - ( 2 * Thickness ), Radius )

        return self.__CutFace( face1, face2 )


    def __CutFace(self, Face1: TopoDS_Face, Face2: TopoDS_Face) -> TopoDS_Compound:
        cut = BRepAlgoAPI_Cut()
        L1 = TopTools_ListOfShape()
        L1.Append(Face1)
        L2 = TopTools_ListOfShape()
        L2.Append(Face2)
        cut.SetArguments(L1)
        cut.SetTools(L2)
        cut.SetFuzzyValue(0.01)
        cut.SetRunParallel(False)
        cut.Build()

        return cut.Shape()