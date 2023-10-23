#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dmaps_interfaces.resource import Resource
from pycatia.dnb_fastener_interfaces.fastener import Fastener
from pycatia.dnb_fastener_interfaces.fastener_set import FastenerSet
from pycatia.system_interfaces.any_object import AnyObject


class DnbFastenerItemServices(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBFastenerItemServices

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.dnb_fastener_item_services = com_object

    def assign_fastener_to_process(self, i_fastener: Fastener, i_process: Activity, e_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AssignFastenerToProcess(Fastener iFastener,
                | Activity iProcess,
                | DNBAssignStatus eStatus)
                | 
                |     Assigns a specified DELMIAFastener to a specified Activity and return the
                |     status of the action. Activity can be a TSA (for Resource) as well. *
                |     
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices") Dim AssignStatus As EnumParam myObject.AssignFastenerToProcess MyFastener,MyActivity,AssignStatus MsgBox AssignStatus

        :param Fastener i_fastener:
        :param Activity i_process:
        :param int e_status:
        :rtype: None
        """
        return self.dnb_fastener_item_services.AssignFastenerToProcess(i_fastener.com_object, i_process.com_object,
                                                                       e_status)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'assign_fastener_to_process'
        # # vba_code = """
        # # Public Function assign_fastener_to_process(dnb_fastener_item_services)
        # #     Dim iFastener (2)
        # #     dnb_fastener_item_services.AssignFastenerToProcess iFastener
        # #     assign_fastener_to_process = iFastener
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def assign_fastener_to_resource(self, i_fastener: Fastener, i_resource: Resource, e_status: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AssignFastenerToResource(Fastener iFastener,
                | Resource iResource,
                | DNBAssignStatus eStatus)
                | 
                |     Assigns a specified DELMIAFastener to a specified Resource and return the
                |     status of the action. * 
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices") Dim AssignStatus As EnumParam myObject.AssignFastenerToResource MyFastener,MyResource,AssignStatus MsgBox AssignStatus

        :param Fastener i_fastener:
        :param Resource i_resource:
        :param int e_status:
        :rtype: None
        """
        return self.dnb_fastener_item_services.AssignFastenerToResource(i_fastener.com_object, i_resource.com_object,
                                                                        e_status)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'assign_fastener_to_resource'
        # # vba_code = """
        # # Public Function assign_fastener_to_resource(dnb_fastener_item_services)
        # #     Dim iFastener (2)
        # #     dnb_fastener_item_services.AssignFastenerToResource iFastener
        # #     assign_fastener_to_resource = iFastener
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fasteners(self, i_products: tuple, b_joining_fasteners: bool, o_fastener_array: tuple) -> list:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetFasteners(CATSafeArrayVariant iProducts,
                | boolean bJoiningFasteners,
                | CATSafeArrayVariant oFastenerArray)
                | 
                |     Gets all the Fasteners on the products.
                | 
                |     Parameters:
                | 
                |         bJoiningFasteners
                |             Decides whether only the fastener joining the products will be
                |             returned(true) or all the fasteners on all the products(false)
                |             
                | 
                |     Example:
                |         Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |         Dim MyNum
                |         MyNum = myObject.GetNumberOfFasteners (MyProductArray, false)
                |         Dim MyFastenerList() As AnyObject
                |         ReDim MyFastenerList(MyNum) myObject.GetFasteners MyProductList,false,MyFastenerList

        :param tuple i_products:
        :param bool b_joining_fasteners:
        :param tuple o_fastener_array:
        :rtype: AnyObject
        """
        return self.dnb_fastener_item_services.GetFasteners(i_products, b_joining_fasteners, o_fastener_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fasteners'
        # # vba_code = """
        # # Public Function get_fasteners(dnb_fastener_item_services)
        # #     Dim iProducts (2)
        # #     dnb_fastener_item_services.GetFasteners iProducts
        # #     get_fasteners = iProducts
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fasteners_from_process(self, i_operation: Activity, i_fasteners: FastenerSet) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetFastenersFromProcess(Activity iOperation,
                | FastenerSet iFasteners)
                | 
                |     Gets all the DELMIAFasteners assigned to the Activity. * 
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |     Dim FastenerLot As FatenerSet
                |     myObject.GetFastenersFromProcess MyActivity,FastenerLot

        :param Activity i_operation:
        :param FastenerSet i_fasteners:
        :rtype: None
        """
        return self.dnb_fastener_item_services.GetFastenersFromProcess(i_operation.com_object, i_fasteners.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fasteners_from_process'
        # # vba_code = """
        # # Public Function get_fasteners_from_process(dnb_fastener_item_services)
        # #     Dim iOperation (2)
        # #     dnb_fastener_item_services.GetFastenersFromProcess iOperation
        # #     get_fasteners_from_process = iOperation
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fasteners_from_resource(self, i_resource: Resource, i_fasteners: FastenerSet) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetFastenersFromResource(Resource iResource,
                | FastenerSet iFasteners)
                | 
                |     Gets all the DELMIAFasteners assigned to the Resource. * 
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |     Dim FastenerLot As FatenerSet
                |     myObject.GetFastenersFromProcess MyResource,FastenerLot

        :param Resource i_resource:
        :param FastenerSet i_fasteners:
        :rtype: None
        """
        return self.dnb_fastener_item_services.GetFastenersFromResource(i_resource.com_object, i_fasteners.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fasteners_from_resource'
        # # vba_code = """
        # # Public Function get_fasteners_from_resource(dnb_fastener_item_services)
        # #     Dim iResource (2)
        # #     dnb_fastener_item_services.GetFastenersFromResource iResource
        # #     get_fasteners_from_resource = iResource
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_of_fasteners(self, i_products: tuple, b_joining_fasteners: bool) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetNumberOfFasteners(CATSafeArrayVariant iProducts,
                | boolean bJoiningFasteners) As long
                | 
                |     Gets the number of Fasteners on the products.
                | 
                |     Parameters:
                | 
                |         bJoiningFasteners
                |             Decides whether only the fastener joining the products will be
                |             returned(true) or all the fasteners on all the products(false)
                |             
                | 
                |     Example:
                |         Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |         Dim MyNum
                |         MyNum = myObject.GetNumberOfFasteners (MyProductArray, false)

        :param tuple i_products:
        :param bool b_joining_fasteners:
        :rtype: int
        """
        return self.dnb_fastener_item_services.GetNumberOfFasteners(i_products, b_joining_fasteners)

    def remove_fastener_from_process(self, i_fastener: Fastener, i_process: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveFastenerFromProcess(Fastener iFastener,
                | Activity iProcess)
                | 
                |     Unassigns a specified DELMIAFastener from a specified Activity. *
                |     
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |     myObject.RemoveFastenerFromProcess MyFastener,MyActivity

        :param Fastener i_fastener:
        :param Activity i_process:
        :rtype: None
        """
        return self.dnb_fastener_item_services.RemoveFastenerFromProcess(i_fastener.com_object, i_process.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_fastener_from_process'
        # # vba_code = """
        # # Public Function remove_fastener_from_process(dnb_fastener_item_services)
        # #     Dim iFastener (2)
        # #     dnb_fastener_item_services.RemoveFastenerFromProcess iFastener
        # #     remove_fastener_from_process = iFastener
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_fastener_from_resource(self, i_fastener: Fastener, i_resource: Resource) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemoveFastenerFromResource(Fastener iFastener,
                | Resource iResource)
                | 
                |     Unassigns a specified DELMIAFastener from a specified Resource. *
                |     
                | 
                | Example:
                |     Set myObject = CATIA.GetItem("DNBFastenerItemServices")
                |     myObject.RemoveFastenerFromResource MyFastener,MyResource

        :param Fastener i_fastener:
        :param Resource i_resource:
        :rtype: None
        """
        return self.dnb_fastener_item_services.RemoveFastenerFromResource(i_fastener.com_object, i_resource.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_fastener_from_resource'
        # # vba_code = """
        # # Public Function remove_fastener_from_resource(dnb_fastener_item_services)
        # #     Dim iFastener (2)
        # #     dnb_fastener_item_services.RemoveFastenerFromResource iFastener
        # #     remove_fastener_from_resource = iFastener
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DnbFastenerItemServices(name="{self.name}")'
