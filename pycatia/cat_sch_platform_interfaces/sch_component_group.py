#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchComponentGroup(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchComponentGroup
                | 
                | Represents a temporary group of schematic objects for component
                | placement.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_component_group = com_object

    def add_member(self, i_cntbl_to_add: SchAppConnectable) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddMember(SchAppConnectable iCntblToAdd)
                | 
                |     Add a member to the component group.
                | 
                |     Parameters:
                | 
                |         iCntblToAdd
                |             The application connectable to be added to the group
                |
                |     Example:
                |
                |          Dim objThisIntf As SchComponentGroup
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          objThisIntf.AddMemberobjArg1

        :param SchAppConnectable i_cntbl_to_add:
        :rtype: None
        """
        return self.sch_component_group.AddMember(i_cntbl_to_add.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_member'
        # # vba_code = """
        # # Public Function add_member(sch_component_group)
        # #     Dim iCntblToAdd (2)
        # #     sch_component_group.AddMember iCntblToAdd
        # #     add_member = iCntblToAdd
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def list_members(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func ListMembers() As SchListOfObjects
                | 
                |     List all connectable members in the group.
                | 
                |     Parameters:
                | 
                |         oLGRR
                |             A list of connectables. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchComponentGroup
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.ListMembers

        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_component_group.ListMembers())

    def remove_member(self, i_cntbl_to_remove: SchAppConnectable) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveMember(SchAppConnectable iCntblToRemove)
                | 
                |     Remove a member to the component group.
                | 
                |     Parameters:
                | 
                |         iCntbleToRemove
                |             The application connectable to be removed from the group
                |
                |     Example:
                |
                |          Dim objThisIntf As SchComponentGroup
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          objThisIntf.RemoveMemberobjArg1

        :param SchAppConnectable i_cntbl_to_remove:
        :rtype: None
        """
        return self.sch_component_group.RemoveMember(i_cntbl_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_member'
        # # vba_code = """
        # # Public Function remove_member(sch_component_group)
        # #     Dim iCntblToRemove (2)
        # #     sch_component_group.RemoveMember iCntblToRemove
        # #     remove_member = iCntblToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchComponentGroup(name="{self.name}")'
