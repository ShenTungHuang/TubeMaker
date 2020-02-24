from OCC.Core.ChFi2d import ChFi2d_AnaFilletAlgo
from OCC.Core.Geom import Geom_Circle
from OCC.Core.gp import gp_XOY, gp_Elips, gp_Pnt, gp_Pln, gp_Dir
from OCC.Core.TopoDS import TopoDS_Face, TopoDS_Edge
from OCC.Extend.ShapeFactory import make_edge, make_wire, make_face
import math


class FaceFactory:

    def MakeCircleFace(self, Radius: float) -> TopoDS_Face:
        circle  = Geom_Circle( gp_XOY(), Radius )
        ed      = make_edge( circle )
        wire    = make_wire( ed )

        return make_face( wire )


    def MakeEllipsFace(self, Major: float, Minor: float) -> TopoDS_Face:
        elip    = gp_Elips( gp_XOY(), Major, Minor )
        ed      = make_edge( elip )
        wire    = make_wire( ed )

        return make_face( wire )


    def MakeTriangleFace(self, Diameter: float, Radius: float) -> TopoDS_Face:
        tubeRadius  = Diameter / 2.0
        degree      = 30 * math.pi / 180.
        sindis      = tubeRadius * math.sin( degree )
        cosdis      = tubeRadius * math.cos( degree )

        p1 = gp_Pnt( 0.,        tubeRadius, 0. )
        p2 = gp_Pnt( -cosdis,   -sindis,    0. )
        p3 = gp_Pnt( cosdis,    -sindis,    0. )

        ed1 = make_edge( p1, p2 )
        ed2 = make_edge( p2, p3 )
        ed3 = make_edge( p3, p1 )

        pln = gp_Pln( gp_Pnt( 0., 0., 0. ), gp_Dir( 0., 0., 1. ) )

        cur1 = self.__MakeFillet( ed1, ed2, pln, Radius )
        cur2 = self.__MakeFillet( ed2, ed3, pln, Radius )
        cur3 = self.__MakeFillet( ed3, ed1, pln, Radius )

        edgeList = [ed1, cur1, ed2, cur2, ed3, cur3]

        wire = make_wire( edgeList )

        return make_face( wire )


    def MakeSquareFace(self, Width: float, High: float, Radius: float) -> TopoDS_Face:
        xDis = Width / 2.0
        yDis = High / 2.0

        p1 = gp_Pnt( xDis,  yDis,   0. )
        p2 = gp_Pnt( xDis,  -yDis,  0. )
        p3 = gp_Pnt( -xDis, -yDis,  0. )
        p4 = gp_Pnt( -xDis, yDis,   0. )

        ed1 = make_edge( p1, p2 )
        ed2 = make_edge( p2, p3 )
        ed3 = make_edge( p3, p4 )
        ed4 = make_edge( p4, p1 )

        pln = gp_Pln( gp_Pnt( 0., 0., 0. ), gp_Dir( 0., 0., 1. ) )

        cur1 = self.__MakeFillet( ed1, ed2, pln, Radius )
        cur2 = self.__MakeFillet( ed2, ed3, pln, Radius )
        cur3 = self.__MakeFillet( ed3, ed4, pln, Radius )
        cur4 = self.__MakeFillet( ed4, ed1, pln, Radius )

        edgeList = [ed1, cur1, ed2, cur2, ed3, cur3, ed4, cur4]

        wire = make_wire( edgeList )

        return make_face( wire )


    def MakePentagonFace(self, Diameter: float, Radius: float) -> TopoDS_Face:
        tubeRadius = Diameter / 2.0
        upX     = tubeRadius * math.cos( 18 * math.pi / 180. )
        upY     = tubeRadius * math.sin( 18 * math.pi / 180. )
        downX   = tubeRadius * math.sin( 36 * math.pi / 180. )
        downY   = tubeRadius * math.cos( 36 * math.pi / 180. )

        p1 = gp_Pnt( 0.,        tubeRadius, 0. )
        p2 = gp_Pnt( upX,       upY,        0. )
        p3 = gp_Pnt( downX,     -downY,     0. )
        p4 = gp_Pnt( -downX,    -downY,     0. )
        p5 = gp_Pnt( -upX,      upY,        0. )

        ed1 = make_edge( p1, p2 )
        ed2 = make_edge( p2, p3 )
        ed3 = make_edge( p3, p4 )
        ed4 = make_edge( p4, p5 )
        ed5 = make_edge( p5, p1 )

        pln = gp_Pln( gp_Pnt( 0., 0., 0. ), gp_Dir( 0., 0., 1. ) )

        cur1 = self.__MakeFillet( ed1, ed2, pln, Radius )
        cur2 = self.__MakeFillet( ed2, ed3, pln, Radius )
        cur3 = self.__MakeFillet( ed3, ed4, pln, Radius )
        cur4 = self.__MakeFillet( ed4, ed5, pln, Radius )
        cur5 = self.__MakeFillet( ed5, ed1, pln, Radius )

        edgeList = [ed1, cur1, ed2, cur2, ed3, cur3, ed4, cur4, ed5, cur5]

        wire = make_wire( edgeList )

        return make_face( wire )


    def MakeHexagonFace(self, Diameter: float, Radius: float) -> TopoDS_Face:
        tubeRadius  = Diameter / 2.0
        degree      = 60 * math.pi / 180.
        sindis      = tubeRadius * math.sin( degree )
        cosdis      = tubeRadius * math.cos( degree )

        p1 = gp_Pnt( cosdis,        sindis,     0. )
        p2 = gp_Pnt( tubeRadius,    0.,         0. )
        p3 = gp_Pnt( cosdis,        -sindis,    0. )
        p4 = gp_Pnt( -cosdis,       -sindis,    0. )
        p5 = gp_Pnt( -tubeRadius,   0.,         0. )
        p6 = gp_Pnt( -cosdis,       sindis,     0. )

        ed1 = make_edge( p1, p2 )
        ed2 = make_edge( p2, p3 )
        ed3 = make_edge( p3, p4 )
        ed4 = make_edge( p4, p5 )
        ed5 = make_edge( p5, p6 )
        ed6 = make_edge( p6, p1 )

        pln = gp_Pln( gp_Pnt( 0., 0., 0. ), gp_Dir( 0., 0., 1. ) )

        cur1 = self.__MakeFillet( ed1, ed2, pln, Radius )
        cur2 = self.__MakeFillet( ed2, ed3, pln, Radius )
        cur3 = self.__MakeFillet( ed3, ed4, pln, Radius )
        cur4 = self.__MakeFillet( ed4, ed5, pln, Radius )
        cur5 = self.__MakeFillet( ed5, ed6, pln, Radius )
        cur6 = self.__MakeFillet( ed6, ed1, pln, Radius )

        edgeList = [ed1, cur1, ed2, cur2, ed3, cur3, ed4, cur4, ed5, cur5, ed6, cur6]

        wire = make_wire( edgeList )

        return make_face( wire )


    def __MakeFillet(self, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Plane: gp_Pln, Radius: float) -> TopoDS_Edge:
        fil1 = ChFi2d_AnaFilletAlgo()
        fil1.Init( Edge1, Edge2, Plane )
        fil1.Perform( Radius )

        return fil1.Result( Edge1, Edge2 )