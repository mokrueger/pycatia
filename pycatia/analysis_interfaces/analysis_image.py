#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.analysis_interfaces.analysis_color_map import AnalysisColorMap
from pycatia.in_interfaces.folder import Folder
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.axis_system import AxisSystem
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.analysis_interfaces.analysis_images import AnalysisImages


class AnalysisImage(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisImage
                | 
                | Represents the analysis image object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_image = com_object

    @property
    def analysis_color_map(self) -> AnalysisColorMap:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisColorMap() As AnalysisColorMap (Read Only)
                | 
                |     Returns the color map object associated with an analysis image.

        :return: AnalysisColorMap
        :rtype: AnalysisColorMap
        """

        return AnalysisColorMap(self.analysis_image.AnalysisColorMap)

    @property
    def analysis_images(self) -> 'AnalysisImages':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisImages() As AnalysisImages (Read Only)
                | 
                |     Returns the analysis images collection associated with an analysis image.

        :return: AnalysisImages
        :rtype: AnalysisImages
        """

        from pycatia.analysis_interfaces.analysis_images import AnalysisImages
        return AnalysisImages(self.analysis_image.AnalysisImages)

    def export_data(self, i_folder: Folder, i_file_name: str, i_extension_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportData(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType)
                | 
                |     Extracts image results.
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file.
                |     Limitations:
                | 
                |         The allowed output positions are: node, element, center of element, and
                |         node of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     To export data with mesh-part identification use
                |     ExportDataWithMeshPartId
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportData(i_folder.com_object, i_file_name, i_extension_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data'
        # # vba_code = """
        # # Public Function export_data(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportData iFolder
        # #     export_data = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_data_in_any_user_axis(
            self,
            i_folder: Folder,
            i_file_name: str,
            i_extension_type: str,
            i_axis_system: AnyObject,
            i_product: Product,
            i_axis_orientation_type: int,
            i_export_mesh_part_id: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportDataInAnyUserAxis(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType,
                | AnyObject iAxisSystem,
                | Product iProduct,
                | CATAxisOrientationType iAxisOrientationType,
                | boolean iExportMeshPartID)
                | 
                |     Extracts image results.
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file. If User has not implemented
                |     CATIAAxisSystem interface for axis system, but has CATIABase interface
                |     implementation.
                |     Limitations:
                | 
                |         The allowed output positions are: node, element, center of element, and
                |         node of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     To export data with mesh-part identification use
                |     ExportDataWithMeshPartId
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.
                | 
                |         iAxisSystem
                |             Reference to the axis system to be used for location
                |             transformation. 
                |         iProduct
                |             Reference to the product, where the above axis system is defined.
                |             
                |         iAxisOrientationType
                |             Coordinate system type of location axis system 
                |         iExportMeshPartID
                |             Flag for exporting with meshpartid or not

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :param AnyObject i_axis_system:
        :param Product i_product:
        :param int i_axis_orientation_type:
        :param bool i_export_mesh_part_id:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportDataInAnyUserAxis(
            i_folder.com_object,
            i_file_name,
            i_extension_type,
            i_axis_system.com_object,
            i_product.com_object,
            i_axis_orientation_type,
            i_export_mesh_part_id
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data_in_any_user_axis'
        # # vba_code = """
        # # Public Function export_data_in_any_user_axis(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportDataInAnyUserAxis iFolder
        # #     export_data_in_any_user_axis = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_data_in_global_axis(
            self,
            i_folder: Folder,
            i_file_name: str,
            i_extension_type: str,
            i_axis_orientation_type: int,
            i_export_mesh_part_id: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportDataInGlobalAxis(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType,
                | CATAxisOrientationType iAxisOrientationType,
                | boolean iExportMeshPartID)
                | 
                |     Extracts image results.
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file.
                |     Limitations:
                | 
                |         The allowed output positions are: node, element, center of element, and
                |         node of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.
                | 
                |         iAxisOrientationType
                |             Coordinate system type of location axis system 
                |         iExportMeshPartID
                |             Flag for exporting with meshpartid or not

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :param int i_axis_orientation_type:
        :param bool i_export_mesh_part_id:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportDataInGlobalAxis(
            i_folder.com_object,
            i_file_name,
            i_extension_type,
            i_axis_orientation_type,
            i_export_mesh_part_id
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data_in_global_axis'
        # # vba_code = """
        # # Public Function export_data_in_global_axis(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportDataInGlobalAxis iFolder
        # #     export_data_in_global_axis = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_data_in_manual_axis(
            self,
            i_folder: Folder,
            i_file_name: str,
            i_extension_type: str,
            i_origin: tuple,
            i_x_direction: tuple,
            i_y_direction: tuple,
            i_z_direction: tuple,
            i_axis_orientation_type: int,
            i_export_mesh_part_id: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportDataInManualAxis(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType,
                | CATSafeArrayVariant iOrigin,
                | CATSafeArrayVariant iXDirection,
                | CATSafeArrayVariant iYDirection,
                | CATSafeArrayVariant iZDirection,
                | CATAxisOrientationType iAxisOrientationType,
                | boolean iExportMeshPartID)
                | 
                |     Extracts image results.
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file.
                |     Limitations:
                | 
                |         The allowed output positions are: node, element, center of element, and
                |         node of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.
                | 
                |         iOrigin
                |             Origin of Location axis system 
                |         iXDirection
                |             co-ordinates of a point on X- axis of Location axis system
                |             
                |         iYDirection
                |             co-ordinates of a point on Y- axis of Location axis system
                |             
                |         iZDirection
                |             co-ordinates of a point on Z- axis of Location axis system
                |             
                |         iAxisOrientationType
                |             Coordinate system type of location axis system 
                |         iExportMeshPartID
                |             Flag for exporting with meshpartid or not

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :param tuple i_origin:
        :param tuple i_x_direction:
        :param tuple i_y_direction:
        :param tuple i_z_direction:
        :param int i_axis_orientation_type:
        :param bool i_export_mesh_part_id:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportDataInManualAxis(
            i_folder.com_object,
            i_file_name,
            i_extension_type,
            i_origin,
            i_x_direction,
            i_y_direction,
            i_z_direction,
            i_axis_orientation_type,
            i_export_mesh_part_id
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data_in_manual_axis'
        # # vba_code = """
        # # Public Function export_data_in_manual_axis(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportDataInManualAxis iFolder
        # #     export_data_in_manual_axis = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_data_in_user_axis(
            self,
            i_folder: Folder,
            i_file_name: str,
            i_extension_type: str,
            i_axis_system: AxisSystem,
            i_product: Product,
            i_axis_orientation_type: int,
            i_export_mesh_part_id: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportDataInUserAxis(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType,
                | AxisSystem iAxisSystem,
                | Product iProduct,
                | CATAxisOrientationType iAxisOrientationType,
                | boolean iExportMeshPartID)
                | 
                |     Extracts image results.
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file.
                |     Limitations:
                | 
                |         The allowed output positions are: node, element, center of element, and
                |         node of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     To export data with mesh-part identification use
                |     ExportDataWithMeshPartId
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.
                | 
                |         iAxisSystem
                |             Reference to the axis system to be used for location
                |             transformation. 
                |         iProduct
                |             Reference to the product, where the above axis system is defined.
                |             
                |         iAxisOrientationType
                |             Coordinate system type of location axis system 
                |         iExportMeshPartID
                |             Flag for exporting with meshpartid or not

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :param AxisSystem i_axis_system:
        :param Product i_product:
        :param int i_axis_orientation_type:
        :param bool i_export_mesh_part_id:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportDataInUserAxis(
            i_folder.com_object,
            i_file_name,
            i_extension_type,
            i_axis_system.com_object,
            i_product.com_object,
            i_axis_orientation_type,
            i_export_mesh_part_id)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data_in_user_axis'
        # # vba_code = """
        # # Public Function export_data_in_user_axis(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportDataInUserAxis iFolder
        # #     export_data_in_user_axis = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_data_with_mesh_part_id(self, i_folder: Folder, i_file_name: str, i_extension_type: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ExportDataWithMeshPartId(Folder iFolder,
                | CATBSTR iFileName,
                | CATBSTR iExtensionType)
                | 
                |     Extracts image results and location with mesh part name (as
                |     identifier).
                |     The export is done related to an existing image and will be stored in a
                |     CATIA Folder as a Text file or as an Excel file.
                |     Limitations:
                | 
                |         The allowed output positions are: element, center of element, and node
                |         of element
                |         The allowed values are: integer, real or double
                |         The allowed value types are: average or discontinuous iso, symbol,
                |         fringe or text
                | 
                |     To export data with mesh-part identification use
                |     ExportData
                | 
                |     Parameters:
                | 
                |         iFolder
                |             The folder to store the file to create 
                |         iFileName
                |             The name of the file to create 
                |         iExtensionType
                |             The extension of the file
                |             Legal values:
                | 
                |                 "xls" for a Microsoft Excel workbook
                |                 "txt" for a text file.

        :param Folder i_folder:
        :param str i_file_name:
        :param str i_extension_type:
        :return: None
        :rtype: None
        """
        return self.analysis_image.ExportDataWithMeshPartId(i_folder.com_object, i_file_name, i_extension_type)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'export_data_with_mesh_part_id'
        # # vba_code = """
        # # Public Function export_data_with_mesh_part_id(analysis_image)
        # #     Dim iFolder (2)
        # #     analysis_image.ExportDataWithMeshPartId iFolder
        # #     export_data_with_mesh_part_id = iFolder
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def reset_selection(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ResetSelection()
                | 
                |     Resets all selections in an image.
                |     This is done related to an existing image

        :return: None
        :rtype: None
        """
        return self.analysis_image.ResetSelection()

    def set_activation_status(self, i_activation_status: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetActivationStatus(CATVariant iActivationStatus)
                | 
                |     Activates oe deactivates an image.
                |     This is done related to an existing image
                | 
                |     Parameters:
                | 
                |         iActivationStatus
                |             To activate or not the current image.

        :param cat_variant i_activation_status:
        :return: None
        :rtype: None
        """
        return self.analysis_image.SetActivationStatus(i_activation_status)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_activation_status'
        # # vba_code = """
        # # Public Function set_activation_status(analysis_image)
        # #     Dim iActivationStatus (2)
        # #     analysis_image.SetActivationStatus iActivationStatus
        # #     set_activation_status = iActivationStatus
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_current_occurrence(self, i_occurrence_number: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCurrentOccurrence(CATVariant iOccurrenceNumber)
                | 
                |     Sets occurrence number for an image.
                |     This is done related to an existing image
                | 
                |     Parameters:
                | 
                |         iOccurrenceNumber
                |             The number to select
                |             Legal value: 1 ≤ iOccurrenceNumber ≤ nbOccurrence

        :param cat_variant i_occurrence_number:
        :return: None
        :rtype: None
        """
        return self.analysis_image.SetCurrentOccurrence(i_occurrence_number)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_current_occurrence'
        # # vba_code = """
        # # Public Function set_current_occurrence(analysis_image)
        # #     Dim iOccurrenceNumber (2)
        # #     analysis_image.SetCurrentOccurrence iOccurrenceNumber
        # #     set_current_occurrence = iOccurrenceNumber
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_selection(self, i_reference: Reference, i_replace_mode: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetSelection(Reference iReference,
                | CATVariant iReplaceMode)
                | 
                |     Adds a selection to an image.
                |     This is done related to an existing image
                | 
                |     Parameters:
                | 
                |         iReference
                |             The selectionGroup to add 
                |         iReplaceMode
                |             To replace or not the current selections.

        :param Reference i_reference:
        :param cat_variant i_replace_mode:
        :return: None
        :rtype: None
        """
        return self.analysis_image.SetSelection(i_reference.com_object, i_replace_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_selection'
        # # vba_code = """
        # # Public Function set_selection(analysis_image)
        # #     Dim iReference (2)
        # #     analysis_image.SetSelection iReference
        # #     set_selection = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Update()
                | 
                |     Updates an image.
                |     This is done related to an existing image

        :return: None
        :rtype: None
        """
        return self.analysis_image.Update()

    def __repr__(self):
        return f'AnalysisImage(name="{self.name}")'