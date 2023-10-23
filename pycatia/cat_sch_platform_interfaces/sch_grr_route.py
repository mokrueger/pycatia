#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_grr import SchGRR
from pycatia.cat_sch_platform_interfaces.sch_list_of_doubles import SchListOfDoubles
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.cat_sch_platform_interfaces.sch_route_symbol import SchRouteSymbol
from pycatia.system_interfaces.any_object import AnyObject


class SchGRRRoute(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRRRoute
                | 
                | Manage the graphical representations of a schematic route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr_route = com_object

    def add_points(self, i_l_db2_pt_path_to_add: tuple, i_after_which_pt_num: int) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPoints(CATSafeArrayVariant iLDb2PtPathToAdd,
                | long iAfterWhichPtNum)
                | 
                |     Add a list of point to a route.
                | 
                |     Parameters:
                | 
                |         iLDbPtPathToAdd
                |             A list of X-Y coordinates of the points to be added. 2 doubles per
                |             point. 
                |         iAfterWhichPtNum
                |             The point number to add the points after. Use 0 to indicate adding
                |             before the first point. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(x) As CATSafeArrayVariant
                |          Dim intVar3 As Integer
                |           ...
                |          objThisIntf.AddPointsdbVar1,intVar3

        :param tuple i_l_db2_pt_path_to_add:
        :param int i_after_which_pt_num:
        :rtype: tuple
        """
        return self.sch_grr_route.AddPoints(i_l_db2_pt_path_to_add, i_after_which_pt_num)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_points'
        # # vba_code = """
        # # Public Function add_points(sch_grr_route)
        # #     Dim iLDb2PtPathToAdd (2)
        # #     sch_grr_route.AddPoints iLDb2PtPathToAdd
        # #     add_points = iLDb2PtPathToAdd
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def break_(self, i_db2_pt1: tuple, i_db2_pt2: tuple, o_new_grr_route: 'SchGRRRoute') -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Break(CATSafeArrayVariant iDb2Pt1,
                | CATSafeArrayVariant iDb2Pt2,
                | SchGRRRoute oNewGRRRoute)
                | 
                |     Break a route graphic into 2 pieces. The old graphic is shortened and a new
                |     graphic is created.
                | 
                |     Parameters:
                | 
                |         iDb2Pt1
                |             X-Y coordinates of point 1 to break the route at (this point is
                |             mandatory). 
                |         iDb2Pt2
                |             X-Y coordinates of point 2 to break the route at (this point is
                |             optional). If provided the points in between point 1 and this point will be
                |             eliminated. Point 1 is the last point of the shortened old route and point 2 is
                |             the first point of the new route. If this point is not provided (i.e. sends in
                |             a NULL). point 1 and point 2 are the same. 
                |         oNewGRRRoute
                |             The new line string graphic created (CATISchGRRRoute interface
                |             pointer) 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(2) As CATSafeArrayVariant
                |          Dim dbVar2(2) As CATSafeArrayVariant
                |          Dim objArg3 As SchGRRRoute
                |           ...
                |          objThisIntf.BreakdbVar1,dbVar2,objArg3

        :param tuple i_db2_pt1:
        :param tuple i_db2_pt2:
        :param SchGRRRoute o_new_grr_route:
        :rtype: tuple
        """
        return self.sch_grr_route.Break(i_db2_pt1, i_db2_pt2, o_new_grr_route.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'break'
        # # vba_code = """
        # # Public Function break(sch_grr_route)
        # #     Dim iDb2Pt1 (2)
        # #     sch_grr_route.Break iDb2Pt1
        # #     break = iDb2Pt1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def compress(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Compress()
                | 
                |     Compress a the defining points of a route graphic, removing coincident
                |     points.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchGRRRoute
                |           ...
                |          objThisIntf.Compress

        :rtype: None
        """
        return self.sch_grr_route.Compress()

    def compress2(self, i_unset_gaps: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Compress2(CatSchIDLRouteUnsetGapsMode iUnsetGaps)
                | 
                |     Compress the defining points of a route graphic, removing coincident
                |     points.
                | 
                |     Parameters:
                | 
                |         iUnsetGaps
                |             Whether to unset gaps (in all the effected routes: this route
                |             and other routes intersecting it) or not = SchUnsetGapsOn :
                |             unset gaps = SchUnsetGapsOff : don't unset gaps
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                | 
                |           ...
                |          objThisIntf.Compress2CatSchIDLRouteUnsetGapsMode_Enum

        :param int i_unset_gaps:
        :rtype: None
        """
        return self.sch_grr_route.Compress2(i_unset_gaps)

    def concatenate(self, i_which_end1: int, i_grr_route2: 'SchGRRRoute', i_which_end2: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Concatenate(long iWhichEnd1,
                | SchGRRRoute iGRRRoute2,
                | long iWhichEnd2)
                | 
                |     Concatenate 2 route graphic objects into one. The first route graphic is
                |     elongated and the second object is deleted.
                | 
                |     Parameters:
                | 
                |         iWhichEnd1
                |             =1 at start point; =2 at end point 
                |         iGRRRoute2
                |             Second route graphic object (CATISchGRRRoute interface pointer) to
                |             be concatenated to the first. This route graphic will be deleted.
                |             
                |         iWhichEnd2
                |             =1 at start point; =2 at end point 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim intVar1 As Integer
                |          Dim objArg2 As SchGRRRoute
                |          Dim intVar3 As Integer
                |           ...
                |          objThisIntf.ConcatenateintVar1,objArg2,intVar3

        :param int i_which_end1:
        :param SchGRRRoute i_grr_route2:
        :param int i_which_end2:
        :rtype: None
        """
        return self.sch_grr_route.Concatenate(i_which_end1, i_grr_route2.com_object, i_which_end2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'concatenate'
        # # vba_code = """
        # # Public Function concatenate(sch_grr_route)
        # #     Dim iWhichEnd1 (2)
        # #     sch_grr_route.Concatenate iWhichEnd1
        # #     concatenate = iWhichEnd1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def concatenate_keep_grr2(self, i_which_end1: int, i_grr_route2: 'SchGRRRoute', i_which_end2: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ConcatenateKeepGRR2(long iWhichEnd1,
                | SchGRRRoute iGRRRoute2,
                | long iWhichEnd2)
                | 
                |     Concatenate 2 route graphic objects into one. The first route graphic is
                |     elongated and the second object is unchanged.
                | 
                |     Parameters:
                | 
                |         iWhichEnd1
                |             =1 at start point; =2 at end point 
                |         iGRRRoute2
                |             Second route graphic object (CATISchGRRRoute interface pointer) to
                |             be concatenated to the first. This route graphic will be unchanged.
                |             
                |         iWhichEnd2
                |             =1 at start point; =2 at end point 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim intVar1 As Integer
                |          Dim objArg2 As SchGRRRoute
                |          Dim intVar3 As Integer
                |           ...
                |         
                |         objThisIntf.ConcatenateKeepGRR2intVar1,objArg2,intVar3

        :param int i_which_end1:
        :param SchGRRRoute i_grr_route2:
        :param int i_which_end2:
        :rtype: None
        """
        return self.sch_grr_route.ConcatenateKeepGRR2(i_which_end1, i_grr_route2.com_object, i_which_end2)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'concatenate_keep_grr2'
        # # vba_code = """
        # # Public Function concatenate_keep_grr2(sch_grr_route)
        # #     Dim iWhichEnd1 (2)
        # #     sch_grr_route.ConcatenateKeepGRR2 iWhichEnd1
        # #     concatenate_keep_grr2 = iWhichEnd1
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_route_symbol(
            self,
            i_seg_num: int,
            i_seg_parm: float,
            i_grr_symbol: SchGRR,
            o_route_symbol: SchRouteSymbol
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateRouteSymbol(long iSegNum,
                | double iSegParm,
                | SchGRR iGRRSymbol,
                | SchRouteSymbol oRouteSymbol)
                | 
                |     Place a symbol on the route.
                | 
                |     Parameters:
                | 
                |         iSegNum
                |             The route segment number to place the symbol on. 
                |         iSegParm
                |             The parameter along the segment used to place the symbol on
                |             (0.<=iSegParm<=1.). 
                |         iGRRSymbol
                |             The graphical primitive (detail) to be used for the symbol.
                |             
                |         oRouteSymbol
                |             The created route symbol (ditto). 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim intVar1 As Integer
                |          Dim dbVar2 As Double;
                |          Dim objArg3 As SchGRR
                |          Dim objArg4 As SchRouteSymbol
                |           ...
                |          objThisIntf.CreateRouteSymbolintVar1,dbVar2,objArg3,objArg4

        :param int i_seg_num:
        :param float i_seg_parm:
        :param SchGRR i_grr_symbol:
        :param SchRouteSymbol o_route_symbol:
        :rtype: None
        """
        return self.sch_grr_route.CreateRouteSymbol(
            i_seg_num,
            i_seg_parm,
            i_grr_symbol.com_object,
            o_route_symbol.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_route_symbol'
        # # vba_code = """
        # # Public Function create_route_symbol(sch_grr_route)
        # #     Dim iSegNum (2)
        # #     sch_grr_route.CreateRouteSymbol iSegNum
        # #     create_route_symbol = iSegNum
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_end_point(self, o_db2_end_pt: SchListOfDoubles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetEndPoint(SchListOfDoubles oDb2EndPt)
                | 
                |     Get the end point of the route graphic.
                | 
                |     Parameters:
                | 
                |         oDb2EndPt
                |             X-Y coordinates of the end point of the route graphic object.
                |             
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim objArg1 As SchListOfDoubles
                |           ...
                |          objThisIntf.GetEndPointobjArg1

        :param SchListOfDoubles o_db2_end_pt:
        :rtype: None
        """
        return self.sch_grr_route.GetEndPoint(o_db2_end_pt.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_end_point'
        # # vba_code = """
        # # Public Function get_end_point(sch_grr_route)
        # #     Dim oDb2EndPt (2)
        # #     sch_grr_route.GetEndPoint oDb2EndPt
        # #     get_end_point = oDb2EndPt
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_path(self, o_l_db2_pt_path: SchListOfDoubles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPath(SchListOfDoubles oLDb2PtPath)
                | 
                |     Get the defining points of a route graphic.
                | 
                |     Parameters:
                | 
                |         oLDbPtPath
                |             A list of X-Y coordinates of the points. 2 doubles per point.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim objArg1 As SchListOfDoubles
                |          Dim intVar2 As Integer
                |           ...
                |          objThisIntf.GetPathobjArg1

        :param SchListOfDoubles o_l_db2_pt_path:
        :rtype: None
        """
        return self.sch_grr_route.GetPath(o_l_db2_pt_path.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_path'
        # # vba_code = """
        # # Public Function get_path(sch_grr_route)
        # #     Dim oLDb2PtPath (2)
        # #     sch_grr_route.GetPath oLDb2PtPath
        # #     get_path = oLDb2PtPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_start_point(self, o_db2_start_pt: SchListOfDoubles) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetStartPoint(SchListOfDoubles oDb2StartPt)
                | 
                |     Get the start point of the route graphic.
                | 
                |     Parameters:
                | 
                |         oDb2StartPt
                |             X-Y coordinates of the start point of the route graphic object.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim objArg1 As SchListOfDoubles
                |           ...
                |          objThisIntf.GetStartPointobjArg1

        :param SchListOfDoubles o_db2_start_pt:
        :rtype: None
        """
        return self.sch_grr_route.GetStartPoint(o_db2_start_pt.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_start_point'
        # # vba_code = """
        # # Public Function get_start_point(sch_grr_route)
        # #     Dim oDb2StartPt (2)
        # #     sch_grr_route.GetStartPoint oDb2StartPt
        # #     get_start_point = oDb2StartPt
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_route_symbols(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListRouteSymbols() As SchListOfObjects
                | 
                |     List route symbols on the route.
                | 
                |     Parameters:
                | 
                |         oLRouteSymbol
                |             A list of route symbols. (members are CATIASchRouteSymbol objects).
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListRouteSymbols

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_grr_route.ListRouteSymbols())

    def remove_points(self, i_num_of_pts_to_remove: int, i_after_which_pt_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePoints(long iNumOfPtsToRemove,
                | long iAfterWhichPtNum)
                | 
                |     Remove points from route graphic.
                | 
                |     Parameters:
                | 
                |         iNumOfPtsToRemove
                |             The number of points to be removed 
                |         iAfterWhichPtNum
                |             The point number at which to start removing the point.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim intVar1 As Integer
                |          Dim intVar2 As Integer
                |           ...
                |          objThisIntf.RemovePointsintVar1,intVar2

        :param int i_num_of_pts_to_remove:
        :param int i_after_which_pt_num:
        :rtype: None
        """
        return self.sch_grr_route.RemovePoints(i_num_of_pts_to_remove, i_after_which_pt_num)

    def set_end_point(self, i_db2_end_pt: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEndPoint(CATSafeArrayVariant iDb2EndPt)
                | 
                |     Set the end point of the route graphic.
                | 
                |     Parameters:
                | 
                |         iDb2EndPt
                |             X-Y coordinates of the end point of the route graphic object to be
                |             set. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetEndPointdbVar1

        :param tuple i_db2_end_pt:
        :rtype: tuple
        """
        return self.sch_grr_route.SetEndPoint(i_db2_end_pt)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_end_point'
        # # vba_code = """
        # # Public Function set_end_point(sch_grr_route)
        # #     Dim iDb2EndPt (2)
        # #     sch_grr_route.SetEndPoint iDb2EndPt
        # #     set_end_point = iDb2EndPt
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_path(self, i_l_db2_pt_path: tuple, i_compress: int) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPath(CATSafeArrayVariant iLDb2PtPath,
                | CatSchIDLRouteCompressMode iCompress)
                | 
                |     Set the defining points of a route graphic.
                | 
                |     Parameters:
                | 
                |         iLDbPtPath
                |             A list of X-Y coordinates of the points to be set. 2 doubles per
                |             point. 
                |         iCompress
                |             Whether to compress the route (i.e., remove duplicate pts, colinear segments, etc.) or
                |             not = SchCompressOn : compress = SchCompressOff : don't compress
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(x) As CATSafeArrayVariant
                | 
                |           ...
                |          objThisIntf.SetPathdbVar1,CatSchIDLRouteCompressMode_Enum

        :param tuple i_l_db2_pt_path:
        :param int i_compress:
        :rtype: tuple
        """
        return self.sch_grr_route.SetPath(i_l_db2_pt_path, i_compress)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_path'
        # # vba_code = """
        # # Public Function set_path(sch_grr_route)
        # #     Dim iLDb2PtPath (2)
        # #     sch_grr_route.SetPath iLDb2PtPath
        # #     set_path = iLDb2PtPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_path2(self, i_l_db2_pt_path: tuple, i_compress: int, i_unset_gaps: int) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPath2(CATSafeArrayVariant iLDb2PtPath,
                | CatSchIDLRouteCompressMode iCompress,
                | CatSchIDLRouteUnsetGapsMode iUnsetGaps)
                | 
                |     Set the defining points of a route graphic.
                | 
                |     Parameters:
                | 
                |         iLDbPtPath
                |             A list of X-Y coordinates of the points to be set. 2 doubles per
                |             point. 
                |         iCompress
                |             Whether to compress the route (i.e., remove duplicate pts, colinear segments, etc.)
                |             or not = SchCompressOn : compress = SchCompressOff : don't compress
                |         iUnsetGaps
                |             Whether to unset gaps (in all the effected routes: this route and other routes
                              intersecting it) or not = SchUnsetGapsOn : unset gaps = SchUnsetGapsOff : don't unset gaps
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(x) As CATSafeArrayVariant
                | 
                |           ...
                |          objThisIntf.SetPath2dbVar1,CatSchIDLRouteCompressMode_Enum,CatSchIDLRouteUnsetGapsMode_Enum

        :param tuple i_l_db2_pt_path:
        :param int i_compress:
        :param int i_unset_gaps:
        :rtype: tuple
        """
        return self.sch_grr_route.SetPath2(i_l_db2_pt_path, i_compress, i_unset_gaps)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_path2'
        # # vba_code = """
        # # Public Function set_path2(sch_grr_route)
        # #     Dim iLDb2PtPath (2)
        # #     sch_grr_route.SetPath2 iLDb2PtPath
        # #     set_path2 = iLDb2PtPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_path3(self, i_l_db2_pt_path: tuple, i_compress: int, i_unset_gaps: int,
                  i_route_update_symbols: int) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPath3(CATSafeArrayVariant iLDb2PtPath,
                | CatSchIDLRouteCompressMode iCompress,
                | CatSchIDLRouteUnsetGapsMode iUnsetGaps,
                | CatSchIDLRouteSymbolUpdateMode iRouteUpdateSymbols)
                | 
                |     Set the defining points of a route graphic.
                | 
                |     Parameters:
                | 
                |         iLDb2PtPath
                |             A list of X-Y coordinates of the points to be set. 2 doubles per
                |             point. 
                |         iCompress
                |             Whether to compress the route (i.e., remove duplicate pts, colinear segments, etc.)
                |             or not = catSchIDLCompressOn : compress = catSchIDLCompressOff : don't compress
                |         iUnsetGaps
                |             Whether to unset gaps (in all the effected routes: this route and other routes
                |             intersecting it) or not = catSchIDLUnsetGapsOn : unset gaps = catSchIDLUnsetGapsOff :
                |             don't unset gaps
                |         iRouteSymbolUpdate
                |             Whether to update route symbols' positions = catSchIDLSymbolUpdateOff : don't update
                |             route symbols = catSchIDLSymbolUpdateOn : update route symbols
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(x) As CATSafeArrayVariant
                | 
                |           ...
                |          objThisIntf.SetPath3dbVar1,CatSchIDLRouteCompressMode_Enum,CatSchIDLRouteUnsetGapsMode_Enum,CatSchIDLRouteSymbolUpdateMode_Enum

        :param tuple i_l_db2_pt_path:
        :param int i_compress:
        :param int i_unset_gaps:
        :param int i_route_update_symbols:
        :rtype: tuple
        """
        return self.sch_grr_route.SetPath3(i_l_db2_pt_path, i_compress, i_unset_gaps, i_route_update_symbols)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_path3'
        # # vba_code = """
        # # Public Function set_path3(sch_grr_route)
        # #     Dim iLDb2PtPath (2)
        # #     sch_grr_route.SetPath3 iLDb2PtPath
        # #     set_path3 = iLDb2PtPath
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_start_point(self, i_db2_start_pt: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetStartPoint(CATSafeArrayVariant iDb2StartPt)
                | 
                |     Set the start point of the route graphic.
                | 
                |     Parameters:
                | 
                |         iDb2StartPt
                |             X-Y coordinates of the start point of the route graphic object to
                |             be set. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchGRRRoute
                |          Dim dbVar1(2) As CATSafeArrayVariant
                |           ...
                |          objThisIntf.SetStartPointdbVar1

        :param tuple i_db2_start_pt:
        :rtype: tuple
        """
        return self.sch_grr_route.SetStartPoint(i_db2_start_pt)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_start_point'
        # # vba_code = """
        # # Public Function set_start_point(sch_grr_route)
        # #     Dim iDb2StartPt (2)
        # #     sch_grr_route.SetStartPoint iDb2StartPt
        # #     set_start_point = iDb2StartPt
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchGRRRoute(name="{self.name}")'
