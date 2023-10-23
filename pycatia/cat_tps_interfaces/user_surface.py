#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.product_structure_interfaces.product import Product


class UserSurface(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     UserSurface

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.user_surface = com_object

    def add_reference(self, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddReference(Reference iSupport)
                | 
                |     Add a surface in a User Surface Support
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The surface that you want to add in the User
                |             Surface.

        :param Reference i_support:
        :rtype: None
        """
        return self.user_surface.AddReference(i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_reference'
        # # vba_code = """
        # # Public Function add_reference(user_surface)
        # #     Dim iSupport (2)
        # #     user_surface.AddReference iSupport
        # #     add_reference = iSupport
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_reference_in_a_product_ctx(self, i_prod_inst: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddReferenceInAProductCtx(Product iProdInst,
                | Reference iSupport)
                | 
                |     Add a surface in a User Surface Support
                | 
                |     Parameters:
                | 
                |         iProdInst
                |             The product instance where there is the geometry. 
                |         iSupport
                |             The surface that you want to add in the User
                |             Surface.

        :param Product i_prod_inst:
        :param Reference i_support:
        :rtype: None
        """
        return self.user_surface.AddReferenceInAProductCtx(i_prod_inst.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_reference_in_a_product_ctx'
        # # vba_code = """
        # # Public Function add_reference_in_a_product_ctx(user_surface)
        # #     Dim iProdInst (2)
        # #     user_surface.AddReferenceInAProductCtx iProdInst
        # #     add_reference_in_a_product_ctx = iProdInst
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_user_surface(self, i_user_surf: 'UserSurface') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddUserSurface(UserSurface iUserSurf)
                | 
                |     Add a User Surface Support in a User Surface Node
                | 
                |     Parameters:
                | 
                |         iUserSurf
                |             The User Surface Support that you want to add in the User
                |             Surface.

        :param UserSurface i_user_surf:
        :rtype: None
        """
        return self.user_surface.AddUserSurface(i_user_surf.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_user_surface'
        # # vba_code = """
        # # Public Function add_user_surface(user_surface)
        # #     Dim iUserSurf (2)
        # #     user_surface.AddUserSurface iUserSurf
        # #     add_user_surface = iUserSurf
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'UserSurface(name="{self.name}")'
