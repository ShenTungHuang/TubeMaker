from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.gp import gp_Trsf, gp_Pnt, gp_Ax1, gp_Dir, gp_Ax3, gp_Vec
import math


class PatternTransform:

    def TransformShape(self, X: float, Y: float, Z: float, RX: float, RY: float, RZ: float, Shape: TopoDS_Compound) -> TopoDS_Compound:
        trsf = self.__GetTransform( X, Y, Z, RX, RY, RZ )

        transform = BRepBuilderAPI_Transform( Shape, trsf, False )
        transform.Build()

        return transform.Shape()


    def __GetTransform(self, X: float, Y: float, Z: float, RX: float, RY: float, RZ: float) -> gp_Trsf:
        trsf_T  = gp_Trsf()
        trsf_RX = gp_Trsf()
        trsf_RY = gp_Trsf()
        trsf_RZ = gp_Trsf()
        center  = gp_Pnt( X, Y, Z )
        ax1_X   = gp_Ax1( center, gp_Dir( 1., 0., 0. ) )
        ax1_Y   = gp_Ax1( center, gp_Dir( 0., 1., 0. ) )
        ax1_Z   = gp_Ax1( center, gp_Dir( 0., 0., 1. ) )

        trsf_T.SetTranslation( gp_Vec( X, Y, Z ) )
        trsf_RX.SetRotation( ax1_X, RX * math.pi / 180 )
        trsf_RY.SetRotation( ax1_Y, RY * math.pi / 180 )
        trsf_RZ.SetRotation( ax1_Z, RZ * math.pi / 180 )

        return trsf_RZ * trsf_RY * trsf_RX * trsf_T


