#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.manufacturing_interfaces.manufacturing_tool_motion import ManufacturingToolMotion
from pycatia.system_interfaces.collection import Collection


class MFGToolMotions(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     MfgToolMotions
                | 
                | The collection of MfgToolMotions related to the Manufacturing Document
                | .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ManufacturingToolMotion)
        self.mfg_tool_motions = com_object

    def add(self, i_real_obj: ManufacturingToolMotion) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Add(ManufacturingToolMotion iRealObj)
                | 
                |     This method adds the specified CATIAManufacturingToolMotion in the current
                |     list CATIAMfgToolMotions.
                | 
                |     Example:
                |         The following example adds in CATIAMfgToolMotions ListToolMotions the
                |         CATIAManufacturingToolMotion ThisToolMotion
                | 
                |          ListToolMotions.Add(ThisToolMotion)

        :param ManufacturingToolMotion i_real_obj:
        :rtype: None
        """
        return self.mfg_tool_motions.Add(i_real_obj.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add'
        # # vba_code = """
        # # Public Function add(mfg_tool_motions)
        # #     Dim iRealObj (2)
        # #     mfg_tool_motions.Add iRealObj
        # #     add = iRealObj
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_element(self, i_index: int) -> ManufacturingToolMotion:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetElement(long iIndex) As ManufacturingToolMotion
                | 
                |     This method return the specified CATIAManufacturingToolMotion in the
                |     current list CATIAMfgToolMotions.
                | 
                |     Example:
                |         The following example return the CATIAManufacturingToolMotion
                |         ThisToolMotion in CATIAMfgToolMotions ListToolMotions in position
                |         NumPos:
                | 
                |          Set ThisToolMotion = ListToolMotions.GetElement(Numpos)

        :param int i_index:
        :rtype: ManufacturingToolMotion
        """
        return ManufacturingToolMotion(self.mfg_tool_motions.GetElement(i_index))

    def __repr__(self):
        return f'MfgToolMotions(name="{self.name}")'
